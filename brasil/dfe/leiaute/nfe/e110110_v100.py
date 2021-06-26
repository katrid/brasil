from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime


class detEvento(ComplexType):
    """Schema XML de validação do evento do carta de correção e1101110"""
    descEvento: str = Element(str)
    xCorrecao: str = Element(str)
    xCondUso: str = Element(str)
    versao: str = Attribute(None)

detEvento: detEvento = Element(detEvento)
