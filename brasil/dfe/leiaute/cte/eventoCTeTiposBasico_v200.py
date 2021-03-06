from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposGeralCTe_v200 import *



class TVerEvento(str):
    """Tipo Versão do Evento"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"2\.00", enumeration=[])
    pass



class TEvento(Element):
    """Tipo Evento"""

    class infEvento(ComplexType):
        cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE, documentation=['Código do órgão de recepção do Evento. Utilizar a Tabela do IBGE extendida, utilizar 90 para identificar SUFRAMA'])
        tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
        CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do emissor do evento'])
        chCTe: TChNFe = Element(TChNFe, documentation=['Chave de Acesso do CT-e vinculado ao evento'])
        dhEvento: str = Element(str, documentation=['Data e Hora do Evento, formato UTC (AAAA-MM-DDThh:mm:ss)'])
        tpEvento: str = Element(str, documentation=['Tipo do Evento'])
        nSeqEvento: str = Element(str, documentation=['Seqüencial do evento para o mesmo tipo de evento.  Para maioria dos eventos será 1, nos casos em que possa existir mais de um evento o autor do evento deve numerar de forma seqüencial.'])

        class detEvento(ComplexType):
            """Detalhamento do evento específico"""
            versaoEvento: str = Attribute(None)
        detEvento: detEvento = Element(detEvento, documentation=['Detalhamento do evento específico'])
        Id: str = Attribute(None)
    infEvento: infEvento = Element(infEvento)
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerEvento)



class TRetEvento(Element):
    """Tipo retorno do Evento"""

    class infEvento(ComplexType):
        tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
        verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que recebeu o Evento'])
        cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE, documentation=['Código do órgão de recepção do Evento. Utilizar a Tabela do IBGE extendida, utilizar 90 para identificar SUFRAMA'])
        cStat: TStat = Element(TStat, documentation=['Código do status da registro do Evento'])
        xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do registro do Evento'])
        chCTe: TChNFe = Element(TChNFe, documentation=['Chave de Acesso CT-e vinculado'])
        tpEvento: str = Element(str, documentation=['Tipo do Evento vinculado'])
        xEvento: str = Element(str, documentation=['Descrição do Evento'])
        nSeqEvento: str = Element(str, documentation=['Seqüencial do evento'])
        dhRegEvento: str = Element(str, documentation=['Data e Hora de do recebimento do evento ou do registro do evento formato AAAA-MM-DDThh:mm:ss'])
        nProt: TProt = Element(TProt, documentation=['Número do protocolo de registro do evento'])
        Id: str = Attribute(None)
    infEvento: infEvento = Element(infEvento)
    Signature: Signature = Element(Signature)
    versao: str = Attribute(None)



class TProcEvento(Element):
    """Tipo procEvento"""
    eventoCTe: TEvento = Element(TEvento)
    retEventoCTe: TRetEvento = Element(TRetEvento)
    versao: str = Attribute(TVerEvento)



class TModTransp(str):
    """Tipo Modal transporte"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['01', '02', '03', '04', '05', '06'])
    pass



class TNSU(str):
    """Tipo número sequencial único do AN"""
    _restriction = Restriction(base=r"xs:string", pattern=r"[0-9]{15}", enumeration=[])
    pass



class TPlaca(str):
    """Tipo Placa"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[A-Z]{2,3}[0-9]{4}|[A-Z]{3,4}[0-9]{3}", enumeration=[])
    pass


