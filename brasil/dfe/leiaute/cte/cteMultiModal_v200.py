from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v200 import *

from .cteTiposBasico_v200 import *



class multimodal(ComplexType):
    """Informações do Multimodal"""
    COTM: str = Element(str, documentation=['Número do Certificado do Operador de Transporte Multimodal', None])
    indNegociavel: str = Element(str, documentation=['Indicador Negociável\nPreencher com: 0 - Não Negociável; 1 - Negociável', None])

multimodal: multimodal = Element(multimodal, documentation=['Informações do Multimodal'])
