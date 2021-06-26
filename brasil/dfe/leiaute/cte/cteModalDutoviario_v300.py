from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v300 import *

from .cteTiposBasico_v300 import *



class duto(ComplexType):
    """Informações do modal Dutoviário"""
    vTar: TDec_0906Opc = Element(TDec_0906Opc, tipo="N", tam=(9, 6), documentation=['Valor da tarifa'])
    dIni: TData = Element(TData, documentation=['Data de Início da prestação do serviço'])
    dFim: TData = Element(TData, documentation=['Data de Fim da prestação do serviço'])

duto: duto = Element(duto, documentation=['Informações do modal Dutoviário'])
