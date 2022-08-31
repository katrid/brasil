from __future__ import annotations
import re
import datetime
from decimal import Decimal
from lxml import etree
from .utils.xml_utils import tag


class SimpleType:
    pass


class ElementType(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        new_cls = super().__new__(cls, name, bases, attrs, **kwargs)
        mod = attrs.get('__module__')
        if mod == 'brasil.dfe.xsd':
            return new_cls
        old_props = new_cls._xml_props
        new_cls._xml_props = {k: v for k, v in attrs.items() if isinstance(v, (Element, Attribute))}
        if old_props:
            new_cls._xml_props.update(old_props)
        new_cls._name = name
        return new_cls


class ComplexType(SimpleType, metaclass=ElementType):
    _name: str = None
    _xmlns: str = None
    _xml_props: dict = None
    _cls: 'ComplexType' = None
    _xmltmp = None
    _parent = None
    _max_occurs = None

    def __init__(self, cls=None,  min_occurs=None, max_occurs=None):
        self._cls = cls
        self.min_occurs = min_occurs
        self.max_occurs = max_occurs
        if max_occurs is None and self._max_occurs:
            self.max_occurs = self._max_occurs
        self._list = []

        if self._xml_props:
            for k, v in self._xml_props.items():
                if v._cls and ((isinstance(v._cls, type) and issubclass(v._cls, ComplexType)) or isinstance(v._cls, ComplexType)):
                    v = v._cls()
                elif v._default:
                    v = v._default
                # elif self._required() and v._base_type is Decimal:
                #     v = 0
                else:
                    v = None
                setattr(self, k, v)

    def _add_to_class(self, name, obj):
        self._cls._xml_props[name] = obj
        setattr(self._cls, name, obj)

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
        if self._list:
            return ''.join([child._xml(name) for child in self._list])
        kwargs = {}
        args = []
        cls = self._cls or self
        if cls._xml_props:
            for k, prop in cls._xml_props.items():
                v = getattr(self, k, None)
                if v is None:
                    continue
                if prop._base_type is datetime.datetime and isinstance(v, datetime.datetime):
                    v = v.strftime('%Y-%m-%dT%H:%M:%S-03:00')
                elif prop._base_type is datetime.date and isinstance(v, datetime.date):
                    v = v.strftime('%Y-%m-%d')
                elif prop._base_type is Decimal and v == 0 and prop._optional:
                    continue
                elif prop._base_type is Decimal and isinstance(v, Decimal) and prop._tam:
                    fmt = '{:.%sf}' % prop._tam[1]
                    v = string.format(fmt, v)
                elif isinstance(v, (int, Decimal)):
                    v = str(v)
                elif isinstance(v, datetime.datetime):
                    v = v.strftime('%Y-%m-%dT%H:%M:%S-03:00')
                if prop._filter:
                    v = ''.join(filter(prop._filter, v))
                if isinstance(prop, Attribute):
                    kwargs[k] = v
                elif isinstance(prop, TXML):
                    args.append(prop._xml())
                elif isinstance(prop._cls, type) and issubclass(prop._cls, str):
                    if v and not v.startswith('<![CDATA['):
                        args.append(tag(k, v.replace('&', '&amp;')))
                    else:
                        args.append(tag(k, v))
                elif isinstance(prop, ComplexType):
                    if isinstance(v, str):
                        args.append(v)
                    else:
                        xml = v._xml(k)
                        if xml:
                            args.append(xml)
        if not args:
            return ''
        if self._xmlns:
            kwargs['xmlns'] = self._xmlns
        self._xmltmp = tag(name or self.__class__.__name__, *args, **kwargs)
        return self._xmltmp

    def _clear(self):
        self._xmltmp = None

    def _read_xml(self, xml):
        if isinstance(xml, (str, bytes)):
            node = etree.fromstring(xml)
        else:
            node = xml
        for k in node.attrib:
            setattr(self, k, node.attrib[k])

        for child in node:
            tag = child.tag.split('}', 1)[-1]
            prop = self._xml_props.get(tag)
            if prop:
                if issubclass(prop._cls, str) or prop._cls is str:
                    v = child.text
                    setattr(self, tag, v)
                else:
                    sub = getattr(self, tag)
                    if sub.max_occurs and (sub.max_occurs > 1 or self.max_occurs == -1):
                        sub.add()._read_xml(child)
                    else:
                        sub._read_xml(child)

    def _validar(self):
        """Validar o conteúdo do elemento conforme regras especificadas no xsd"""
        res = []
        cls = self._cls or self
        if cls._xml_props:
            for k, prop in cls._xml_props.items():
                v = getattr(self, k, None)
                if getattr(prop, '_choice', None):
                    print(prop._choice)
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


class Element(ComplexType):
    _restriction = None
    _caption: str = None
    _tipo: str = None

    def __init__(self, cls=None, min_occurs=None, max_occurs=None, documentation: list[str]=None, *args, **kwargs):
        if min_occurs is None:
            min_occurs = 1
        super().__init__(cls, min_occurs=min_occurs, max_occurs=max_occurs)
        self.documentation = documentation
        if documentation:
            self._caption = documentation[0]
        self._tipo = kwargs.get('tipo')
        self._tam = kwargs.get('tam')
        self._base_type = kwargs.get('base_type')
        self._optional = kwargs.get('optional')
        self._filter = kwargs.get('filter')
        self._default = kwargs.get('default')
        self.min_occurs = min_occurs
        self.max_occurs = max_occurs
        self._values = {}
        # if cls is None and self._xml_props:
        #     for k, v in self._xml_props.items():
        #         v = getattr(self, k)
        #         if isinstance(v, Element):
        #             setattr(self, k, v())
        #         else:
        #             setattr(self, k, None)

    def __call__(self, *args, **kwargs):
        if issubclass(self._cls, str):
            return None
        _kwargs = {}
        if self.min_occurs:
            _kwargs['min_occurs'] = self.min_occurs
        if self.max_occurs:
            _kwargs['max_occurs'] = self.max_occurs
        new_obj = self._cls(**_kwargs)
        if isinstance(new_obj, ComplexType):
            for k, prop in new_obj._xml_props.items():
                if isinstance(prop, Element):
                    if issubclass(prop._cls, str):
                        if prop._default:
                            v = prop._default
                        else:
                            v = None
                    else:
                        v = prop()
                elif isinstance(v, Attribute):
                    if v._default:
                        v = v._default
                    else:
                        v = None
                if v is not None:
                    setattr(new_obj, k, v)
        return new_obj

    def __set_name__(self, owner, name):
        self._parent = owner


class Alias:
    def __init__(self, element):
        self.element = element


class Attribute:
    _base_type = None
    _filter = None
    _cls = None
    _required = None

    def __init__(self, type, default=None):
        self.type = type
        self._default = default


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
    pass


class ID(SimpleTypeElement):
    pass


class base64Binary(str):
    pass


class anyURI(SimpleTypeElement):
    pass


class string(str):
    pass


class dateTime(SimpleTypeElement):
    pass


class TXML(SimpleTypeElement):
    _value = None

    def _xml(self, name=None):
        if not self._value:
            return ''
        return self._value

    def __set__(self, instance, value):
        if instance is not None:
            self._value = value
