from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v400 import *

from .cteTiposBasico_v400 import *



class duto(ComplexType):
    """Informações do modal Dutoviário"""
    vTar: TDec_0906Opc = Element(TDec_0906Opc, tipo="N", tam=(9, 6), base_type=Decimal, optional=True, documentation=['Valor da tarifa'])
    dIni: TData = Element(TData, base_type=date, documentation=['Data de Início da prestação do serviço'])
    dFim: TData = Element(TData, base_type=date, documentation=['Data de Fim da prestação do serviço'])

duto: duto = Element(duto, documentation=['Informações do modal Dutoviário'])
