from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v300 import *

from .cteTiposBasico_v300 import *



class multimodal(ComplexType):
    """Informações do Multimodal"""
    COTM: str = Element(str)
    indNegociavel: str = Element(str)

    class seg(ComplexType):
        """Informações de Seguro do Multimodal"""

        class infSeg(ComplexType):
            """Informações da seguradora"""
            xSeg: str = Element(str)
            CNPJ: TCnpjOpc = Element(TCnpjOpc)
        infSeg: infSeg = Element(infSeg)
        nApol: str = Element(str)
        nAver: str = Element(str)
    seg: seg = Element(seg)

multimodal: multimodal = Element(multimodal)
