from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .cteTiposBasico_v400 import *



class cteProc(ComplexType):
    """CT-e processado"""
    CTe: TCTe = Element(TCTe)
    protCTe: TProtCTe = Element(TProtCTe)
    versao: str = Attribute(TVerCTe)
    ipTransmissor: str = Attribute(TIPv4)
    nPortaCon: str = Attribute(None)
    dhConexao: str = Attribute(TDateTimeUTC)

cteProc: cteProc = Element(cteProc, documentation=[' CT-e processado'])
