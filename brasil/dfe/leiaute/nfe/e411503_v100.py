from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *



class TRespCancPedido(Element):
    """Resposta a um tpEvento 111502 ou 111503."""
    statCancPedido: str = Element(str)
    justStatus: str = Element(str)
    justStaOutra: List[str] = Element(str, max_occurs=1)



class detEvento(ComplexType):
    """Informações do Fisco"""
    descEvento: str = Element(str)
    idPedido: str = Element(str)
    respCancPedido: TRespCancPedido = Element(TRespCancPedido)
    versao: str = Attribute(None)

detEvento: detEvento = Element(detEvento)
