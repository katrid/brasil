from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v300 import *


class evCCeCTe(ComplexType):
    descEvento: str = Element(str)
    class infCorrecao(ComplexType):
        grupoAlterado: str = Element(str)
        campoAlterado: str = Element(str)
        valorAlterado: str = Element(str)
        nroItemAlterado: str = Element(str, min_occurs=0)
    infCorrecao: infCorrecao
    xCondUso: str = Element(str)

evCCeCTe: evCCeCTe
