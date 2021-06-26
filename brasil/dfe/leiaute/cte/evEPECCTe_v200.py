from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v200 import *



class evEPECCTe(ComplexType):
    """Schema XML de validação do evento de emissão prévia de emissão em contingência 
110113"""
    descEvento: str = Element(str)
    xJust: TJust = Element(TJust)
    vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
    vTPrest: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
    vCarga: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))

    class toma04(ComplexType):
        """Indicador do \"papel\" do tomador do serviço no CT-e"""
        _choice = [['CNPJ', 'CPF']]
        toma: str = Element(str)
        UF: TUf = Element(TUf)
        CNPJ: TCnpjOpc = Element(TCnpjOpc)
        CPF: TCpf = Element(TCpf)
        IE: TIeDest = Element(TIeDest)
    toma04: toma04 = Element(toma04)
    modal: TModTransp = Element(TModTransp)
    UFIni: TUf = Element(TUf)
    UFFim: TUf = Element(TUf)

evEPECCTe: evEPECCTe = Element(evEPECCTe)
