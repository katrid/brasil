from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v300 import *

from .xmldsig_core_schema_v101 import *


class TConsSitCTe(Element):
    """Tipo Pedido de Consulta da Situação Atual do Conhecimento de Transporte eletrônico"""
    tpAmb: TAmb = Element(TAmb)
    xServ: TServ = Element(TServ)
    chCTe: TChNFe = Element(TChNFe)
    versao: str = Attribute(None)


class TVerConsSitCTe(str):
    """Tipo Versão do Consulta situação de CT-e - 2.00"""
    _restriction = Restriction(base=r"xs:string", pattern=r"3\.00", enumeration=[])
    pass


class TRetConsSitCTe(Element):
    """Tipo Retorno de Pedido de Consulta da Situação Atual do Conhecimento de Transporte eletrônico"""
    tpAmb: TAmb = Element(TAmb)
    verAplic: TVerAplic = Element(TVerAplic)
    cStat: TStat = Element(TStat)
    xMotivo: TMotivo = Element(TMotivo)
    cUF: TCodUfIBGE = Element(TCodUfIBGE)
    class procEventoCTe(ComplexType):
        versao: str = Attribute(None)
    procEventoCTe: procEventoCTe
    versao: str = Attribute(TVerConsSitCTe)


