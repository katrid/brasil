from __future__ import annotations
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
        """Dados do protocolo de status"""
        tpAmb: TAmb = Element(TAmb)
        verAplic: TVerAplic = Element(TVerAplic)
        chNFe: TChNFe = Element(TChNFe)
        dhRecbto: dateTime = Element(dateTime)
        nProt: TProt = Element(TProt)
        digVal: DigestValueType = Element(DigestValueType)
        cStat: TStat = Element(TStat)
        xMotivo: TMotivo = Element(TMotivo)
        Id: str = Attribute(ID)
    infProt: infProt = Element(infProt)
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerNFe)



class TVerCancNFe(TString):
    """Tipo Versão do leiaute de Cancelamento de NF-e - 2.00/1.07"""
    _restriction = Restriction(base=r"TString", pattern=r"[1-9]{1}\.[0-9]{2}", enumeration=[])
    pass



class TRetCancNFe(Element):
    """Tipo retorno Pedido de Cancelamento da Nota Fiscal Eletrônica"""

    class infCanc(ComplexType):
        """Dados do Resultado do Pedido de Cancelamento da Nota Fiscal Eletrônica"""
        tpAmb: TAmb = Element(TAmb)
        verAplic: TVerAplic = Element(TVerAplic)
        cStat: TStat = Element(TStat)
        xMotivo: TMotivo = Element(TMotivo)
        cUF: TCodUfIBGE = Element(TCodUfIBGE)
        chNFe: TChNFe = Element(TChNFe)
        dhRecbto: dateTime = Element(dateTime)
        nProt: TProt = Element(TProt)
        Id: str = Attribute(ID)
    infCanc: infCanc = Element(infCanc)
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerCancNFe)



class TRetVerEvento(TString):
    """Tipo Versão do Evento"""
    _restriction = Restriction(base=r"TString", pattern=r"[1-9]{1}\.[0-9]{2}", enumeration=[])
    pass



class TRetEvento(Element):
    """Tipo retorno do Evento"""

    class infEvento(ComplexType):
        _choice = [['CNPJDest', 'CPFDest']]
        tpAmb: TAmb = Element(TAmb)
        verAplic: TVerAplic = Element(TVerAplic)
        cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE)
        cStat: TStat = Element(TStat)
        xMotivo: TMotivo = Element(TMotivo)
        chNFe: TChNFe = Element(TChNFe)
        tpEvento: str = Element(str)
        xEvento: str = Element(str)
        nSeqEvento: str = Element(str)
        CNPJDest: TCnpjOpc = Element(TCnpjOpc)
        CPFDest: TCpf = Element(TCpf)
        emailDest: str = Element(str)
        dhRegEvento: TDateTimeUTC = Element(TDateTimeUTC)
        nProt: TProt = Element(TProt)
        Id: str = Attribute(None)
    infEvento: infEvento = Element(infEvento)
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TRetVerEvento)



class TVerEvento(TString):
    """Tipo Versão do Evento 1.00"""
    _restriction = Restriction(base=r"TString", pattern=r"[1-9]{1}\.[0-9]{2}", enumeration=[])
    pass



class TEvento(Element):
    """Tipo Evento"""

    class infEvento(ComplexType):
        _choice = [['CNPJ', 'CPF']]
        cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE)
        tpAmb: TAmb = Element(TAmb)
        CNPJ: TCnpjOpc = Element(TCnpjOpc)
        CPF: TCpf = Element(TCpf)
        chNFe: TChNFe = Element(TChNFe)
        dhEvento: TDateTimeUTC = Element(TDateTimeUTC)
        tpEvento: str = Element(str)
        nSeqEvento: str = Element(str)
        verEvento: str = Element(str)

        class detEvento(ComplexType):
            """Detalhe Específico do Evento"""
            pass
        detEvento: detEvento = Element(detEvento)
        Id: str = Attribute(None)
    infEvento: infEvento = Element(infEvento)
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
    protNFe: TProtNFe = Element(TProtNFe)
    retCancNFe: TRetCancNFe = Element(TRetCancNFe)
    procEventoNFe: List[TProcEvento] = Element(TProcEvento, max_occurs=-1)
    versao: str = Attribute(TVerConsSitNFe)


