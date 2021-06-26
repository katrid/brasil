from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposGeralCTe_v300 import *

from .cteTiposBasico_v300 import *



class TVerConsReciCTe(str):
    """Tipo Versão do Consulta Lote de CT-e"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"3\.00", enumeration=[])
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


