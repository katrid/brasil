from typing import List, Annotated, get_args, get_origin
import re
from datetime import date, datetime
import inspect


class Field:
    def __init__(self, name: str, definition: Annotated, default=None):
        meta = definition.__metadata__
        self.name = name
        self.type = definition.__origin__
        self.length = meta[0]
        self.default = default
        if len(meta) > 1:
            self.description = meta[1]

    def get_regex(self):
        if self.default is not None:
            if self.type is int:
                return str(self.default).zfill(self.length)
            if self.type is str:
                return str(self.default).zfill(self.length)
        if self.type is int or self.type is float or self.type is date:
            return rf"[\d\s]{{{self.length}}}"
        if self.type is str:
            return rf".{{{self.length}}}"

    def to_string(self, value):
        if self.type is int:
            return str(value or 0).zfill(self.length)
        if self.type is str:
            return str(value or '').ljust(self.length)
        if self.type is date:
            if value is None:
                return '0'.zfill(self.length)
            else:
                return value.strftime('%d%m%y')
        if self.type is float:
            return str(int(round(value or 0, 2) * 100)).zfill(self.length)

    def from_string(self, value):
        value = value.strip()
        if not value:
            return
        if self.type is int:
            return int(value)
        if self.type is str:
            return value.strip()
        if self.type is date:
            if value == '000000':
                return None
            return datetime.strptime(value, '%d%m%y').date()
        if self.type is float:
            return int(value) / 100


class Record:
    _fields: List[Field]
    _re: re.Pattern = None

    def __init__(self, content: str = None):
        if content:
            pos = 0
            for field in self._fields:
                setattr(self, field.name, field.from_string(content[pos:pos + field.length]))
                pos += field.length

    def __init_subclass__(cls, **kwargs):
        cls._fields = [Field(k, a, default=getattr(cls, k, None)) for k, a in inspect.get_annotations(cls).items()]

    def __str__(self):
        """
        Converter linha para string
        :return:
        """
        return ''.join(f.to_string(getattr(self, f.name, None)) for f in self._fields)

    @classmethod
    def match(cls, line: str) -> bool:
        if cls._re is None:
            cls._re = re.compile(''.join(f.get_regex() for f in cls._fields))
        return bool(cls._re.match(line))

    @classmethod
    def re_debug(cls, line: str):
        pos = 0
        print('Errors')
        for field in cls._fields:
            r = re.compile(field.get_regex()).match(line[pos:pos + field.length])
            if not r:
                print(f'{field.name} ({field.get_regex()}): {line[pos:pos + field.length]}')
            pos += field.length

    def print(self):
        print(f'  Record({self.__class__.__name__}):')
        for f in self._fields:
            print(f'    {f.name}: {getattr(self, f.name, None)}')

    def dict(self):
        return {f.name: getattr(self, f.name, None) for f in self._fields}


class DocumentoBase(type):
    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)
        new_cls._records = [v for k, v in attrs.items() if inspect.isclass(v) and issubclass(v, Record)]
        return new_cls


class Arquivo(metaclass=DocumentoBase):
    _records: List[type[Record]]
    _defaults: dict
    _type_map: dict[type[Record], str]

    def __init__(self, content: str = None):
        for name, default in self._defaults.items():
            if callable(default):
                default = default()
            setattr(self, name, default)

        if content:
            self.fromstring(content)

    def __init_subclass__(cls, **kwargs):
        annotations = inspect.get_annotations(cls).items()
        cls._defaults = {k: get_origin(a) or None for k, a in annotations}
        cls._type_map = {((args := get_args(a)) and args[0]) or a: k for k, a in annotations}

    def fromstring(self, content: str):
        for i, s in enumerate(content.splitlines()):
            for rec in self._records:
                if rec.match(s):
                    self.read_record(rec, s)
                    break
            else:
                # debug
                print('Erro importando linha ' + str(i + 1))
                self.re_debug(s)

    def re_debug(self, line: str):
        pass

    def read_record(self, record: type[Record], line: str) -> Record:
        prop = self._type_map[record]
        attr = getattr(self, prop, None)
        rec = record(line)
        if isinstance(attr, list):
            attr.append(rec)
        elif prop:
            setattr(self, prop, rec)
        return rec

    def print(self):
        for t, k in self._type_map.items():
            rec = getattr(self, k)
            if isinstance(rec, list):
                for r in rec:
                    r.print()

    def dict(self):
        res = {}
        for t, k in self._type_map.items():
            rec = getattr(self, k)
            if isinstance(rec, list):
                res[k] = [r.dict() for r in rec]
            else:
                res[k] = rec.dict()
        return res


class Remessa(Arquivo):
    pass
