from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposBasico_v310 import *



class TVerEvento(str):
    """Tipo Versão do Evento"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{1,2}\.[0-9]{1,2}", enumeration=[])
    pass



class TCOrgaoIBGE(str):
    """Tipo Código de orgão (UF da tabela do IBGE + 91 RFB)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53', '91'])
    pass



class retEnvEvento(ComplexType):
    idLote: str = Element(str)
    tpAmb: TAmb = Element(TAmb)
    verAplic: TVerAplic = Element(TVerAplic)
    cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE)
    cStat: TStat = Element(TStat)
    xMotivo: TMotivo = Element(TMotivo)

    class retEvento(ComplexType):
        _max_occurs = 20

        def add(self, infEvento=None, versao=None) -> retEnvEvento.retEvento:
            return super().add(infEvento=infEvento, versao=versao)


        class infEvento(ComplexType):
            tpAmb: TAmb = Element(TAmb)
            verAplic: TVerAplic = Element(TVerAplic)
            cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE)
            cStat: TStat = Element(TStat)
            xMotivo: TMotivo = Element(TMotivo)
            chNFe: TChNFe = Element(TChNFe)
            tpEvento: str = Element(str)
            xEvento: str = Element(str)
            nSeqEvento: str = Element(str)
            cOrgaoAutor: TCodUfIBGE = Element(TCodUfIBGE)
            dhRegEvento: TDateTimeUTC = Element(TDateTimeUTC)
            nProt: TProt = Element(TProt)
            chNFePend: List[TChNFe] = Element(TChNFe, max_occurs=50)
            Id: str = Attribute(None)
        infEvento: infEvento = Element(infEvento)
        Signature: Signature = Element(Signature)
        versao: str = Attribute(TVerEvento)
    retEvento: List[retEvento] = Element(retEvento, max_occurs=20)
    versao: str = Attribute(TVerEvento)

retEnvEvento: retEnvEvento = Element(retEnvEvento)
