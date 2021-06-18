from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *


class TUfCons(token):
    """Tipo Sigla da UF consultada"""
    _restriction = Restriction(base=r"xs:token", enumeration=['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO', 'SU'])
    pass


class TVerConsCad(token):
    """Tipo Versão do Leiaute da Consulta Cadastro 2.00"""
    _restriction = Restriction(base=r"xs:token", pattern=r"2\.00", enumeration=[])
    pass


class TConsCad(Element):
    """Tipo Pedido de Consulta de cadastro de contribuintes"""
    class infCons(ComplexType):
        xServ: str = Element(str)
        UF: TUfCons = Element(TUfCons)
    infCons: infCons
    versao: str = Attribute(TVerConsCad)


class TEndereco(Element):
    """Tipo Dados do Endereço"""
    xLgr: str = Element(str, min_occurs=0)
    nro: str = Element(str, min_occurs=0)
    xCpl: str = Element(str, min_occurs=0)
    xBairro: str = Element(str, min_occurs=0)
    cMun: TCodMunIBGE = Element(TCodMunIBGE, min_occurs=0)
    xMun: str = Element(str, min_occurs=0)
    CEP: str = Element(str, min_occurs=0)


class TRetConsCad(Element):
    """Tipo Retorno Pedido de Consulta de cadastro de contribuintes"""
    class infCons(ComplexType):
        verAplic: TVerAplic = Element(TVerAplic)
        cStat: TStat = Element(TStat)
        xMotivo: TMotivo = Element(TMotivo)
        UF: TUfCons = Element(TUfCons)
        dhCons: dateTime = Element(dateTime)
        cUF: TCodUfIBGE = Element(TCodUfIBGE)
        class infCad(ComplexType):
            IE: TIe = Element(TIe)
            UF: TUf = Element(TUf)
            cSit: str = Element(str)
            indCredNFe: str = Element(str)
            indCredCTe: str = Element(str)
            xNome: str = Element(str)
            xFant: str = Element(str, min_occurs=0)
            xRegApur: str = Element(str, min_occurs=0)
            CNAE: str = Element(str, min_occurs=0)
            dIniAtiv: date = Element(date, min_occurs=0)
            dUltSit: date = Element(date, min_occurs=0)
            dBaixa: date = Element(date, min_occurs=0)
            IEUnica: TIe = Element(TIe, min_occurs=0)
            IEAtual: TIe = Element(TIe, min_occurs=0)
            ender: TEndereco = Element(TEndereco, min_occurs=0)
        infCad: infCad
    infCons: infCons
    versao: str = Attribute(TVerConsCad)


