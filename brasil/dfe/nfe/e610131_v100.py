from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *


class detEvento(ComplexType):
    descEvento: str = Element(str)
    cOrgaoAutor: TCOrgaoIBGE = Element(TCOrgaoIBGE)
    tpAutor: str = Element(str)
    verAplic: TVerAplic = Element(TVerAplic)
    chCTe: str = Element(str)
    nProtCTeCanc: str = Element(str)
    versao: str = Attribute(None)

detEvento: detEvento
