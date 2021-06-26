from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v300 import *

from .cteTiposBasico_v300 import *



class rodo(ComplexType):
    """Informações do modal Rodoviário"""
    RNTRC: str = Element(str)

    class occ(ComplexType):
        """Ordens de Coleta associados"""
        _max_occurs = 10

        def add(self, serie=None, nOcc=None, dEmi=None, emiOcc=None) -> rodo.occ:
            return super().add(serie=serie, nOcc=nOcc, dEmi=dEmi, emiOcc=emiOcc)

        serie: str = Element(str)
        nOcc: str = Element(str)
        dEmi: TData = Element(TData)

        class emiOcc(ComplexType):
            CNPJ: TCnpj = Element(TCnpj)
            cInt: str = Element(str)
            IE: TIe = Element(TIe)
            UF: TUf = Element(TUf)
            fone: TFone = Element(TFone)
        emiOcc: emiOcc = Element(emiOcc)
    occ: List[occ] = Element(occ, max_occurs=10)

rodo: rodo = Element(rodo)
