from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposGeralCTe_v200 import *



class TInutCTe(Element):
    """Tipo Pedido de Inutilização de Numeração do Conhecimento de Transporte eletrônico"""

    class infInut(ComplexType):
        """Dados do Pedido de Inutilização de Numeração do Conhecimento de Transporte eletrônico"""
        tpAmb: TAmb = Element(TAmb)
        xServ: TServ = Element(TServ)
        cUF: TCodUfIBGE = Element(TCodUfIBGE)
        ano: str = Element(str)
        CNPJ: TCnpj = Element(TCnpj)
        mod: TModCT = Element(TModCT)
        serie: TSerie = Element(TSerie)
        nCTIni: TNF = Element(TNF)
        nCTFin: TNF = Element(TNF)
        xJust: TJust = Element(TJust)
        Id: str = Attribute(None)
    infInut: infInut = Element(infInut)
    Signature: Signature = Element(Signature)
    versao: str = Attribute(None)



class TVerInutCTe(str):
    """Tipo Versão Inutilização de numeração de CT-e - 1.04"""
    _restriction = Restriction(base=r"xs:string", pattern=r"2\.00", enumeration=[])
    pass



class TRetInutCTe(Element):
    """Tipo retorno do Pedido de Inutilização de Numeração do Conhecimento de Transporte eletrônico"""

    class infInut(ComplexType):
        """Dados do Retorno do Pedido de Inutilização de Numeração do Conhecimento de Transporte eletrônico"""
        tpAmb: TAmb = Element(TAmb)
        verAplic: TVerAplic = Element(TVerAplic)
        cStat: TStat = Element(TStat)
        xMotivo: str = Element(str)
        cUF: TCodUfIBGE = Element(TCodUfIBGE)
        ano: str = Element(str)
        CNPJ: TCnpj = Element(TCnpj)
        mod: TModCT = Element(TModCT)
        serie: TSerie = Element(TSerie)
        nCTIni: TNF = Element(TNF)
        nCTFin: TNF = Element(TNF)
        dhRecbto: dateTime = Element(dateTime)
        nProt: TProt = Element(TProt)
        Id: str = Attribute(ID)
    infInut: infInut = Element(infInut)
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerInutCTe)



class TProcInutCTe(Element):
    """Tipo Pedido de inutilzação de númeração de CT-e processado"""
    inutCTe: TInutCTe = Element(TInutCTe)
    retInutCTe: TRetInutCTe = Element(TRetInutCTe)
    versao: str = Attribute(TVerInutCTe)


