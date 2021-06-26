from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposDistDFe_v101 import *



class TVerResNFe(str):
    """Tipo Versão do leiate resNFe"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1.01'])
    pass



class resNFe(ComplexType):
    """Schema da estrutura XML gerada pelo Ambiente Nacional com o conjunto de informações resumidas de uma NF-e"""
    _choice = [['CNPJ', 'CPF']]
    chNFe: TChNFe = Element(TChNFe, documentation=['Chave de acesso da NF-e'])
    CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do Emitente'])
    CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CPF do Emitente'])
    xNome: str = Element(str, documentation=['Razão Social ou Nome do emitente'])
    IE: TIe = Element(TIe, filter=str.isdigit, documentation=['Inscrição Estadual do Emitente'])
    dhEmi: TDateTimeUTC = Element(TDateTimeUTC, documentation=['Data e Hora de emissão do Documento Fiscal (AAAA-MM-DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00'])
    tpNF: str = Element(str, documentation=['Tipo do Documento Fiscal (0 - entrada; 1 - saída)'])
    vNF: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), documentation=['Valor Total da NF-e'])
    digVal: DigestValueType = Element(DigestValueType, documentation=['Digest Value da NF-e processada. Utilizado para conferir a integridade da NF-e original'])
    dhRecbto: TDateTimeUTC = Element(TDateTimeUTC, documentation=['Data e hora de autorização da NF-e, no formato AAAA-MM-DDTHH:MM:SSTZD'])
    nProt: TProt = Element(TProt, documentation=['Número do Protocolo de Status da NF-e. 1 posição (1 – Secretaria de Fazenda Estadual 2 – Receita Federal); 2 - códiga da UF - 2 posições ano; 10 seqüencial no ano'])
    cSitNFe: str = Element(str, documentation=['\n            Situação da NF-e\n            1-Uso autorizado no momento da consulta;\n            2-Uso denegado;\n            '])
    versao: str = Attribute(TVerResNFe)

resNFe: resNFe = Element(resNFe, documentation=['Schema da estrutura XML gerada pelo Ambiente Nacional com o conjunto de informações resumidas de uma NF-e'])
