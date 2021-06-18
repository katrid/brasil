from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposBasico_v103 import *


class TVerEvento(str):
    """Tipo Versão do Evento"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"1\.00", enumeration=[])
    pass


class TCOrgaoIBGE(str):
    """Tipo Código de orgão (UF da tabela do IBGE + 90 RFB)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53', '90', '91'])
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
            PINe: str = Element(str)
            dVistoria: TDateTimeUTC = Element(TDateTimeUTC)
            locVistoria: str = Element(str)
            postoVistoria: str = Element(str)
            xHistorico: str = Element(str)
            versao: str = Attribute(None)
        detEvento: detEvento
        Id: str = Attribute(None)
    infEvento: infEvento
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerEvento)


class TretEvento(Element):
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
    retEvento: List[TretEvento] = Element(TretEvento, min_occurs=0, max_occurs=20)
    versao: str = Attribute(TVerEnvEvento)


class TProcEvento(Element):
    """Tipo procEvento"""
    evento: TEvento = Element(TEvento)
    retEvento: TretEvento = Element(TretEvento)
    versao: str = Attribute(TVerEvento)


class descEvento(str):
    pass

class cOrgaoAutor(TCOrgaoIBGE):
    pass

class cPostoUF(str):
    pass

class xPostoUF(str):
    pass

class latGPS(str):
    pass

class longGPS(str):
    pass

class CPFOper(TCpf):
    pass

class xNomeOper(str):
    pass

class indOffline(str):
    pass

class dhPas(TDateTimeUTC):
    pass

class sentidoVia(str):
    pass

class indRet(str):
    pass

class UFDest(TUf):
    pass

class xObs(str):
    pass

class chMDFe(str):
    pass

class chCTe(str):
    pass

class modalRodov(ComplexType):
    placaVeic: placaVeic = Element(placaVeic, min_occurs=0)
    UFVeic: UFVeic = Element(UFVeic, min_occurs=0)
    placaCarreta: placaCarreta = Element(placaCarreta, min_occurs=0)
    UFCarreta: UFCarreta = Element(UFCarreta, min_occurs=0)
    placaCarreta2: placaCarreta2 = Element(placaCarreta2, min_occurs=0)
    UFCarreta2: UFCarreta2 = Element(UFCarreta2, min_occurs=0)

modalRodov: modalRodov
class placaVeic(TPlaca):
    pass

class UFVeic(TUf):
    pass

class placaCarreta(TPlaca):
    pass

class UFCarreta(TUf):
    pass

class placaCarreta2(TPlaca):
    pass

class UFCarreta2(TUf):
    pass

class modalOutro(ComplexType):
    tpModal: tpModal = Element(tpModal)
    xIdent: xIdent = Element(xIdent, min_occurs=0)

modalOutro: modalOutro
class tpModal(str):
    pass

class xIdent(str):
    pass

class ctg(ComplexType):
    nFormSeg: nFormSeg = Element(nFormSeg, min_occurs=0)
    UFDest: UFDest = Element(UFDest)
    tpEmis: tpEmis = Element(tpEmis)
    vTotalNFe: vTotalNFe = Element(vTotalNFe)
    indICMS: indICMS = Element(indICMS)
    indICMSST: indICMSST = Element(indICMSST)
    diaEmi: diaEmi = Element(diaEmi)

ctg: ctg
class nFormSeg(str):
    pass

class tpEmis(str):
    pass

class CNPJDest(TCnpj):
    pass

class CPFDest(TCpf):
    pass

class vTotalNFe(TDec_1302):
    pass

class indICMS(str):
    pass

class indICMSST(str):
    pass

class diaEmi(str):
    pass

