from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v300 import *

from .cteTiposBasico_v300 import *


class multimodal(ComplexType):
    COTM: str = Element(str)
    indNegociavel: str = Element(str)
    class seg(ComplexType):
        class infSeg(ComplexType):
            xSeg: str = Element(str)
            CNPJ: TCnpjOpc = Element(TCnpjOpc)
        infSeg: infSeg
        nApol: str = Element(str)
        nAver: str = Element(str)
    seg: seg

multimodal: multimodal
