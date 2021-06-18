from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .cteTiposBasico_v300 import *


class aquav(ComplexType):
    vPrest: TDec_1302 = Element(TDec_1302)
    vAFRMM: TDec_1302 = Element(TDec_1302)
    xNavio: str = Element(str)
    class balsa(ComplexType):
        xBalsa: str = Element(str)
    balsa: balsa
    nViag: str = Element(str, min_occurs=0)
    direc: str = Element(str)
    irin: str = Element(str)
    class detCont(ComplexType):
        nCont: TContainer = Element(TContainer)
        class lacre(ComplexType):
            nLacre: str = Element(str)
        lacre: lacre
        class infDoc(ComplexType):
            pass
        infDoc: infDoc
    detCont: detCont
    tpNav: str = Element(str, min_occurs=0)

aquav: aquav
