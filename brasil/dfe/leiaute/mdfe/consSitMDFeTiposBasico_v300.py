from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralMDFe_v300 import *

from .xmldsig_core_schema_v101 import *



class TConsSitMDFe(Element):
    """Tipo Pedido de Consulta da Situação Atual do MDF-e"""
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    xServ: TServ = Element(TServ, documentation=['Serviço Solicitado'])
    chMDFe: TChNFe = Element(TChNFe, documentation=['Chaves de acesso do MDF-e, compostas por: UF do emitente, AAMM da emissão do MDF-e, CNPJ do emitente, modelo, série, tipo de emissão e número do MDF-e e código numérico + DV.'])
    versao: str = Attribute(None)



class TVerConsSitMDFe(str):
    """Tipo Versão do Consulta situação de MDF-e - 1.00"""
    _restriction = Restriction(base=r"xs:string", pattern=r"3\.00", enumeration=[])
    pass



class TRetConsSitMDFe(Element):
    """Tipo Retorno de Pedido de Consulta da Situação Atual do MDF-e"""
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que processou o MDF-e'])
    cStat: TStat = Element(TStat, documentation=['Código do status da mensagem enviada.'])
    xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do serviço solicitado.'])
    cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['código da UF de atendimento'])

    class protMDFe(ComplexType):
        versao: str = Attribute(None)
    protMDFe: protMDFe = Element(protMDFe)

    class procEventoMDFe(ComplexType):
        _max_occurs = -1

        def add(self, versao=None) -> TRetConsSitMDFe.procEventoMDFe:
            return super().add(versao=versao)

        versao: str = Attribute(None)
    procEventoMDFe: List[procEventoMDFe] = Element(procEventoMDFe, max_occurs=-1)

    class procInfraSA(ComplexType):
        """Grupo de informações do compartilhamento do MDFe com InfraSA para geração do DTe"""
        nProtDTe: TProt = Element(TProt, documentation=['Número do Protocolo de geração do DTe'])
        dhProt: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e hora de geração do protocolo, no formato AAAA-MM-DDTHH:MM:SS TZD.'])
    procInfraSA: procInfraSA = Element(procInfraSA, documentation=['Grupo de informações do compartilhamento do MDFe com InfraSA para geração do DTe'])
    versao: str = Attribute(TVerConsSitMDFe)


