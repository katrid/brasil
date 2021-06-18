from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposGeralCTe_v300 import *


class TVerCancCTe(str):
    """Tipo Versão de cancela CT-e"""
    _restriction = Restriction(base=r"xs:string", pattern=r"1\.04", enumeration=[])
    pass


class TCancCTe(Element):
    """Tipo Pedido de Cancelamento de CT-e"""
    class infCanc(ComplexType):
        tpAmb: TAmb = Element(TAmb)
        xServ: TServ = Element(TServ)
        chCTe: TChNFe = Element(TChNFe)
        nProt: TProt = Element(TProt)
        xJust: TJust = Element(TJust)
        Id: str = Attribute(None)
    infCanc: infCanc
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerCancCTe)


class TRetCancCTe(Element):
    """Tipo retorno Pedido de Cancelamento CT-e"""
    class infCanc(ComplexType):
        tpAmb: TAmb = Element(TAmb)
        cUF: TCodUfIBGE = Element(TCodUfIBGE)
        verAplic: TVerAplic = Element(TVerAplic)
        cStat: TStat = Element(TStat)
        xMotivo: TMotivo = Element(TMotivo)
        chCTe: TChNFe = Element(TChNFe, min_occurs=0)
        dhRecbto: dateTime = Element(dateTime, min_occurs=0)
        nProt: TProt = Element(TProt, min_occurs=0)
        Id: str = Attribute(ID)
    infCanc: infCanc
    Signature: Signature = Element(Signature, min_occurs=0)
    versao: str = Attribute(TVerCancCTe)


class TProcCancCTe(Element):
    """Tipo Pedido de Cancelamento de CT-e processado"""
    cancCTe: TCancCTe = Element(TCancCTe)
    retCancCTe: TRetCancCTe = Element(TRetCancCTe)
    versao: str = Attribute(TVerCancCTe)


