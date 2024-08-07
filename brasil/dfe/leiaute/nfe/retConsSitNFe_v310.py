# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: retConsSitNFe_v3.10.xsd
# xmlns: http://www.portalfiscal.inf.br/nfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .leiauteConsSitNFe_v310 import *


class retConsSitNFe(TRetConsSitNFe):
    """Schema XML de validação do retorno da consulta da situação atual da NF-e"""
    _xmlns = "http://www.portalfiscal.inf.br/nfe"


