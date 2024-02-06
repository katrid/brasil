from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoMDFeTiposBasico_v300 import *



class evConfirmaServMDFe(ComplexType):
    """Schema XML de validação do evento de confirmação do serviço de transporte 110117"""
    descEvento: str = Element(str, documentation=['Descrição do Evento - “Confirmação Serviço Transporte”'])
    nProt: TProt = Element(TProt, documentation=['Número do Protocolo de Status do MDF-e. \n1 posição tipo de autorizador (9 - SEFAZ Nacional ); \n2 posições ano;\n10 seqüencial no ano.'])

evConfirmaServMDFe: evConfirmaServMDFe = Element(evConfirmaServMDFe, documentation=['Schema XML de validação do evento de confirmação do serviço de transporte 110117'])
