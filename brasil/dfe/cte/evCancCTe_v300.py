from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v300 import *


class evCancCTe(ComplexType):
    descEvento: str = Element(str)
    nProt: TProt = Element(TProt)
    xJust: TJust = Element(TJust)

evCancCTe: evCancCTe
