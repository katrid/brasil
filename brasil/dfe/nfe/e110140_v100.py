from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *


class detEvento(ComplexType):
    descEvento: descEvento = Element(descEvento)
    cOrgaoAutor: cOrgaoAutor = Element(cOrgaoAutor)
    tpAutor: tpAutor = Element(tpAutor)
    verAplic: verAplic = Element(verAplic)
    dhEmi: dhEmi = Element(dhEmi)
    tpNF: tpNF = Element(tpNF)
    IE: IE = Element(IE)
    class dest(ComplexType):
        UF: UF = Element(UF)
        IE: IE = Element(IE, min_occurs=0)
        vNF: vNF = Element(vNF)
        vICMS: vICMS = Element(vICMS)
        vST: vST = Element(vST)
    dest: dest
    versao: str = Attribute(None)

detEvento: detEvento
class descEvento(str):
    pass

class tpAutor(str):
    pass

class verAplic(TVerAplic):
    pass

class dhEmi(TDateTimeUTC):
    pass

class tpNF(str):
    pass

class cOrgaoAutor(TCodUfIBGE):
    pass

class IE(str):
    pass

class UF(TUf):
    pass

class vNF(TDec_1302):
    pass

class vICMS(TDec_1302):
    pass

class vST(TDec_1302):
    pass

