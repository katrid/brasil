from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *



class detEvento(ComplexType):
    """Schema XML de validação do evento de averbação da NFe (e790700)"""
    descEvento: str = Element(str)
    tpAutor: str = Element(str)
    verAplic: TVerAplic = Element(TVerAplic)

    class itensAverbados(ComplexType):
        """Informações dos itens da NF-e do evento."""
        _min_occurs = 1
        _max_occurs = 990

        def add(self, dhEmbarque=None, dhAverbacao=None, nDue=None, nItem=None, nItemDue=None, qItem=None, motAlteracao=None) -> detEvento.itensAverbados:
            return super().add(dhEmbarque=dhEmbarque, dhAverbacao=dhAverbacao, nDue=nDue, nItem=nItem, nItemDue=nItemDue, qItem=qItem, motAlteracao=motAlteracao)

        dhEmbarque: TDateTimeUTC = Element(TDateTimeUTC)
        dhAverbacao: TDateTimeUTC = Element(TDateTimeUTC)
        nDue: str = Element(str)
        nItem: str = Element(str)
        nItemDue: str = Element(str)
        qItem: TDec_1104Neg = Element(TDec_1104Neg)
        motAlteracao: str = Element(str)
    itensAverbados: List[itensAverbados] = Element(itensAverbados, min_occurs=1, max_occurs=990)
    versao: str = Attribute(None)

detEvento: detEvento = Element(detEvento)
