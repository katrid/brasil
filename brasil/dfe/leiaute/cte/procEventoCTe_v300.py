from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v300 import *



class procEventoCTe(ComplexType):
    """Pedido de Registro de Eventos de CT-e processado"""
    pass

procEventoCTe: procEventoCTe = Element(procEventoCTe)
