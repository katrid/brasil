from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .cteTiposBasico_v400 import *



class aquav(ComplexType):
    """Informações do modal Aquaviário"""
    vPrest: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da Prestação Base de Cálculo do AFRMM'])
    vAFRMM: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['AFRMM (Adicional de Frete para Renovação da Marinha Mercante)'])
    xNavio: str = Element(str, documentation=['Identificação do Navio '])

    class balsa(ComplexType):
        """Grupo de informações das balsas"""
        _max_occurs = 3

        def add(self, xBalsa=None) -> aquav.balsa:
            return super().add(xBalsa=xBalsa)

        xBalsa: str = Element(str, documentation=['Identificador da Balsa'])
    balsa: List[balsa] = Element(balsa, max_occurs=3, documentation=['Grupo de informações das balsas'])
    nViag: str = Element(str, documentation=['Número da Viagem'])
    direc: str = Element(str, documentation=['Direção', 'Preencher com: N-Norte, L-Leste, S-Sul, O-Oeste  '])
    irin: str = Element(str, documentation=['Irin do navio sempre deverá ser informado'])

    class detCont(ComplexType):
        """Grupo de informações de detalhamento dos conteiners 
(Somente para Redespacho Intermediário e Serviço Vinculado a Multimodal)"""
        _max_occurs = -1

        def add(self, nCont=None, lacre=None, infDoc=None) -> aquav.detCont:
            return super().add(nCont=nCont, lacre=lacre, infDoc=infDoc)

        nCont: TContainer = Element(TContainer, documentation=['Identificação do Container'])

        class lacre(ComplexType):
            """Grupo de informações dos lacres dos cointainers da qtde da carga"""
            _max_occurs = 3

            def add(self, nLacre=None) -> aquav.detCont.lacre:
                return super().add(nLacre=nLacre)

            nLacre: str = Element(str, documentation=['Lacre'])
        lacre: List[lacre] = Element(lacre, max_occurs=3, documentation=['Grupo de informações dos lacres dos cointainers da qtde da carga '])

        class infDoc(ComplexType):
            """Informações dos documentos dos conteiners"""
            _choice = [['infNF', 'infNFe']]

            class infNF(ComplexType):
                """Informações das NF"""
                _max_occurs = -1

                def add(self, serie=None, nDoc=None, unidRat=None) -> aquav.detCont.infDoc.infNF:
                    return super().add(serie=serie, nDoc=nDoc, unidRat=unidRat)

                serie: str = Element(str, documentation=['Série'])
                nDoc: str = Element(str, documentation=['Número '])
                unidRat: TDec_0302_0303 = Element(TDec_0302_0303, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Unidade de medida rateada (Peso,Volume)'])
            infNF: List[infNF] = Element(infNF, max_occurs=-1, documentation=['Informações das NF'])

            class infNFe(ComplexType):
                """Informações das NFe"""
                _max_occurs = -1

                def add(self, chave=None, unidRat=None) -> aquav.detCont.infDoc.infNFe:
                    return super().add(chave=chave, unidRat=unidRat)

                chave: TChDFe = Element(TChDFe, documentation=['Chave de acesso da NF-e'])
                unidRat: TDec_0302_0303 = Element(TDec_0302_0303, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Unidade de medida rateada (Peso,Volume)'])
            infNFe: List[infNFe] = Element(infNFe, max_occurs=-1, documentation=['Informações das NFe'])
        infDoc: infDoc = Element(infDoc, documentation=['Informações dos documentos dos conteiners'])
    detCont: List[detCont] = Element(detCont, max_occurs=-1, documentation=['Grupo de informações de detalhamento dos conteiners \n(Somente para Redespacho Intermediário e Serviço Vinculado a Multimodal)'])
    tpNav: str = Element(str, documentation=['Tipo de Navegação', 'Preencher com: \n\t\t\t\t\t\t0 - Interior;\n\t\t\t\t\t\t1 - Cabotagem'])

aquav: aquav = Element(aquav, documentation=['Informações do modal Aquaviário'])
