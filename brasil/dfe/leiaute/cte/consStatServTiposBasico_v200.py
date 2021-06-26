from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v200 import *



class TConsStatServ(Element):
    """Tipo Pedido de Consulta do Status do Serviço CTe"""
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    xServ: TServ = Element(TServ, documentation=['Serviço Solicitado'])
    versao: str = Attribute(None)



class TVerConsStat(str):
    """Tipo Versão do Consulta do Status do Serviço CTe"""
    _restriction = Restriction(base=r"xs:string", pattern=r"2\.00", enumeration=[])
    pass



class TRetConsStatServ(Element):
    """Tipo Resultado da Consulta do Status do Serviço CTe"""
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    verAplic: str = Element(str, documentation=['Versão do Aplicativo que processou o CT-e'])
    cStat: TStat = Element(TStat, documentation=['Código do status da mensagem enviada.'])
    xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do serviço solicitado.'])
    cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['Código da UF responsável pelo serviço'])
    dhRecbto: dateTime = Element(dateTime, documentation=['AAAA-MM-DDTHH:MM:SS'])
    tMed: str = Element(str, documentation=['Tempo médio de resposta do serviço (em segundos) dos últimos 5 minutos'])
    dhRetorno: dateTime = Element(dateTime, documentation=['AAAA-MM-DDTHH:MM:SSDeve ser preenchida com data e hora previstas para o retorno dos serviços prestados.'])
    xObs: str = Element(str, documentation=['Campo observação utilizado para incluir informações ao contribuinte'])
    versao: str = Attribute(TVerConsStat)


