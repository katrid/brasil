from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposBasico_v103 import *



class TVerEvento(str):
    """Tipo Versão do Evento"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"1\.00", enumeration=[])
    pass



class TCOrgaoIBGE(str):
    """Tipo Código de orgão (UF da tabela do IBGE + 91 RFB)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53', '91'])
    pass



class TEvento(Element):
    """Tipo Evento"""

    class infEvento(ComplexType):
        _choice = [['CNPJ', 'CPF']]
        cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE)
        tpAmb: TAmb = Element(TAmb)
        CNPJ: TCnpjOpc = Element(TCnpjOpc)
        CPF: TCpf = Element(TCpf)
        chNFe: TChNFe = Element(TChNFe)
        dhEvento: TDateTimeUTC = Element(TDateTimeUTC)
        tpEvento: str = Element(str)
        nSeqEvento: str = Element(str)
        verEvento: str = Element(str)

        class detEvento(ComplexType):
            """Schema XML de validação do evento de emissão prévia em contingência - 110140"""
            descEvento: descEvento = Element(descEvento)
            cOrgaoAutor: cOrgaoAutor = Element(cOrgaoAutor)
            tpAutor: tpAutor = Element(tpAutor)
            verAplic: verAplic = Element(verAplic)
            dhEmi: dhEmi = Element(dhEmi)
            tpNF: tpNF = Element(tpNF)
            IE: IE = Element(IE)

            class dest(ComplexType):
                _choice = [['CNPJ', 'CPF', 'idEstrangeiro']]
                UF: UF = Element(UF)
                CNPJ: TCnpj = Element(TCnpj)
                CPF: TCpf = Element(TCpf)
                idEstrangeiro: str = Element(str)
                IE: IE = Element(IE)
                vNF: vNF = Element(vNF)
                vICMS: vICMS = Element(vICMS)
                vST: vST = Element(vST)
            dest: dest = Element(dest)
            versao: str = Attribute(None)
        detEvento: detEvento = Element(detEvento)
        Id: str = Attribute(None)
    infEvento: infEvento = Element(infEvento)
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerEvento)



class TRetEvento(Element):
    """Tipo retorno do Evento"""

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
        cOrgaoAutor: cOrgaoAutor = Element(cOrgaoAutor)
        dhRegEvento: str = Element(str)
        nProt: TProt = Element(TProt)
        chNFePend: List[TChNFe] = Element(TChNFe, max_occurs=50)
        Id: str = Attribute(None)
    infEvento: infEvento = Element(infEvento)
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerEvento)



class TVerEnvEvento(str):
    """Tipo Versão do EnvEvento"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"1\.00", enumeration=[])
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
    retEvento: List[TRetEvento] = Element(TRetEvento, max_occurs=20)
    versao: str = Attribute(TVerEnvEvento)



class TProcEvento(Element):
    """Tipo procEvento"""
    evento: TEvento = Element(TEvento)
    retEvento: TRetEvento = Element(TRetEvento)
    versao: str = Attribute(TVerEvento)


class descEvento(str):
    pass

class tpAutor(str):
    pass

class verAplic(TVerAplic):
    pass

class dhEmi(TDateTimeUTC):
    pass

class tpNF(str):
    pass

class cOrgaoAutor(TCodUfIBGE):
    pass

class IE(str):
    pass

class UF(TUf):
    pass

class vNF(TDec_1302):
    pass

class vICMS(TDec_1302):
    pass

class vST(TDec_1302):
    pass

