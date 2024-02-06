from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposGeralMDFe_v300 import *



class TVerConsReciMDFe(str):
    """Tipo Versão do Consulta de MDF-e - 3.00"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"3\.00", enumeration=[])
    pass



class TProtMDFe(Element):
    """Tipo Protocolo de status resultado do processamento do MDF-e"""

    class infProt(ComplexType):
        """Dados do protocolo de status"""
        tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
        verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que processou o MDF-e'])
        chMDFe: TChMDFe = Element(TChMDFe, documentation=['Chaves de acesso do MDF-e, '])
        dhRecbto: str = Element(str, documentation=['Data e hora de processamento, no formato AAAA-MM-DDTHH:MM:SS TZD. '])
        nProt: TProt = Element(TProt, documentation=['Número do Protocolo de Status do MDF-e.'])
        digVal: DigestValueType = Element(DigestValueType, documentation=['Digest Value do MDF-e processado. Utilizado para conferir a integridade do MDF-e original.'])
        cStat: str = Element(str, documentation=['Código do status do MDF-e.'])
        xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do MDF-e.'])
        Id: str = Attribute(ID)
    infProt: infProt = Element(infProt, documentation=['Dados do protocolo de status'])

    class infFisco(ComplexType):
        """Mensagem do Fisco"""
        cMsg: str = Element(str, documentation=['Código do status da mensagem do fisco'])
        xMsg: TMotivo = Element(TMotivo, documentation=['Mensagem do Fisco'])
    infFisco: infFisco = Element(infFisco, documentation=['Mensagem do Fisco'])
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerConsReciMDFe)



class TConsReciMDFe(Element):
    """Tipo Pedido de Consulta do Recibo do MDF-e"""
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    nRec: TRec = Element(TRec, documentation=['Número do Recibo do arquivo a ser consultado'])
    versao: str = Attribute(TVerConsReciMDFe)



class TRetConsReciMDFe(Element):
    """Tipo Retorno do Pedido de  Consulta do Recibo do MDF-e"""
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que processou o MDF-e'])
    nRec: TRec = Element(TRec, documentation=['Número do Recibo Consultado'])
    cStat: TStat = Element(TStat, documentation=['código do status do retorno da consulta.'])
    xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do do retorno da consulta.'])
    cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['Idntificação da UF'])
    protMDFe: TProtMDFe = Element(TProtMDFe, documentation=['Resultado do processamento do MDF-e'])
    versao: str = Attribute(TVerConsReciMDFe)


