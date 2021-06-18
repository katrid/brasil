from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v200 import *


class aereo(ComplexType):
    nMinu: str = Element(str, min_occurs=0)
    nOCA: str = Element(str, min_occurs=0)
    dPrevAereo: TData = Element(TData)
    xLAgEmi: str = Element(str, min_occurs=0)
    IdT: str = Element(str, min_occurs=0)
    class tarifa(ComplexType):
        CL: str = Element(str)
        cTar: str = Element(str, min_occurs=0)
        vTar: TDec_1302 = Element(TDec_1302)
    tarifa: tarifa
    class natCarga(ComplexType):
        xDime: str = Element(str, min_occurs=0)
        cInfManu: List[str] = Element(str, min_occurs=0, max_occurs=-1)
        cIMP: List[str] = Element(str, max_occurs=-1)
    natCarga: natCarga

aereo: aereo
