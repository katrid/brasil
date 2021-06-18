from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v300 import *


class evGTV(ComplexType):
    descEvento: str = Element(str)
    class infGTV(ComplexType):
        nDoc: str = Element(str)
        id: str = Element(str)
        serie: str = Element(str, min_occurs=0)
        subserie: str = Element(str, min_occurs=0)
        dEmi: TData = Element(TData)
        nDV: str = Element(str)
        qCarga: TDec_1104 = Element(TDec_1104)
        class infEspecie(ComplexType):
            tpEspecie: str = Element(str)
            vEspecie: TDec_1302 = Element(TDec_1302, min_occurs=0)
        infEspecie: infEspecie
        class rem(ComplexType):
            IE: str = Element(str, min_occurs=0)
            UF: TUf = Element(TUf)
            xNome: str = Element(str)
        rem: rem
        class dest(ComplexType):
            IE: str = Element(str, min_occurs=0)
            UF: TUf = Element(TUf)
            xNome: str = Element(str)
        dest: dest
        placa: TPlaca = Element(TPlaca, min_occurs=0)
        UF: TUf = Element(TUf, min_occurs=0)
        RNTRC: str = Element(str, min_occurs=0)
    infGTV: infGTV

evGTV: evGTV
