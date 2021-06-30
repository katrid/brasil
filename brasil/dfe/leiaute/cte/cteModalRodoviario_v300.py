from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v300 import *

from .cteTiposBasico_v300 import *



class rodo(ComplexType):
    """Informações do modal Rodoviário"""
    RNTRC: str = Element(str, documentation=['Registro Nacional de Transportadores Rodoviários de Carga', 'Registro obrigatório do emitente do CT-e junto à ANTT para exercer a atividade de transportador rodoviário de cargas por conta de terceiros e mediante remuneração.\n\t\t\t\t\t\t'])

    class occ(ComplexType):
        """Ordens de Coleta associados"""
        _max_occurs = 10

        def add(self, serie=None, nOcc=None, dEmi=None, emiOcc=None) -> rodo.occ:
            return super().add(serie=serie, nOcc=nOcc, dEmi=dEmi, emiOcc=emiOcc)

        serie: str = Element(str, documentation=['Série da OCC'])
        nOcc: str = Element(str, documentation=['Número da Ordem de coleta'])
        dEmi: TData = Element(TData, base_type=date, documentation=['Data de emissão da ordem de coleta', 'Formato AAAA-MM-DD'])

        class emiOcc(ComplexType):
            CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['Número do CNPJ', 'Informar os zeros não significativos.'])
            cInt: str = Element(str, documentation=['Código interno de uso da transportadora', 'Uso intermo das transportadoras.'])
            IE: TIe = Element(TIe, filter=str.isdigit, documentation=['Inscrição Estadual'])
            UF: TUf = Element(TUf, documentation=['Sigla da UF', 'Informar EX para operações com o exterior.'])
            fone: TFone = Element(TFone, filter=str.isdigit, documentation=['Telefone'])
        emiOcc: emiOcc = Element(emiOcc)
    occ: List[occ] = Element(occ, max_occurs=10, documentation=['Ordens de Coleta associados'])

