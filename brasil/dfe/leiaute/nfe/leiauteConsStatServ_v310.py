from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v310 import *



class TVerConsStatServ(token):
    """Tipo versão do leiuate da Consulta Status do Serviço 3.10"""
    _restriction = Restriction(base=r"xs:token", pattern=r"3\.10", enumeration=[])
    pass



class TConsStatServ(Element):
    """Tipo Pedido de Consulta do Status do Serviço"""
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['Sigla da UF consultada'])
    xServ: str = Element(str, documentation=['Serviço Solicitado'])
    versao: str = Attribute(TVerConsStatServ)



class TRetConsStatServ(Element):
    """Tipo Resultado da Consulta do Status do Serviço"""
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que processou a NF-e'])
    cStat: TStat = Element(TStat, documentation=['Código do status da mensagem enviada.'])
    xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do serviço solicitado.'])
    cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['Código da UF responsável pelo serviço'])
    dhRecbto: TDateTimeUTC = Element(TDateTimeUTC, documentation=['Data e hora do recebimento da consulta no formato AAAA-MM-DDTHH:MM:SSTZD'])
    tMed: TMed = Element(TMed, documentation=['Tempo médio de resposta do serviço (em segundos) dos últimos 5 minutos'])
    dhRetorno: TDateTimeUTC = Element(TDateTimeUTC, documentation=['AAAA-MM-DDTHH:MM:SSDeve ser preenchida com data e hora previstas para o retorno dos serviços prestados.'])
    xObs: TMotivo = Element(TMotivo, documentation=['Campo observação utilizado para incluir informações ao contribuinte'])
    versao: str = Attribute(TVerConsStatServ)


