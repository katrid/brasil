from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v300 import *



class aereo(ComplexType):
    """Informações do modal Aéreo"""
    nMinu: str = Element(str)
    nOCA: str = Element(str)
    dPrevAereo: TData = Element(TData)

    class natCarga(ComplexType):
        """Natureza da carga"""
        xDime: str = Element(str)
        cInfManu: List[str] = Element(str, max_occurs=-1)
    natCarga: natCarga = Element(natCarga)

    class tarifa(ComplexType):
        """Informações de tarifa"""
        CL: str = Element(str)
        cTar: str = Element(str)
        vTar: TDec_1302 = Element(TDec_1302)
    tarifa: tarifa = Element(tarifa)

    class peri(ComplexType):
        """Preenchido quando for  transporte de produtos classificados pela ONU como perigosos.
O preenchimento desses campos não desobriga a empresa aérea de emitir os demais documentos que constam na legislação vigente."""
        _max_occurs = -1

        def add(self, nONU=None, qTotEmb=None, infTotAP=None) -> aereo.peri:
            return super().add(nONU=nONU, qTotEmb=qTotEmb, infTotAP=infTotAP)

        nONU: str = Element(str)
        qTotEmb: str = Element(str)

        class infTotAP(ComplexType):
            """Grupo de informações das quantidades totais de artigos perigosos
Preencher conforme a legislação de transporte de produtos perigosos aplicada ao modal"""
            qTotProd: TDec_1104 = Element(TDec_1104)
            uniAP: str = Element(str)
        infTotAP: infTotAP = Element(infTotAP)
    peri: List[peri] = Element(peri, max_occurs=-1)

aereo: aereo = Element(aereo)
