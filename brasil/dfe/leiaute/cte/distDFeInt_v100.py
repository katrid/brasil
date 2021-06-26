from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposDistDFe_v100 import *



class distDFeInt(ComplexType):
    """Schema de pedido de distribuição de DF-e de interesse"""
    _choice = [['CNPJ', 'CPF'], ['distNSU', 'consNSU']]
    tpAmb: TAmb = Element(TAmb)
    cUFAutor: TCodUfIBGE = Element(TCodUfIBGE)
    CNPJ: TCnpj = Element(TCnpj)
    CPF: TCpf = Element(TCpf)

    class distNSU(ComplexType):
        """Grupo para distribuir DF-e de interesse"""
        ultNSU: TNSU = Element(TNSU)
    distNSU: distNSU = Element(distNSU)

    class consNSU(ComplexType):
        """Grupo para consultar um DF-e a partir de um NSU específico"""
        NSU: TNSU = Element(TNSU)
    consNSU: consNSU = Element(consNSU)
    versao: str = Attribute(TVerDistDFe)

distDFeInt: distDFeInt = Element(distDFeInt)
