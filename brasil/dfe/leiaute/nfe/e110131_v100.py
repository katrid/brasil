from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *



class detEvento(ComplexType):
    """Schema XML de validação do evento de Cancelamento do Comprovante de Entrega de NF-e"""
    descEvento: str = Element(str)
    cOrgaoAutor: TCOrgaoIBGE = Element(TCOrgaoIBGE)
    tpAutor: str = Element(str)
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo do Autor do Evento'])
    nProtEvento: TProt = Element(TProt, documentation=['Número do Protocolo de Autorização do Evento da NF-e a que se refere este cancelamento.'])
    versao: str = Attribute(None)

detEvento: detEvento = Element(detEvento, documentation=['Schema XML de validação do evento de Cancelamento do Comprovante de Entrega de NF-e'])
