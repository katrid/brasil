from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v200 import *



class aereo(ComplexType):
    """Informações do modal Aéreo"""
    nMinu: str = Element(str)
    nOCA: str = Element(str)
    dPrevAereo: TData = Element(TData)
    xLAgEmi: str = Element(str)
    IdT: str = Element(str)

    class tarifa(ComplexType):
        """Informações de tarifa"""
        CL: str = Element(str)
        cTar: str = Element(str)
        vTar: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
    tarifa: tarifa = Element(tarifa)

    class natCarga(ComplexType):
        """Natureza da carga"""
        xDime: str = Element(str)
        cInfManu: List[str] = Element(str, max_occurs=-1)
        cIMP: List[str] = Element(str, max_occurs=-1)
    natCarga: natCarga = Element(natCarga)

aereo: aereo = Element(aereo)
