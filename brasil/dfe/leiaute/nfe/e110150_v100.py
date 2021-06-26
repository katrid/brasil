from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *



class detEvento(ComplexType):
    """Schema XML de validação do evento de Ator Interessado na NF-e - Transportador (110150)”"""
    descEvento: str = Element(str)
    cOrgaoAutor: TCodUfIBGE = Element(TCodUfIBGE)
    tpAutor: str = Element(str)
    verAplic: TVerAplic = Element(TVerAplic)

    class autXML(ComplexType):
        """Pessoas autorizadas a acessar o XML da NF-e"""
        _choice = [['CNPJ', 'CPF']]
        CNPJ: TCnpj = Element(TCnpj)
        CPF: TCpf = Element(TCpf)
    autXML: autXML = Element(autXML)
    tpAutorizacao: str = Element(str)
    xCondUso: str = Element(str)
    versao: str = Attribute(None)

detEvento: detEvento = Element(detEvento)
