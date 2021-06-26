from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v300 import *



class evCancCECTe(ComplexType):
    """Schema XML de validação do evento cancelamento do comprovante de entrega eletrônico do CT-e 
110181"""
    descEvento: str = Element(str)
    nProt: TProt = Element(TProt)
    nProtCE: TProt = Element(TProt)

evCancCECTe: evCancCECTe = Element(evCancCECTe)
