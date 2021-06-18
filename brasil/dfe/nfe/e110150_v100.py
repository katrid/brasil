from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *


class detEvento(ComplexType):
    descEvento: str = Element(str)
    cOrgaoAutor: TCodUfIBGE = Element(TCodUfIBGE)
    tpAutor: str = Element(str)
    verAplic: TVerAplic = Element(TVerAplic)
    class autXML(ComplexType):
        pass
    autXML: autXML
    tpAutorizacao: str = Element(str, min_occurs=0)
    xCondUso: str = Element(str, min_occurs=0)
    versao: str = Attribute(None)

detEvento: detEvento
