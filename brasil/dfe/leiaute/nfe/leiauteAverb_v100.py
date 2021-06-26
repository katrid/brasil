from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposBasico_v103 import *



class TVerEvento(str):
    """Tipo Versão do Evento"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"1.00", enumeration=[])
    pass



class TEvento(Element):
    """Tipo Evento"""

    class infEvento(ComplexType):
        cOrgao: str = Element(str)
        tpAmb: TAmb = Element(TAmb)
        CNPJ: TCnpj = Element(TCnpj)
        chNFe: TChNFe = Element(TChNFe)
        dhEvento: TDateTimeUTC = Element(TDateTimeUTC)
        tpEvento: str = Element(str)
        nSeqEvento: str = Element(str)
        verEvento: str = Element(str)

        class detEvento(ComplexType):
            """Schema XML de validação do evento de averbação da NFe (e790700)"""
            descEvento: str = Element(str)
            tpAutor: str = Element(str)
            verAplic: TVerAplic = Element(TVerAplic)

            class itensAverbados(ComplexType):
                """Informações dos itens da NF-e do evento."""
                _min_occurs = 1
                _max_occurs = 990

                def add(self, dhEmbarque=None, dhAverbacao=None, nDue=None, nItem=None, nItemDue=None, qItem=None, motAlteracao=None) -> TEvento.infEvento.detEvento.itensAverbados:
                    return super().add(dhEmbarque=dhEmbarque, dhAverbacao=dhAverbacao, nDue=nDue, nItem=nItem, nItemDue=nItemDue, qItem=qItem, motAlteracao=motAlteracao)

                dhEmbarque: TDateTimeUTC = Element(TDateTimeUTC)
                dhAverbacao: TDateTimeUTC = Element(TDateTimeUTC)
                nDue: str = Element(str)
                nItem: str = Element(str)
                nItemDue: str = Element(str)
                qItem: TDec_1104Neg = Element(TDec_1104Neg, tipo="N", tam=(11, 4))
                motAlteracao: str = Element(str)
            itensAverbados: List[itensAverbados] = Element(itensAverbados, min_occurs=1, max_occurs=990)
            versao: str = Attribute(None)
        detEvento: detEvento = Element(detEvento)
        Id: str = Attribute(None)
    infEvento: infEvento = Element(infEvento)
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerEvento)



class TCOrgaoIBGE(str):
    """Tipo Código de orgão (UF da tabela do IBGE)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53', '90', '91'])
    pass



class TretEvento(Element):
    """Tipo retorno do Evento"""

    class infEvento(ComplexType):
        _choice = [['CNPJDest', 'CPFDest']]
        tpAmb: TAmb = Element(TAmb)
        verAplic: TVerAplic = Element(TVerAplic)
        cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE)
        cStat: TStat = Element(TStat)
        xMotivo: TMotivo = Element(TMotivo)
        chNFe: TChNFe = Element(TChNFe)
        tpEvento: str = Element(str)
        xEvento: str = Element(str)
        nSeqEvento: str = Element(str)
        CNPJDest: TCnpjOpc = Element(TCnpjOpc)
        CPFDest: TCpf = Element(TCpf)
        emailDest: str = Element(str)
        dhRegEvento: str = Element(str)
        nProt: TProt = Element(TProt)
        Id: str = Attribute(None)
    infEvento: infEvento = Element(infEvento)
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerEvento)



class TVerEnvEvento(str):
    """Tipo Versão do EnvEvento"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"1.00", enumeration=[])
    pass



class TEnvEvento(Element):
    """Tipo Lote de Envio"""
    idLote: str = Element(str)
    evento: List[TEvento] = Element(TEvento, max_occurs=20)
    versao: str = Attribute(TVerEnvEvento)



class TRetEnvEvento(Element):
    """Tipo Retorno de Lote de Envio"""
    idLote: str = Element(str)
    tpAmb: TAmb = Element(TAmb)
    verAplic: TVerAplic = Element(TVerAplic)
    cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE)
    cStat: TStat = Element(TStat)
    xMotivo: TMotivo = Element(TMotivo)
    retEvento: List[TretEvento] = Element(TretEvento, max_occurs=20)
    versao: str = Attribute(TVerEnvEvento)



class TProcEvento(Element):
    """Tipo procEvento"""
    evento: TEvento = Element(TEvento)
    retEvento: TretEvento = Element(TretEvento)
    versao: str = Attribute(TVerEvento)


