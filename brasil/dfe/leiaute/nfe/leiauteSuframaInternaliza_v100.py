from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
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
        @property
        def CNPJCPF(self):
            return self.CPF or self.CNPJ

        @CNPJCPF.setter
        def CNPJCPF(self, value):
            value = "".join(filter(str.isdigit, value))
            if len(value) == 11:
                self.CPF = value
            else:
                self.CNPJ = value
        cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE, documentation=['Código do órgão de recepção do Evento. Utilizar a Tabela do IBGE extendida, utilizar 90 para identificar o Ambiente Nacional'])
        tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
        CNPJ: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['CNPJ'])
        CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CPF'])
        chNFe: TChNFe = Element(TChNFe, documentation=['Chave de Acesso da NF-e vinculada ao evento'])
        dhEvento: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data de emissão no formato UTC.  AAAA-MM-DDThh:mm:ssTZD'])
        tpEvento: str = Element(str, documentation=['Tipo do Evento'])
        nSeqEvento: str = Element(str, documentation=['Seqüencial do evento para o mesmo tipo de evento.  Para maioria dos eventos será 1, nos casos em que possa existir mais de um evento, como é o caso da carta de correção, o autor do evento deve numerar de forma seqüencial.'])
        verEvento: str = Element(str, documentation=['Versão do Tipo do Evento'])

        class detEvento(ComplexType):
            """Schema XML de validação do evento do Confirmação de Internalização da Mercadoria na SUFRAMA 990910"""
            descEvento: str = Element(str, documentation=['Descrição do Evento - “Confirmação de Internalização da Mercadoria na SUFRAMA”'])
            PINe: str = Element(str, documentation=['Número do PIN-e -  Protocolo de Internalização de Mercadoria Nacional eletronico'])
            dVistoria: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data de ocorrência da vistoria, formato UTC (AAAA-MM-DDThh:mm:ssTZD, onde TZD = +hh:mm ou -hh:mm)'])
            locVistoria: str = Element(str, documentation=['Localidade onde ocorreu a vistoria'])
            postoVistoria: str = Element(str, documentation=['Nome Posto do ponto onde ocorreu a vistoria'])
            xHistorico: str = Element(str, documentation=['Histórico da ocorrência, se existir.'])
            versao: str = Attribute(None)
        detEvento: detEvento = Element(detEvento, documentation=['Schema XML de validação do evento do Confirmação de Internalização da Mercadoria na SUFRAMA 990910'])
        Id: str = Attribute(None)
    infEvento: infEvento = Element(infEvento)
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerEvento)



class TretEvento(Element):
    """Tipo retorno do Evento"""

    class infEvento(ComplexType):
        _choice = [['CNPJDest', 'CPFDest']]
        tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
        verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que recebeu o Evento'])
        cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE, documentation=['Código do órgão de recepção do Evento. Utilizar a Tabela do IBGE extendida, utilizar 90 para identificar o Ambiente Nacional'])
        cStat: TStat = Element(TStat, documentation=['Código do status da registro do Evento'])
        xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do registro do Evento'])
        chNFe: TChNFe = Element(TChNFe, documentation=['Chave de Acesso NF-e vinculada'])
        tpEvento: str = Element(str, documentation=['Tipo do Evento vinculado'])
        xEvento: str = Element(str, documentation=['Descrição do Evento'])
        nSeqEvento: str = Element(str, documentation=['Seqüencial do evento'])
        CNPJDest: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['CNPJ Destinatário'])
        CPFDest: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CPF Destiantário'])
        emailDest: str = Element(str, documentation=['email do destinatário'])
        dhRegEvento: str = Element(str, documentation=['Data e Hora de do recebimento do evento ou do registro do evento formato UTC AAAA-MM-DDThh:mm:ssTZD.'])
        nProt: TProt = Element(TProt, documentation=['Número do protocolo de registro do evento'])
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
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que recebeu o Evento'])
    cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE, documentation=['Código do òrgao que registrou o Evento'])
    cStat: TStat = Element(TStat, documentation=['Código do status da registro do Evento'])
    xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do registro do Evento'])
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

