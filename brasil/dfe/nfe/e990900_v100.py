from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *


class detEvento(ComplexType):
    descEvento: str = Element(str)
    PINe: str = Element(str)
    dVistoria: str = Element(str)
    locVistoria: str = Element(str)
    postoVistoria: str = Element(str)
    xHistorico: str = Element(str)
    versao: str = Attribute(None)

detEvento: detEvento
