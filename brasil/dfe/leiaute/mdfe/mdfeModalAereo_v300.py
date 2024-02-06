from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralMDFe_v300 import *



class aereo(ComplexType):
    """Informações do modal Aéreo"""
    nac: str = Element(str, documentation=['Marca da Nacionalidade da aeronave'])
    matr: str = Element(str, documentation=['Marca de Matrícula da aeronave'])
    nVoo: str = Element(str, documentation=['Número do Voo', 'Formato = AB1234, sendo AB a designação da empresa e 1234 o número do voo. Quando não for possível incluir as marcas de nacionalidade e matrícula sem hífen.\n'])
    cAerEmb: str = Element(str, documentation=['Aeródromo de Embarque', 'O código de três letras IATA do aeroporto de partida deverá ser incluído como primeira anotação. Quando não for possível, utilizar a sigla OACI.'])
    cAerDes: str = Element(str, documentation=['Aeródromo de Destino', 'O código de três letras IATA do aeroporto de destino deverá ser incluído como primeira anotação. Quando não for possível, utilizar a sigla OACI.'])
    dVoo: TData = Element(TData, base_type=date, documentation=['Data do Voo', 'Formato AAAA-MM-DD'])

aereo: aereo = Element(aereo, documentation=['Informações do modal Aéreo'])
