from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposDistDFe_v101 import *



class retDistDFeInt(ComplexType):
    """Schema do resultado do pedido de distribuição de DF-e de interesse"""
    tpAmb: TAmb = Element(TAmb, documentation=['\n            Identificação do Ambiente:\n            1 - Produção\n            2 - Homologação\n            '])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Web Service NFeDistribuicaoDFe'])
    cStat: TStat = Element(TStat, documentation=['Código do status de processamento da requisição'])
    xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do processamento da requisição'])
    dhResp: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e Hora de processamento da requisição no formato AAAA-MM-DDTHH:MM:SSTZD'])
    ultNSU: TNSU = Element(TNSU, documentation=['Último NSU pesquisado no Ambiente Nacional. Se for o caso, o solicitante pode continuar a consulta a partir deste NSU para obter novos resultados.'])
    maxNSU: TNSU = Element(TNSU, documentation=['Maior NSU existente no Ambiente Nacional para o CNPJ/CPF informado'])

    class loteDistDFeInt(ComplexType):
        """Conjunto de informações resumidas e documentos fiscais eletrônicos de interesse da pessoa ou empresa."""

        class docZip(ComplexType):
            """Informação resumida ou documento fiscal eletrônico de interesse da pessoa ou empresa. O conteúdo desta tag estará compactado no padrão gZip. O tipo do campo é base64Binary."""
            pass
        docZip: docZip = Element(docZip, documentation=['Informação resumida ou documento fiscal eletrônico de interesse da pessoa ou empresa. O conteúdo desta tag estará compactado no padrão gZip. O tipo do campo é base64Binary.'])
    loteDistDFeInt: loteDistDFeInt = Element(loteDistDFeInt, documentation=['Conjunto de informações resumidas e documentos fiscais eletrônicos de interesse da pessoa ou empresa. '])
    versao: str = Attribute(TVerDistDFe)

retDistDFeInt: retDistDFeInt = Element(retDistDFeInt, documentation=['Schema do resultado do pedido de distribuição de DF-e de interesse'])
