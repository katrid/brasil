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
    """Tipo Código de orgão (UF da tabela do IBGE + 91 RFB)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53', '91'])
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
        cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE, documentation=['Código do órgão de recepção do Evento. Utilizar a Tabela do IBGE extendida, utilizar 91 para identificar o Ambiente Nacional'])
        tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
        CNPJ: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['CNPJ'])
        CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CPF'])
        chNFe: TChNFe = Element(TChNFe, documentation=['Chave de Acesso da NF-e vinculada ao evento'])
        dhEvento: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e Hora do Evento, formato UTC (AAAA-MM-DDThh:mm:ssTZD, onde TZD = +hh:mm ou -hh:mm)'])
        tpEvento: str = Element(str, documentation=['Tipo do Evento'])
        nSeqEvento: str = Element(str, documentation=['Seqüencial do evento para o mesmo tipo de evento.'])
        verEvento: str = Element(str, documentation=['Versão do Tipo do Evento'])

        class detEvento(ComplexType):
            """Schema XML de validação do evento de emissão prévia em contingência - 110140"""
            descEvento: descEvento = Element(descEvento)
            cOrgaoAutor: cOrgaoAutor = Element(cOrgaoAutor)
            tpAutor: tpAutor = Element(tpAutor)
            verAplic: verAplic = Element(verAplic)
            dhEmi: dhEmi = Element(dhEmi)
            tpNF: tpNF = Element(tpNF)
            IE: IE = Element(IE)

            class dest(ComplexType):
                _choice = [['CNPJ', 'CPF', 'idEstrangeiro']]
                UF: UF = Element(UF)
                CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit)
                CPF: TCpf = Element(TCpf, filter=str.isdigit)
                idEstrangeiro: str = Element(str, documentation=['Identificador do destinatário, em caso de comprador estrangeiro'])
                IE: IE = Element(IE)
                vNF: vNF = Element(vNF)
                vICMS: vICMS = Element(vICMS)
                vST: vST = Element(vST)
            dest: dest = Element(dest)
            versao: str = Attribute(None)
        detEvento: detEvento = Element(detEvento, documentation=['Schema XML de validação do evento de emissão prévia em contingência - 110140'])
        Id: str = Attribute(None)
    infEvento: infEvento = Element(infEvento)
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerEvento)



class TRetEvento(Element):
    """Tipo retorno do Evento"""

    class infEvento(ComplexType):
        tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
        verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que recebeu o Evento'])
        cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE, documentation=['Código do órgão de recepção do Evento. Utilizar a Tabela do IBGE extendida, utilizar 91 para identificar o Ambiente Nacional'])
        cStat: TStat = Element(TStat, documentation=['Código do status da registro do Evento'])
        xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do registro do Evento'])
        chNFe: TChNFe = Element(TChNFe, documentation=['Chave de Acesso NF-e vinculada'])
        tpEvento: str = Element(str, documentation=['Tipo do Evento vinculado'])
        xEvento: str = Element(str, documentation=['Descrição do Evento'])
        nSeqEvento: str = Element(str, documentation=['Seqüencial do evento'])
        cOrgaoAutor: cOrgaoAutor = Element(cOrgaoAutor)
        dhRegEvento: str = Element(str, documentation=['Data e Hora de do recebimento do evento ou do registro do evento formato UTC AAAA-MM-DDThh:mm:ssTZD.'])
        nProt: TProt = Element(TProt, documentation=['Número do protocolo de registro do evento'])
        chNFePend: List[TChNFe] = Element(TChNFe, max_occurs=50, documentation=['Relação de Chaves de Acesso de EPEC não conciliados (pendentes de conciliação) existentes no AN.'])
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
    retEvento: List[TRetEvento] = Element(TRetEvento, max_occurs=20)
    versao: str = Attribute(TVerEnvEvento)



class TProcEvento(Element):
    """Tipo procEvento"""
    evento: TEvento = Element(TEvento)
    retEvento: TRetEvento = Element(TRetEvento)
    versao: str = Attribute(TVerEvento)


class descEvento(str):
    pass

class tpAutor(str):
    pass

class verAplic(TVerAplic):
    pass

class dhEmi(TDateTimeUTC):
    pass

class tpNF(str):
    pass

class cOrgaoAutor(TCodUfIBGE):
    pass

class IE(str):
    pass

class UF(TUf):
    pass

class vNF(TDec_1302):
    pass

class vICMS(TDec_1302):
    pass

class vST(TDec_1302):
    pass

