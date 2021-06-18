from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v300 import *

from .cteTiposBasico_v300 import *


class rodo(ComplexType):
    RNTRC: str = Element(str)
    class occ(ComplexType):
        serie: str = Element(str, min_occurs=0)
        nOcc: str = Element(str)
        dEmi: TData = Element(TData)
        class emiOcc(ComplexType):
            CNPJ: TCnpj = Element(TCnpj)
            cInt: str = Element(str, min_occurs=0)
            IE: TIe = Element(TIe)
            UF: TUf = Element(TUf)
            fone: TFone = Element(TFone, min_occurs=0)
        emiOcc: emiOcc
    occ: occ

rodo: rodo
