from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime

class detEvento(ComplexType):
    descEvento: str = Element(str)
    xJust: str = Element(str, min_occurs=0)
    versao: str = Attribute(None)

detEvento: detEvento
