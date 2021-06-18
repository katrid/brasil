from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v300 import *

from .cteTiposBasico_v300 import *


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
        vFrete: TDec_1302 = Element(TDec_1302)
        chCTeFerroOrigem: TChNFe = Element(TChNFe, min_occurs=0)
        class ferroEnv(ComplexType):
            CNPJ: TCnpj = Element(TCnpj)
            cInt: str = Element(str, min_occurs=0)
            IE: TIe = Element(TIe, min_occurs=0)
            xNome: str = Element(str)
            enderFerro: TEnderFer = Element(TEnderFer)
        ferroEnv: ferroEnv
    trafMut: trafMut
    fluxo: str = Element(str)

ferrov: ferrov
