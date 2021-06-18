from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v200 import *

from .cteTiposBasico_v200 import *


class TRNTRC(str):
    """Tipo RNTRC - Registro Nacional Transportadores Rodoviários de Carga"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{8}|ISENTO", enumeration=[])
    pass


class TPlaca(str):
    """Tipo Placa"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[A-Z]{3}(([1-9]\d{3})|(0[1-9]\d{2})|(00[1-9]\d)|(000[1-9]))", enumeration=[])
    pass


class TCIOT(str):
    """Tipo CIOT - Código Identificador da Operação de Transporte"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{12}", enumeration=[])
    pass


class rodo(ComplexType):
    RNTRC: str = Element(str)
    dPrev: TData = Element(TData)
    lota: str = Element(str)
    CIOT: str = Element(str, min_occurs=0)
    class occ(ComplexType):
        serie: str = Element(str, min_occurs=0)
        nOcc: str = Element(str)
        dEmi: TData = Element(TData)
        class emiOcc(ComplexType):
            CNPJ: TCnpj = Element(TCnpj)
            cInt: str = Element(str, min_occurs=0)
            IE: TIe = Element(TIe)
            UF: TUf = Element(TUf)
            fone: TFone = Element(TFone, min_occurs=0)
        emiOcc: emiOcc
    occ: occ
    class valePed(ComplexType):
        CNPJForn: str = Element(str)
        nCompra: str = Element(str)
        CNPJPg: TCnpjOpc = Element(TCnpjOpc, min_occurs=0)
        vValePed: TDec_1302 = Element(TDec_1302)
    valePed: valePed
    class veic(ComplexType):
        cInt: str = Element(str, min_occurs=0)
        RENAVAM: str = Element(str)
        placa: str = Element(str)
        tara: str = Element(str)
        capKG: str = Element(str)
        capM3: str = Element(str)
        tpProp: str = Element(str)
        tpVeic: str = Element(str)
        tpRod: str = Element(str)
        tpCar: str = Element(str)
        UF: TUf = Element(TUf)
        class prop(ComplexType):
            RNTRC: TRNTRC = Element(TRNTRC)
            xNome: str = Element(str)
            IE: str = Element(str)
            UF: TUf = Element(TUf)
            tpProp: str = Element(str)
        prop: prop
    veic: veic
    class lacRodo(ComplexType):
        nLacre: str = Element(str)
    lacRodo: lacRodo
    class moto(ComplexType):
        xNome: str = Element(str)
        CPF: TCpf = Element(TCpf)
    moto: moto

rodo: rodo
