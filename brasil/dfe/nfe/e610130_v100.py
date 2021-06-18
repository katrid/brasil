from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *


class detEvento(ComplexType):
    descEvento: str = Element(str)
    cOrgaoAutor: TCOrgaoIBGE = Element(TCOrgaoIBGE)
    tpAutor: str = Element(str)
    verAplic: TVerAplic = Element(TVerAplic)
    class CTe(ComplexType):
        chCTe: str = Element(str)
        nProtCTe: str = Element(str)
        dhEntrega: TDateTimeUTC = Element(TDateTimeUTC)
        nDoc: str = Element(str)
        xNome: str = Element(str)
        latGPS: TLatitude = Element(TLatitude, min_occurs=0)
        longGPS: TLongitude = Element(TLongitude, min_occurs=0)
        hashEntregaCTe: str = Element(str)
        dhHashEntregaCTe: TDateTimeUTC = Element(TDateTimeUTC, min_occurs=0)
    CTe: CTe
    versao: str = Attribute(None)

detEvento: detEvento
