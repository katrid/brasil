from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v400 import *

from .cteTiposBasico_v400 import *



class multimodal(ComplexType):
    """Informações do Multimodal"""
    COTM: str = Element(str, documentation=['Número do Certificado do Operador de Transporte Multimodal', None])
    indNegociavel: str = Element(str, documentation=['Indicador Negociável\nPreencher com: 0 - Não Negociável; 1 - Negociável', None])

    class seg(ComplexType):
        """Informações de Seguro do Multimodal"""

        class infSeg(ComplexType):
            """Informações da seguradora"""
            xSeg: str = Element(str, documentation=['Nome da Seguradora'])
            CNPJ: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['Número do CNPJ da seguradora', 'Obrigatório apenas se responsável pelo seguro for (2) responsável pela contratação do transporte - pessoa jurídica'])
        infSeg: infSeg = Element(infSeg, documentation=['Informações da seguradora'])
        nApol: str = Element(str, documentation=['Número da Apólice', 'Obrigatório pela lei 11.442/07 (RCTRC)'])
        nAver: str = Element(str, documentation=['Número da Averbação', 'Não é obrigatório, pois muitas averbações ocorrem aapós a emissão do CT, mensalmente, por exemplo.'])
    seg: seg = Element(seg, documentation=['Informações de Seguro do Multimodal'])

multimodal: multimodal = Element(multimodal, documentation=['Informações do Multimodal'])
