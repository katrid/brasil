from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *


class detEvento(ComplexType):
    descEvento: str = Element(str)
    cOrgaoAutor: TCOrgaoIBGE = Element(TCOrgaoIBGE)
    tpAutor: str = Element(str)
    verAplic: TVerAplic = Element(TVerAplic)
    dhEntrega: TDateTimeUTC = Element(TDateTimeUTC)
    nDoc: str = Element(str)
    xNome: str = Element(str)
    latGPS: TLatitude = Element(TLatitude, min_occurs=0)
    longGPS: TLongitude = Element(TLongitude, min_occurs=0)
    hashComprovante: str = Element(str)
    dhHashComprovante: TDateTimeUTC = Element(TDateTimeUTC, min_occurs=0)
    versao: str = Attribute(None)

detEvento: detEvento
