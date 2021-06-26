from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposDistDFe_v100 import *



class retDistDFeInt(ComplexType):
    """Schema do resultado do pedido de distribuição de DF-e de interesse"""
    tpAmb: TAmb = Element(TAmb)
    verAplic: TVerAplic = Element(TVerAplic)
    cStat: TStat = Element(TStat)
    xMotivo: TMotivo = Element(TMotivo)
    dhResp: str = Element(str)
    ultNSU: TNSU = Element(TNSU)
    maxNSU: TNSU = Element(TNSU)

    class loteDistDFeInt(ComplexType):
        """Conjunto de informações resumidas e documentos fiscais eletrônicos de interesse da pessoa ou empresa."""

        class docZip(ComplexType):
            """Informação resumida ou documento fiscal eletrônico de interesse da pessoa ou empresa. O conteúdo desta tag estará compactado no padrão gZip. O tipo do campo é base64Binary."""
            pass
        docZip: docZip = Element(docZip)
    loteDistDFeInt: loteDistDFeInt = Element(loteDistDFeInt)
    versao: str = Attribute(TVerDistDFe)

retDistDFeInt: retDistDFeInt = Element(retDistDFeInt)
