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
    chNFe: TChNFe = Element(TChNFe)
    CNPJ: TCnpj = Element(TCnpj)
    CPF: TCpf = Element(TCpf)
    xNome: str = Element(str)
    IE: TIe = Element(TIe)
    dhEmi: TDateTimeUTC = Element(TDateTimeUTC)
    tpNF: str = Element(str)
    vNF: TDec_1302 = Element(TDec_1302)
    digVal: DigestValueType = Element(DigestValueType)
    dhRecbto: TDateTimeUTC = Element(TDateTimeUTC)
    nProt: TProt = Element(TProt)
    cSitNFe: str = Element(str)
    versao: str = Attribute(TVerResNFe)

resNFe: resNFe = Element(resNFe)
