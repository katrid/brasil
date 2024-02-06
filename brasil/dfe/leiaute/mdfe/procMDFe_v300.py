from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .mdfeTiposBasico_v300 import *



class mdfeProc(ComplexType):
    """MDF-e processado"""
    MDFe: TMDFe = Element(TMDFe)
    protMDFe: TProtMDFe = Element(TProtMDFe)
    versao: str = Attribute(TVerMDe)
    ipTransmissor: str = Attribute(TIPv4)
    nPortaCon: str = Attribute(None)
    dhConexao: str = Attribute(TDateTimeUTC)

mdfeProc: mdfeProc = Element(mdfeProc, documentation=[' MDF-e processado'])
