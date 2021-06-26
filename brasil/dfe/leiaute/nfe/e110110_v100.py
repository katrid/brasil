from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime


class detEvento(ComplexType):
    """Schema XML de validação do evento do carta de correção e1101110"""
    descEvento: str = Element(str, documentation=['Descrição do Evento - “Carta de Correção”'])
    xCorrecao: str = Element(str, documentation=['Correção a ser considerada'])
    xCondUso: str = Element(str, documentation=['Texto Fixo com as condições de uso da Carta de Correção'])
    versao: str = Attribute(None)

detEvento: detEvento = Element(detEvento, documentation=['Schema XML de validação do evento do carta de correção e1101110'])
