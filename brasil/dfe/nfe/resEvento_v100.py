from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposDistDFe_v100 import *


class TVerResEvento(str):
    """Tipo Versão do leiate resNFe"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1.00'])
    pass


class resEvento(ComplexType):
    cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE)
    chNFe: TChNFe = Element(TChNFe)
    dhEvento: TDateTimeUTC = Element(TDateTimeUTC)
    tpEvento: str = Element(str)
    nSeqEvento: str = Element(str)
    xEvento: str = Element(str)
    dhRecbto: TDateTimeUTC = Element(TDateTimeUTC)
    nProt: TProt = Element(TProt)
    versao: str = Attribute(TVerResEvento)

resEvento: resEvento
