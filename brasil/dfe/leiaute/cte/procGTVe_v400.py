from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .cteTiposBasico_v400 import *



class GTVeProc(ComplexType):
    """GTV-e processada"""
    GTVe: TGTVe = Element(TGTVe)
    protCTe: TProtGTVe = Element(TProtGTVe)
    versao: str = Attribute(TVerCTe)
    ipTransmissor: str = Attribute(TIPv4)
    nPortaCon: str = Attribute(None)
    dhConexao: str = Attribute(TDateTimeUTC)

GTVeProc: GTVeProc = Element(GTVeProc, documentation=[' GTV-e processada'])
