import re
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

    def __init__(self, cls=None,  min_occurs=None, max_occurs=None):
        self._cls = cls
        self.min_occurs = min_occurs
        self.max_occurs = max_occurs
        self._list = []

    def _add_to_class(self, name, obj):
        self._cls._xml_props[name] = obj
        setattr(self._cls, name, obj)

    def add(self, **kwargs):
        new_obj = self.__class__()
        for k, v in kwargs.items():
            setattr(new_obj, k, v)
        self._list.append(new_obj)
        return new_obj

    def append(self, obj):
        self._list.append(obj)

    def _xml(self, name=None):
        if self._list:
            return ''.join([child._xml(name) for child in self._list])
        kwargs = {}
        args = []
        if self._xmlns:
            kwargs['xmlns'] = self._xmlns
        cls = self._cls or self
        if cls._xml_props:
            for k, prop in cls._xml_props.items():
                v = getattr(self, k, None)
                if v is None:
                    continue
                if isinstance(v, (int, Decimal)):
                    v = str(v)
                if isinstance(prop, Attribute):
                    kwargs[k] = v
                elif issubclass(prop._cls, str):
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
        return tag(name or self.__class__.__name__, *args, **kwargs)

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
                    getattr(self, tag)._read_xml(child)

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
                    res.extend(v._validar())
        return res


class Element(ComplexType):
    _restriction = None

    def __init__(self, cls=None, min_occurs=None, max_occurs=None, *args, **kwargs):
        if min_occurs is None:
            min_occurs = 1
        super().__init__(cls, min_occurs=min_occurs, max_occurs=max_occurs)
        self.min_occurs = min_occurs
        self.max_occurs = max_occurs
        self._values = {}
        if cls is None and self._xml_props:
            for k, v in self._xml_props.items():
                v = getattr(self, k)
                if isinstance(v, Element):
                    setattr(self, k, v())
                else:
                    setattr(self, k, None)

    def __getattr__(self, item):
        return getattr(self._cls, item)

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
            for k, v in new_obj._xml_props.items():
                v = getattr(self, k)
                if isinstance(v, Element):
                    if v._cls is str or issubclass(v._cls, str):
                        v = None
                    else:
                        v = v()
                elif isinstance(v, Attribute):
                    v = None
                setattr(new_obj, k, v)
        return new_obj


class Alias:
    def __init__(self, element):
        self.element = element


class Attribute:
    def __init__(self, type):
        self.type = type


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
