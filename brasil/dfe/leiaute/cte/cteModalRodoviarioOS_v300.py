from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v300 import *

from .cteTiposBasico_v300 import *



class TTermoAutFreta(str):
    """Tipo Termo  de Autorização de Fretamento – TAF"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{12}", max_length=r"12", enumeration=[])
    pass



class TNroRegEstadual(str):
    """Tipo Número de Registro Estadual"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{25}", max_length=r"25", enumeration=[])
    pass



class rodoOS(ComplexType):
    """Informações do modal Rodoviário"""
    _choice = [['TAF', 'NroRegEstadual']]
    TAF: TTermoAutFreta = Element(TTermoAutFreta)
    NroRegEstadual: TNroRegEstadual = Element(TNroRegEstadual)

    class veic(ComplexType):
        """Dados do Veículo"""
        placa: str = Element(str)
        RENAVAM: str = Element(str)

        class prop(ComplexType):
            """Proprietários do Veículo.
Só preenchido quando o veículo não pertencer à empresa emitente do CT-e OS"""
            _choice = [['CPF', 'CNPJ'], ['TAF', 'NroRegEstadual']]
            CPF: TCpf = Element(TCpf)
            CNPJ: TCnpjOpc = Element(TCnpjOpc)
            TAF: TTermoAutFreta = Element(TTermoAutFreta)
            NroRegEstadual: TNroRegEstadual = Element(TNroRegEstadual)
            xNome: str = Element(str)
            IE: str = Element(str)
            UF: TUf = Element(TUf)
            tpProp: str = Element(str)
        prop: prop = Element(prop)
        UF: TUf = Element(TUf)
    veic: veic = Element(veic)

    class infFretamento(ComplexType):
        """Dados do fretamento (apenas para Transporte de Pessoas)"""
        tpFretamento: str = Element(str)
        dhViagem: TDateTimeUTC = Element(TDateTimeUTC)
    infFretamento: infFretamento = Element(infFretamento)

rodoOS: rodoOS = Element(rodoOS)
