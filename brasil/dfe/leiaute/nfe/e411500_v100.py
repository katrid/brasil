from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *



class TRespPedido(Element):
    """Resposta a um tpEvento 111500 ou 111501"""
    statPrazo: str = Element(str, documentation=['Identificador do cumprimento do prazo para solicitação do pedido de prorrogação: 0 \x96 Após o prazo, 1 \x96 Dentro do prazo'])

    class itemPedido(ComplexType):
        """Item do Pedido de Prorrogação"""
        _min_occurs = 1
        _max_occurs = 990

        def add(self, statPedido=None, justStatus=None, justStaOutra=None, numItem=None) -> TRespPedido.itemPedido:
            return super().add(statPedido=statPedido, justStatus=justStatus, justStaOutra=justStaOutra, numItem=numItem)

        statPedido: str = Element(str, documentation=['Resposta do Fisco ao item do Pedido de Prorrogação: 1 - Deferido,    2 - Indeferido'])
        justStatus: str = Element(str, documentation=['Justificativa da resposta do Fisco ao item do Pedido de Prorrogação'])
        justStaOutra: List[str] = Element(str, max_occurs=1, documentation=['Justificativa diferente das opções disponíveis no campo P25'])
        numItem: str = Attribute(None)
    itemPedido: List[itemPedido] = Element(itemPedido, min_occurs=1, max_occurs=990, documentation=['Item do Pedido de Prorrogação'])



class detEvento(ComplexType):
    """Informações do Fisco"""
    descEvento: str = Element(str, documentation=['Fisco Prorrogação ICMS remessa para industrialização\x94'])
    idPedido: str = Element(str, documentation=['Identificador do Pedido de Prorrogação ou Cancelamento de Pedido de Prorrogação que deu origem ao evento do Fisco, a regra de formação do Id é:\n                        \x93ID\x94 + tpEvento + chave da NF-e + nSeqEvento\n                    '])
    respPedido: TRespPedido = Element(TRespPedido)
    versao: str = Attribute(None)

detEvento: detEvento = Element(detEvento, documentation=['Informações do Fisco'])
