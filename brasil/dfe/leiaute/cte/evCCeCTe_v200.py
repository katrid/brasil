from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v200 import *



class evCCeCTe(ComplexType):
    """Schema XML de validação do evento carta de correção 
110110"""
    descEvento: str = Element(str)

    class infCorrecao(ComplexType):
        """Grupo de Informações de Correção"""
        _max_occurs = -1

        def add(self, grupoAlterado=None, campoAlterado=None, valorAlterado=None, nroItemAlterado=None) -> evCCeCTe.infCorrecao:
            return super().add(grupoAlterado=grupoAlterado, campoAlterado=campoAlterado, valorAlterado=valorAlterado, nroItemAlterado=nroItemAlterado)

        grupoAlterado: str = Element(str)
        campoAlterado: str = Element(str)
        valorAlterado: str = Element(str)
        nroItemAlterado: str = Element(str)
    infCorrecao: List[infCorrecao] = Element(infCorrecao, max_occurs=-1)
    xCondUso: str = Element(str)

evCCeCTe: evCCeCTe = Element(evCCeCTe)
