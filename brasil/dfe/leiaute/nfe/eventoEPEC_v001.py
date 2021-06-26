from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposBasico_v310 import *



class TVerEvento(str):
    """Versão do Tipo do Evento"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{1,2}\.[0-9]{1,2}", enumeration=[])
    pass



class TCOrgaoIBGE(str):
    """Tipo Código de orgão (UF da tabela do IBGE + 91 RFB)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53', '91'])
    pass



class envEvento(ComplexType):
    idLote: str = Element(str, documentation=['Identificador de controle do Lote de envio do Evento.'])

    class evento(ComplexType):
        _max_occurs = 20

        def add(self, infEvento=None, versao=None) -> envEvento.evento:
            return super().add(infEvento=infEvento, versao=versao)


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
            cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE, documentation=['Código do órgão de recepção do Evento.'])
            tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente: 1=Produção /2=Homologação'])
            CNPJ: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['CNPJ'])
            CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CPF'])
            chNFe: TChNFe = Element(TChNFe, documentation=['Para o evento de EPEC, a posição 35 da Chave de Acesso deve ser 4 (tpEmis=4).'])
            dhEvento: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e hora do evento no formato AAAA-MM-DDThh:mm:ssTZD (UTC - Universal Coordinated Time).'])
            tpEvento: str = Element(str, documentation=['Código do evento: 110140 -EPEC'])
            nSeqEvento: str = Element(str, documentation=['Informar o valor "1" para o evento do EPEC.'])
            verEvento: TVerEvento = Element(TVerEvento, documentation=['Versão do detalhe do evento (grupo detEvento - P17), informação usada pela SEFAZ para validar o grupo detEvento.'])

            class detEvento(ComplexType):
                descEvento: str = Element(str, documentation=['"EPEC"'])
                cOrgaoAutor: TCodUfIBGE = Element(TCodUfIBGE, documentation=['Código do Órgão do Autor do Evento.'])
                tpAutor: str = Element(str, documentation=['Informar "1=Empresa Emitente" para este evento.'])
                verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do aplicativo do Autor do Evento.'])
                dhEmi: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e hora no formato UTC (Universal Coordinated Time): "AAAA-MM-DDThh:mm:ss TZD".'])
                tpNF: str = Element(str, documentation=['Informar 1=Saída.'])
                IE: TIe = Element(TIe, filter=str.isdigit, documentation=['IE do Emitente'])

                class dest(ComplexType):
                    _choice = [['CNPJ', 'CPF', 'idEstrangeiro']]
                    UF: TUf = Element(TUf, documentation=['Sigla da UF do destinatário. '])
                    CNPJ: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['CNPJ'])
                    CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CPF'])
                    idEstrangeiro: str = Element(str, documentation=['ID Estrangeiro'])
                dest: dest = Element(dest)
                vNF: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor total da NFC-e'])
                vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor total do ICMS'])
                versao: str = Attribute(TVerEvento)
            detEvento: detEvento = Element(detEvento)
            Id: str = Attribute(None)
        infEvento: infEvento = Element(infEvento)
        Signature: Signature = Element(Signature)
        versao: str = Attribute(TVerEvento)
    evento: List[evento] = Element(evento, max_occurs=20)
    versao: str = Attribute(TVerEvento)

envEvento: envEvento = Element(envEvento)
