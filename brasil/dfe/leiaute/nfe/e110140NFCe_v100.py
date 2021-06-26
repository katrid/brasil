from __future__ import annotations
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
        _choice = [['CNPJ', 'CPF', 'idEstrangeiro']]
        UF: UF = Element(UF)
        CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit)
        CPF: TCpf = Element(TCpf, filter=str.isdigit)
        idEstrangeiro: str = Element(str, documentation=['Identificador do destinatário, em caso de comprador estrangeiro'])
        IE: IE = Element(IE)
    dest: dest = Element(dest)
    vNF: vNF = Element(vNF)
    vICMS: vICMS = Element(vICMS)
    versao: str = Attribute(None)

detEvento: detEvento = Element(detEvento)
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

