from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposGeralCTe_v300 import *


class TVerEvento(str):
    """Tipo Versão do Evento"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"3\.00", enumeration=[])
    pass


class TEvento(Element):
    """Tipo Evento"""
    class infEvento(ComplexType):
        cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE)
        tpAmb: TAmb = Element(TAmb)
        CNPJ: TCnpj = Element(TCnpj)
        chCTe: TChNFe = Element(TChNFe)
        dhEvento: TDateTimeUTC = Element(TDateTimeUTC)
        tpEvento: str = Element(str)
        nSeqEvento: str = Element(str)
        class detEvento(ComplexType):
            versaoEvento: str = Attribute(None)
        detEvento: detEvento
        Id: str = Attribute(None)
    infEvento: infEvento
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerEvento)


class TRetEvento(Element):
    """Tipo retorno do Evento"""
    class infEvento(ComplexType):
        tpAmb: TAmb = Element(TAmb)
        verAplic: TVerAplic = Element(TVerAplic)
        cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE)
        cStat: TStat = Element(TStat)
        xMotivo: TMotivo = Element(TMotivo)
        chCTe: TChNFe = Element(TChNFe, min_occurs=0)
        tpEvento: str = Element(str, min_occurs=0)
        xEvento: str = Element(str, min_occurs=0)
        nSeqEvento: str = Element(str, min_occurs=0)
        dhRegEvento: TDateTimeUTC = Element(TDateTimeUTC, min_occurs=0)
        nProt: TProt = Element(TProt, min_occurs=0)
        Id: str = Attribute(None)
    infEvento: infEvento
    Signature: Signature = Element(Signature, min_occurs=0)
    versao: str = Attribute(None)


class TProcEvento(Element):
    """Tipo procEvento"""
    eventoCTe: TEvento = Element(TEvento)
    retEventoCTe: TRetEvento = Element(TRetEvento)
    versao: str = Attribute(TVerEvento)


class TModTransp(str):
    """Tipo Modal transporte"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['01', '02', '03', '04', '05', '06'])
    pass


class TNSU(str):
    """Tipo número sequencial único do AN"""
    _restriction = Restriction(base=r"xs:string", pattern=r"[0-9]{15}", enumeration=[])
    pass


