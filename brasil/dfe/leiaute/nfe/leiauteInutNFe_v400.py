from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposBasico_v400 import *



class TVerInutNFe(str):
    """Tipo Versão do leiaute de Inutilização 4.00"""
    _restriction = Restriction(base=r"xs:token", pattern=r"4\.00", enumeration=[])
    pass



class TInutNFe(Element):
    """Tipo Pedido de Inutilização de Numeração da Nota Fiscal Eletrônica"""

    class infInut(ComplexType):
        """Dados do Pedido de Inutilização de Numeração da Nota Fiscal Eletrônica"""
        tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
        xServ: str = Element(str, documentation=['Serviço Solicitado'], default='INUTILIZAR')
        cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['Código da UF do emitente'])
        ano: Tano = Element(Tano, documentation=['Ano de inutilização da numeração'])
        CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do emitente'])
        mod: TMod = Element(TMod, documentation=['Modelo da NF-e (55, 65 etc.)'])
        serie: TSerie = Element(TSerie, documentation=['Série da NF-e'])
        nNFIni: TNF = Element(TNF, documentation=['Número da NF-e inicial'])
        nNFFin: TNF = Element(TNF, documentation=['Número da NF-e final'])
        xJust: TJust = Element(TJust, documentation=['Justificativa do pedido de inutilização'])
        Id: str = Attribute(None)
    infInut: infInut = Element(infInut, documentation=['Dados do Pedido de Inutilização de Numeração da Nota Fiscal Eletrônica'])
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerInutNFe, default='4.00')



class TRetInutNFe(Element):
    """Tipo retorno do Pedido de Inutilização de Numeração da Nota Fiscal Eletrônica"""

    class infInut(ComplexType):
        """Dados do Retorno do Pedido de Inutilização de Numeração da Nota Fiscal Eletrônica"""
        tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
        verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que processou a NF-e'])
        cStat: TStat = Element(TStat, documentation=['Código do status da mensagem enviada.'])
        xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do serviço solicitado.'])
        cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['Código da UF que atendeu a solicitação'])
        ano: Tano = Element(Tano, documentation=['Ano de inutilização da numeração'])
        CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do emitente'])
        mod: TMod = Element(TMod, documentation=['Modelo da NF-e (55, etc.)'])
        serie: TSerie = Element(TSerie, documentation=['Série da NF-e'])
        nNFIni: TNF = Element(TNF, documentation=['Número da NF-e inicial'])
        nNFFin: TNF = Element(TNF, documentation=['Número da NF-e final'])
        dhRecbto: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e hora de recebimento, no formato AAAA-MM-DDTHH:MM:SS. Deve ser preenchida com data e hora da gravação no Banco em caso de Confirmação. Em caso de Rejeição, com data e hora do recebimento do Pedido de Inutilização.'])
        nProt: TProt = Element(TProt, documentation=['Número do Protocolo de Status da NF-e. 1 posição (1 – Secretaria de Fazenda Estadual 2 – Receita Federal); 2 - código da UF - 2 posições ano; 10 seqüencial no ano.'])
        Id: str = Attribute(ID)
    infInut: infInut = Element(infInut, documentation=['Dados do Retorno do Pedido de Inutilização de Numeração da Nota Fiscal Eletrônica'])
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerInutNFe)



class TProcInutNFe(Element):
    """Tipo Pedido de inutilzação de númeração de  NF-e processado"""
    inutNFe: TInutNFe = Element(TInutNFe)
    retInutNFe: TRetInutNFe = Element(TRetInutNFe)
    versao: str = Attribute(TVerInutNFe)


