from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposDistDFe_v100 import *


class distDFeInt(ComplexType):
    tpAmb: TAmb = Element(TAmb)
    cUFAutor: TCodUfIBGE = Element(TCodUfIBGE)
    versao: str = Attribute(TVerDistDFe)

distDFeInt: distDFeInt
