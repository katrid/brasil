from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposDistDFe_v100 import *


class retDistDFeInt(ComplexType):
    tpAmb: TAmb = Element(TAmb)
    verAplic: TVerAplic = Element(TVerAplic)
    cStat: TStat = Element(TStat)
    xMotivo: TMotivo = Element(TMotivo)
    dhResp: dateTime = Element(dateTime)
    ultNSU: TNSU = Element(TNSU)
    maxNSU: TNSU = Element(TNSU)
    class loteDistDFeInt(ComplexType):
        class docZip(ComplexType):
            pass
        docZip: docZip
    loteDistDFeInt: loteDistDFeInt
    versao: str = Attribute(TVerDistDFe)

retDistDFeInt: retDistDFeInt
