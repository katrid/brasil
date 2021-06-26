from __future__ import annotations
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
            """Schema XML de validação do evento doVistoria SUFRAMA 990900"""
            descEvento: str = Element(str)
            PINe: str = Element(str)
            dVistoria: str = Element(str)
            locVistoria: str = Element(str)
            postoVistoria: str = Element(str)
            xHistorico: str = Element(str)
            versao: str = Attribute(None)
        detEvento: detEvento = Element(detEvento)
        Id: str = Attribute(None)
    infEvento: infEvento = Element(infEvento)
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerEvento)



class TretEvento(Element):
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
        dhRegEvento: str = Element(str)
        nProt: TProt = Element(TProt)
        Id: str = Attribute(None)
    infEvento: infEvento = Element(infEvento)
    Signature: Signature = Element(Signature)
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
    retEvento: List[TretEvento] = Element(TretEvento, max_occurs=20)
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
    placaVeic: placaVeic = Element(placaVeic)
    UFVeic: UFVeic = Element(UFVeic)
    placaCarreta: placaCarreta = Element(placaCarreta)
    UFCarreta: UFCarreta = Element(UFCarreta)
    placaCarreta2: placaCarreta2 = Element(placaCarreta2)
    UFCarreta2: UFCarreta2 = Element(UFCarreta2)

modalRodov: modalRodov = Element(modalRodov)
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
    xIdent: xIdent = Element(xIdent)

modalOutro: modalOutro = Element(modalOutro)
class tpModal(str):
    pass

class xIdent(str):
    pass


class ctg(ComplexType):
    _choice = [[None, None]]
    nFormSeg: nFormSeg = Element(nFormSeg)
    UFDest: UFDest = Element(UFDest)
    tpEmis: tpEmis = Element(tpEmis)
    CNPJDest: CNPJDest = Element(CNPJDest)
    CPFDest: CPFDest = Element(CPFDest)
    vTotalNFe: vTotalNFe = Element(vTotalNFe)
    indICMS: indICMS = Element(indICMS)
    indICMSST: indICMSST = Element(indICMSST)
    diaEmi: diaEmi = Element(diaEmi)

ctg: ctg = Element(ctg)
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

