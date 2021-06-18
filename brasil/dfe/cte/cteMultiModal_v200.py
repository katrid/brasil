from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v200 import *

from .cteTiposBasico_v200 import *


class multimodal(ComplexType):
    COTM: str = Element(str)
    indNegociavel: str = Element(str)

multimodal: multimodal
