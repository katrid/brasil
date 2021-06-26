from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *



class TRespPedido(Element):
    """Resposta a um tpEvento 111500 ou 111501"""
    statPrazo: str = Element(str)

    class itemPedido(ComplexType):
        """Item do Pedido de Prorrogação"""
        _min_occurs = 1
        _max_occurs = 990

        def add(self, statPedido=None, justStatus=None, justStaOutra=None, numItem=None) -> TRespPedido.itemPedido:
            return super().add(statPedido=statPedido, justStatus=justStatus, justStaOutra=justStaOutra, numItem=numItem)

        statPedido: str = Element(str)
        justStatus: str = Element(str)
        justStaOutra: List[str] = Element(str, max_occurs=1)
        numItem: str = Attribute(None)
    itemPedido: List[itemPedido] = Element(itemPedido, min_occurs=1, max_occurs=990)



class detEvento(ComplexType):
    """Informações do Fisco"""
    descEvento: str = Element(str)
    idPedido: str = Element(str)
    respPedido: TRespPedido = Element(TRespPedido)
    versao: str = Attribute(None)

detEvento: detEvento = Element(detEvento)
