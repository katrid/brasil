from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoMDFeTiposBasico_v300 import *



class evIncDFeMDFe(ComplexType):
    """Schema XML de validação do evento de inclusão de DFe 
110115"""
    descEvento: str = Element(str, documentation=['Descrição do Evento - “Inclusão DF-e”'])
    nProt: TProt = Element(TProt, documentation=['Número do Protocolo de Status do MDF-e. \n1 posição tipo de autorizador (9 - SEFAZ Nacional ); \n2 posições ano;\n10 seqüencial no ano.'])
    cMunCarrega: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do Município de Carregamento'])
    xMunCarrega: str = Element(str, documentation=['Nome do Município de Carregamento'])

    class infDoc(ComplexType):
        """Informações dos Documentos fiscais vinculados ao manifesto"""
        _max_occurs = -1

        def add(self, cMunDescarga=None, xMunDescarga=None, chNFe=None) -> evIncDFeMDFe.infDoc:
            return super().add(cMunDescarga=cMunDescarga, xMunDescarga=xMunDescarga, chNFe=chNFe)

        cMunDescarga: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do Município de Descarregamento'])
        xMunDescarga: str = Element(str, documentation=['Nome do Município de Descarregamento'])
        chNFe: TChNFe = Element(TChNFe, documentation=['Nota Fiscal Eletrônica'])
    infDoc: List[infDoc] = Element(infDoc, max_occurs=-1, documentation=['Informações dos Documentos fiscais vinculados ao manifesto'])

evIncDFeMDFe: evIncDFeMDFe = Element(evIncDFeMDFe, documentation=['Schema XML de validação do evento de inclusão de DFe \n110115'])
