from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposBasico_v103 import *



class TVerEnvEvento(str):
    """Tipo Versão do EnvEvento"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"1\.00", enumeration=[])
    pass



class TVerEvento(str):
    """Tipo Versão do Evento"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"1\.00", enumeration=[])
    pass



class TCOrgaoIBGE(str):
    """Tipo Código de orgão (UF da tabela do IBGE + 90 SUFRAMA + 91 - RFB)"""
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
        dhEvento: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e Hora do Evento, formato UTC (AAAA-MM-DDThh:mm:ssTZD, onde TZD = +hh:mm ou -hh:mm)'])
        tpEvento: str = Element(str, documentation=['Tipo do Evento:\n210200 - Confirmacao da Operação\n210210 – Ciência da Operação\n210220 - Deconhecimento da operacao\n210240 - Operação não Realizada'])
        nSeqEvento: str = Element(str, documentation=['Seqüencial do evento para o mesmo tipo de evento.  Para maioria dos eventos será 1, nos casos em que possa existir mais de um evento, como é o caso da carta de correção, o autor do evento deve numerar de forma seqüencial.'])
        verEvento: TVerEnvEvento = Element(TVerEnvEvento, documentation=['Versão do Tipo do Evento'])

        class detEvento(ComplexType):
            """Evento da confirmação de recebimento e210200"""
            descEvento: str = Element(str, documentation=['Descrição do Evento:\n\t\t\t\t\t\t\t\t\t\t\t "Confirmacao da Operacao"\n\t\t\t\t\t\t\t\t\t\t\t "Ciencia da Operacao"\n\t\t\t\t\t\t\t\t\t\t\t "Desconhecimento da Operacao"\n\t\t\t\t\t\t\t\t\t\t\t "Operação não Realizada"'])
            xJust: str = Element(str, documentation=['Justificativa de Operação não Realizada'])
            versao: str = Attribute(None)
        detEvento: detEvento = Element(detEvento, documentation=['Evento da confirmação de recebimento e210200'])
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
        cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE, documentation=['Código do órgão de recepção do Evento. Utilizar a Tabela do IBGE extendida, utilizar 91 para identificar o Ambiente Nacional'])
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


