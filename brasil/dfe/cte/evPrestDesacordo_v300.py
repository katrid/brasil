from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v300 import *


class evPrestDesacordo(ComplexType):
    descEvento: str = Element(str)
    indDesacordoOper: str = Element(str)
    xObs: str = Element(str)

evPrestDesacordo: evPrestDesacordo
