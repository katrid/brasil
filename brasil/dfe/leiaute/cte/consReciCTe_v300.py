from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .consReciCTeTiposBasico_v300 import *


class consReciCTe(TConsReciCTe):
    pass


class retConsReciCTe(TRetConsReciCTe):
    pass

