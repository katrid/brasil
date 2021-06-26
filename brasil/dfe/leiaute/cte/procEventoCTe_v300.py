from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v300 import *



class procEventoCTe(ComplexType):
    """Pedido de Registro de Eventos de CT-e processado"""
    pass

procEventoCTe: procEventoCTe = Element(procEventoCTe, documentation=['Pedido de Registro de Eventos de CT-e processado'])
