from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .cteTiposBasico_v200 import *



class aquav(ComplexType):
    """Informações do modal Aquaviário"""
    vPrest: TDec_1302 = Element(TDec_1302)
    vAFRMM: TDec_1302 = Element(TDec_1302)
    nBooking: str = Element(str)
    nCtrl: str = Element(str)
    xNavio: str = Element(str)

    class balsa(ComplexType):
        """Grupo de informações das balsas"""
        _max_occurs = 3

        def add(self, xBalsa=None) -> aquav.balsa:
            return super().add(xBalsa=xBalsa)

        xBalsa: str = Element(str)
    balsa: List[balsa] = Element(balsa, max_occurs=3)
    nViag: str = Element(str)
    direc: str = Element(str)
    prtEmb: str = Element(str)
    prtTrans: str = Element(str)
    prtDest: str = Element(str)
    tpNav: str = Element(str)
    irin: str = Element(str)

    class detCont(ComplexType):
        """Grupo de informações de detalhamento dos conteiners
(Somente para Redespacho Intermediario)"""
        _max_occurs = -1

        def add(self, nCont=None, lacre=None, infDoc=None) -> aquav.detCont:
            return super().add(nCont=nCont, lacre=lacre, infDoc=infDoc)

        nCont: TContainer = Element(TContainer)

        class lacre(ComplexType):
            """Grupo de informações dos lacres dos cointainers da qtde da carga"""
            _max_occurs = 3

            def add(self, nLacre=None) -> aquav.detCont.lacre:
                return super().add(nLacre=nLacre)

            nLacre: str = Element(str)
        lacre: List[lacre] = Element(lacre, max_occurs=3)

        class infDoc(ComplexType):
            """Informações dos documentos dos conteiners"""
            _choice = [['infNF', 'infNFe']]

            class infNF(ComplexType):
                """Informações das NF"""
                _max_occurs = -1

                def add(self, serie=None, nDoc=None, unidRat=None) -> aquav.detCont.infDoc.infNF:
                    return super().add(serie=serie, nDoc=nDoc, unidRat=unidRat)

                serie: str = Element(str)
                nDoc: str = Element(str)
                unidRat: TDec_0302_0303 = Element(TDec_0302_0303)
            infNF: List[infNF] = Element(infNF, max_occurs=-1)

            class infNFe(ComplexType):
                """Informações das NFe"""
                _max_occurs = -1

                def add(self, chave=None, unidRat=None) -> aquav.detCont.infDoc.infNFe:
                    return super().add(chave=chave, unidRat=unidRat)

                chave: TChNFe = Element(TChNFe)
                unidRat: TDec_0302_0303 = Element(TDec_0302_0303)
            infNFe: List[infNFe] = Element(infNFe, max_occurs=-1)
        infDoc: infDoc = Element(infDoc)
    detCont: List[detCont] = Element(detCont, max_occurs=-1)

aquav: aquav = Element(aquav)
