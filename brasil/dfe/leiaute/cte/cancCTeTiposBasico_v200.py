from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposGeralCTe_v200 import *



class TVerCancCTe(str):
    """Tipo Versão de cancela CT-e - 1.04"""
    _restriction = Restriction(base=r"xs:string", pattern=r"1\.04", enumeration=[])
    pass



class TCancCTe(Element):
    """Tipo Pedido de Cancelamento de CT-e"""

    class infCanc(ComplexType):
        """Dados do Pedido de Cancelamentode Conhecimento de Transporte Eletrônico"""
        tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
        xServ: TServ = Element(TServ, documentation=['Serviço Solicitado'])
        chCTe: TChNFe = Element(TChNFe, documentation=['Chaves de acesso compostas por Código da UF + AAMM da emissão + CNPJ do Emitente + Modelo, Série e Número do CT-e+ Código Numérico + DV.'])
        nProt: TProt = Element(TProt, documentation=['Número do Protocolo de Status do CT-e. 1 posição tipo de autorizador (1 – Secretaria de Fazenda Estadual 2 – Receita Federal - SCAN, 3 - SEFAZ Virtual RFB ); 2 posições ano; 10 seqüencial no ano.'])
        xJust: TJust = Element(TJust, documentation=['Justificativa do cancelamento'])
        Id: str = Attribute(None)
    infCanc: infCanc = Element(infCanc, documentation=['Dados do Pedido de Cancelamentode Conhecimento de Transporte Eletrônico'])
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerCancCTe)



class TRetCancCTe(Element):
    """Tipo retorno Pedido de Cancelamento CT-e"""

    class infCanc(ComplexType):
        """Dados do Resultado do Pedido de Cancelamento do Conhecimento de Transporte Eletrônico"""
        tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
        cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['Identificação da UF'])
        verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que processou o pedido de cancelamento'])
        cStat: TStat = Element(TStat, documentation=['Código do status da mensagem enviada.'])
        xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do serviço solicitado.'])
        chCTe: TChNFe = Element(TChNFe, documentation=['Chaves de acesso do CT-e, compostas por: UF do emitente, AAMM da emissão do CT-e, CNPJ do emitente, modelo, série e número do CT-e e código numérico + DV.'])
        dhRecbto: dateTime = Element(dateTime, documentation=['Data e hora de recebimento, no formato AAAA-MM-DDTHH:MM:SS. Deve ser preenchida com data e hora da gravação no Banco em caso de Confirmação.'])
        nProt: TProt = Element(TProt, documentation=['Número do Protocolo de homologação do cancelamento: 1 posição tipo de autorizador (1 – Secretaria de Fazenda Estadual, 3 - SEFAZ Virtual RS, 5 - SEFAZ Virtual SP ); 2 posições ano; 10 seqüencial no ano.'])
        Id: str = Attribute(ID)
    infCanc: infCanc = Element(infCanc, documentation=['Dados do Resultado do Pedido de Cancelamento do Conhecimento de Transporte Eletrônico'])
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerCancCTe)



class TProcCancCTe(Element):
    """Tipo Pedido de Cancelamento de CT-e processado"""
    cancCTe: TCancCTe = Element(TCancCTe)
    retCancCTe: TRetCancCTe = Element(TRetCancCTe)
    versao: str = Attribute(TVerCancCTe)


