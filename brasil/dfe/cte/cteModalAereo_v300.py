from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v300 import *


class aereo(ComplexType):
    nMinu: str = Element(str, min_occurs=0)
    nOCA: str = Element(str, min_occurs=0)
    dPrevAereo: TData = Element(TData)
    class natCarga(ComplexType):
        xDime: str = Element(str, min_occurs=0)
        cInfManu: List[str] = Element(str, min_occurs=0, max_occurs=-1)
    natCarga: natCarga
    class tarifa(ComplexType):
        CL: str = Element(str)
        cTar: str = Element(str, min_occurs=0)
        vTar: TDec_1302 = Element(TDec_1302)
    tarifa: tarifa
    class peri(ComplexType):
        nONU: str = Element(str)
        qTotEmb: str = Element(str)
        class infTotAP(ComplexType):
            qTotProd: TDec_1104 = Element(TDec_1104)
            uniAP: str = Element(str)
        infTotAP: infTotAP
    peri: peri

aereo: aereo
