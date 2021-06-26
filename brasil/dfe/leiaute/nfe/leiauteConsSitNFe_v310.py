from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v310 import *

from .xmldsig_core_schema_v101 import *



class TVerConsSitNFe(str):
    """Tipo Versão do Leiaute da Cosulta situação NF-e - 3.10"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['3.10'])
    pass



class TConsSitNFe(Element):
    """Tipo Pedido de Consulta da Situação Atual da Nota Fiscal Eletrônica"""
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    xServ: str = Element(str, documentation=['Serviço Solicitado'])
    chNFe: TChNFe = Element(TChNFe, documentation=['Chaves de acesso da NF-e, compostas por: UF do emitente, AAMM da emissão da NFe, CNPJ do emitente, modelo, série e número da NF-e e código numérico + DV.'])
    versao: str = Attribute(TVerConsSitNFe)



class TVerNFe(TString):
    """Tipo Versão da NF-e"""
    _restriction = Restriction(base=r"TString", pattern=r"[1-9]{1}\.[0-9]{2}", enumeration=[])
    pass



class TProtNFe(Element):
    """Tipo Protocolo de status resultado do processamento da NF-e"""

    class infProt(ComplexType):
        """Dados do protocolo de status"""
        tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
        verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que processou a NF-e'])
        chNFe: TChNFe = Element(TChNFe, documentation=['Chaves de acesso da NF-e, compostas por: UF do emitente, AAMM da emissão da NFe, CNPJ do emitente, modelo, série e número da NF-e e código numérico+DV.'])
        dhRecbto: dateTime = Element(dateTime, documentation=['Data e hora de processamento, no formato AAAA-MM-DDTHH:MM:SS (ou AAAA-MM-DDTHH:MM:SSTZD, de acordo com versão). Deve ser preenchida com data e hora da gravação no Banco em caso de Confirmação. Em caso de Rejeição, com data e hora do recebimento do Lote de NF-e enviado.'])
        nProt: TProt = Element(TProt, documentation=['Número do Protocolo de Status da NF-e. 1 posição (1 – Secretaria de Fazenda Estadual 2 – Receita Federal); 2 - códiga da UF - 2 posições ano; 10 seqüencial no ano.'])
        digVal: DigestValueType = Element(DigestValueType, documentation=['Digest Value da NF-e processada. Utilizado para conferir a integridade da NF-e original.'])
        cStat: TStat = Element(TStat, documentation=['Código do status da mensagem enviada.'])
        xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do serviço solicitado.'])
        Id: str = Attribute(ID)
    infProt: infProt = Element(infProt, documentation=['Dados do protocolo de status'])
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
        tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
        verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que processou o pedido de cancelamento'])
        cStat: TStat = Element(TStat, documentation=['Código do status da mensagem enviada.'])
        xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do serviço solicitado.'])
        cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['código da UF de atendimento'])
        chNFe: TChNFe = Element(TChNFe, documentation=['Chaves de acesso da NF-e, compostas por: UF do emitente, AAMM da emissão da NFe, CNPJ do emitente, modelo, série e número da NF-e e código numérico + DV.'])
        dhRecbto: dateTime = Element(dateTime, documentation=['Data e hora de recebimento, no formato AAAA-MM-DDTHH:MM:SS. Deve ser preenchida com data e hora da gravação no Banco em caso de Confirmação.'])
        nProt: TProt = Element(TProt, documentation=['Número do Protocolo de Status da NF-e. 1 posição (1 – Secretaria de Fazenda Estadual 2 – Receita Federal); 2 - código da UF - 2 posições ano; 10 seqüencial no ano.'])
        Id: str = Attribute(ID)
    infCanc: infCanc = Element(infCanc, documentation=['Dados do Resultado do Pedido de Cancelamento da Nota Fiscal Eletrônica'])
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
        dhRegEvento: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e Hora de registro do evento formato UTC AAAA-MM-DDTHH:MM:SSTZD'])
        nProt: TProt = Element(TProt, documentation=['Número do protocolo de registro do evento'])
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
        dhEvento: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e Hora do Evento, formato UTC (AAAA-MM-DDThh:mm:ssTZD, onde TZD = +hh:mm ou -hh:mm)'])
        tpEvento: str = Element(str, documentation=['Tipo do Evento'])
        nSeqEvento: str = Element(str, documentation=['Seqüencial do evento para o mesmo tipo de evento.  Para maioria dos eventos será 1, nos casos em que possa existir mais de um evento, como é o caso da carta de correção, o autor do evento deve numerar de forma seqüencial.'])
        verEvento: str = Element(str, documentation=['Versão do Tipo do Evento'])

        class detEvento(ComplexType):
            """Detalhe Específico do Evento"""
            pass
        detEvento: detEvento = Element(detEvento, documentation=['Detalhe Específico do Evento'])
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
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que processou a NF-e'])
    cStat: TStat = Element(TStat, documentation=['Código do status da mensagem enviada.'])
    xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do serviço solicitado.'])
    cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['código da UF de atendimento'])
    dhRecbto: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['AAAA-MM-DDTHH:MM:SSTZD'])
    chNFe: TChNFe = Element(TChNFe, documentation=['Chaves de acesso da NF-e consultada'])
    protNFe: TProtNFe = Element(TProtNFe, documentation=['Protocolo de autorização de uso da NF-e'])
    retCancNFe: TRetCancNFe = Element(TRetCancNFe, documentation=['Protocolo de homologação de cancelamento de uso da NF-e'])
    procEventoNFe: List[TProcEvento] = Element(TProcEvento, max_occurs=-1, documentation=['Protocolo de registro de evento da NF-e'])
    versao: str = Attribute(TVerConsSitNFe)


