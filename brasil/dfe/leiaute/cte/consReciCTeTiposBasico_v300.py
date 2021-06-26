from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposGeralCTe_v300 import *

from .cteTiposBasico_v300 import *



class TVerConsReciCTe(str):
    """Tipo Versão do Consulta Lote de CT-e"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"3\.00", enumeration=[])
    pass



class TConsReciCTe(Element):
    """Tipo Pedido de Consulta do Recibo do Lote de CT-e"""
    tpAmb: TAmb = Element(TAmb)
    nRec: TRec = Element(TRec)
    versao: str = Attribute(TVerConsReciCTe)



class TRetConsReciCTe(Element):
    """Tipo Retorno do Pedido de  Consulta do Recibo do Lote de CT-e"""
    tpAmb: TAmb = Element(TAmb)
    verAplic: TVerAplic = Element(TVerAplic)
    nRec: TRec = Element(TRec)
    cStat: TStat = Element(TStat)
    xMotivo: TMotivo = Element(TMotivo)
    cUF: TCodUfIBGE = Element(TCodUfIBGE)
    protCTe: List[TProtCTe] = Element(TProtCTe, max_occurs=50)
    versao: str = Attribute(TVerConsReciCTe)


