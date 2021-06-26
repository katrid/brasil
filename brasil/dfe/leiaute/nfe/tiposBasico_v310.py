from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime


class TCodUfIBGE(str):
    """Tipo Código da UF da tabela do IBGE"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53'])
    pass



class TCodMunIBGE(str):
    """Tipo Código do Município da tabela do IBGE"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{7}", enumeration=[])
    pass



class TChNFe(str):
    """Tipo Chave da Nota Fiscal Eletrônica"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{44}", max_length=r"44", enumeration=[])
    pass



class TProt(str):
    """Tipo Número do Protocolo de Status"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{15}", max_length=r"15", enumeration=[])
    pass



class TRec(str):
    """Tipo Número do Recibo do envio de lote de NF-e"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{15}", max_length=r"15", enumeration=[])
    pass



class TStat(str):
    """Tipo Código da Mensagem enviada"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{3}", max_length=r"3", enumeration=[])
    pass



class TCnpj(str):
    """Tipo Número do CNPJ"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{14}", max_length=r"14", enumeration=[])
    pass



class TCnpjVar(str):
    """Tipo Número do CNPJ tmanho varíavel (3-14)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{3,14}", max_length=r"14", enumeration=[])
    pass



class TCnpjOpc(str):
    """Tipo Número do CNPJ Opcional"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{0}|[0-9]{14}", max_length=r"14", enumeration=[])
    pass



class TCpf(str):
    """Tipo Número do CPF"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{11}", max_length=r"11", enumeration=[])
    pass



class TCpfVar(str):
    """Tipo Número do CPF de tamanho variável (3-11)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{3,11}", max_length=r"11", enumeration=[])
    pass



class TDec_0204v(str):
    """Tipo Decimal com até 2 dígitos inteiros, podendo ter de 1 até 4 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,1}(\.[0-9]{1,4})?", enumeration=[])
    pass



class TDec_0302a04(str):
    """Tipo Decimal com até 3 dígitos inteiros, podendo ter de 2 até 4 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?", enumeration=[])
    pass



class TDec_0302a04Opc(str):
    """Tipo Decimal com até 3 dígitos inteiros e 2 até 4 decimais. Utilizados em TAGs opcionais, não aceita valor zero."""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?", enumeration=[])
    pass



class TDec_0302Max100(str):
    """Tipo Decimal com 3 inteiros (no máximo 100), com 2 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0(\.[0-9]{2})?|100(\.00)?|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})?", enumeration=[])
    pass



class TDec_0302a04Max100(str):
    """Tipo Decimal com 3 inteiros (no máximo 100), com até 4 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[1-9]{1}(\.[0-9]{2,4})?|[1-9]{1}[0-9]{1}(\.[0-9]{2,4})?|100(\.0{2,4})?", enumeration=[])
    pass



class TDec_0803v(str):
    """Tipo Decimal com 8 inteiros, podendo ter de 1 até 3 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,7}(\.[0-9]{1,3})?", enumeration=[])
    pass



class TDec_1104(str):
    """Tipo Decimal com 11 inteiros, podendo ter 4 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?", enumeration=[])
    pass



class TDec_1104v(str):
    """Tipo Decimal com 11 inteiros, podendo ter de 1 até 4 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,4})?", enumeration=[])
    pass



class TDec_1104Opc(str):
    """Tipo Decimal com 11 inteiros, podendo ter 4 decimais (utilizado em tags opcionais)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0\.[1-9]{1}[0-9]{3}|0\.[0-9]{3}[1-9]{1}|0\.[0-9]{2}[1-9]{1}[0-9]{1}|0\.[0-9]{1}[1-9]{1}[0-9]{2}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?", enumeration=[])
    pass



class TDec_1110v(str):
    """Tipo Decimal com 11 inteiros, podendo ter de 1 até 10 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{1,10}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,10})?", enumeration=[])
    pass



class TDec_1203(str):
    """Tipo Decimal com 12 inteiros, podendo ter  3 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,11}(\.[0-9]{3})?", enumeration=[])
    pass



class TDec_1204(str):
    """Tipo Decimal com 12 inteiros e 4 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,11}|[1-9]{1}[0-9]{0,11}(\.[0-9]{4})?", enumeration=[])
    pass



class TDec_1204v(str):
    """Tipo Decimal com 12 inteiros de 1 até 4 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,11}|[1-9]{1}[0-9]{0,11}(\.[0-9]{1,4})?", enumeration=[])
    pass



class TDec_1204Opc(str):
    """Tipo Decimal com 12 inteiros com 1 até 4 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,11}|[1-9]{1}[0-9]{0,11}(\.[0-9]{1,4})?", enumeration=[])
    pass



class TDec_1204temperatura(str):
    """Tipo Decimal com 12 inteiros, 1 a 4 decimais"""
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
    """Tipo Inscrição Estadual do Destinatário // alterado para aceitar vazio ou ISENTO - maio/2010 v2.0"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"ISENTO|[0-9]{2,14}", max_length=r"14", enumeration=[])
    pass



class TIeDestNaoIsento(str):
    """Tipo Inscrição Estadual do Destinatário // alterado para aceitar vazio ou ISENTO - maio/2010 v2.0"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{2,14}", max_length=r"14", enumeration=[])
    pass



class TIeST(str):
    """Tipo Inscrição Estadual do ST // acrescentado EM 24/10/08"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{2,14}", max_length=r"14", enumeration=[])
    pass



class TIe(str):
    """Tipo Inscrição Estadual do Emitente // alterado EM 24/10/08 para aceitar ISENTO"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{2,14}|ISENTO", max_length=r"14", enumeration=[])
    pass



class TMod(str):
    """Tipo Modelo Documento Fiscal"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['55', '65'])
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



class TUfEmi(str):
    """Tipo Sigla da UF de emissor // acrescentado em 24/10/08"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO'])
    pass



class TAmb(str):
    """Tipo Ambiente"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1', '2'])
    pass



class TVerAplic(TString):
    """Tipo Versão do Aplicativo"""
    _restriction = Restriction(base=r"nfe:TString", min_length=r"1", max_length=r"20", enumeration=[])
    pass



class TMotivo(TString):
    """Tipo Motivo"""
    _restriction = Restriction(base=r"nfe:TString", min_length=r"1", max_length=r"255", enumeration=[])
    pass



class TJust(TString):
    """Tipo Justificativa"""
    _restriction = Restriction(base=r"nfe:TString", min_length=r"15", max_length=r"255", enumeration=[])
    pass



class TServ(TString):
    """Tipo Serviço solicitado"""
    _restriction = Restriction(base=r"nfe:TString", enumeration=[])
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
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[!-ÿ]{1}[ -ÿ]*[!-ÿ]{1}|[!-ÿ]{1}", enumeration=[])
    pass



class TData(str):
    """Tipo data AAAA-MM-DD"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))", enumeration=[])
    pass



class TTime(str):
    """Tipo hora HH:MM:SS // tipo acrescentado na v2.0"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])", enumeration=[])
    pass



class TDateTimeUTC(str):
    """Data e Hora, formato UTC (AAAA-MM-DDThh:mm:ssTZD, onde TZD = +hh:mm ou -hh:mm)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))", enumeration=[])
    pass



class TPlaca(str):
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[A-Z]{2,3}[0-9]{4}|[A-Z]{3,4}[0-9]{3}", enumeration=[])
    pass



class TCOrgaoIBGE(str):
    """Tipo Código de orgão (UF da tabela do IBGE + 90 RFB)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53', '90', '91', '92'])
    pass


