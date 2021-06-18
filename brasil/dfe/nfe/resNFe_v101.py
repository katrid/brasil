from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposDistDFe_v101 import *


class TVerResNFe(str):
    """Tipo Versão do leiate resNFe"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1.01'])
    pass


class resNFe(ComplexType):
    chNFe: TChNFe = Element(TChNFe)
    xNome: str = Element(str)
    IE: TIe = Element(TIe)
    dhEmi: TDateTimeUTC = Element(TDateTimeUTC)
    tpNF: str = Element(str)
    vNF: TDec_1302 = Element(TDec_1302)
    digVal: DigestValueType = Element(DigestValueType, min_occurs=0)
    dhRecbto: TDateTimeUTC = Element(TDateTimeUTC)
    nProt: TProt = Element(TProt)
    cSitNFe: str = Element(str)
    versao: str = Attribute(TVerResNFe)

resNFe: resNFe
