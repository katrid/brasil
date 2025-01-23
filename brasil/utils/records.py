import enum
from typing import List, Type, get_origin, Self, cast
from datetime import date
from decimal import Decimal
from re import Pattern


class Field:
    data_type: type = None
    name: str = None
    description: str = None
    pattern: str | Pattern = None
    min_length: int = None
    max_length: int = None
    type_origin: type = None


class Block:
    _content: str
    _fields: List[Field]
    _eol = ''
    _separator = ''

    def __init__(self, **kwargs):
        for f in self._fields:
            if not hasattr(self, f.name) and f.name not in kwargs:
                setattr(self, f.name, BlockList[f.data_type](f.data_type) if f.type_origin is BlockList else None)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __init_subclass__(cls, **kwargs):
        cls._fields = []
        for k, v in cls.__annotations__.items():
            field = Field()
            field.name = k
            field.data_type = v
            field.type_origin = get_origin(v)
            cls._fields.append(field)

    def _read_value(self, field: Field, val: str):
        pass

    def _write_value(self, field: Field, val) -> str:
        pass

    def _write_list(self, val: List[Self]) -> str:
        return self._eol.join(v._write() for v in val)

    def __getitem__(self, item):
        return self._write_value(getattr(self.__class__, item), getattr(self, item))

    def __setitem__(self, key, value):
        self._read_value(getattr(self.__class__, key), value)

    def __iter__(self):
        return iter(f.name for f in self._fields)

    def _begin_write(self):
        return self._separator.join(
            self._write_value(f, getattr(self, f.name)) for f in self._fields if f.type_origin is not BlockList
        )

    def _write(self):
        s = self._begin_write()
        # process lists
        children = self._eol.join(
            self._write_list(getattr(self, f.name)) for f in self._fields if f.type_origin is BlockList
        )
        if children:
            s += self._eol + children
        return s

    def __str__(self):
        return self._write()


class BlockList[T](list):
    def __init__(self, block: T):
        super().__init__()
        self._block = block

    def add(self, **kwargs) -> T:
        b = self._block()
        for k, v in kwargs.items():
            b[k] = v
        self.append(b)
        return b


class BaseFile:
    _eol: str = ''
    _separator: str = ''
    structure: List[Type[Block]]
    blocks: List[Block]  # prepared blocks

    def __init__(self):
        self.blocks = []

    def __init_subclass__(cls, **kwargs):
        pass

    def load(self, content: str | bytes):
        pass

    def dump(self) -> str | bytes:
        stream = []
        self.write(stream)
        return self._eol.join(stream)

    def write(self, stream: List[str]):
        for b in self.blocks:
            stream.append(b._write(self._separator, self._eol))


class TextFile(BaseFile):
    _eol: str = '\n'
    _separator: str = ','


class TextBlock(Block):
    _content = None
    _pattern: Pattern = None
    _eol = '\n'
    _separator = ','
    _begin = ''
    _end = ''

    def _read_value(self, field: Field, val: str):
        pass

    def _read_bool(self, val: str) -> bool:
        return val == '1'

    def _read_int(self, val: str) -> int:
        return int(val or 0)

    def _read_str(self, val: str) -> str:
        return val

    def _read_date(self, val: str) -> date:
        return date(int(val[4:8]), int(val[2:4]), int(val[:2]))

    def _read_number(self, val: str) -> float:
        return float(val.replace(',', '.'))

    def _write_value(self, field: Field, val) -> str:
        if field.data_type is bool:
            return self._write_bool(val)
        if field.data_type is int:
            return self._write_int(val)
        if field.data_type is date:
            return self._write_date(val)
        if field.data_type in (float, Decimal):
            return self._write_number(val)
        return self._write_str(val)

    def _write_enum(self, val: enum.Enum) -> str:
        return val.value

    def _write_bool(self, val: bool) -> str:
        return '1' if val else '0'

    def _write_int(self, val: int) -> str:
        if val is None:
            return '0'
        return str(val)

    def _write_str(self, val: str) -> str:
        if val is None:
            return ''
        return str(val)

    def _write_date(self, val: date) -> str:
        if val:
            return val.strftime('%d%m%Y')
        return ''

    def _write_number(self, val: float | Decimal | int) -> str:
        if val is None:
            return ''
        return f'{val:.2f}'.replace('.', ',')

    def _begin_write(self):
        return self._begin + super()._begin_write() + self._end
