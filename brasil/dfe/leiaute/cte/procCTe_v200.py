from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .cteTiposBasico_v200 import *

from .consReciCTeTiposBasico_v200 import *



class cteProc(ComplexType):
    """CT-e processado"""
    CTe: TCTe = Element(TCTe)
    protCTe: TProtCTe = Element(TProtCTe)
    versao: str = Attribute(TVerCTe)

cteProc: cteProc = Element(cteProc, documentation=[' CT-e processado'])
