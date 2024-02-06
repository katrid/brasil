from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralMDFe_v300 import *



class ferrov(ComplexType):
    """Informações do modal Ferroviário"""

    class trem(ComplexType):
        """Informações da composição do trem"""
        xPref: str = Element(str, documentation=['Prefixo do Trem'])
        dhTrem: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e hora de liberação do trem na origem'])
        xOri: str = Element(str, documentation=['Origem do Trem', 'Sigla da estação de origem'])
        xDest: str = Element(str, documentation=['Destino do Trem', 'Sigla da estação de destino'])
        qVag: str = Element(str, documentation=['Quantidade de vagões carregados'])
    trem: trem = Element(trem, documentation=['Informações da composição do trem'])

    class vag(ComplexType):
        """informações dos Vagões"""
        _max_occurs = -1

        def add(self, pesoBC=None, pesoR=None, tpVag=None, serie=None, nVag=None, nSeq=None, TU=None) -> ferrov.vag:
            return super().add(pesoBC=pesoBC, pesoR=pesoR, tpVag=tpVag, serie=serie, nVag=nVag, nSeq=nSeq, TU=TU)

        pesoBC: TDec_0303 = Element(TDec_0303, tipo="N", tam=(3, 3), base_type=Decimal, documentation=['Peso Base de Cálculo de Frete em Toneladas'])
        pesoR: TDec_0303 = Element(TDec_0303, tipo="N", tam=(3, 3), base_type=Decimal, documentation=['Peso Real em Toneladas'])
        tpVag: str = Element(str, documentation=['Tipo de Vagão'])
        serie: str = Element(str, documentation=['Serie de Identificação do vagão'])
        nVag: str = Element(str, documentation=['Número de Identificação do vagão'])
        nSeq: str = Element(str, documentation=['Sequencia do vagão na composição'])
        TU: str = Element(str, documentation=['Tonelada Útil', 'Unidade de peso referente à carga útil (apenas o peso da carga transportada), expressa em toneladas.'])
    vag: List[vag] = Element(vag, max_occurs=-1, documentation=['informações dos Vagões'])

ferrov: ferrov = Element(ferrov, documentation=['Informações do modal Ferroviário'])
