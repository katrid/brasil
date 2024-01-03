from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposGeralCTe_v400 import *



class TVerEvento(str):
    """Tipo Versão do Evento"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"4\.00", enumeration=[])
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
        cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE, documentation=['Código do órgão de recepção do Evento. Utilizar a Tabela do IBGE extendida, utilizar 90 para identificar SUFRAMA'])
        tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
        CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do emissor do evento'])
        CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CPF do emissor do evento', 'Informar zeros não significativos.\n\nUsar com série específica 920-969 para emitente pessoa física com inscrição estadual'])
        chCTe: TChDFe = Element(TChDFe, documentation=['Chave de Acesso do CT-e vinculado ao evento'])
        dhEvento: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e Hora do Evento, formato UTC (AAAA-MM-DDThh:mm:ssTZD)'])
        tpEvento: str = Element(str, documentation=['Tipo do Evento'])
        nSeqEvento: str = Element(str, documentation=['Seqüencial do evento para o mesmo tipo de evento.  Para maioria dos eventos será 1, nos casos em que possa existir mais de um evento o autor do evento deve numerar de forma seqüencial.'])

        class detEvento(ComplexType):
            """Detalhamento do evento específico"""
            versaoEvento: str = Attribute(None)
        detEvento: detEvento = Element(detEvento, documentation=['Detalhamento do evento específico'])

        class infSolicNFF(ComplexType):
            """Grupo de informações do pedido de registro de evento da Nota Fiscal Fácil"""
            xSolic: str = Element(str, documentation=['Solicitação do pedido de registro de evento da NFF.', 'Será preenchido com a totalidade de campos informados no aplicativo emissor serializado.'])
        infSolicNFF: infSolicNFF = Element(infSolicNFF, documentation=['Grupo de informações do pedido de registro de evento da Nota Fiscal Fácil'])

        class infPAA(ComplexType):
            """Grupo de Informação do Provedor de Assinatura e Autorização"""
            CNPJPAA: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do Provedor de Assinatura e Autorização'])

            class PAASignature(ComplexType):
                """Assinatura RSA do Emitente para DFe gerados por PAA"""
                SignatureValue: base64Binary = Element(base64Binary, documentation=['Assinatura digital padrão RSA', 'Converter o atributo Id do DFe para array de bytes e assinar com a chave privada do RSA com algoritmo SHA1 gerando um valor no formato base64.'])
                RSAKeyValue: TRSAKeyValueType = Element(TRSAKeyValueType, documentation=['Chave Publica no padrão XML RSA Key'])
            PAASignature: PAASignature = Element(PAASignature, documentation=['Assinatura RSA do Emitente para DFe gerados por PAA'])
        infPAA: infPAA = Element(infPAA, documentation=['Grupo de Informação do Provedor de Assinatura e Autorização'])
        Id: str = Attribute(None)
    infEvento: infEvento = Element(infEvento)
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerEvento)



class TRetEvento(Element):
    """Tipo retorno do Evento"""

    class infEvento(ComplexType):
        tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
        verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que recebeu o Evento'])
        cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE, documentation=['Código do órgão de recepção do Evento. Utilizar a Tabela do IBGE extendida, utilizar 90 para identificar SUFRAMA'])
        cStat: TStat = Element(TStat, documentation=['Código do status da registro do Evento'])
        xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do registro do Evento'])
        chCTe: TChDFe = Element(TChDFe, documentation=['Chave de Acesso CT-e vinculado'])
        tpEvento: str = Element(str, documentation=['Tipo do Evento vinculado'])
        xEvento: str = Element(str, documentation=['Descrição do Evento'])
        nSeqEvento: str = Element(str, documentation=['Seqüencial do evento'])
        dhRegEvento: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e Hora de do recebimento do evento ou do registro do evento formato AAAA-MM-DDThh:mm:ssTZD'])
        nProt: TProt = Element(TProt, documentation=['Número do protocolo de registro do evento'])
        Id: str = Attribute(None)
    infEvento: infEvento = Element(infEvento)
    Signature: Signature = Element(Signature)
    versao: str = Attribute(None)



class TProcEvento(Element):
    """Tipo procEvento"""
    eventoCTe: TEvento = Element(TEvento)
    retEventoCTe: TRetEvento = Element(TRetEvento)
    versao: str = Attribute(TVerEvento)
    ipTransmissor: str = Attribute(TIPv4)
    nPortaCon: str = Attribute(None)
    dhConexao: str = Attribute(TDateTimeUTC)



class TModTransp(str):
    """Tipo Modal transporte"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['01', '02', '03', '04', '05', '06'])
    pass



class TNSU(str):
    """Tipo número sequencial único do AN"""
    _restriction = Restriction(base=r"xs:string", pattern=r"[0-9]{15}", enumeration=[])
    pass


