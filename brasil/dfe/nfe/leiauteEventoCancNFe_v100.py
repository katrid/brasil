from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposBasico_v103 import *


class TVerEvento(str):
    """Tipo Versão do Evento"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"1\.00", enumeration=[])
    pass


class TEvento(Element):
    """Tipo Evento"""
    class infEvento(ComplexType):
        cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE)
        tpAmb: TAmb = Element(TAmb)
        chNFe: TChNFe = Element(TChNFe)
        dhEvento: TDateTimeUTC = Element(TDateTimeUTC)
        tpEvento: str = Element(str)
        nSeqEvento: str = Element(str)
        verEvento: str = Element(str)
        class detEvento(ComplexType):
            descEvento: str = Element(str)
            nProt: TProt = Element(TProt)
            xJust: TJust = Element(TJust)
            versao: str = Attribute(None)
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
        chNFe: TChNFe = Element(TChNFe, min_occurs=0)
        tpEvento: str = Element(str, min_occurs=0)
        xEvento: str = Element(str, min_occurs=0)
        nSeqEvento: str = Element(str, min_occurs=0)
        emailDest: str = Element(str, min_occurs=0)
        dhRegEvento: str = Element(str)
        nProt: TProt = Element(TProt, min_occurs=0)
        Id: str = Attribute(None)
    infEvento: infEvento
    Signature: Signature = Element(Signature, min_occurs=0)
    versao: str = Attribute(TVerEvento)


class TVerEnvEvento(str):
    """Tipo Versão do EnvEvento"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"1\.00", enumeration=[])
    pass


class TEnvEvento(Element):
    """Tipo Lote de Envio"""
    idLote: str = Element(str)
    evento: List[TEvento] = Element(TEvento, max_occurs=20)
    versao: str = Attribute(TVerEnvEvento)


class TRetEnvEvento(Element):
    """Tipo Retorno de Lote de Envio"""
    idLote: str = Element(str)
    tpAmb: TAmb = Element(TAmb)
    verAplic: TVerAplic = Element(TVerAplic)
    cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE)
    cStat: TStat = Element(TStat)
    xMotivo: TMotivo = Element(TMotivo)
    retEvento: List[TRetEvento] = Element(TRetEvento, min_occurs=0, max_occurs=20)
    versao: str = Attribute(TVerEnvEvento)


class TProcEvento(Element):
    """Tipo procEvento"""
    evento: TEvento = Element(TEvento)
    retEvento: TRetEvento = Element(TRetEvento)
    versao: str = Attribute(TVerEvento)


