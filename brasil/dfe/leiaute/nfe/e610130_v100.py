from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *



class detEvento(ComplexType):
    """Schema XML de validação do evento de Comprovante de Entrega de CT-e"""
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
        latGPS: TLatitude = Element(TLatitude)
        longGPS: TLongitude = Element(TLongitude)
        hashEntregaCTe: str = Element(str)
        dhHashEntregaCTe: TDateTimeUTC = Element(TDateTimeUTC)
    CTe: CTe = Element(CTe)
    versao: str = Attribute(None)

detEvento: detEvento = Element(detEvento)
