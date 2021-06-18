from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v200 import *


class evRegMultimodal(ComplexType):
    descEvento: str = Element(str)
    xRegistro: str = Element(str)
    nDoc: str = Element(str, min_occurs=0)

evRegMultimodal: evRegMultimodal
