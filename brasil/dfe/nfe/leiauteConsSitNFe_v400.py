from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v400 import *

from .xmldsig_core_schema_v101 import *


class TVerConsSitNFe(str):
    """Tipo Versão do Leiaute da Cosulta situação NF-e - 4.00"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['4.00'])
    pass


class TConsSitNFe(Element):
    """Tipo Pedido de Consulta da Situação Atual da Nota Fiscal Eletrônica"""
    tpAmb: TAmb = Element(TAmb)
    xServ: str = Element(str)
    chNFe: TChNFe = Element(TChNFe)
    versao: str = Attribute(TVerConsSitNFe)


class TVerNFe(TString):
    """Tipo Versão da NF-e"""
    _restriction = Restriction(base=r"TString", pattern=r"[1-9]{1}\.[0-9]{2}", enumeration=[])
    pass


class TProtNFe(Element):
    """Tipo Protocolo de status resultado do processamento da NF-e"""
    class infProt(ComplexType):
        tpAmb: TAmb = Element(TAmb)
        verAplic: TVerAplic = Element(TVerAplic)
        chNFe: TChNFe = Element(TChNFe)
        dhRecbto: dateTime = Element(dateTime)
        nProt: TProt = Element(TProt, min_occurs=0)
        digVal: DigestValueType = Element(DigestValueType, min_occurs=0)
        cStat: TStat = Element(TStat)
        xMotivo: TMotivo = Element(TMotivo)
        Id: str = Attribute(ID)
    infProt: infProt
    Signature: Signature = Element(Signature, min_occurs=0)
    versao: str = Attribute(TVerNFe)


class TVerCancNFe(TString):
    """Tipo Versão do leiaute de Cancelamento de NF-e - 2.00/1.07"""
    _restriction = Restriction(base=r"TString", pattern=r"[1-9]{1}\.[0-9]{2}", enumeration=[])
    pass


class TRetCancNFe(Element):
    """Tipo retorno Pedido de Cancelamento da Nota Fiscal Eletrônica"""
    class infCanc(ComplexType):
        tpAmb: TAmb = Element(TAmb)
        verAplic: TVerAplic = Element(TVerAplic)
        cStat: TStat = Element(TStat)
        xMotivo: TMotivo = Element(TMotivo)
        cUF: TCodUfIBGE = Element(TCodUfIBGE)
        chNFe: TChNFe = Element(TChNFe, min_occurs=0)
        dhRecbto: dateTime = Element(dateTime, min_occurs=0)
        nProt: TProt = Element(TProt, min_occurs=0)
        Id: str = Attribute(ID)
    infCanc: infCanc
    Signature: Signature = Element(Signature, min_occurs=0)
    versao: str = Attribute(TVerCancNFe)


class TRetVerEvento(TString):
    """Tipo Versão do Evento"""
    _restriction = Restriction(base=r"TString", pattern=r"[1-9]{1}\.[0-9]{2}", enumeration=[])
    pass


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
        dhRegEvento: TDateTimeUTC = Element(TDateTimeUTC)
        nProt: TProt = Element(TProt, min_occurs=0)
        Id: str = Attribute(None)
    infEvento: infEvento
    Signature: Signature = Element(Signature, min_occurs=0)
    versao: str = Attribute(TRetVerEvento)


class TVerEvento(TString):
    """Tipo Versão do Evento 1.00"""
    _restriction = Restriction(base=r"TString", pattern=r"[1-9]{1}\.[0-9]{2}", enumeration=[])
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
            pass
        detEvento: detEvento
        Id: str = Attribute(None)
    infEvento: infEvento
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerEvento)


class TProcEvento(Element):
    """Tipo procEvento"""
    evento: TEvento = Element(TEvento)
    retEvento: TRetEvento = Element(TRetEvento)
    versao: str = Attribute(TVerEvento)


class TRetConsSitNFe(Element):
    """Tipo Retorno de Pedido de Consulta da Situação Atual da Nota Fiscal Eletrônica"""
    tpAmb: TAmb = Element(TAmb)
    verAplic: TVerAplic = Element(TVerAplic)
    cStat: TStat = Element(TStat)
    xMotivo: TMotivo = Element(TMotivo)
    cUF: TCodUfIBGE = Element(TCodUfIBGE)
    dhRecbto: TDateTimeUTC = Element(TDateTimeUTC)
    chNFe: TChNFe = Element(TChNFe)
    protNFe: TProtNFe = Element(TProtNFe, min_occurs=0)
    retCancNFe: TRetCancNFe = Element(TRetCancNFe, min_occurs=0)
    procEventoNFe: List[TProcEvento] = Element(TProcEvento, min_occurs=0, max_occurs=-1)
    versao: str = Attribute(TVerConsSitNFe)


