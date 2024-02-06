from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoMDFeTiposBasico_v300 import *



class evCancMDFe(ComplexType):
    """Schema XML de validação do evento do cancelamento 
110111"""
    descEvento: str = Element(str, documentation=['Descrição do Evento - “Cancelamento”'])
    nProt: TProt = Element(TProt, documentation=['Número do Protocolo de Status do MDF-e.\n1 posição tipo de autorizador (9 -SEFAZ Nacional ); \n2 posições ano; \n10 seqüencial no ano.'])
    xJust: TJust = Element(TJust, documentation=['Justificativa do Cancelamento'])

evCancMDFe: evCancMDFe = Element(evCancMDFe, documentation=['Schema XML de validação do evento do cancelamento \n110111'])
