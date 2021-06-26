from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposBasico_v103 import *



class TVerEvento(str):
    """Tipo Versão do Evento"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"1.00", enumeration=[])
    pass



class TEvento(Element):
    """Tipo Evento"""

    class infEvento(ComplexType):
        cOrgao: str = Element(str, documentation=['Código do órgão de recepção do Evento. Para o evento de averbação de exportação será utilizado o valor 91 para o Ambiente Nacional.'])
        tpAmb: TAmb = Element(TAmb, documentation=['\n                  Identificação do Ambiente:\n                  1 - Produção\n                  2 - Homologação\n                '])
        CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do  autor do evento'])
        chNFe: TChNFe = Element(TChNFe, documentation=['Chave de Acesso da NF-e vinculada ao evento'])
        dhEvento: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data de emissão no formato UTC.  AAAA-MM-DDThh:mm:ssTZD'])
        tpEvento: str = Element(str, documentation=['Tipo do Evento'])
        nSeqEvento: str = Element(str, documentation=['\n                  Seqüencial do evento para o mesmo tipo de evento. Para maioria dos eventos será 1, nos casos em que possa existir mais de um evento, como é o caso dos eventos de averbação, o autor do evento deve numerar de forma seqüencial\n                '])
        verEvento: str = Element(str, documentation=['Versão do Tipo do Evento'])

        class detEvento(ComplexType):
            """Schema XML de validação do evento de averbação da NFe (e790700)"""
            descEvento: str = Element(str, documentation=['Descrição do Evento - “Averbação para Exportação”'])
            tpAutor: str = Element(str, documentation=['Tipo do Autor do Evento (6=RFB)'])
            verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do aplicativo do Autor do evento'])

            class itensAverbados(ComplexType):
                """Informações dos itens da NF-e do evento."""
                _min_occurs = 1
                _max_occurs = 990

                def add(self, dhEmbarque=None, dhAverbacao=None, nDue=None, nItem=None, nItemDue=None, qItem=None, motAlteracao=None) -> TEvento.infEvento.detEvento.itensAverbados:
                    return super().add(dhEmbarque=dhEmbarque, dhAverbacao=dhAverbacao, nDue=nDue, nItem=nItem, nItemDue=nItemDue, qItem=qItem, motAlteracao=motAlteracao)

                dhEmbarque: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data do Embarque no formato AAAA-MM-DDThh:mm:ssTZD'])
                dhAverbacao: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data da averbação no formato AAAA-MM-DDThh:mm:ssTZD'])
                nDue: str = Element(str, documentation=['Número Identificador da Declaração Única do Comércio Exterior associada'])
                nItem: str = Element(str, documentation=['Número do item da NF-e averbada'])
                nItemDue: str = Element(str, documentation=['Informação do número do item na Declaração de Exportação associada a averbação.'])
                qItem: TDec_1104Neg = Element(TDec_1104Neg, tipo="N", tam=(11, 4), base_type=Decimal, documentation=['Quantidade averbada do item na unidade tributária (campo uTrib)'])
                motAlteracao: str = Element(str, documentation=['\n                              Motivo da Alteração\n                              1 - Exportação Averbada;\n                              2 - Retificação da Quantidade Averbada;\n                              3 - Cancelamento da Exportação;\n                            '])
            itensAverbados: List[itensAverbados] = Element(itensAverbados, min_occurs=1, max_occurs=990, documentation=['Informações dos itens da NF-e do evento.'])
            versao: str = Attribute(None)
        detEvento: detEvento = Element(detEvento, documentation=['Schema XML de validação do evento de averbação da NFe (e790700)'])
        Id: str = Attribute(None)
    infEvento: infEvento = Element(infEvento)
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerEvento)



class TCOrgaoIBGE(str):
    """Tipo Código de orgão (UF da tabela do IBGE)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53', '90', '91'])
    pass



class TretEvento(Element):
    """Tipo retorno do Evento"""

    class infEvento(ComplexType):
        _choice = [['CNPJDest', 'CPFDest']]
        tpAmb: TAmb = Element(TAmb, documentation=['\n                  Identificação do Ambiente:\n                  1 - Produção\n                  2 - Homologação\n                '])
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



class TVerEnvEvento(str):
    """Tipo Versão do EnvEvento"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"1.00", enumeration=[])
    pass



class TEnvEvento(Element):
    """Tipo Lote de Envio"""
    idLote: str = Element(str)
    evento: List[TEvento] = Element(TEvento, max_occurs=20)
    versao: str = Attribute(TVerEnvEvento)



class TRetEnvEvento(Element):
    """Tipo Retorno de Lote de Envio"""
    idLote: str = Element(str)
    tpAmb: TAmb = Element(TAmb, documentation=['\n            Identificação do Ambiente:\n            1 - Produção\n            2 - Homologação\n          '])
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


