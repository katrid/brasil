from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoMDFeTiposBasico_v300 import *



class evEncMDFe(ComplexType):
    """Schema XML de validação do evento do encerramento 
110112"""
    descEvento: str = Element(str, documentation=['Descrição do Evento - “Encerramento”'])
    nProt: TProt = Element(TProt, documentation=['Número do Protocolo de Status do MDF-e. \n1 posição tipo de autorizador (9 - SEFAZ Nacional ); \n2 posições ano;\n10 seqüencial no ano.'])
    dtEnc: TData = Element(TData, base_type=date, documentation=['Data que o Manifesto foi encerrado'])
    cUF: TCodUfIBGE_EX = Element(TCodUfIBGE_EX, documentation=['UF de encerramento do Manifesto'])
    cMun: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do Município de Encerramento do manifesto'])
    indEncPorTerceiro: str = Element(str, documentation=['Indicador que deve ser informado quando o encerramento for registrado pelo transportador terceiro', 'Informar valor 1 quando o MDFe for encerrado pelo transportador terceiro, este sendo diferente do emitente do MDFe'])

evEncMDFe: evEncMDFe = Element(evEncMDFe, documentation=['Schema XML de validação do evento do encerramento \n110112'])
