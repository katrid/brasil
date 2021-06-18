from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *


class detEvento(ComplexType):
    descEvento: str = Element(str)
    cOrgaoAutor: TCodUfIBGE = Element(TCodUfIBGE)
    tpAutor: str = Element(str)
    verAplic: TVerAplic = Element(TVerAplic)
    nProt: TProt = Element(TProt)
    xJust: TJust = Element(TJust)
    chNFeRef: TChNFe = Element(TChNFe)
    versao: str = Attribute(None)

detEvento: detEvento
