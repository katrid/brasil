import re
from datetime import datetime
import random

from brasil.utils.formulas import modulo11

FRETE = {
    '0': '0 - Remetente (CIF)',
    '1': '1 - Destinatário (FOB)',
    '2': '2 - Terceiros',
    '3': '3 - Próprio Remetente',
    '4': '4 - Próprio Destinatário',
    '9': '9 - Sem Frete'
}

TP_CTE ={
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

def validar_cpf(cpf):
    cpf = ''.join(re.findall('\d', str(cpf)))
    if (not cpf) or (len(cpf) < 11):
        return False

    # Pega apenas os 9 primeiros dígitos do CPF e gera os 2 dígitos que faltam
    inteiros = map(int, cpf)
    novo = inteiros[:9]

    while len(novo) < 11:
        r = sum([(len(novo)+1-i)*v for i,v in enumerate(novo)]) % 11

        if r > 1:
            f = 11 - r
        else:
            f = 0
        novo.append(f)
    # Se o número gerado coincidir com o número original, é válido
    if novo == inteiros:
        return True
    return False

def validar_cnpj(cnpj):
    cnpj = ''.join(re.findall('\d', str(cnpj)))
    if (not cnpj) or (len(cnpj) < 14):
        return False
    # Pega apenas os 12 primeiros dígitos do CNPJ e gera os 2 dígitos que faltam
    inteiros = list(map(int, cnpj))
    novo = inteiros[:12]

    prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    while len(novo) < 14:
        r = sum([x*y for (x, y) in zip(novo, prod)]) % 11
        if r > 1:
            f = 11 - r
        else:
            f = 0
        novo.append(f)
        prod.insert(0, 6)
    # Se o número gerado coincidir com o número original, é válido
    if novo == inteiros:
        return True
    return False

def format_number(v: str) -> str:
    return '{:,.2f}'.format(round(float(v), 2)).replace(',', '*').replace('.', ',').replace('*', '.')

def is_float(value: str) -> bool:
    return value.replace('.', '').isnumeric()

def format_doc(ator: dict) -> str:
    if 'CNPJ' in ator:
        doc = ator['CNPJ']
        return f'{doc[:2]}.{doc[2:5]}.{doc[5:8]}/{doc[8:11]}-{doc[11:]}'
    elif 'CPF' in ator:
        doc = ator['CPF']
        return f'{doc[:3]}.{doc[3:6]}.{doc[6:9]}-{doc[9:]}'