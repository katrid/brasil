from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposDistDFe_v101 import *



class TVerResEvento(str):
    """Tipo Versão do leiate resNFe"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1.01'])
    pass



class resEvento(ComplexType):
    """Schema da estrutura XML gerada pelo Ambiente Nacional com o conjunto de informações resumidas de um evento de NF-e"""
    _choice = [['CNPJ', 'CPF']]
    cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE)
    CNPJ: TCnpj = Element(TCnpj)
    CPF: TCpf = Element(TCpf)
    chNFe: TChNFe = Element(TChNFe)
    dhEvento: TDateTimeUTC = Element(TDateTimeUTC)
    tpEvento: str = Element(str)
    nSeqEvento: str = Element(str)
    xEvento: str = Element(str)
    dhRecbto: TDateTimeUTC = Element(TDateTimeUTC)
    nProt: TProt = Element(TProt)
    versao: str = Attribute(TVerResEvento)

resEvento: resEvento = Element(resEvento)
