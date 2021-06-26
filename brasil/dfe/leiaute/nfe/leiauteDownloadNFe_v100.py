from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *



class TVerDownloadNFe(str):
    """Tipo Versão da consultaNFeDest"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1.00'])
    pass



class TDownloadNFe(Element):
    """Tipo Pedido de Download de NF-e"""
    tpAmb: TAmb = Element(TAmb)
    xServ: str = Element(str)
    CNPJ: TCnpj = Element(TCnpj)
    chNFe: List[TChNFe] = Element(TChNFe, max_occurs=10)
    versao: str = Attribute(TVerDownloadNFe)



class TRetDownloadNFe(Element):
    """Tipo Retorno do pedido de Download de NF-e"""
    tpAmb: TAmb = Element(TAmb)
    verAplic: TVerAplic = Element(TVerAplic)
    cStat: TStat = Element(TStat)
    xMotivo: TMotivo = Element(TMotivo)
    dhResp: dateTime = Element(dateTime)

    class retNFe(ComplexType):
        """Conjunto de informação das  NF-e localizadas"""
        _max_occurs = 10
        _choice = [['procNFeGrupoZip', 'procNFeZip', 'procNFe']]

        def add(self, chNFe=None, cStat=None, xMotivo=None, procNFeGrupoZip=None, procNFeZip=None, procNFe=None) -> TRetDownloadNFe.retNFe:
            return super().add(chNFe=chNFe, cStat=cStat, xMotivo=xMotivo, procNFeGrupoZip=procNFeGrupoZip, procNFeZip=procNFeZip, procNFe=procNFe)

        chNFe: TChNFe = Element(TChNFe)
        cStat: TStat = Element(TStat)
        xMotivo: TMotivo = Element(TMotivo)

        class procNFeGrupoZip(ComplexType):
            NFeZip: base64Binary = Element(base64Binary)
            protNFeZip: base64Binary = Element(base64Binary)
        procNFeGrupoZip: procNFeGrupoZip = Element(procNFeGrupoZip)
        procNFeZip: base64Binary = Element(base64Binary)

        class procNFe(ComplexType):
            schema: str = Attribute(string)
        procNFe: procNFe = Element(procNFe)
    retNFe: List[retNFe] = Element(retNFe, max_occurs=10)
    versao: str = Attribute(TVerDownloadNFe)


