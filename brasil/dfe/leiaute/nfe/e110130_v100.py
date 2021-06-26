from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *



class detEvento(ComplexType):
    """Schema XML de validação do evento de Comprovante de Entrega de NF-e"""
    descEvento: str = Element(str)
    cOrgaoAutor: TCOrgaoIBGE = Element(TCOrgaoIBGE)
    tpAutor: str = Element(str)
    verAplic: TVerAplic = Element(TVerAplic)
    dhEntrega: TDateTimeUTC = Element(TDateTimeUTC)
    nDoc: str = Element(str)
    xNome: str = Element(str)
    latGPS: TLatitude = Element(TLatitude)
    longGPS: TLongitude = Element(TLongitude)
    hashComprovante: str = Element(str)
    dhHashComprovante: TDateTimeUTC = Element(TDateTimeUTC)
    versao: str = Attribute(None)

detEvento: detEvento = Element(detEvento)
