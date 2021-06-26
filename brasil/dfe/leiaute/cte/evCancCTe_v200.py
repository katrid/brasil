from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v200 import *



class evCancCTe(ComplexType):
    """Schema XML de validação do evento do cancelamento 
110111"""
    descEvento: str = Element(str)
    nProt: TProt = Element(TProt)
    xJust: TJust = Element(TJust)

evCancCTe: evCancCTe = Element(evCancCTe)
