from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *


class detEvento(ComplexType):
    descEvento: str = Element(str)
    nProt: TProt = Element(TProt)
    class itemPedido(ComplexType):
        qtdeItem: TDec_1104v = Element(TDec_1104v)
        numItem: str = Attribute(None)
    itemPedido: itemPedido
    versao: str = Attribute(None)

detEvento: detEvento
