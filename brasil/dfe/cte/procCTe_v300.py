from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .cteTiposBasico_v300 import *

from .consReciCTeTiposBasico_v300 import *


class cteProc(ComplexType):
    CTe: TCTe = Element(TCTe)
    protCTe: TProtCTe = Element(TProtCTe)
    versao: str = Attribute(TVerCTe)
    ipTransmissor: str = Attribute(TIPv4)

cteProc: cteProc
