from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *


class detEvento(ComplexType):
    descEvento: str = Element(str)
    tpAutor: str = Element(str)
    verAplic: TVerAplic = Element(TVerAplic)
    class itensAverbados(ComplexType):
        dhEmbarque: TDateTimeUTC = Element(TDateTimeUTC)
        dhAverbacao: TDateTimeUTC = Element(TDateTimeUTC)
        nDue: str = Element(str)
        nItem: str = Element(str)
        nItemDue: str = Element(str)
        qItem: TDec_1104Neg = Element(TDec_1104Neg)
        motAlteracao: str = Element(str, min_occurs=0)
    itensAverbados: itensAverbados
    versao: str = Attribute(None)

detEvento: detEvento
