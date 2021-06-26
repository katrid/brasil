from __future__ import annotations
import os
import sys
from lxml import etree


class Include:
    name: str = None


class Restriction:
    base: str = None
    white_space: str = None
    pattern: str = None
    min_length: str = None
    max_length: str = None

    def __init__(self):
        self.enumeration = []

    def read(self, el):
        self.base = el.attrib.get('base')

        for child in el:
            if child.tag == '{http://www.w3.org/2001/XMLSchema}whiteSpace':
                self.white_space = child.attrib.get('value')
            elif child.tag == '{http://www.w3.org/2001/XMLSchema}enumeration':
                self.enumeration.append(child.attrib['value'])
            elif child.tag == '{http://www.w3.org/2001/XMLSchema}pattern':
                self.pattern = child.attrib['value']
            elif child.tag == '{http://www.w3.org/2001/XMLSchema}minLength':
                self.min_length = child.attrib['value']
            elif child.tag == '{http://www.w3.org/2001/XMLSchema}maxLength':
                self.max_length = child.attrib['value']

    def render(self, indent):
        kwargs = {}
        if self.base:
            kwargs['base'] = self.base
        if self.white_space:
            kwargs['white_space'] = self.white_space
        if self.pattern:
            kwargs['pattern'] = self.pattern
        if self.min_length:
            kwargs['min_length'] = self.min_length
        if self.max_length:
            kwargs['max_length'] = self.max_length
        return f'{" " * (indent * 4)}_restriction = Restriction({"".join([k + f"""=r"{v}", """ for k, v in kwargs.items()])}enumeration={self.enumeration})'


class Attribute:
    name: str = None
    type_: str = None
    use: str = None

    def read(self, el):
        self.name = el.attrib['name']
        self.type_ = el.attrib.get('type')
        self.use = el.attrib.get('use')

    def render(self, indent):
        tp = self.type_
        if tp and ':' in tp:
            tp = tp.split(':', 1)[1]
        return f'{" " * (indent * 4)}{self.name}: str = Attribute({tp})'


def adjust_deps(types):
    res = []
    for k, t in types.items():
        for i, sub in enumerate(res):
            if k in sub.deps:
                res.insert(i, t)
                for dep in t.deps:
                    v = types.get(dep)
                    if v and v in res:
                        if res.index(v) > i:
                            res.pop(res.index(v))
                        res.insert(i, v)
                break
        else:
            res.append(t)
    return res


class SimpleType:
    parent: SimpleType = None
    name: str = None
    complex_type: ComplexType = None
    simple_type: SimpleType = None
    _min_occurs: int = None
    _max_occurs: int = None
    type_: str = None
    restriction: Restriction = None

    def __init__(self, parent=None):
        if isinstance(parent, Element):
            parent = parent.parent
        self.documentation: list[str] = []
        self.parent = parent
        self.types = {}
        self.choices = []
        self.sequence = []
        self.enumeration = []
        self.deps = []

    @property
    def min_occurs(self):
        return self._min_occurs

    @min_occurs.setter
    def min_occurs(self, value):
        if isinstance(value, str) and value.isdigit():
            self._min_occurs = int(value)
        else:
            self._min_occurs = value

    @property
    def max_occurs(self):
        return self._max_occurs

    @max_occurs.setter
    def max_occurs(self, value):
        if value == 'unbounded':
            self._max_occurs = -1
        elif isinstance(value, str) and value.isdigit():
            self._max_occurs = int(value)
        else:
            self._max_occurs = value

    def read(self, el):
        self.name = el.attrib.get('name')
        if self.name == 'pass':
            self.name = 'pass_'
        self.type_ = el.attrib.get('type')
        self.min_occurs = el.attrib.get('minOccurs')
        self.max_occurs = el.attrib.get('maxOccurs')
        if self.type_ and self.type_ not in self.deps:
            if ':' in self.type_:
                self.type_ = self.type_.split(':', 1)[1]
            self.deps.append(self.type_)

        for child in el:
            self.read_node(child)

    def read_nodes(self, el):
        for child in el:
            self.read_node(child)

    def read_node(self, el):
        if el.tag == '{http://www.w3.org/2001/XMLSchema}annotation':
            self.read_nodes(el)
        elif el.tag == '{http://www.w3.org/2001/XMLSchema}documentation':
            self.documentation.append(el.text)
        elif el.tag == '{http://www.w3.org/2001/XMLSchema}element':
            element = Element(self)
            element.read(el)
            self.deps.extend(element.deps)
            self.sequence.append(element)
        elif el.tag == '{http://www.w3.org/2001/XMLSchema}sequence':
            self.read_nodes(el)
        elif el.tag == '{http://www.w3.org/2001/XMLSchema}restriction':
            self.restriction = Restriction()
            self.restriction.read(el)
        elif el.tag == '{http://www.w3.org/2001/XMLSchema}choice':
            choices = [child.attrib.get('name') for child in el if child.tag.endswith('element')]
            self.choices.append(choices)
            self.read_nodes(el)
        elif el.tag == '{http://www.w3.org/2001/XMLSchema}complexType':
            self.complex_type = ComplexType(parent=self)
            self.complex_type.read(el)
            self.deps.extend(self.complex_type.deps)
            self.complex_type.name = self.name
        elif el.tag == '{http://www.w3.org/2001/XMLSchema}simpleType':
            self.simple_type = SimpleType(parent=self)
            self.simple_type.read(el)
            self.deps.extend(self.simple_type.deps)
            self.simple_type.name = self.name
        elif el.tag == '{http://www.w3.org/2001/XMLSchema}attribute':
            attr = Attribute()
            attr.read(el)
            if isinstance(attr.type_, str) and ':' in attr.type_:
                attr.type_ = attr.type_.split(':', 1)[1]
            self.deps.append(attr.type_)
            self.sequence.append(attr)

    def render(self, indent=0):
        stream = []
        level0 = ' ' * (indent * 4)
        level1 = ' ' * ((indent + 1) * 4)
        if self.name:
            base_type = self.type_
            if not base_type and self.restriction:
                base_type = self.restriction.base
            elif not base_type:
                if self.__class__.__name__ == 'ComplexType':
                    base_type = 'Element'
                else:
                    base_type = 'str'
            if base_type == 'xs:string':
                base_type = 'str'
            elif ':' in base_type:
                base_type = base_type.split(':', 1)[1]

            stream.append(f'\n{level0}class {self.name}({base_type}):')
            if self.documentation:
                doc = "\n".join([s.strip().replace('"', '\\"') for s in self.documentation])
                stream.append(f'{level1}"""{doc}"""')

            if self.min_occurs:
                stream.append(f'{level1}_min_occurs = {self.min_occurs}')
            if self.max_occurs:
                stream.append(f'{level1}_max_occurs = {self.max_occurs}')

            if self.restriction:
                stream.append(self.restriction.render(indent + 1))

            if self.choices:
                stream.append(f'{level1}_choice = {self.choices}')

            if self._max_occurs:
                args = [s.name for s in self.sequence if s.name]
                stream.append(f'\n{level1}def add(self, {", ".join([a + "=None" for a in args])}) -> {self.qualname()}:')
                stream.append(f'{" " * ((indent + 2) * 4)}return super().add({", ".join([a + "=" + a for a in args])})')
                stream.append('')
            elif not self.sequence:
                stream.append(f'{level1}pass')


            types = []
            if self.types:
                types = adjust_deps(self.types)
                for tp in types:
                    stream.append(tp.render(indent + 1))

            for seq in self.sequence:
                if seq not in types:
                    stream.append(seq.render(indent + 1))
        if indent == 0:
            stream.append('')
        return '\n'.join(stream) + '\n'

    def qualname(self):
        name = self.name
        if self.parent and self.parent.name:
            name = self.parent.qualname() + '.' + name
        return name

    def __str__(self):
        return self.render()


class Element(SimpleType):
    ref: str = None

    def render(self, indent=0):
        s = ''
        name = self.name
        el_type = self.type_ or self.ref or 'str'
        if ':' in el_type:
            el_type = el_type.split(':', 1)[1]
        if not name:
            name = el_type

        args = ''
        is_lst = False
        if self.min_occurs:
            args += f', min_occurs={self.min_occurs}'
            if int(self.min_occurs) > 0:
                is_lst = True
        if self.max_occurs:
            max_occurs = self.max_occurs
            if max_occurs == 'unbounded':
                max_occurs = -1
            args += f', max_occurs={max_occurs}'
            if int(max_occurs) > 0 or max_occurs == -1:
                is_lst = True

        if self.complex_type:
            self.complex_type.type_ = 'ComplexType'
            self.complex_type.documentation = self.documentation
            self.complex_type.min_occurs = self.min_occurs
            self.complex_type.max_occurs = self.max_occurs
            s = self.complex_type.render(indent)
            el_type = self.name
            if is_lst:
                ref_type = f'List[{el_type}]'
            else:
                ref_type = el_type
            return s + f'{" " * (indent * 4)}{name}: {ref_type} = Element({el_type}{args})'
        else:
            if is_lst:
                ref_type = f'List[{el_type}]'
            else:
                ref_type = el_type
            if indent == 0:
                return s + f'class {name}({ref_type}):\n    pass\n'
            return s + f'{" " * (indent * 4)}{name}: {ref_type} = Element({el_type}{args})'

    def read(self, el):
        super().read(el)
        self.ref = el.get('ref')


class ComplexType(SimpleType):
    pass


class Module(SimpleType):
    def __init__(self, xsd, lst):
        super().__init__()
        self.xsd = xsd
        self.lst = lst
        self.imports = [
            'from __future__ import annotations',
            'from typing import List',
            'from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime'
        ]

    def read_node(self, el):
        if el.tag == '{http://www.w3.org/2001/XMLSchema}include':
            inc_file = el.attrib['schemaLocation']
            convert_file(os.path.join(os.path.dirname(self.xsd), inc_file), self.lst)
            self.imports.append(f'from .{get_module(inc_file)} import *\n')
        elif el.tag == '{http://www.w3.org/2001/XMLSchema}import':
            inc_file = el.attrib['schemaLocation']
            convert_file(os.path.join(os.path.dirname(self.xsd), inc_file), self.lst)
            self.imports.append(f'from .{get_module(inc_file)} import *\n')
        elif el.tag == '{http://www.w3.org/2001/XMLSchema}complexType':
            complex_type = ComplexType()
            complex_type.read(el)
            self.sequence.append(complex_type)
            self.types[complex_type.name] = complex_type
        elif el.tag == '{http://www.w3.org/2001/XMLSchema}simpleType':
            simple_type = SimpleType()
            simple_type.read(el)
            self.sequence.append(simple_type)
            self.types[simple_type.name] = simple_type
        else:
            super().read_node(el)

    def render(self):
        stream = []
        stream.extend(self.imports)
        stream.append('')
        types = []
        all_types = list(self.types.values())
        if self.types:
            types = adjust_deps(self.types)
            for tp in types:
                stream.append(tp.render(0))
            for tp in all_types:
                if tp not in types:
                    stream.append(tp.render(0))

        for seq in self.sequence:
            if seq not in types and not isinstance(seq, ComplexType) and seq not in all_types:
                stream.append(seq.render(0))
        return '\n'.join(stream) + '\n'


def get_module(filename: str):
    return os.path.basename(filename).replace('.xsd', '').replace('.', '').replace('-', '_')


def convert_file(xsd: str, lst: dict):
    print('Convert file:', xsd)
    if os.path.isfile(xsd):
        with open(xsd, 'rb') as f:
            xml = etree.fromstring(f.read())
        mod = Module(xsd, lst)
        mod.read_nodes(xml)
        lst[xsd] = mod.render()


def convert_dir(directory: str):
    lst = {}
    for s in os.listdir(directory):
        if s.endswith('.xsd') and s not in lst:
            outfile = convert_file(os.path.join(directory, s), lst)
    return lst
