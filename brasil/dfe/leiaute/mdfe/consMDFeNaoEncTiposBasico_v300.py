from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralMDFe_v300 import *

from .xmldsig_core_schema_v101 import *



class TConsMDFeNaoEnc(Element):
    """Tipo Pedido de Consulta MDF-e Não Encerrados
Identificação do emitente"""
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
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    xServ: TServ = Element(TServ, documentation=['Serviço Solicitado'])
    CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do emitente do MDF-e', 'Informar zeros não significativos'])
    CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CPF do emitente do MDF-e', 'Informar zeros não significativos\nUsar com serie específica 920-969 para emitente pessoa física com inscrição estadual'])
    versao: str = Attribute(None)



class TVerConsMDFeNaoEnc(str):
    """Tipo Versão do Consulta MDF-e não encerrados - 3.00"""
    _restriction = Restriction(base=r"xs:string", pattern=r"3\.00", enumeration=[])
    pass



class TRetConsMDFeNaoEnc(Element):
    """Tipo Retorno de Pedido de Consulta MDF-e não Encerrados"""
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que processou o MDF-e'])
    cStat: TStat = Element(TStat, documentation=['Código do status da mensagem enviada.'])
    xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do serviço solicitado.'])
    cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['código da UF de atendimento'])

    class infMDFe(ComplexType):
        _max_occurs = -1

        def add(self, chMDFe=None, nProt=None) -> TRetConsMDFeNaoEnc.infMDFe:
            return super().add(chMDFe=chMDFe, nProt=nProt)

        chMDFe: TChMDFe = Element(TChMDFe, documentation=['Chaves de acesso do MDF-e não encerrado'])
        nProt: TProt = Element(TProt, documentation=['Número do Protocolo de autorização do MDF-e não encerrado'])
    infMDFe: List[infMDFe] = Element(infMDFe, max_occurs=-1)
    versao: str = Attribute(TVerConsMDFeNaoEnc)


