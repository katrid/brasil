from inspect import get_annotations
from typing import get_origin, get_args, Annotated, List, Self
import re
import datetime
from decimal import Decimal

from lxml import etree

from .utils.xml_utils import tag


class SimpleType:
    _tag: str = None

    def __init__(self, min_occurs: int = None, max_occurs: int = None, enumeration: List[str] = None):
        self.min_occurs = min_occurs
        self.max_occurs = max_occurs
        self.enumeration = enumeration
        if self._tag is None:
            self._tag = self.__class__.__name__


class XmlProp:
    type = None
    origin = None
    element = None

    def __init__(self, name: str, annotations):
        self.name = name
        for i, arg in enumerate(get_args(annotations)):
            if i == 0:
                self.origin = get_origin(arg)
                if self.origin:
                    args = get_args(arg)
                    if args:
                        self.type = args[0]
                else:
                    self.type = arg
            elif i == 1:
                self.element = arg


class ElementList[T](list):
    def __init__(self, type):
        super().__init__()
        self.type = type

    def add(self, *args, **kwargs) -> T:
        item = self.type()
        if args:
            props = iter(item._props.keys())
            for arg in args:
                setattr(item, next(props), arg)
        for k, v in kwargs.items():
            setattr(item, k, v)
        self.append(item)
        return item


class ElementType(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        new_cls = super().__new__(cls, name, bases, attrs, **kwargs)
        mod = attrs.get('__module__')
        if mod == 'brasil.dfe.xsd':
            return new_cls

        new_cls._name = name
        return new_cls


class ComplexType(SimpleType, metaclass=ElementType):
    _xmlns: str = None
    _props: dict[str, XmlProp] = None
    _cls: 'ComplexType' = None
    _xmltmp = None
    _parent = None
    _max_occurs = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # inicializar elemento
        if self._props:
            for k, prop in self._props.items():
                # init the list
                if prop.origin is ElementList or prop.origin is list:
                    setattr(self, prop.name, ElementList(prop.type))
                elif issubclass(prop.type, ComplexType):
                    setattr(self, prop.name, prop.type())

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.__module__ != 'brasil.dfe.xsd':
            props = {'pass' if k == 'pass_' else k: XmlProp(k, a) for k, a in get_annotations(cls).items()}
            if props:
                if not cls._props:
                    cls._props = {}
                cls._props = {**cls._props, **props}

    def add(self, *args, **kwargs):
        new_obj = self.__class__()
        for k, v in kwargs.items():
            if v is not None:
                setattr(new_obj, k, v)
        self._list.append(new_obj)
        if args:
            new_obj._read_xml(args[0])
        return new_obj

    def append(self, obj):
        self._list.append(obj)

    def _xml(self, name=None):
        name = name or self._tag
        kwargs = {}
        args = []
        props = self._props
        if props:
            for k, prop in props.items():
                v = getattr(self, k, None)
                if v is None:
                    continue
                if isinstance(prop.element, Attribute):
                    kwargs[k] = str(v)
                    continue
                elif prop.type is XmlSignature:
                    args.append(v)
                    continue
                elif prop.type is datetime.datetime and isinstance(v, datetime.datetime):
                    v = v.strftime('%Y-%m-%dT%H:%M:%S-03:00')
                elif prop.type is datetime.date and isinstance(v, datetime.date):
                    v = v.strftime('%Y-%m-%d')
                elif issubclass(prop.type, Decimal) and v == 0 and prop.type._xs_optional:
                    continue
                elif issubclass(prop.type, Decimal) and v is not None and prop.type._xs_dec:
                    fmt = '{:.%sf}' % prop.type._xs_dec[1]
                    if isinstance(v, str):
                        v = float(v)
                    v = string.format(fmt, v)
                    xml = tag(k, v)
                    args.append(xml)
                    continue
                elif isinstance(v, ElementList):
                    for item in v:
                        if isinstance(item, ComplexType):
                            xml = item._xml(k)
                            if xml:
                                args.append(xml)
                        elif isinstance(item, str):
                            args.append(item)
                elif isinstance(v, (int, Decimal)):
                    v = str(v)
                elif isinstance(v, datetime.datetime):
                    v = v.strftime('%Y-%m-%dT%H:%M:%S-03:00')
                if prop.element is Attribute:
                    kwargs[k] = v
                elif isinstance(prop, TXML):
                    args.append(prop._xml())
                elif issubclass(prop.type, str):
                    if v:
                        v = str(v)
                        if not v.startswith('<![CDATA['):
                            args.append(tag(k, v.replace('&', '&amp;')))
                        else:
                            args.append(tag(k, v))
                elif isinstance(v, (ComplexType, SimpleTypeElement)):
                    xml = v._xml(k)
                    if xml:
                        args.append(xml)
                elif issubclass(prop.type, ComplexType):
                    if isinstance(v, str):
                        args.append(v)
        if not args:
            return ''
        if self._xmlns:
            kwargs['xmlns'] = self._xmlns
        self._xmltmp = tag(name or self.__class__.__name__, *args, **kwargs)
        return self._xmltmp

    def _clear(self):
        self._xmltmp = None

    def _read_xml(self, xml):
        if isinstance(xml, str):
            xml = xml.encode('utf-8')
        if isinstance(xml, bytes):
            node = etree.fromstring(xml)
        else:
            node = xml
        for k in node.attrib:
            setattr(self, k, node.attrib[k])

        for child in node:
            tag = child.tag.split('}', 1)[-1]
            prop = self._props.get(tag)
            if prop:
                if issubclass(prop.type, (ComplexType, ElementList)):
                    sub = getattr(self, tag, None)
                    if isinstance(sub, ElementList):
                        if issubclass(prop.type, ComplexType):
                            if prop.type._props:
                                sub.add()._read_xml(child)
                            else:
                                sub.add()._read_xml(etree.tostring(child))
                    elif isinstance(sub, ComplexType):
                        if sub._props:
                            sub._read_xml(child)
                        else:
                            setattr(self, tag, etree.tostring(child))
                    else:
                        raise NotImplementedError
                elif issubclass(prop.type, (SimpleType, SimpleTypeElement, str)):
                    setattr(self, tag, child.text)
                elif issubclass(prop.type, (datetime.datetime, datetime.date, int, Decimal)):
                    v = child.text
                    # conveter para datetime?
                    setattr(self, tag, v)
                else:
                    raise NotImplementedError

    def _validar(self):
        """Validar o conteúdo do elemento conforme regras especificadas no xsd"""
        res = []
        cls = self._cls or self
        if cls._xml_props:
            for k, prop in cls._xml_props.items():
                v = getattr(self, k, None)
                if v is None:
                    continue
                if isinstance(prop, Element) and (restriction := getattr(prop._cls, '_restriction', None)):
                    if msg := restriction.validate(v):
                        res.append(k + ': ' + msg)
                if isinstance(v, ComplexType):
                    if isinstance(prop, Element) and not prop._required and self._xml(k):
                        res.extend(v._validar())
        return res

    def _required(self):
        req = (self.min_occurs is None) or (self.min_occurs > 0)
        if self._parent and req:
            req = req and self._parent._required()
        return req

    @classmethod
    def fromstring(cls, s: str) -> Self:
        obj = cls()
        obj._read_xml(s)
        return obj

    def __iter__(self):
        return iter(self._list)

    def __str__(self):
        return self._xml()

    def dict(self):
        if self._props:
            r = {}
            for k, prop in self._props.items():
                v = getattr(self, k, None)
                if v is None:
                    continue
                if isinstance(v, ComplexType):
                    v = v.dict()
                    if not v:
                        continue
                elif isinstance(v, ElementList):
                    v = [item.dict() if isinstance(item, ComplexType) else v for item in v if issubclass(prop.type, ComplexType)]
                    if not v:
                        continue
                r[k] = v
            return r


class Element:
    _restriction = None
    _caption: str = None
    _tipo: str = None
    _tag: str = None

    def __init__(self, *args, **kwargs):
        pass

    def _xml(self):
        raise NotImplemented

    def __set_name__(self, owner, name):
        if not self._tag:
            self._tag = name


class Alias:
    def __init__(self, element):
        self.element = element


class Attribute:
    _base_type = None
    _filter = None
    _cls = None
    _pattern: str = None
    _required = None

    def __init__(
            self, type=None, default=None, pattern: str = None, min_length=None, max_length=None, required=None,
            enumeration=None
    ):
        self.type = type
        self._default = default
        self._pattern = pattern
        self._min_length = min_length
        self._max_length = max_length
        self._required = required


class TString(str):
    pass


class Restriction:
    def __init__(self, base=None, white_space=None, enumeration=None, pattern=None, min_length=None, max_length=None):
        self.base = base
        self.white_space = white_space
        self.enumeration = enumeration
        self.pattern = pattern
        if isinstance(min_length, str):
            min_length = int(min_length)
        self.min_length = min_length
        if isinstance(max_length, str):
            max_length = int(max_length)
        self.max_length = max_length

    def validate(self, value):
        if not isinstance(value, str):
            value = str(value)
        if self.min_length and len(value) < self.min_length:
            return f'O campo deve ter no mínimo {self.min_length} caracteres.'
        if self.max_length and len(value) > self.max_length:
            return f'O campo deve ter no máximo {self.max_length} caracteres.'
        if self.pattern and not re.match(self.pattern, value):
            return f'{value} é um valor inválido.'


class SimpleTypeElement(Element):
    _value = None

    def __init__(self, value=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._value = value

    def __set__(self, instance, value):
        if instance is not None:
            self._value = value

    def _xml(self, t: str = None):
        t = t or self._tag
        return tag(t, self._value)

    def __bool__(self):
        return bool(self._value)


class ID(SimpleTypeElement):
    pass


class base64Binary(SimpleTypeElement):
    pass


class anyURI(SimpleTypeElement):
    pass


class string(str):
    pass


class dateTime(SimpleTypeElement):
    pass


class TXML(str):
    _value = None

    def _xml(self, name=None):
        if not self._value:
            return ''
        return self._value

    def __set__(self, instance, value):
        if instance is not None:
            self._value = value


class Choice:
    def __init__(self, *args):
        self.choices: list[str] = list(args)
        # tratamento especial para CNPJ e CPF
        self._cnpj_cpf = 'CNPJ' in self.choices and 'CPF' in self.choices

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self._cnpj_cpf:
            return instance.CNPJ or instance.CPF

    def __set__(self, instance, value):
        if instance is not None:
            # decide automaticamente se CNPJ ou CPF
            if self._cnpj_cpf:
                if len(value) == 14:
                    instance.CNPJ = value
                else:
                    instance.CPF = value


class XmlSignature(str):
    pass
