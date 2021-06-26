from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v300 import *



class evRegMultimodal(ComplexType):
    """Schema XML de validação do evento Registro Multimodal 110160"""
    descEvento: str = Element(str, documentation=['Descrição do Evento - “Registro Multimodal”'])
    xRegistro: str = Element(str, documentation=['Informação complementar sobre o registro, indicação do tipo de documento utilizado e demais situações ocorridas no Multimodal (Texto Livre).'])
    nDoc: str = Element(str, documentation=['Numero do Documento lançado no CT-e Multimodal'])

evRegMultimodal: evRegMultimodal = Element(evRegMultimodal, documentation=['Schema XML de validação do evento Registro Multimodal 110160'])
