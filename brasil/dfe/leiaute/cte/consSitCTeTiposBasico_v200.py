from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v200 import *

from .consReciCTeTiposBasico_v200 import *

from .cancCTeTiposBasico_v200 import *

from .eventoCTeTiposBasico_v200 import *

from .xmldsig_core_schema_v101 import *



class TConsSitCTe(Element):
    """Tipo Pedido de Consulta da Situação Atual do Conhecimento de Transporte eletrônico"""
    tpAmb: TAmb = Element(TAmb)
    xServ: TServ = Element(TServ)
    chCTe: TChNFe = Element(TChNFe)
    versao: str = Attribute(None)



class TVerConsSitCTe(str):
    """Tipo Versão do Consulta situação de CT-e - 2.00"""
    _restriction = Restriction(base=r"xs:string", pattern=r"2\.00", enumeration=[])
    pass



class TRetConsSitCTe(Element):
    """Tipo Retorno de Pedido de Consulta da Situação Atual do Conhecimento de Transporte eletrônico"""
    _choice = [['protCTe', 'retCancCTe']]
    tpAmb: TAmb = Element(TAmb)
    verAplic: TVerAplic = Element(TVerAplic)
    cStat: TStat = Element(TStat)
    xMotivo: TMotivo = Element(TMotivo)
    cUF: TCodUfIBGE = Element(TCodUfIBGE)
    protCTe: TProtCTe = Element(TProtCTe)
    retCancCTe: TRetCancCTe = Element(TRetCancCTe)
    procEventoCTe: List[TProcEvento] = Element(TProcEvento, max_occurs=-1)
    versao: str = Attribute(TVerConsSitCTe)


