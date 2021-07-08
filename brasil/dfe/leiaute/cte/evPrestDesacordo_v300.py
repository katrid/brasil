from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v300 import *



class evPrestDesacordo(ComplexType):
    """Schema XML de validação do evento Prestação do Serviço em Desacordo 610110"""
    descEvento: str = Element(str, documentation=['Descrição do Evento - “Prestação do Serviço em Desacordo”'])
    indDesacordoOper: str = Element(str, documentation=['Indicador de operação em desacordo'])
    xObs: str = Element(str, documentation=['Observações do tomador'])

