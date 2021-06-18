from datetime import datetime
import random


def gerar_codigo(num: int) -> int:
    INVALIDOS = (
        0, 11111111, 22222222,
        33333333, 44444444, 55555555, 66666666, 77777777, 88888888, 99999999,
        12345678, 23456789, 34567890, 45678901, 56789012, 67890123, 78901234,
        89012345, 90123456, 1234567
    )
    while (i := random.randint(1, 99999999)) and i in INVALIDOS:
        pass
    return i


def gerar_chave_acesso(uf: int, emis: datetime, cnpj: str, serie: int, numero: int, tpEmi: int, codigo: int,
                       modelo: int) -> str:
    if codigo == 0:
        codigo = gerar_codigo(numero)
    return f'{uf}{emis.strftime("%y%m")}{cnpj.zfill(14)}{str(modelo).zfill(2)}{str(serie).zfill(3)}{str(numero).zfill(9)}{tpEmi}'
