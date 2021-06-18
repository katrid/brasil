from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v300 import *


class evEPECCTe(ComplexType):
    descEvento: str = Element(str)
    xJust: TJust = Element(TJust)
    vICMS: TDec_1302 = Element(TDec_1302)
    vTPrest: TDec_1302 = Element(TDec_1302)
    vCarga: TDec_1302 = Element(TDec_1302)
    class toma4(ComplexType):
        toma: str = Element(str)
        UF: TUf = Element(TUf)
        IE: TIeDest = Element(TIeDest, min_occurs=0)
    toma4: toma4
    modal: TModTransp = Element(TModTransp)
    UFIni: TUf = Element(TUf)
    UFFim: TUf = Element(TUf)
    tpCTe: str = Element(str)
    dhEmi: str = Element(str)

evEPECCTe: evEPECCTe
