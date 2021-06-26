from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposGeralCTe_v200 import *



class TProtCTe(Element):
    """Tipo Protocolo de status resultado do processamento da CT-e"""

    class infProt(ComplexType):
        """Dados do protocolo de status"""
        tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
        verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que processou a NF-e'])
        chCTe: TChNFe = Element(TChNFe, documentation=['Chaves de acesso da CT-e, compostas por: UF do emitente, AAMM da emissão da NFe, CNPJ do emitente, modelo, subsérie e número da CT-e e código numérico+DV.'])
        dhRecbto: dateTime = Element(dateTime, documentation=['Data e hora de processamento, no formato AAAA-MM-DDTHH:MM:SS. Deve ser preenchida com data e hora da gravação no Banco em caso de Confirmação. Em caso de Rejeição, com data e hora do recebimento do Lote de CT-e enviado.'])
        nProt: TProt = Element(TProt, documentation=['Número do Protocolo de Status do CT-e. 1 posição tipo de autorizador (1 – Secretaria de Fazenda Estadual,  3 - SEFAZ Virtual RS, 5 - SEFAZ Virtual SP ); 2 posições ano; 10 seqüencial no ano.'])
        digVal: DigestValueType = Element(DigestValueType, documentation=['Digest Value da CT-e processado. Utilizado para conferir a integridade do CT-e original.'])
        cStat: str = Element(str, documentation=['Código do status do CT-e.'])
        xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do CT-e.'])
        Id: str = Attribute(ID)
    infProt: infProt = Element(infProt, documentation=['Dados do protocolo de status'])
    Signature: Signature = Element(Signature)
    versao: str = Attribute(None)



class TVerConsReciCTe(str):
    """Tipo Versão do Consulta Lote de CT-e - 1.04"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"2\.00", enumeration=[])
    pass



class TConsReciCTe(Element):
    """Tipo Pedido de Consulta do Recibo do Lote de CT-e"""
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    nRec: TRec = Element(TRec, documentation=['Número do Recibo do lote a ser consultado'])
    versao: str = Attribute(TVerConsReciCTe)



class TRetConsReciCTe(Element):
    """Tipo Retorno do Pedido de  Consulta do Recibo do Lote de CT-e"""
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que processou a CT-e'])
    nRec: TRec = Element(TRec, documentation=['Número do Recibo Consultado'])
    cStat: TStat = Element(TStat, documentation=['código do status do retorno da consulta.'])
    xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do do retorno da consulta.'])
    cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['Idntificação da UF'])
    protCTe: List[TProtCTe] = Element(TProtCTe, max_occurs=50, documentation=['Conjunto de CT-es processados, só existe nos casos em que o lote consultado se encontra processado'])
    versao: str = Attribute(TVerConsReciCTe)


