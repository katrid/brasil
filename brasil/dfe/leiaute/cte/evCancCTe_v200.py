from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v200 import *



class evCancCTe(ComplexType):
    """Schema XML de validação do evento do cancelamento 
110111"""
    descEvento: str = Element(str, documentation=['Descrição do Evento - “Cancelamento”'])
    nProt: TProt = Element(TProt, documentation=['Número do Protocolo de Status do CT-e. 1 posição tipo de autorizador (1 – Secretaria de Fazenda Estadual,  3 - SEFAZ Virtual RS, 5 - SEFAZ Virtual SP ); 2 posições ano; 10 seqüencial no ano.'])
    xJust: TJust = Element(TJust, documentation=['Justificativa do Cancelamento'])

evCancCTe: evCancCTe = Element(evCancCTe, documentation=['Schema XML de validação do evento do cancelamento \n110111'])
