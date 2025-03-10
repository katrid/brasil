import re
from datetime import datetime
import random
from dateutil.parser import isoparse

from brasil.utils.formulas import modulo11

FRETE = {
    '0': '0 - Remetente (CIF)',
    '1': '1 - Destinatário (FOB)',
    '2': '2 - Terceiros',
    '3': '3 - Próprio Remetente',
    '4': '4 - Próprio Destinatário',
    '9': '9 - Sem Frete'
}

TP_CTE = {
    '0': 'CT-e Normal',
    '1': 'CT-e de Complemento de Valores',
    '2': 'CT-e de Anulação',
    '3': 'CT-e Substituto',
}

CST_ICMS = {
    '00': '00 - Tributação normal ICMS',
    '20': '20 - Tributação com BC reduzida do ICMS',
    '40': '40 - ICMS isenção',
    '41': '41 - ICMS não tributada',
    '51': '51 - ICMS diferido',
    '60': '60 - ICMS cobrado por substituição tributária',
    '90.1': '90 - ICMS outros',
    '90.2': '90 - ICMS Outra UF',
    '90.3': '90 - ICMS Simples Nacional',
}

CTE_TP_EMIS = {
    '1': 'Normal',
    '4': 'EPEC pela SVC',
    '5': 'Contingência FSDA',
    '7': 'Autorização pela SVC-RS',
    '8': 'Autorização pela SVC-SP',
}

CTE_TP_MODAL = {
    '01': 'Rodoviário',
    '02': 'Aéreo',
    '03': 'Ferroviário',
    '05': 'Dutoviário',
    '06': 'Multimodal',
}

CTE_TP_SERV = {
    '0': 'Normal',
    '1': 'Subcontratação',
    '2': 'Redespacho',
    '3': 'Redespacho Intermediário',
    '4': 'Serviço Vinculado a Multimodal',
}


def gerar_codigo(num: int) -> int:
    INVALIDOS = (
        0, 11111111, 22222222,
        33333333, 44444444, 55555555, 66666666, 77777777, 88888888, 99999999,
        12345678, 23456789, 34567890, 45678901, 56789012, 67890123, 78901234,
        89012345, 90123456, 1234567
    )
    while (i := random.randint(1, 99999999)) and (i in INVALIDOS or i == num):
        pass
    return i


def gerar_chave_acesso(uf: int, emis: datetime, cnpj: str, serie: int, numero: int, tp_emi: int, codigo: int,
                       modelo: int) -> str:
    if codigo == 0:
        codigo = gerar_codigo(numero)
    emis = emis.strftime("%y%m")
    res = f'{uf}{emis}{cnpj.zfill(14)}{str(modelo).zfill(2)}{str(serie).zfill(3)}{str(numero).zfill(9)}{tp_emi}{str(codigo).zfill(8)}'
    return res + str(modulo11(res))


def parse_chave_acesso(chave: str):
    return {
        'uf': chave[:2],
        'emissao': chave[2:6],
        'cnpj': chave[6:20],
        'modelo': chave[20:22],
        'serie': chave[22:25],
        'numero': chave[25:34],
        'tp_emis': chave[34:35],
        'codigo': chave[35:43],
        'dv': chave[43:44],
    }
