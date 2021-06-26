from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v200 import *

from .cteTiposBasico_v200 import *



class duto(ComplexType):
    """Informações do modal Dutoviário"""
    vTar: TDec_0906Opc = Element(TDec_0906Opc, tipo="N", tam=(9, 6))
    dIni: TData = Element(TData)
    dFim: TData = Element(TData)

duto: duto = Element(duto)
