from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *



class detEvento(ComplexType):
    """Schema XML de validação do evento do cancelamento por substituição 110112"""
    descEvento: str = Element(str, documentation=['Descrição do Evento - “Cancelamento por substituição”'])
    cOrgaoAutor: TCodUfIBGE = Element(TCodUfIBGE, documentation=['Código do Órgão Autor do Evento. Informar o Código da UF para este Evento.'])
    tpAutor: str = Element(str, documentation=['Autor do Evento de Irregularidade FiscalInformar 5=Fisco para este Evento.\n\t\t\t\t\t\t\t\t\t\t\t\t\tValores: 1=Empresa Emitente, 2=Empresa destinatária; 3=Empresa; 5=Fisco;6=RFB; 9=Outros Órgãos;\n\t\t\t\t\t\t'])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que recebeu o Evento'])
    nProt: TProt = Element(TProt, documentation=['Número do Protocolo de Status da NF-e. 1 posição (1 – Secretaria de Fazenda Estadual 2 – Receita Federal); 2 posições ano; 10 seqüencial no ano.'])
    xJust: TJust = Element(TJust, documentation=['Justificativa do cancelamento'])
    chNFeRef: TChNFe = Element(TChNFe, documentation=['Chave de Acesso NF-e vinculada'])
    versao: str = Attribute(None)

detEvento: detEvento = Element(detEvento, documentation=['Schema XML de validação do evento do cancelamento por substituição 110112'])
