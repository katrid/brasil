from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *


class TNSU(str):
    """Tipo número sequencial único do AN"""
    _restriction = Restriction(base=r"xs:string", pattern=r"[0-9]{1,15}", enumeration=[])
    pass


class TVeConsNFeDest(str):
    """Tipo Versão da consultaNFeDest"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1.01'])
    pass


class TConsNFeDest(Element):
    """Tipo Pedido de Consulta de Nota Fiscal Eletrônica"""
    tpAmb: TAmb = Element(TAmb)
    xServ: str = Element(str)
    CNPJ: TCnpj = Element(TCnpj)
    indNFe: str = Element(str)
    indEmi: str = Element(str)
    ultNSU: str = Element(str)
    versao: str = Attribute(TVeConsNFeDest)


class TRetConsNFeDest(Element):
    """Tipo Retorno do pedido de Consulta de Nota Fiscal Eletrônica"""
    tpAmb: TAmb = Element(TAmb)
    verAplic: TVerAplic = Element(TVerAplic)
    cStat: TStat = Element(TStat)
    xMotivo: TMotivo = Element(TMotivo)
    dhResp: dateTime = Element(dateTime)
    indCont: str = Element(str, min_occurs=0)
    ultNSU: str = Element(str, min_occurs=0)
    class ret(ComplexType):
        pass
    ret: ret
    versao: str = Attribute(TVeConsNFeDest)


