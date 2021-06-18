from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *


class TRespPedido(Element):
    """Resposta a um tpEvento 111500 ou 111501"""
    statPrazo: str = Element(str)
    class itemPedido(ComplexType):
        statPedido: str = Element(str)
        justStatus: str = Element(str)
        justStaOutra: List[str] = Element(str, min_occurs=0, max_occurs=1)
        numItem: str = Attribute(None)
    itemPedido: itemPedido


class detEvento(ComplexType):
    descEvento: str = Element(str)
    idPedido: str = Element(str)
    respPedido: TRespPedido = Element(TRespPedido)
    versao: str = Attribute(None)

detEvento: detEvento
