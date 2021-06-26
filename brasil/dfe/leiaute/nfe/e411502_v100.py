from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *



class TRespCancPedido(Element):
    """Resposta a um tpEvento 111502 ou 111503."""
    statCancPedido: str = Element(str, documentation=['Resposta do Fisco ao Cancelamento do Pedido de Prorrogação: 1 - Deferido, 2 - Indeferido'])
    justStatus: str = Element(str, documentation=['Justificativa da resposta do Fisco ao Cancelamento de Pedido de Prorrogação'])
    justStaOutra: List[str] = Element(str, max_occurs=1, documentation=['Justificativa diferente das opções disponíveis no campo P29'])



class detEvento(ComplexType):
    """Informações do Fisco"""
    descEvento: str = Element(str, documentation=['Fisco Prorrogação ICMS remessa para industrialização\x94'])
    idPedido: str = Element(str, documentation=['Identificador do Pedido de Prorrogação ou Cancelamento de Pedido de Prorrogação que deu origem ao evento do Fisco, a regra de formação do Id é:\n                        \x93ID\x94 + tpEvento + chave da NF-e + nSeqEvento\n                    '])
    respCancPedido: TRespCancPedido = Element(TRespCancPedido)
    versao: str = Attribute(None)

detEvento: detEvento = Element(detEvento, documentation=['Informações do Fisco'])
