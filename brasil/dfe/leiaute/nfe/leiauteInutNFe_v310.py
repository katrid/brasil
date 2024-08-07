# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: leiauteInutNFe_v3.10.xsd
# xmlns: http://www.portalfiscal.inf.br/nfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposBasico_v310 import *


class TVerInutNFe(str):
    """Tipo Versão do leiaute de Inutilização 3.10"""
    pass


class TInutNFe(ComplexType):
    """Tipo Pedido de Inutilização de Numeração da Nota Fiscal Eletrônica"""
    versao: Annotated[TVerInutNFe, Attribute] = None

    class _infInut(ComplexType):
        """Dados do Pedido de Inutilização de Numeração da Nota Fiscal Eletrônica"""
        Id: Annotated[str, Attribute(pattern=r'ID[0-9]{41}')] = None
        tpAmb: Annotated[TAmb, Element] = None
        xServ: Annotated[TServ, Element] = None
        cUF: Annotated[TCodUfIBGE, Element] = None
        ano: Annotated[Tano, Element] = None
        CNPJ: Annotated[TCnpj, Element] = None
        mod: Annotated[TMod, Element] = None
        serie: Annotated[TSerie, Element] = None
        nNFIni: Annotated[TNF, Element] = None
        nNFFin: Annotated[TNF, Element] = None
        xJust: Annotated[TJust, Element] = None

    infInut: Annotated[_infInut, Element] = None
    Signature: Annotated[XmlSignature, Element] = None


class TRetInutNFe(ComplexType):
    """Tipo retorno do Pedido de Inutilização de Numeração da Nota Fiscal Eletrônica"""
    versao: Annotated[TVerInutNFe, Attribute] = None

    class _infInut(ComplexType):
        """Dados do Retorno do Pedido de Inutilização de Numeração da Nota Fiscal Eletrônica"""
        Id: Annotated[str, Attribute] = None
        tpAmb: Annotated[TAmb, Element] = None
        verAplic: Annotated[TVerAplic, Element] = None
        cStat: Annotated[TStat, Element] = None
        xMotivo: Annotated[TMotivo, Element] = None
        cUF: Annotated[TCodUfIBGE, Element] = None
        ano: Annotated[Tano, Element] = None
        CNPJ: Annotated[TCnpj, Element] = None
        mod: Annotated[TMod, Element] = None
        serie: Annotated[TSerie, Element] = None
        nNFIni: Annotated[TNF, Element] = None
        nNFFin: Annotated[TNF, Element] = None
        dhRecbto: Annotated[TDateTimeUTC, Element] = None
        nProt: Annotated[TProt, Element] = None

    infInut: Annotated[_infInut, Element] = None
    Signature: Annotated[XmlSignature, Element] = None


class TProcInutNFe(ComplexType):
    """Tipo Pedido de inutilzação de númeração de  NF-e processado"""
    versao: Annotated[TVerInutNFe, Attribute] = None
    inutNFe: Annotated[TInutNFe, Element] = None
    retInutNFe: Annotated[TRetInutNFe, Element] = None


