from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v400 import *



class evCancPrestDesacordo(ComplexType):
    """Schema XML de validação do evento Cancelamento Prestação do Serviço em Desacordo 610111"""
    descEvento: str = Element(str, documentation=['Descrição do Evento - “Cancelamento Prestação do Serviço em Desacordo”'])
    nProtEvPrestDes: TProt = Element(TProt, documentation=['Protocolo do evento que será cancelado', 'Informar o número do protocolo de autorização do evento de prestação de serviço em desacordo que será cancelado '])

evCancPrestDesacordo: evCancPrestDesacordo = Element(evCancPrestDesacordo, documentation=['Schema XML de validação do evento Cancelamento Prestação do Serviço em Desacordo 610111'])
