from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .envCancelPProrrogNFe_v10 import *

from .retEnvCancelPProrrogNFe_v10 import *



class procEventoNFe(ComplexType):

    class evento(ComplexType):
        envEvento: envEvento = Element(envEvento)
    evento: evento = Element(evento)

    class retEvento(ComplexType):
        retEnvEvento: retEnvEvento = Element(retEnvEvento)
    retEvento: retEvento = Element(retEvento)
    versao: str = Attribute(None)

procEventoNFe: procEventoNFe = Element(procEventoNFe)
