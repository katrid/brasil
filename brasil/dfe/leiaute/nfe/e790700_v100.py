from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *



class detEvento(ComplexType):
    """Schema XML de validação do evento de averbação da NFe (e790700)"""
    descEvento: str = Element(str, documentation=['Descrição do Evento - “Averbação para Exportação”'])
    tpAutor: str = Element(str, documentation=['Tipo do Autor do Evento (6=RFB)'])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do aplicativo do autor do evento'])

    class itensAverbados(ComplexType):
        """Informações dos itens da NF-e do evento."""
        _min_occurs = 1
        _max_occurs = 990

        def add(self, dhEmbarque=None, dhAverbacao=None, nDue=None, nItem=None, nItemDue=None, qItem=None, motAlteracao=None) -> detEvento.itensAverbados:
            return super().add(dhEmbarque=dhEmbarque, dhAverbacao=dhAverbacao, nDue=nDue, nItem=nItem, nItemDue=nItemDue, qItem=qItem, motAlteracao=motAlteracao)

        dhEmbarque: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data do Embarque no formato AAAA-MM-DDThh:mm:ssTZD'])
        dhAverbacao: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data da averbação no formato AAAA-MM-DDThh:mm:ssTZD'])
        nDue: str = Element(str, documentation=['Número Identificador da Declaração Única do Comércio Exterior associada'])
        nItem: str = Element(str, documentation=['Número do item da NF-e averbada'])
        nItemDue: str = Element(str, documentation=['Informação do número do item na Declaração de Exportação associada a averbação.'])
        qItem: TDec_1104Neg = Element(TDec_1104Neg, tipo="N", tam=(11, 4), base_type=Decimal, documentation=['Quantidade averbada do item na unidade tributária (campo uTrib)'])
        motAlteracao: str = Element(str, documentation=['\n                    Motivo da Alteração\n                    1 - Exportação Averbada;\n                    2 - Retificação da Quantidade Averbada;\n                    3 - Cancelamento da Exportação;\n                  '])
    itensAverbados: List[itensAverbados] = Element(itensAverbados, min_occurs=1, max_occurs=990, documentation=['Informações dos itens da NF-e do evento.'])
    versao: str = Attribute(None)

detEvento: detEvento = Element(detEvento, documentation=['Schema XML de validação do evento de averbação da NFe (e790700)'])
