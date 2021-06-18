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
        """TAG de grupo do resultado do processamento do Evento"""
        class infEvento(ComplexType):
            """Grupo de informações do registro do Evento"""
            tpAmb: TAmb = Element(TAmb)
            verAplic: TVerAplic = Element(TVerAplic)
            cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE)
            cStat: TStat = Element(TStat)
            xMotivo: TMotivo = Element(TMotivo)
            chNFe: TChNFe = Element(TChNFe, min_occurs=0)
            tpEvento: str = Element(str, min_occurs=0)
            xEvento: str = Element(str, min_occurs=0)
            nSeqEvento: str = Element(str, min_occurs=0)
            cOrgaoAutor: TCodUfIBGE = Element(TCodUfIBGE, min_occurs=0)
            dhRegEvento: TDateTimeUTC = Element(TDateTimeUTC)
            nProt: TProt = Element(TProt, min_occurs=0)
            chNFePend: List[TChNFe] = Element(TChNFe, min_occurs=0, max_occurs=50)
            Id: str = Attribute(None)
        infEvento: infEvento
        Signature: Signature = Element(Signature, min_occurs=0)
        versao: str = Attribute(TVerEvento)
    retEvento: retEvento
    versao: str = Attribute(TVerEvento)

retEnvEvento: retEnvEvento
