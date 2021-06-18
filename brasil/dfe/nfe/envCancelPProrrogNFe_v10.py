from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v310 import *


class detEvento(ComplexType):
    descEvento: str = Element(str)
    idPedidoCancelado: str = Element(str)
    nProt: TProt = Element(TProt)
    versao: str = Attribute(None)

detEvento: detEvento
