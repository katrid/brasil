from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *



class detEvento(ComplexType):
    """Schema XML de validação do evento do Confirmação de Internalização da Mercadoria na SUFRAMA 990910"""
    descEvento: str = Element(str, documentation=['Descrição do Evento - “Confirmação de Internalização da Mercadoria na SUFRAMA”'])
    PINe: str = Element(str, documentation=['Número do PIN-e -  Protocolo de Internalização de Mercadoria Nacional eletronico'])
    dVistoria: TDateTimeUTC = Element(TDateTimeUTC, documentation=['Data de ocorrência da vistoria, formato UTC (AAAA-MM-DDThh:mm:ssTZD, onde TZD = +hh:mm ou -hh:mm)'])
    locVistoria: str = Element(str, documentation=['Localidade onde ocorreu a vistoria'])
    postoVistoria: str = Element(str, documentation=['Nome Posto do ponto onde ocorreu a vistoria'])
    xHistorico: str = Element(str, documentation=['Histórico da ocorrência, se existir.'])
    versao: str = Attribute(None)

detEvento: detEvento = Element(detEvento, documentation=['Schema XML de validação do evento do Confirmação de Internalização da Mercadoria na SUFRAMA 990910'])
