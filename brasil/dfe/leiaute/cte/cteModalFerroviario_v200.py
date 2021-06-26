from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v200 import *

from .cteTiposBasico_v200 import *



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
    trafMut: trafMut = Element(trafMut)
    fluxo: str = Element(str)
    idTrem: str = Element(str)
    vFrete: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))

    class ferroEnv(ComplexType):
        """Informações das Ferrovias Envolvidas"""
        _max_occurs = -1

        def add(self, CNPJ=None, cInt=None, IE=None, xNome=None, enderFerro=None) -> ferrov.ferroEnv:
            return super().add(CNPJ=CNPJ, cInt=cInt, IE=IE, xNome=xNome, enderFerro=enderFerro)

        CNPJ: TCnpj = Element(TCnpj)
        cInt: str = Element(str)
        IE: TIe = Element(TIe)
        xNome: str = Element(str)
        enderFerro: TEnderFer = Element(TEnderFer)
    ferroEnv: List[ferroEnv] = Element(ferroEnv, max_occurs=-1)

    class detVag(ComplexType):
        """informações de detalhes dos Vagões"""
        _max_occurs = -1

        def add(self, nVag=None, cap=None, tpVag=None, pesoR=None, pesoBC=None) -> ferrov.detVag:
            return super().add(nVag=nVag, cap=cap, tpVag=tpVag, pesoR=pesoR, pesoBC=pesoBC)

        nVag: str = Element(str)
        cap: TDec_0303 = Element(TDec_0303, tipo="N", tam=(3, 3))
        tpVag: str = Element(str)
        pesoR: TDec_0303 = Element(TDec_0303, tipo="N", tam=(3, 3))
        pesoBC: TDec_0303 = Element(TDec_0303, tipo="N", tam=(3, 3))
    detVag: List[detVag] = Element(detVag, max_occurs=-1)

ferrov: ferrov = Element(ferrov)
