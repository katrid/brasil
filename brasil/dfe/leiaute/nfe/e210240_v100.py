from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime


class detEvento(ComplexType):
    """Schema XML de validação do evento de Recusa de Recebimento (Operação não Realizada)"""
    descEvento: str = Element(str, documentation=['Descrição do Evento:"Operação não Realizada"'])
    xJust: str = Element(str, documentation=['Justificativa de recusa do recebimento da mercadoria'])
    versao: str = Attribute(None)

detEvento: detEvento = Element(detEvento, documentation=['Schema XML de validação do evento de Recusa de Recebimento (Operação não Realizada)'])
