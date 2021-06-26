from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposBasico_v400 import *



class TVerInutNFe(token):
    """Tipo Versão do leiaute de Inutilização 4.00"""
    _restriction = Restriction(base=r"xs:token", pattern=r"4\.00", enumeration=[])
    pass



class TInutNFe(Element):
    """Tipo Pedido de Inutilização de Numeração da Nota Fiscal Eletrônica"""

    class infInut(ComplexType):
        """Dados do Pedido de Inutilização de Numeração da Nota Fiscal Eletrônica"""
        tpAmb: TAmb = Element(TAmb)
        xServ: str = Element(str)
        cUF: TCodUfIBGE = Element(TCodUfIBGE)
        ano: Tano = Element(Tano)
        CNPJ: TCnpj = Element(TCnpj)
        mod: TMod = Element(TMod)
        serie: TSerie = Element(TSerie)
        nNFIni: TNF = Element(TNF)
        nNFFin: TNF = Element(TNF)
        xJust: TJust = Element(TJust)
        Id: str = Attribute(None)
    infInut: infInut = Element(infInut)
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerInutNFe)



class TRetInutNFe(Element):
    """Tipo retorno do Pedido de Inutilização de Numeração da Nota Fiscal Eletrônica"""

    class infInut(ComplexType):
        """Dados do Retorno do Pedido de Inutilização de Numeração da Nota Fiscal Eletrônica"""
        tpAmb: TAmb = Element(TAmb)
        verAplic: TVerAplic = Element(TVerAplic)
        cStat: TStat = Element(TStat)
        xMotivo: TMotivo = Element(TMotivo)
        cUF: TCodUfIBGE = Element(TCodUfIBGE)
        ano: Tano = Element(Tano)
        CNPJ: TCnpj = Element(TCnpj)
        mod: TMod = Element(TMod)
        serie: TSerie = Element(TSerie)
        nNFIni: TNF = Element(TNF)
        nNFFin: TNF = Element(TNF)
        dhRecbto: TDateTimeUTC = Element(TDateTimeUTC)
        nProt: TProt = Element(TProt)
        Id: str = Attribute(ID)
    infInut: infInut = Element(infInut)
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerInutNFe)



class TProcInutNFe(Element):
    """Tipo Pedido de inutilzação de númeração de  NF-e processado"""
    inutNFe: TInutNFe = Element(TInutNFe)
    retInutNFe: TRetInutNFe = Element(TRetInutNFe)
    versao: str = Attribute(TVerInutNFe)


