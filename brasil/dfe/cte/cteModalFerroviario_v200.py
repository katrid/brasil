from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v200 import *

from .cteTiposBasico_v200 import *


class TEnderFer(Element):
    """Tipo Dados do Endereço"""
    xLgr: str = Element(str)
    nro: str = Element(str, min_occurs=0)
    xCpl: str = Element(str, min_occurs=0)
    xBairro: str = Element(str, min_occurs=0)
    cMun: TCodMunIBGE = Element(TCodMunIBGE)
    xMun: str = Element(str)
    CEP: str = Element(str)
    UF: TUf = Element(TUf)


class ferrov(ComplexType):
    tpTraf: str = Element(str)
    class trafMut(ComplexType):
        respFat: str = Element(str)
        ferrEmi: str = Element(str)
    trafMut: trafMut
    fluxo: str = Element(str)
    idTrem: str = Element(str, min_occurs=0)
    vFrete: TDec_1302 = Element(TDec_1302)
    class ferroEnv(ComplexType):
        CNPJ: TCnpj = Element(TCnpj)
        cInt: str = Element(str, min_occurs=0)
        IE: TIe = Element(TIe, min_occurs=0)
        xNome: str = Element(str)
        enderFerro: TEnderFer = Element(TEnderFer)
    ferroEnv: ferroEnv
    class detVag(ComplexType):
        nVag: str = Element(str)
        cap: TDec_0303 = Element(TDec_0303, min_occurs=0)
        tpVag: str = Element(str, min_occurs=0)
        pesoR: TDec_0303 = Element(TDec_0303)
        pesoBC: TDec_0303 = Element(TDec_0303)
    detVag: detVag

ferrov: ferrov
