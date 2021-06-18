from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposBasico_v310 import *


class TVerEvento(str):
    """Versão do Tipo do Evento"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{1,2}\.[0-9]{1,2}", enumeration=[])
    pass


class TCOrgaoIBGE(str):
    """Tipo Código de orgão (UF da tabela do IBGE + 91 RFB)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53', '91'])
    pass


class envEvento(ComplexType):
    idLote: str = Element(str)
    class evento(ComplexType):
        """Evento, um lote pode conter até 20 eventos"""
        class infEvento(ComplexType):
            """Grupo de informações do registro do Evento"""
            cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE)
            tpAmb: TAmb = Element(TAmb)
            chNFe: TChNFe = Element(TChNFe)
            dhEvento: TDateTimeUTC = Element(TDateTimeUTC)
            tpEvento: str = Element(str)
            nSeqEvento: str = Element(str)
            verEvento: TVerEvento = Element(TVerEvento)
            class detEvento(ComplexType):
                """Informações de detalhes do evento"""
                descEvento: str = Element(str)
                cOrgaoAutor: TCodUfIBGE = Element(TCodUfIBGE)
                tpAutor: str = Element(str)
                verAplic: TVerAplic = Element(TVerAplic)
                dhEmi: TDateTimeUTC = Element(TDateTimeUTC)
                tpNF: str = Element(str)
                IE: TIe = Element(TIe)
                class dest(ComplexType):
                    UF: TUf = Element(TUf)
                dest: dest
                vNF: TDec_1302 = Element(TDec_1302)
                vICMS: TDec_1302 = Element(TDec_1302)
                versao: str = Attribute(TVerEvento)
            detEvento: detEvento
            Id: str = Attribute(None)
        infEvento: infEvento
        Signature: Signature = Element(Signature)
        versao: str = Attribute(TVerEvento)
    evento: evento
    versao: str = Attribute(TVerEvento)

envEvento: envEvento
