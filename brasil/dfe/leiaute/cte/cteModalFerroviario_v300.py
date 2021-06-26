from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v300 import *

from .cteTiposBasico_v300 import *



class TEnderFer(Element):
    """Tipo Dados do Endereço"""
    xLgr: str = Element(str)
    nro: str = Element(str)
    xCpl: str = Element(str)
    xBairro: str = Element(str)
    cMun: TCodMunIBGE = Element(TCodMunIBGE)
    xMun: str = Element(str)
    CEP: str = Element(str)
    UF: TUf = Element(TUf)



class ferrov(ComplexType):
    """Informações do modal Ferroviário"""
    tpTraf: str = Element(str)

    class trafMut(ComplexType):
        """Detalhamento de informações para o tráfego mútuo"""
        respFat: str = Element(str)
        ferrEmi: str = Element(str)
        vFrete: TDec_1302 = Element(TDec_1302)
        chCTeFerroOrigem: TChNFe = Element(TChNFe)

        class ferroEnv(ComplexType):
            """Informações das Ferrovias Envolvidas"""
            _max_occurs = -1

            def add(self, CNPJ=None, cInt=None, IE=None, xNome=None, enderFerro=None) -> ferrov.trafMut.ferroEnv:
                return super().add(CNPJ=CNPJ, cInt=cInt, IE=IE, xNome=xNome, enderFerro=enderFerro)

            CNPJ: TCnpj = Element(TCnpj)
            cInt: str = Element(str)
            IE: TIe = Element(TIe)
            xNome: str = Element(str)
            enderFerro: TEnderFer = Element(TEnderFer)
        ferroEnv: List[ferroEnv] = Element(ferroEnv, max_occurs=-1)
    trafMut: trafMut = Element(trafMut)
    fluxo: str = Element(str)

ferrov: ferrov = Element(ferrov)
