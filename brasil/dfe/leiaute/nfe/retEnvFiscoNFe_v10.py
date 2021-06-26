from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposBasico_v310 import *



class TCOrgaoIBGE(str):
    """Tipo Código de orgão (UF da tabela do IBGE + 91 RFB)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53', '91'])
    pass



class retEnvEvento(ComplexType):
    """TAG raiz do Resultado do Envio do Evento"""
    idLote: str = Element(str)
    tpAmb: TAmb = Element(TAmb)
    verAplic: TVerAplic = Element(TVerAplic)
    cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE)
    cStat: TStat = Element(TStat)
    xMotivo: TMotivo = Element(TMotivo)

    class retEvento(ComplexType):
        """TAG de grupo do resultado do processamento do Evento"""
        _max_occurs = 20

        def add(self, infEvento=None, versao=None) -> retEnvEvento.retEvento:
            return super().add(infEvento=infEvento, versao=versao)


        class infEvento(ComplexType):
            """Grupo de informações do registro do Evento"""
            tpAmb: TAmb = Element(TAmb)
            verAplic: TVerAplic = Element(TVerAplic)
            cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE)
            cStat: TStat = Element(TStat)
            xMotivo: TMotivo = Element(TMotivo)
            chNFe: List[TChNFe] = Element(TChNFe, max_occurs=1)
            tpEvento: List[str] = Element(str, max_occurs=1)
            xEvento: List[str] = Element(str, max_occurs=1)
            nSeqEvento: List[str] = Element(str, max_occurs=1)
            CNPJDest: List[TCnpjOpc] = Element(TCnpjOpc, max_occurs=1)
            emailDest: List[str] = Element(str, max_occurs=1)
            dhRegEvento: TDateTimeUTC = Element(TDateTimeUTC)
            nProt: List[TProt] = Element(TProt, max_occurs=1)
            Id: str = Attribute(None)
        infEvento: infEvento = Element(infEvento)
        Signature: Signature = Element(Signature)
        versao: str = Attribute(None)
    retEvento: List[retEvento] = Element(retEvento, max_occurs=20)
    versao: str = Attribute(None)

retEnvEvento: retEnvEvento = Element(retEnvEvento)
