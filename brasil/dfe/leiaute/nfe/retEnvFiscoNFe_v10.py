from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposBasico_v310 import *



class TCOrgaoIBGE(str):
    """Tipo Código de orgão (UF da tabela do IBGE + 91 RFB)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53', '91'])
    pass



class retEnvEvento(ComplexType):
    """TAG raiz do Resultado do Envio do Evento"""
    idLote: str = Element(str, documentation=['Identificador de controle do Lote de envio do Evento. Número sequencial autoincremental único para identificação do Lote.'])
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente: 1 - Produção, 2 \x96 Homologação'])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão da aplicação que processou o evento.'])
    cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE, documentation=['Código da UF que registrou o Evento. Utilizar 90 para o Ambiente Nacional.'])
    cStat: TStat = Element(TStat, documentation=['Código do status da resposta'])
    xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição do status da resposta'])

    class retEvento(ComplexType):
        """TAG de grupo do resultado do processamento do Evento"""
        _max_occurs = 20

        def add(self, infEvento=None, versao=None) -> retEnvEvento.retEvento:
            return super().add(infEvento=infEvento, versao=versao)


        class infEvento(ComplexType):
            """Grupo de informações do registro do Evento"""
            tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente: 1 \x96 Produção / 2 \x96 Homologação'])
            verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão da aplicação que registrou o Evento, utilizar literal que permita a identificação do órgão, como a sigla da UF ou\n\tdo órgão.'])
            cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE, documentation=['Código da UF que registrou o Evento. Utilizar 90 para o Ambiente Nacional.'])
            cStat: TStat = Element(TStat, documentation=['Código do status da resposta.'])
            xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição do status da resposta.'])
            chNFe: List[TChNFe] = Element(TChNFe, max_occurs=1, documentation=['Chave de Acesso da NF-e vinculada ao evento.'])
            tpEvento: List[str] = Element(str, max_occurs=1, documentation=['Código do Tipo do Evento.'])
            xEvento: List[str] = Element(str, max_occurs=1, documentation=['Descrição do Evento \x96 \x93Cancelamento de Pedido de Prorrogação registrado\x94'])
            nSeqEvento: List[str] = Element(str, max_occurs=1, documentation=['Sequencial do evento para o mesmo tipo de evento. '])
            CNPJDest: List[TCnpjOpc] = Element(TCnpjOpc, max_occurs=1, filter=str.isdigit, documentation=['Informar o CNPJ do destinatário da NF-e.'])
            emailDest: List[str] = Element(str, max_occurs=1, documentation=['email do destinatário informado na NF-e.'])
            dhRegEvento: TDateTimeUTC = Element(TDateTimeUTC, documentation=['Data e hora de registro do evento no formato AAAA-MMDDTHH:MM:SSTZD (formato UTC, onde TZD é +HH:MM ou\n\t\x96\t\t\t\t\t\t\tHH:MM), se o evento for rejeitado informar a data e hora de recebimento do evento.'])
            nProt: List[TProt] = Element(TProt, max_occurs=1, documentation=['Número do Protocolo do Evento 1 posição (1-Secretaria da Fazenda Estadual, 2-RFB), 2 posições para o código da UF, 2 posições para o ano e 10 posições para o sequencial no ano.'])
            Id: str = Attribute(None)
        infEvento: infEvento = Element(infEvento, documentation=['Grupo de informações do registro do Evento'])
        Signature: Signature = Element(Signature)
        versao: str = Attribute(None)
    retEvento: List[retEvento] = Element(retEvento, max_occurs=20, documentation=['TAG de grupo do resultado do processamento do Evento'])
    versao: str = Attribute(None)

retEnvEvento: retEnvEvento = Element(retEnvEvento, documentation=['TAG raiz do Resultado do Envio do Evento'])
