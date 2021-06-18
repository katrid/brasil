from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *


class TRespCancPedido(Element):
    """Resposta a um tpEvento 111502 ou 111503."""
    statCancPedido: str = Element(str)
    justStatus: str = Element(str)
    justStaOutra: List[str] = Element(str, min_occurs=0, max_occurs=1)


class detEvento(ComplexType):
    descEvento: str = Element(str)
    idPedido: str = Element(str)
    respCancPedido: TRespCancPedido = Element(TRespCancPedido)
    versao: str = Attribute(None)

detEvento: detEvento
