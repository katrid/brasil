from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v400 import *



class evCancIECTe(ComplexType):
    """Schema XML de validação do evento cancelamento do insucesso de entrega eletrônico do CT-e 
110191"""
    descEvento: str = Element(str, documentation=['Descrição do Evento - “Cancelamento do Insucesso de Entrega do CT-e”'])
    nProt: TProt = Element(TProt, documentation=['Número do Protocolo de autorização do CT-e'])
    nProtIE: TProt = Element(TProt, documentation=['Número do Protocolo de autorização do evento a ser cancelado '])

evCancIECTe: evCancIECTe = Element(evCancIECTe, documentation=['Schema XML de validação do evento cancelamento do insucesso de entrega eletrônico do CT-e \n110191'])
