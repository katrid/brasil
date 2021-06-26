from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .cteTiposBasico_v300 import *



class cteOSProc(ComplexType):
    """CT-e OS processado"""
    CTeOS: TCTeOS = Element(TCTeOS)
    protCTe: TProtCTeOS = Element(TProtCTeOS)
    versao: str = Attribute(TVerCTe)
    ipTransmissor: str = Attribute(TIPv4)

cteOSProc: cteOSProc = Element(cteOSProc)
