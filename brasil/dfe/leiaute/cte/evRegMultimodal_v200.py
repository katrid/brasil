from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v200 import *



class evRegMultimodal(ComplexType):
    """Schema XML de validação do evento Registro Multimodal 110160"""
    descEvento: str = Element(str)
    xRegistro: str = Element(str)
    nDoc: str = Element(str)

evRegMultimodal: evRegMultimodal = Element(evRegMultimodal)
