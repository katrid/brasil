from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposBasico_v310 import *



class TVerEvento(str):
    """Tipo Versão do Evento"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{1,2}\.[0-9]{1,2}", enumeration=[])
    pass



class TCOrgaoIBGE(str):
    """Tipo Código de orgão (UF da tabela do IBGE + 91 RFB)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53', '91'])
    pass



class retEnvEvento(ComplexType):
    idLote: str = Element(str, documentation=['Identificador de controle do Lote de envio do Evento, conforme informado na mensagem de entrada.'])
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente: 1=Produção /2=Homologação'])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão da aplicação que processou o evento.'])
    cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE, documentation=['Código da UF que registrou o Evento. '])
    cStat: TStat = Element(TStat, documentation=['Código do status da resposta '])
    xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição do status da resposta '])

    class retEvento(ComplexType):
        _max_occurs = 20

        def add(self, infEvento=None, versao=None) -> retEnvEvento.retEvento:
            return super().add(infEvento=infEvento, versao=versao)


        class infEvento(ComplexType):
            tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente: 1=Produção /2=Homologação'])
            verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão da aplicação que registrou o Evento, utilizar literal que permita a identificação do órgão, como a sigla da UF ou do órgão.'])
            cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE, documentation=['Código da UF que registrou o Evento. '])
            cStat: TStat = Element(TStat, documentation=['Código do status da resposta.'])
            xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição do status da resposta.'])
            chNFe: TChNFe = Element(TChNFe, documentation=['Chave de Acesso da NFC-e vinculada ao evento.'])
            tpEvento: str = Element(str, documentation=['110140 \x96 EPEC'])
            xEvento: str = Element(str, documentation=['\x93EPEC autorizado\x94'])
            nSeqEvento: str = Element(str, documentation=['Sequencial do evento, conforme a mensagem de entrada.'])
            cOrgaoAutor: TCodUfIBGE = Element(TCodUfIBGE, documentation=['Idem a mensagem de entrada.'])
            dhRegEvento: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e hora de registro do evento no formato AAAA-MM-DDTHH:MM:SSTZD (formato UTC, onde TZD é +HH:MM ou \x96HH:MM). Se o evento for rejeitado informar a data e hora de recebimento do evento.'])
            nProt: TProt = Element(TProt, documentation=['Número do Protocolo do Evento'])
            chNFePend: List[TChNFe] = Element(TChNFe, max_occurs=50, documentation=['Relação de Chaves de Acesso de EPEC pendentes de'])
            Id: str = Attribute(None)
        infEvento: infEvento = Element(infEvento)
        Signature: Signature = Element(Signature)
        versao: str = Attribute(TVerEvento)
    retEvento: List[retEvento] = Element(retEvento, max_occurs=20)
    versao: str = Attribute(TVerEvento)

retEnvEvento: retEnvEvento = Element(retEnvEvento)
