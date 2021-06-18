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
    class veic(ComplexType):
        placa: str = Element(str)
        RENAVAM: str = Element(str, min_occurs=0)
        class prop(ComplexType):
            xNome: str = Element(str)
            IE: str = Element(str)
            UF: TUf = Element(TUf)
            tpProp: str = Element(str)
        prop: prop
        UF: TUf = Element(TUf)
    veic: veic
    class infFretamento(ComplexType):
        tpFretamento: str = Element(str)
        dhViagem: TDateTimeUTC = Element(TDateTimeUTC, min_occurs=0)
    infFretamento: infFretamento

rodoOS: rodoOS
