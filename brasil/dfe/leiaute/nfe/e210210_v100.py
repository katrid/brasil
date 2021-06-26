from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime


class detEvento(ComplexType):
    """Schema XML de validação do evento de Ciência da Operação"""
    descEvento: str = Element(str, documentation=['Descrição do Evento:\n\t\t\t\t\t\t\t\t\t\t\t "Ciência da Operação"'])
    versao: str = Attribute(None)

detEvento: detEvento = Element(detEvento, documentation=['Schema XML de validação do evento de Ciência da Operação'])
