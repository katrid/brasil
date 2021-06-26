from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *



class TNSU(str):
    """Tipo número sequencial único do AN"""
    _restriction = Restriction(base=r"xs:string", pattern=r"[0-9]{1,15}", enumeration=[])
    pass



class TVeConsNFeDest(str):
    """Tipo Versão da consultaNFeDest"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1.01'])
    pass



class TConsNFeDest(Element):
    """Tipo Pedido de Consulta de Nota Fiscal Eletrônica"""
    tpAmb: TAmb = Element(TAmb)
    xServ: str = Element(str)
    CNPJ: TCnpj = Element(TCnpj)
    indNFe: str = Element(str)
    indEmi: str = Element(str)
    ultNSU: str = Element(str)
    versao: str = Attribute(TVeConsNFeDest)



class TRetConsNFeDest(Element):
    """Tipo Retorno do pedido de Consulta de Nota Fiscal Eletrônica"""
    tpAmb: TAmb = Element(TAmb)
    verAplic: TVerAplic = Element(TVerAplic)
    cStat: TStat = Element(TStat)
    xMotivo: TMotivo = Element(TMotivo)
    dhResp: dateTime = Element(dateTime)
    indCont: str = Element(str)
    ultNSU: str = Element(str)

    class ret(ComplexType):
        """Resumo de NF-e ou CC-e"""
        _max_occurs = 50
        _choice = [['resNFe', 'resCanc', 'resCCe']]

        def add(self, resNFe=None, resCanc=None, resCCe=None) -> TRetConsNFeDest.ret:
            return super().add(resNFe=resNFe, resCanc=resCanc, resCCe=resCCe)


        class resNFe(ComplexType):
            """Informações resumo da NF-e localizadas"""
            _choice = [['CNPJ', 'CPF']]
            chNFe: TChNFe = Element(TChNFe)
            CNPJ: TCnpj = Element(TCnpj)
            CPF: TCpf = Element(TCpf)
            xNome: str = Element(str)
            IE: TIe = Element(TIe)
            dEmi: TData = Element(TData)
            tpNF: str = Element(str)
            vNF: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
            digVal: str = Element(str)
            dhRecbto: dateTime = Element(dateTime)
            cSitNFe: str = Element(str)
            cSitConf: str = Element(str)
            NSU: str = Attribute(TNSU)
        resNFe: resNFe = Element(resNFe)

        class resCanc(ComplexType):
            """Informações resumo da NF-e canceladas localizadas"""
            _choice = [['CNPJ', 'CPF']]
            chNFe: TChNFe = Element(TChNFe)
            CNPJ: TCnpj = Element(TCnpj)
            CPF: TCpf = Element(TCpf)
            xNome: str = Element(str)
            IE: TIe = Element(TIe)
            dEmi: TData = Element(TData)
            tpNF: str = Element(str)
            vNF: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
            digVal: str = Element(str)
            dhRecbto: dateTime = Element(dateTime)
            cSitNFe: str = Element(str)
            cSitConf: str = Element(str)
            NSU: str = Attribute(TNSU)
        resCanc: resCanc = Element(resCanc)

        class resCCe(ComplexType):
            """Informações da carta de correção da NF-e localizadas"""
            chNFe: TChNFe = Element(TChNFe)
            dhEvento: str = Element(str)
            tpEvento: str = Element(str)
            nSeqEvento: str = Element(str)
            descEvento: str = Element(str)
            xCorrecao: str = Element(str)
            tpNF: str = Element(str)
            dhRecbto: dateTime = Element(dateTime)
            NSU: str = Attribute(TNSU)
        resCCe: resCCe = Element(resCCe)
    ret: List[ret] = Element(ret, max_occurs=50)
    versao: str = Attribute(TVeConsNFeDest)


