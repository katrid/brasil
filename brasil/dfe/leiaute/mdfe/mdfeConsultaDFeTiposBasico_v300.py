from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralMDFe_v300 import *



class TVerMDFeConsultaDFe(str):
    """Tipo Versão do Consulta DFe de MDF-e - 3.00"""
    _restriction = Restriction(base=r"xs:string", pattern=r"3\.00", enumeration=[])
    pass



class TMDFeConsultaDFe(Element):
    """Tipo Pedido de Consulta do Manifesto Eletrônico de Documentos Fiscais"""
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    xServ: TServ = Element(TServ, documentation=['Serviço Solicitado'])
    chMDFe: TChNFe = Element(TChNFe, documentation=['Chaves de acesso do MDF-e, compostas por: UF do emitente, AAMM da emissão do MDF-e, CNPJ do emitente, modelo, série e número do MDF-e e código numérico + DV.'])
    versao: str = Attribute(TVerMDFeConsultaDFe)



class TMDFeDFe(Element):
    """Tipo Documento Fiscal Eletrônico MDF-e"""

    class procMDFe(ComplexType):
        versao: str = Attribute(TVerMDFeConsultaDFe)
    procMDFe: procMDFe = Element(procMDFe)

    class procEventoMDFe(ComplexType):
        _max_occurs = -1

        def add(self, versao=None) -> TMDFeDFe.procEventoMDFe:
            return super().add(versao=versao)

        versao: str = Attribute(TVerMDFeConsultaDFe)
    procEventoMDFe: List[procEventoMDFe] = Element(procEventoMDFe, max_occurs=-1)



class TRetMDFeConsultaDFe(Element):
    """Tipo Retorno de Pedido de Consulta do Manifesto Eletrônico de Documentos Fiscais"""
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que processou a consulta do MDF-e'])
    cStat: TStat = Element(TStat, documentation=['Código do status da consulta do MDF-e'])
    xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status da consulta do MDF-e'])
    MDFeDFe: TMDFeDFe = Element(TMDFeDFe)
    versao: str = Attribute(TVerMDFeConsultaDFe)


