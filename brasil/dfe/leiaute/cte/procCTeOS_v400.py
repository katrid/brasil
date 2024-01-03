from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .cteTiposBasico_v400 import *



class cteOSProc(ComplexType):
    """CT-e OS processado"""
    CTeOS: TCTeOS = Element(TCTeOS)
    protCTe: TProtCTeOS = Element(TProtCTeOS)
    versao: str = Attribute(TVerCTe)
    ipTransmissor: str = Attribute(TIPv4)
    nPortaCon: str = Attribute(None)
    dhConexao: str = Attribute(TDateTimeUTC)

cteOSProc: cteOSProc = Element(cteOSProc, documentation=[' CT-e OS processado'])
