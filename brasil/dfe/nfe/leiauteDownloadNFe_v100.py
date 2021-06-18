from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *


class TVerDownloadNFe(str):
    """Tipo Versão da consultaNFeDest"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1.00'])
    pass


class TDownloadNFe(Element):
    """Tipo Pedido de Download de NF-e"""
    tpAmb: TAmb = Element(TAmb)
    xServ: str = Element(str)
    CNPJ: TCnpj = Element(TCnpj)
    chNFe: List[TChNFe] = Element(TChNFe, max_occurs=10)
    versao: str = Attribute(TVerDownloadNFe)


class TRetDownloadNFe(Element):
    """Tipo Retorno do pedido de Download de NF-e"""
    tpAmb: TAmb = Element(TAmb)
    verAplic: TVerAplic = Element(TVerAplic)
    cStat: TStat = Element(TStat)
    xMotivo: TMotivo = Element(TMotivo)
    dhResp: dateTime = Element(dateTime)
    class retNFe(ComplexType):
        chNFe: TChNFe = Element(TChNFe)
        cStat: TStat = Element(TStat)
        xMotivo: TMotivo = Element(TMotivo)
    retNFe: retNFe
    versao: str = Attribute(TVerDownloadNFe)


