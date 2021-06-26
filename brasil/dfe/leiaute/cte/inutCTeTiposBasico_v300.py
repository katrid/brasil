from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposGeralCTe_v300 import *



class TInutCTe(Element):
    """Tipo Pedido de Inutilização de Numeração do Conhecimento de Transporte eletrônico"""

    class infInut(ComplexType):
        """Dados do Pedido de Inutilização de Numeração do Conhecimento de Transporte eletrônico"""
        tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
        xServ: TServ = Element(TServ, documentation=['Serviço Solicitado'])
        cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['Código da UF solicitada'])
        ano: str = Element(str, documentation=['Ano de inutilização da numeração'])
        CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do emitente'])
        mod: TModCT_Carga_OS = Element(TModCT_Carga_OS, documentation=['Modelo da CT-e (57 ou 67)'])
        serie: TSerie = Element(TSerie, documentation=['Série da CT-e'])
        nCTIni: TNF = Element(TNF, documentation=['Número da CT-e inicial'])
        nCTFin: TNF = Element(TNF, documentation=['Número da CT-e final'])
        xJust: TJust = Element(TJust, documentation=['Justificativa do pedido de inutilização'])
        Id: str = Attribute(None)
    infInut: infInut = Element(infInut, documentation=['Dados do Pedido de Inutilização de Numeração do Conhecimento de Transporte eletrônico'])
    Signature: Signature = Element(Signature)
    versao: str = Attribute(None)



class TVerInutCTe(str):
    """Tipo Versão Inutilização de numeração de CT-e"""
    _restriction = Restriction(base=r"xs:string", pattern=r"3\.00", enumeration=[])
    pass



class TRetInutCTe(Element):
    """Tipo retorno do Pedido de Inutilização de Numeração do Conhecimento de Transporte eletrônico"""

    class infInut(ComplexType):
        """Dados do Retorno do Pedido de Inutilização de Numeração do Conhecimento de Transporte eletrônico"""
        tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
        verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que processou a CT-e'])
        cStat: TStat = Element(TStat, documentation=['Código do status da mensagem enviada.'])
        xMotivo: str = Element(str, documentation=['Descrição literal do status do serviço solicitado.'])
        cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['Código da UF solicitada'])
        ano: str = Element(str, documentation=['Ano de inutilização da numeração'])
        CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do emitente'])
        mod: TModCT_Carga_OS = Element(TModCT_Carga_OS, documentation=['Modelo da CT-e (57 ou 67)'])
        serie: TSerie = Element(TSerie, documentation=['Série da CT-e'])
        nCTIni: TNF = Element(TNF, documentation=['Número da CT-e inicial'])
        nCTFin: TNF = Element(TNF, documentation=['Número da CT-e final'])
        dhRecbto: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e hora de recebimento, no formato AAAA-MM-DDTHH:MM:SS TZD. Deve ser preenchida com data e hora da gravação no Banco em caso de Confirmação. Em caso de Rejeição, com data e hora do recebimento do Pedido de Inutilização.'])
        nProt: TProt = Element(TProt, documentation=['Número do Protocolo de Status do CT-e. 1 posição (1 – Secretaria de Fazenda Estadual , 3 - SEFAZ Virtual RS, 5 - SEFAZ Virtual SP); 2 - código da UF - 2 posições ano; 10 seqüencial no ano.'])
        Id: str = Attribute(ID)
    infInut: infInut = Element(infInut, documentation=['Dados do Retorno do Pedido de Inutilização de Numeração do Conhecimento de Transporte eletrônico'])
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerInutCTe)



class TProcInutCTe(Element):
    """Tipo Pedido de inutilzação de númeração de CT-e processado"""
    inutCTe: TInutCTe = Element(TInutCTe)
    retInutCTe: TRetInutCTe = Element(TRetInutCTe)
    versao: str = Attribute(TVerInutCTe)
    ipTransmissor: str = Attribute(TIPv4)


