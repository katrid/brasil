from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposGeralCTe_v200 import *



class TProtCTe(Element):
    """Tipo Protocolo de status resultado do processamento da CT-e"""

    class infProt(ComplexType):
        """Dados do protocolo de status"""
        tpAmb: TAmb = Element(TAmb)
        verAplic: TVerAplic = Element(TVerAplic)
        chCTe: TChNFe = Element(TChNFe)
        dhRecbto: dateTime = Element(dateTime)
        nProt: TProt = Element(TProt)
        digVal: DigestValueType = Element(DigestValueType)
        cStat: str = Element(str)
        xMotivo: TMotivo = Element(TMotivo)
        Id: str = Attribute(ID)
    infProt: infProt = Element(infProt)
    Signature: Signature = Element(Signature)
    versao: str = Attribute(None)



class TVerConsReciCTe(str):
    """Tipo Versão do Consulta Lote de CT-e - 1.04"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"2\.00", enumeration=[])
    pass



class TConsReciCTe(Element):
    """Tipo Pedido de Consulta do Recibo do Lote de CT-e"""
    tpAmb: TAmb = Element(TAmb)
    nRec: TRec = Element(TRec)
    versao: str = Attribute(TVerConsReciCTe)



class TRetConsReciCTe(Element):
    """Tipo Retorno do Pedido de  Consulta do Recibo do Lote de CT-e"""
    tpAmb: TAmb = Element(TAmb)
    verAplic: TVerAplic = Element(TVerAplic)
    nRec: TRec = Element(TRec)
    cStat: TStat = Element(TStat)
    xMotivo: TMotivo = Element(TMotivo)
    cUF: TCodUfIBGE = Element(TCodUfIBGE)
    protCTe: List[TProtCTe] = Element(TProtCTe, max_occurs=50)
    versao: str = Attribute(TVerConsReciCTe)


