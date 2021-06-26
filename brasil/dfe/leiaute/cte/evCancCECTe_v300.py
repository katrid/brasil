from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v300 import *



class evCancCECTe(ComplexType):
    """Schema XML de validação do evento cancelamento do comprovante de entrega eletrônico do CT-e 
110181"""
    descEvento: str = Element(str, documentation=['Descrição do Evento - “Cancelamento do Comprovante de Entrega do CT-e”'])
    nProt: TProt = Element(TProt, documentation=['Número do Protocolo de autorização do CT-e'])
    nProtCE: TProt = Element(TProt, documentation=['Número do Protocolo de autorização do evento a ser cancelado '])

evCancCECTe: evCancCECTe = Element(evCancCECTe, documentation=['Schema XML de validação do evento cancelamento do comprovante de entrega eletrônico do CT-e \n110181'])
