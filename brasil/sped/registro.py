from brasil.utils.records import TextBlock, BlockList, Field  # noqa


class Registro(TextBlock):
    REG: str = None
    _separator = '|'
    _begin = '|'
    _end = '|'

    def __init_subclass__(cls, abstract=False, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.REG is None and not abstract:
            cls.REG = cls.__name__[-4:]
            field = Field()
            field.name = 'REG'
            field.data_type = str
            cls._fields.insert(0, field)

    def _write_bool(self, val: bool) -> str:
        return 'S' if val else 'N'


class BlocoSPED:
    pass
