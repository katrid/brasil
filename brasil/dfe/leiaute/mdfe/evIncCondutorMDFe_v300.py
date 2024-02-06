from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoMDFeTiposBasico_v300 import *



class evIncCondutorMDFe(ComplexType):
    """Schema XML de validação do evento de inclusao de condutor 110114"""
    descEvento: str = Element(str, documentation=['Descrição do Evento - “Inclusao Condutor”'])

    class condutor(ComplexType):
        """Informações do(s) Condutor(s) do veículo"""
        xNome: str = Element(str, documentation=['Nome do Condutor'])
        CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CPF do Condutor'])
    condutor: condutor = Element(condutor, documentation=['Informações do(s) Condutor(s) do veículo'])

evIncCondutorMDFe: evIncCondutorMDFe = Element(evIncCondutorMDFe, documentation=['Schema XML de validação do evento de inclusao de condutor 110114'])
