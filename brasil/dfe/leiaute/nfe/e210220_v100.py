from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime


class detEvento(ComplexType):
    """Schema XML de validação do evento de desconhecimento da operação"""
    descEvento: str = Element(str, documentation=['Descrição do Evento:\n\t\t\t\t\t\t\t\t\t\t\t "Desconhecimento da Operacao"'])
    xJust: str = Element(str, documentation=['Justificativa de desconhecimento da Operacao'])
    versao: str = Attribute(None)

detEvento: detEvento = Element(detEvento, documentation=['Schema XML de validação do evento de desconhecimento da operação'])
