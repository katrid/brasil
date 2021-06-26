from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposDistDFe_v100 import *



class TVerResEvento(str):
    """Tipo Versão do leiate resNFe"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1.00'])
    pass



class resEvento(ComplexType):
    """Schema da estrutura XML gerada pelo Ambiente Nacional com o conjunto de informações resumidas de um evento de NF-e"""
    _choice = [['CNPJ', 'CPF']]
    @property
    def CNPJCPF(self):
        return self.CPF or self.CNPJ

    @CNPJCPF.setter
    def CNPJCPF(self, value):
        value = "".join(filter(str.isdigit, value))
        if len(value) == 11:
            self.CPF = value
        else:
            self.CNPJ = value
    cOrgao: TCOrgaoIBGE = Element(TCOrgaoIBGE, documentation=['Código do órgão de recepção do Evento. Utilizar a Tabela do IBGE extendida, utilizar 91 para identificar o Ambiente Nacional'])
    CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do Emitente'])
    CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CPF do Emitente'])
    chNFe: TChNFe = Element(TChNFe, documentation=['Chave de acesso da NF-e'])
    dhEvento: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e Hora do Evento, formato UTC (AAAA-MM-DDThh:mm:ssTZD, onde TZD = +hh:mm ou -hh:mm)'])
    tpEvento: str = Element(str, documentation=['Tipo do Evento'])
    nSeqEvento: str = Element(str, documentation=['Seqüencial do evento para o mesmo tipo de evento.  Para maioria dos eventos será 1, nos casos em que possa existir mais de um evento, como é o caso da carta de correção, o autor do evento deve numerar de forma seqüencial'])
    xEvento: str = Element(str, documentation=['Descrição do Evento'])
    dhRecbto: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e hora de autorização do evento no formato AAAA-MM-DDTHH:MM:SSTZD'])
    nProt: TProt = Element(TProt, documentation=['Número do Protocolo do evento. 1 posição (1 – Secretaria de Fazenda Estadual 2 – Receita Federal); 2 - códiga da UF - 2 posições ano; 10 seqüencial no ano'])
    versao: str = Attribute(TVerResEvento)

resEvento: resEvento = Element(resEvento, documentation=['Schema da estrutura XML gerada pelo Ambiente Nacional com o conjunto de informações resumidas de um evento de NF-e'])
