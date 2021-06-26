from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v310 import *



class detEvento(ComplexType):
    """Informações do Cancelamento de Pedido de Prorrogação"""
    descEvento: str = Element(str, documentation=['Cancelamento de Pedido de Prorrogação\x94 ou \x93Cancelamento de Pedido de Prorrogacao\x94'])
    idPedidoCancelado: str = Element(str, documentation=['Identificador do evento a ser cancelado, a regra de formação do Id é: \x93ID\x94 + tpEvento + chave da NF-e + nSeqEvento'])
    nProt: TProt = Element(TProt, documentation=['Informar o número do Protocolo de Autorização do Pedido de Prorrogaçãoa ser cancelado.'])
    versao: str = Attribute(None)

detEvento: detEvento = Element(detEvento, documentation=['Informações do Cancelamento de Pedido de Prorrogação'])
