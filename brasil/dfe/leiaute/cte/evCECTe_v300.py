from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v300 import *



class evCECTe(ComplexType):
    """Schema XML de validação do evento comprovante de entrega eletrônico do CT-e 
110180"""
    descEvento: str = Element(str)
    nProt: TProt = Element(TProt)
    dhEntrega: str = Element(str)
    nDoc: str = Element(str)
    xNome: str = Element(str)
    latitude: TLatitude = Element(TLatitude)
    longitude: TLongitude = Element(TLongitude)
    hashEntrega: str = Element(str)
    dhHashEntrega: str = Element(str)

    class infEntrega(ComplexType):
        """Grupo de informações das NF-e que foram entregues ao Destinatário
Informar o grupo apenas para CT-e com tipo de serviço Normal"""
        _max_occurs = 2000

        def add(self, chNFe=None) -> evCECTe.infEntrega:
            return super().add(chNFe=chNFe)

        chNFe: TChNFe = Element(TChNFe)
    infEntrega: List[infEntrega] = Element(infEntrega, max_occurs=2000)

evCECTe: evCECTe = Element(evCECTe)
