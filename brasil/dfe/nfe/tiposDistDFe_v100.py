from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime

class TNSU(token):
    """Tipo número sequencial único"""
    _restriction = Restriction(base=r"xs:token", pattern=r"[0-9]{15}", enumeration=[])
    pass


class TQNSU(unsignedShort):
    """Tipo quantidade de NSU"""
    _restriction = Restriction(base=r"xs:unsignedShort", enumeration=[])
    pass


class TVerDistDFe(str):
    """Tipo Versão dos leiautes do Web Service NFeDistribuicaoDFe"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1.00'])
    pass


class TAmb(str):
    """Tipo Ambiente"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1', '2'])
    pass


class TCodUfIBGE(str):
    """Tipo Código da UF da tabela do IBGE"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53'])
    pass


class TCOrgaoIBGE(str):
    """Tipo Código de orgão (UF da tabela do IBGE + 90 RFB)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53', '90', '91', '92'])
    pass


class TCnpj(str):
    """Tipo Número do CNPJ"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{14}", max_length=r"14", enumeration=[])
    pass


class TCpf(str):
    """Tipo Número do CPF"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{11}", max_length=r"11", enumeration=[])
    pass


class TVerAplic(TString):
    """Tipo Versão do Aplicativo"""
    _restriction = Restriction(base=r"TString", min_length=r"1", max_length=r"20", enumeration=[])
    pass


class TStat(str):
    """Tipo Código da Mensagem enviada"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{3}", max_length=r"3", enumeration=[])
    pass


class TMotivo(TString):
    """Tipo Motivo"""
    _restriction = Restriction(base=r"TString", min_length=r"1", max_length=r"255", enumeration=[])
    pass


class TString(str):
    """Tipo string genérico"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}", enumeration=[])
    pass


class TChNFe(str):
    """Tipo Chave da Nota Fiscal Eletrônica"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{44}", max_length=r"44", enumeration=[])
    pass


class TProt(str):
    """Tipo Número do Protocolo de Status"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{15}", max_length=r"15", enumeration=[])
    pass


class TDateTimeUTC(str):
    """Data e Hora, formato UTC (AAAA-MM-DDThh:mm:ssTZD, onde TZD = +hh:mm ou -hh:mm)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))", enumeration=[])
    pass


class TIe(str):
    """Tipo Inscrição Estadual do Emitente // alterado EM 24/10/08 para aceitar ISENTO"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{2,14}|ISENTO", max_length=r"14", enumeration=[])
    pass


class TDec_1302(str):
    """Tipo Decimal com 15 dígitos, sendo 13 de corpo e 2 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?", enumeration=[])
    pass


