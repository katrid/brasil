from __future__ import annotations

import os
from typing import List, Self

from lxml import etree
from lxml.etree import _Element


class Parser:
    current_file: str = None

    def __init__(self):
        self.schemas: dict[str, 'XsSchema'] = {}

    def parse(self, xml: _Element):
        tag = _get_tag(xml.tag)
        if tag == 'schema':
            schema = XsSchema()
            schema.name = self.current_file
            schema.parse(xml)
            self.schemas[schema.name] = schema

    def fromstring(self, xml: str | bytes):
        node = etree.fromstring(xml)
        self.parse(node)

    def fromfile(self, filename: str):
        self.current_file = os.path.basename(filename)
        with open(filename, 'rb') as f:
            self.fromstring(f.read())

    def compile_dir(self, dirname: str):
        for fname in os.listdir(dirname):
            if fname.endswith('.xsd'):
                self.fromfile(os.path.join(dirname, fname))

    def compile(self) -> str:
        stream = []
        for schema in self.schemas.values():
            schema.compile(stream)
        return '\n'.join(stream)


class XsRestriction:
    base: str = None
    white_space: str = None
    min_length: int = None
    max_length: int = None
    pattern: str = None
    enumeration: List[str]

    def __init__(self):
        self.enumeration = []

    def read_node(self, xml: _Element):
        self.base = xml.attrib.get('base')
        for child in xml:
            tag = _get_tag(child.tag)
            if tag == 'whiteSpace':
                self.white_space = child.attrib.get('value')
            elif tag == 'enumeration':
                self.enumeration.append(child.attrib.get('value'))
            elif tag == 'minLength':
                self.min_length = int(child.attrib.get('value'))
            elif tag == 'maxLength':
                self.max_length = int(child.attrib.get('value'))
            elif tag == 'pattern':
                self.pattern = child.attrib.get('value')


class XsBaseElement:
    name: str = None
    xmlns: str = None
    documentation: List[str]
    parent: XsBaseElement = None

    def __init__(self):
        self.documentation = []

    def read_node(self, xml: _Element):
        for child in xml:
            self.read_child_node(_get_tag(child.tag), child)

    def read_child_node(self, tag: str, child: _Element):
        if tag == 'annotation':
            self.read_node(child)
        elif tag == 'documentation':
            self.documentation.append(child.text)

    def compile(self, indent: int, stream: List[str]):
        pass

    def _prepare(self):
        pass

    def get_deps(self):
        yield


class XsAttribute(XsBaseElement):
    type: str | XsSimpleType = None
    use: str = None

    def read_node(self, xml: _Element):
        super().read_node(xml)
        if 'name' in xml.attrib:
            self.name = xml.attrib.get('name')
        if 'type' in xml.attrib:
            self.type = xml.attrib.get('type')
        if 'use' in xml.attrib:
            self.use = xml.attrib.get('use')

    def read_child_node(self, tag: str, child: _Element):
        super().read_child_node(tag, child)
        if tag == 'simpleType':
            simple_type = XsSimpleType()
            simple_type.parent = self
            simple_type.read_node(child)
            self.type = simple_type
            return simple_type

    def compile(self, indent: int, stream: List[str]):
        indent_str = '    ' * indent
        tp = self.type
        kw = {}
        if isinstance(tp, XsSimpleType):
            tp = self.type.type
            kw = self.type.get_kwargs()
        tp = BASE_TYPE_MAP.get(tp, tp)
        ks = ''
        if kw:
            ks = f'({_kwargs_to_str(kw)})'
        stream.append(f"""{indent_str}{self.name}: Annotated[{tp}, Attribute{ks}] = None""")

    def _prepare(self):
        if isinstance(self.type, XsSimpleType):
            self.type._prepare()

    def get_deps(self):
        if isinstance(self.type, XsSimpleType):
            yield self.type.name
        elif isinstance(self.type, str):
            yield self.type


class XsElement(XsBaseElement):
    type: str | XsComplexType | XsSimpleType = None
    base: str = None
    max_occurs: int = None
    min_occurs: int = None
    sequence: List[XsSequence] = None

    def read_node(self, xml: _Element):
        super().read_node(xml)
        tag = _get_tag(xml.tag)
        if 'name' in xml.attrib:
            self.name = xml.attrib['name']
        if 'ref' in xml.attrib:
            ref = xml.attrib['ref']
            # signature special case
            self.name = NAME_REF_MAP.get(ref, ref)
            if ref == 'ds:Signature':
                self.base = 'XmlSignature'
            else:
                self.base = NAME_REF_TYPE.get(ref, 'str')
        if tag == 'element' or tag == 'sequence':
            if 'type' in xml.attrib:
                self.type = xml.attrib['type']
            if 'maxOccurs' in xml.attrib:
                if (mo := xml.attrib.get('maxOccurs', '1')) == 'unbounded':
                    mo = -1
                self.max_occurs = int(mo)
            if 'minOccurs' in xml.attrib:
                self.min_occurs = int(xml.attrib.get('minOccurs', 1))

    def read_child_node(self, tag: str, child: _Element):
        super().read_child_node(tag, child)
        if tag == 'complexType':
            complex_type = XsComplexType()
            complex_type.parent = self
            complex_type.read_node(child)
            self.type = complex_type
            return complex_type
        elif tag == 'simpleType':
            simple_type = XsSimpleType()
            simple_type.parent = self
            simple_type.read_node(child)
            self.type = simple_type
            return simple_type
        elif tag == 'choice':
            choice = XsChoice()
            choice.parent = self
            choice.read_node(child)
            self.sequence.append(choice)
            return choice
        elif tag == 'sequence':
            sequence = XsSequence()
            sequence.parent = self
            sequence.read_node(child)
            self.sequence.append(sequence)
            return sequence

    def compile(self, indent: int, stream: List[str]):
        indent_str = '    ' * indent
        tp = self.type
        if isinstance(tp, XsComplexType):
            self.type.compile(indent, stream)
            tp = tp.name
            if self.parent is None:
                return
        elif isinstance(tp, str) and self.parent is None:
            tp = BASE_TYPE_MAP.get(tp, tp)
            stream.append('')
            stream.append(f'{indent_str}class {self.name}({tp}):')
            if self.documentation:
                stream.append(f'{indent_str}    """{'\n'.join(self.documentation).replace('"', '\\"')}"""')
            if self.xmlns:
                stream.append(f'{indent_str}    _xmlns = "{self.xmlns}"')
            else:
                stream.append(f'{indent_str}    pass')
            stream.append('')
            return
        elif isinstance(tp, XsSimpleType):
            tp = tp.type
        elif self.base:
            tp = self.base
        tp = BASE_TYPE_MAP.get(tp, tp)
        if self.max_occurs is not None and (self.max_occurs > 1 or self.max_occurs == -1):
            tp = f'List[{tp}]'
        stream.append(f'{indent_str}{self.name}: Annotated[{tp}, Element] = None')

    def _prepare(self):
        super()._prepare()
        if isinstance(self.type, XsComplexType):
            if self.parent is None:
                self.type.name = self.name
            else:
                self.type.name = f'_{self.name}'
            if not self.type.documentation:
                self.type.documentation = self.documentation
            self.type._prepare()
        elif isinstance(self.type, XsSimpleType):
            self.type._prepare()
        if self.sequence:
            for seq in self.sequence:
                seq._prepare()

    def get_deps(self):
        if isinstance(self.type, XsComplexType):
            yield from self.type.get_deps()
            yield self.type.name
        elif isinstance(self.type, XsSimpleType):
            yield from self.type.get_deps()
            yield self.type.name
        elif isinstance(self.type, str):
            yield self.type
        if self.sequence:
            for seq in self.sequence:
                yield from seq.get_deps()


class XsSimpleType(XsBaseElement):
    type: str = None
    restrictions: List[XsRestriction]

    def __init__(self):
        super().__init__()
        self.restrictions = []

    def read_node(self, xml: _Element):
        super().read_node(xml)
        if 'name' in xml.attrib:
            self.name = xml.attrib['name']

    def read_child_node(self, tag: str, child: _Element):
        super().read_child_node(tag, child)
        if tag == 'restriction':
            restriction = XsRestriction()
            restriction.read_node(child)
            self.restrictions.append(restriction)
            return restriction

    def get_kwargs(self):
        kw = {}
        for r in self.restrictions:
            if r.pattern:
                kw['pattern'] = r.pattern
            if r.min_length is not None:
                kw['min_length'] = r.min_length
            if r.max_length is not None:
                kw['max_length'] = r.max_length
            if r.enumeration:
                kw['enumeration'] = r.enumeration
        return kw

    def _prepare(self):
        if not self.type:
            if self.restrictions:
                self.type = self.restrictions[0].base
        super()._prepare()

    def compile(self, indent: int, stream: List[str]):
        indent_str = '    ' * indent
        stream.append('')
        # decimal special type
        base = BASE_TYPE_MAP.get(self.type, self.type)
        if self.name.startswith('TDec_'):
            base = 'Decimal'
        stream.append(f'{indent_str}class {self.name}({base}):')
        if self.documentation:
            stream.append(f'{indent_str}    """{'\n'.join(self.documentation).replace('"', '\\"')}"""')
        if base == 'Decimal':
            tam = self.name.split('_')[1]
            tam = f'({int(tam[0:2])}, {int(tam[2:4])})'
            stream.append(f'{indent_str}    _xs_dec = {tam}')
            stream.append(f'{indent_str}    _xs_optional = {self.name.endswith('Opc')}')
        else:
            stream.append(f'{indent_str}    pass')
        stream.append('')

    def get_deps(self):
        if self.type:
            yield self.type


class XsSequence(XsElement):
    elements: List[XsElement]
    sequence = List[Self]

    def __init__(self):
        super().__init__()
        self.elements = []
        self.sequence = []

    def read_child_node(self, tag: str, child: _Element):
        super().read_child_node(tag, child)
        if tag == 'element':
            element = XsElement()
            element.parent = self
            element.read_node(child)
            self.sequence.append(element)
            self.elements.append(element)
            return element
        elif tag == 'any':
            return self.read_node(child)

    def compile(self, indent: int, stream: List[str]):
        for seq in self.sequence:
            seq.compile(indent, stream)
        # for el in self.elements:
        #     el.compile(indent, stream)

    def _prepare(self):
        for el in self.elements:
            if self.max_occurs is not None:
                el.max_occurs = self.max_occurs
            if self.min_occurs is not None:
                el.min_occurs = self.min_occurs
            el._prepare()
        super()._prepare()

    def get_deps(self):
        for seq in self.sequence:
            yield from seq.get_deps()
        for el in self.elements:
            yield from el.get_deps()


class XsChoice(XsSequence):
    def compile(self, indent: int, stream: List[str]):
        super().compile(indent, stream)
        indent_str = '    ' * indent
        name = '_'.join([el.name for el in self.elements])
        if name:
            choices = ', '.join([f'"{el.name}"' for el in self.elements])
            stream.append(f'{indent_str}{name} = Choice({choices})')


class XsComplexType(XsElement):
    content: XsSimpleContent = None
    attributes: List[XsAttribute]

    def __init__(self):
        super().__init__()
        self.sequence = []
        self.attributes = []

    def read_child_node(self, tag: str, child: _Element):
        super().read_child_node(tag, child)
        if tag == 'attribute':
            attribute = XsAttribute()
            attribute.read_node(child)
            self.attributes.append(attribute)
            return attribute
        elif tag == 'simpleContent':
            content = XsSimpleContent()
            content.parent = self
            content.read_node(child)
            self.content = content
            return content

    def compile(self, indent: int, stream: List[str]):
        indent_str = '    ' * indent
        stream.append('')
        stream.append(f'{indent_str}class {self.name}(ComplexType):')
        if self.content:
            self.content.compile(indent + 1, stream)
        if self.documentation:
            stream.append(f'{indent_str}    """{'\n'.join(self.documentation).replace('"', '\\"')}"""')
        for attr in self.attributes:
            attr.compile(indent + 1, stream)
        for el in self.sequence:
            el.compile(indent + 1, stream)
        stream.append('')

    def _prepare(self):
        super()._prepare()
        if not self.documentation and self.sequence:
            for seq in self.sequence:
                if seq.documentation:
                    self.documentation = seq.documentation
        for attr in self.attributes:
            attr._prepare()

    def get_deps(self):
        for attr in self.attributes:
            yield from attr.get_deps()
        for el in self.sequence:
            yield from el.get_deps()


class XsSimpleContent(XsComplexType):
    extension: str = None

    def read_child_node(self, tag: str, child: _Element):
        super().read_child_node(tag, child)
        if tag == 'extension':
            self.extension = child.attrib.get('base')

    def compile(self, indent: int, stream: List[str]):
        indent_str = '    ' * indent
        stream.append(f'{indent_str}value: {BASE_TYPE_MAP.get(self.extension, self.extension)} = None')


class XsSchema:
    name: str = None
    xmlns: str = None
    elements: List[XsBaseElement]
    includes: List[str]

    def __init__(self):
        super().__init__()
        self.includes = []
        self.elements = []

    def parse(self, xml: _Element):
        tag = _get_tag(xml.tag)
        if tag == 'schema':
            self.xmlns = xml.attrib.get('targetNamespace')
            for child in xml:
                tag = _get_tag(child.tag)
                if tag == 'element':
                    element = XsElement()
                    element.xmlns = self.xmlns
                    element.read_node(child)
                    self.elements.append(element)
                elif tag == 'complexType':
                    complex_type = XsComplexType()
                    complex_type.read_node(child)
                    self.elements.append(complex_type)
                elif tag == 'simpleType':
                    simple_type = XsSimpleType()
                    simple_type.read_node(child)
                    self.elements.append(simple_type)
                elif tag == 'include':
                    self.includes.append(child.attrib.get('schemaLocation'))

    def compile(self, stream: List[str]):
        stream.append(f'# Generated by xsd2py.py')
        stream.append(f'# xmlns: {self.xmlns}')
        # prepare symbols
        for el in self.elements:
            el._prepare()
        stream.extend([
            'from typing import List, Annotated',
            'from datetime import date, datetime',
            'from decimal import Decimal',
            '',
            'from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature'
        ])
        for i in self.includes:
            s = i.rsplit('.', 1)[0].replace('.', '')
            stream.append(f'from .{s} import *')
        stream.append('')
        types = adjust_deps({s.name: s for s in self.elements if s.name})
        for el in types:
            el.compile(0, stream)
        stream.append('')

    def to_python(self) -> str:
        stream = []
        self.compile(stream)
        return '\n'.join(stream)

    @property
    def module_name(self):
        return self.name.rsplit('.', 1)[0].replace('.', '')


NS_LEN = len('{http://www.w3.org/2001/XMLSchema}')


def _get_tag(tag_name: str):
    if isinstance(tag_name, str):
        return tag_name[NS_LEN:]


def _kwargs_to_str(kwargs: dict):
    return ', '.join([f"{k}={'\'' + v + '\'' if isinstance(v, str) else v}" for k, v in kwargs.items()])


def adjust_deps(types):
    res = []
    for k, t in types.items():
        if not t.name:
            continue
        k = t.name
        for i, sub in enumerate(res):
            deps = list(sub.get_deps())
            if k in deps:
                res.insert(i, t)
                for dep in t.get_deps():
                    v = types.get(dep)
                    if v and v in res:
                        if res.index(v) > i:
                            res.pop(res.index(v))
                        res.insert(i, v)
                break
        else:
            res.append(t)
    return res


BASE_TYPE_MAP = {
    'xs:string': 'str',
    'xs:ID': 'str',
    'xs:dateTime': 'datetime',
    'TString': 'str',
    'ds:SignedInfoType': 'TXML',
    'ds:SignatureValueType': 'TXML',
    'ds:KeyInfoType': 'TXML',
    'ds:TransformType': 'TXML',
    'ds:X509DataType': 'TXML',
    'ds:DigestValueType': 'TXML',
    'ds:ReferenceType': 'TXML',
    'ds:TransformsType': 'TXML',
    'ds:SignatureType': 'TXML',
    'xs:base64Binary': 'base64Binary',
    'nfe:TString': 'TString',
    'xs:token': 'str',
    'xs:unsignedShort': 'int',
}

NAME_REF_MAP = {
    'ds:Signature': 'Signature',
}

NAME_REF_TYPE = {
    'ds:Signature': 'str',
}
