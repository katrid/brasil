from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v300 import *



class evPrestDesacordo(ComplexType):
    """Schema XML de validação do evento Prestação do Serviço em Desacordo 610110"""
    descEvento: str = Element(str)
    indDesacordoOper: str = Element(str)
    xObs: str = Element(str)

evPrestDesacordo: evPrestDesacordo = Element(evPrestDesacordo)
