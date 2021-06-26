from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *



class detEvento(ComplexType):
    """Informações do Pedido de Prorrogação"""
    descEvento: str = Element(str, documentation=['Pedido de Prorrogação ou Pedido de Prorrogacao\x94'])
    nProt: TProt = Element(TProt, documentation=['Informar o número do Protocolo de Autorização da NF-e a ser Prorrogada. (vide item 5.6).'])

    class itemPedido(ComplexType):
        """Item do Pedido de Prorrogação. Recomenda-se agrupar a maior quantidade de itens em cada Pedido de Prorrogação"""
        _min_occurs = 1
        _max_occurs = 990

        def add(self, qtdeItem=None, numItem=None) -> detEvento.itemPedido:
            return super().add(qtdeItem=qtdeItem, numItem=numItem)

        qtdeItem: TDec_1104v = Element(TDec_1104v, tipo="N", tam=(11, 4), base_type=Decimal, documentation=['Quantidade do item que será solicitado a prorrogação de prazo'])
        numItem: str = Attribute(None)
    itemPedido: List[itemPedido] = Element(itemPedido, min_occurs=1, max_occurs=990, documentation=['Item do Pedido de Prorrogação. Recomenda-se agrupar a maior quantidade de itens em cada Pedido de Prorrogação'])
    versao: str = Attribute(None)

detEvento: detEvento = Element(detEvento, documentation=['Informações do Pedido de Prorrogação'])
