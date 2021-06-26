from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *



class detEvento(ComplexType):
    """Schema XML de validação do evento do cancelamento 1101111"""
    descEvento: str = Element(str, documentation=['Descrição do Evento - “Cancelamento”'])
    nProt: TProt = Element(TProt, documentation=['Número do Protocolo de Status da NF-e. 1 posição (1 – Secretaria de Fazenda Estadual 2 – Receita Federal); 2 posições ano; 10 seqüencial no ano.'])
    xJust: TJust = Element(TJust, documentation=['Justificativa do cancelamento'])
    versao: str = Attribute(None)

detEvento: detEvento = Element(detEvento, documentation=['Schema XML de validação do evento do cancelamento 1101111'])
