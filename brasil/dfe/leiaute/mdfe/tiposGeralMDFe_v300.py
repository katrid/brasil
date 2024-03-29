from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime


class TDateTimeUTC(str):
    """Data e Hora, formato UTC (AAAA-MM-DDThh:mm:ssTZD, onde TZD = +hh:mm ou -hh:mm)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))", enumeration=[])
    pass



class TCodUfIBGE(str):
    """Tipo Código da UF da tabela do IBGE"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53'])
    pass



class TCodMunIBGE(str):
    """Tipo Código do Município da tabela do IBGE"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{7}", enumeration=[])
    pass



class TCOrgaoIBGE(str):
    """Tipo Código de orgão (UF da tabela do IBGE + 90 SUFRAMA + 91 RFB + 92 BRId)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53', '90', '91', '92', '93', '94'])
    pass



class TCodUfIBGE_EX(str):
    """Tipo Código da UF da tabela do IBGE + 99 para Exterior"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53', '99'])
    pass



class TChCTe(str):
    """Tipo Chave do Conhecimento de Transporte Eletrônico"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{44}", max_length=r"44", enumeration=[])
    pass



class TChNFe(str):
    """Tipo Chave da Nota Fiscal Eletrônica"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{44}", max_length=r"44", enumeration=[])
    pass



class TChMDFe(str):
    """Tipo Chave de Manifesto de Documentos Fiscais Eletrônico"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{44}", max_length=r"44", enumeration=[])
    pass



class TSegCodBarra(str):
    """Tipo Segundo Codigo Barra"""
    _restriction = Restriction(base=r"xs:string", pattern=r"[0-9]{36}", enumeration=[])
    pass



class TProt(str):
    """Tipo Número do Protocolo de Status"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{15}", enumeration=[])
    pass



class TRec(str):
    """Tipo Número do Recibo do envio de lote de NF-e"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{15}", enumeration=[])
    pass



class TStat(str):
    """Tipo Código da Mensagem enviada"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{3}", enumeration=[])
    pass



class TCnpj(str):
    """Tipo Número do CNPJ"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{14}", enumeration=[])
    pass



class TCnpjVar(str):
    """Tipo Número do CNPJ tamanho varíavel (3-14)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{3,14}", enumeration=[])
    pass



class TCnpjOpc(str):
    """Tipo Número do CNPJ Opcional"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{0}|[0-9]{14}", enumeration=[])
    pass



class TCpf(str):
    """Tipo Número do CPF"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{11}", enumeration=[])
    pass



class TCpfVar(str):
    """Tipo Número do CPF de tamanho variável (3-11)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{3,11}", enumeration=[])
    pass



class TDec_0302(str):
    """Tipo Decimal com 5 dígitos, sendo 3 de corpo e 2 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?", enumeration=[])
    pass



class TDec_0303(str):
    """Tipo Decimal com 6 dígitos, sendo 3 de corpo e 3 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{3})?", enumeration=[])
    pass



class TDec_0302Opc(str):
    """Tipo Decimal com 5 dígitos, sendo 3 de corpo e 2 decimais, utilizado em tags opcionais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?", enumeration=[])
    pass



class TDec_0302_0303(str):
    """Tipo Decimal com 6  ou 5 dígitos, sendo 3 de corpo e 3 ou 2 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{1,3}(\.[0-9]{2,3})?", enumeration=[])
    pass



class TDec_0803(str):
    """Tipo Decimal com 11 dígitos, sendo 8 de corpo e 3 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,7}(\.[0-9]{3})?", enumeration=[])
    pass



class TDec_0803Opc(str):
    """Tipo Decimal com 11 dígitos, sendo 8 de corpo e 3 decimais utilizado em tags opcionais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0\.[1-9]{1}[0-9]{2}|0\.[0-9]{2}[1-9]{1}|0\.[0-9]{1}[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,7}(\.[0-9]{3})?", enumeration=[])
    pass



class TDec_0804(str):
    """Tipo Decimal com 12 dígitos, sendo 8 de corpo e 4decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,7}(\.[0-9]{4})?", enumeration=[])
    pass



class TDec_0804Opc(str):
    """Tipo Decimal com 12 dígitos, sendo 8 de corpo e 4 decimais, utilizado em tags opcionais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0\.[1-9]{1}[0-9]{3}|0\.[0-9]{3}[1-9]{1}|0\.[0-9]{2}[1-9]{1}[0-9]{1}|0\.[0-9]{1}[1-9]{1}[0-9]{2}|[1-9]{1}[0-9]{0,7}(\.[0-9]{4})?", enumeration=[])
    pass



class TDec_0906Opc(str):
    """Tipo Decimal com 15 dígitos, sendo 9 de corpo e 6 decimais, utilizado em tags opcionais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0\.[1-9]{1}[0-9]{5}|0\.[0-9]{1}[1-9]{1}[0-9]{4}|0\.[0-9]{2}[1-9]{1}[0-9]{3}|0\.[0-9]{3}[1-9]{1}[0-9]{2}|0\.[0-9]{4}[1-9]{1}[0-9]{1}|0\.[0-9]{5}[1-9]{1}|[1-9]{1}[0-9]{0,8}(\.[0-9]{6})?", enumeration=[])
    pass



class TDec_1104(str):
    """Tipo Decimal com 15 dígitos, sendo 11 de corpo e 4 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?", enumeration=[])
    pass



class TDec_1104Opc(str):
    """Tipo Decimal com 15 dígitos, sendo 11 de corpo e 4 decimais, utilizado em tags opcionais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0\.[1-9]{1}[0-9]{3}|0\.[0-9]{3}[1-9]{1}|0\.[0-9]{2}[1-9]{1}[0-9]{1}|0\.[0-9]{1}[1-9]{1}[0-9]{2}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?", enumeration=[])
    pass



class TDec_1203(str):
    """Tipo Decimal com 15 dígitos, sendo 12 de corpo e 3 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,11}(\.[0-9]{3})?", enumeration=[])
    pass



class TDec_1203Opc(str):
    """Tipo Decimal com 15 dígitos, sendo 12 de corpo e 3 decimais, utilizado em tags opcionais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0\.[1-9]{1}[0-9]{2}|0\.[0-9]{2}[1-9]{1}|0\.[0-9]{1}[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,11}(\.[0-9]{3})?", enumeration=[])
    pass



class TDec_1204(str):
    """Tipo Decimal com 16 dígitos, sendo 12 de corpo e 4 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,11}(\.[0-9]{4})?", enumeration=[])
    pass



class TDec_1204Opc(str):
    """Tipo Decimal com 16 dígitos, sendo 12 de corpo e 4 decimais, utilizado em tags opcionais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0\.[1-9]{1}[0-9]{3}|0\.[0-9]{3}[1-9]{1}|0\.[0-9]{2}[1-9]{1}[0-9]{1}|0\.[0-9]{1}[1-9]{1}[0-9]{2}|[1-9]{1}[0-9]{0,11}(\.[0-9]{4})?", enumeration=[])
    pass



class TDec_1302(str):
    """Tipo Decimal com 15 dígitos, sendo 13 de corpo e 2 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?", enumeration=[])
    pass



class TDec_1302Opc(str):
    """Tipo Decimal com 15 dígitos, sendo 13 de corpo e 2 decimais, utilizado em tags opcionais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?", enumeration=[])
    pass



class TIeDest(str):
    """Tipo Inscrição Estadual do Destinatário"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{0,14}|ISENTO|PR[0-9]{4,8}", enumeration=[])
    pass



class TModMD(str):
    """Tipo Modelo Manifesto de Documento Fiscal Eletrônico"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['58'])
    pass



class TIe(str):
    """Tipo Inscrição Estadual do Emitente"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{2,14}", enumeration=[])
    pass



class TNF(str):
    """Tipo Número do Documento Fiscal"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[1-9]{1}[0-9]{0,8}", enumeration=[])
    pass



class TSerie(str):
    """Tipo Série do Documento Fiscal"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|[1-9]{1}[0-9]{0,2}", enumeration=[])
    pass



class TUf(str):
    """Tipo Sigla da UF"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO', 'EX'])
    pass



class TAmb(str):
    """Tipo Ambiente"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1', '2'])
    pass



class TEmit(str):
    """Tipo Emitente"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1', '2', '3'])
    pass



class TTransp(str):
    """Tipo Transportador"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1', '2', '3'])
    pass



class TVerAplic(TString):
    """Tipo Versão do Aplicativo"""
    _restriction = Restriction(base=r"TString", min_length=r"1", max_length=r"20", enumeration=[])
    pass



class TMotivo(TString):
    """Tipo Motivo"""
    _restriction = Restriction(base=r"TString", min_length=r"1", max_length=r"255", enumeration=[])
    pass



class TJust(TString):
    """Tipo Justificativa"""
    _restriction = Restriction(base=r"TString", min_length=r"15", max_length=r"255", enumeration=[])
    pass



class TServ(TString):
    """Tipo Serviço solicitado"""
    _restriction = Restriction(base=r"TString", enumeration=[])
    pass



class Tano(str):
    """Tipo ano"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{2}", enumeration=[])
    pass



class TMed(str):
    """Tipo temp médio em segundos"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{1,4}", enumeration=[])
    pass



class TString(str):
    """Tipo string genérico"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}", enumeration=[])
    pass



class TData(str):
    """Tipo data AAAA-MM-DD"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))", enumeration=[])
    pass



class TLatitude(TString):
    """Coordenada geográfica Latitude"""
    _restriction = Restriction(base=r"TString", pattern=r"[0-9]\.[0-9]{6}|[1-8][0-9]\.[0-9]{6}|90\.[0-9]{6}|-[0-9]\.[0-9]{6}|-[1-8][0-9]\.[0-9]{6}|-90\.[0-9]{6}", enumeration=[])
    pass



class TLongitude(TString):
    """Coordenada geográfica Longitude"""
    _restriction = Restriction(base=r"TString", pattern=r"[0-9]\.[0-9]{6}|[1-9][0-9]\.[0-9]{6}|1[0-7][0-9]\.[0-9]{6}|180\.[0-9]{6}|-[0-9]\.[0-9]{6}|-[1-9][0-9]\.[0-9]{6}|-1[0-7][0-9]\.[0-9]{6}|-180\.[0-9]{6}", enumeration=[])
    pass



class TtipoUnidTransp(str):
    """Tipo da Unidade de Transporte"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1', '2', '3', '4', '5', '6', '7'])
    pass



class TtipoUnidCarga(str):
    """Tipo da Unidade de Carga"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1', '2', '3', '4'])
    pass



class TNSU(str):
    """Tipo número sequencial único do AN"""
    _restriction = Restriction(base=r"xs:string", pattern=r"[0-9]{15}", enumeration=[])
    pass



class TIPv4(str):
    """Tipo IP versão 4"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])", enumeration=[])
    pass



class TRSAKeyValueType(Element):
    """Tipo que representa uma chave publica padrão RSA"""
    Modulus: base64Binary = Element(base64Binary)
    Exponent: base64Binary = Element(base64Binary)



class TPlaca(str):
    """Tipo Placa"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[A-Z]{2,3}[0-9]{4}|[A-Z]{3,4}[0-9]{3}|[A-Z0-9]{7}", enumeration=[])
    pass


