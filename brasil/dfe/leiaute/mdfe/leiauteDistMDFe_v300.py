from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralMDFe_v300 import *



class TVerDFe(str):
    """Tipo Versão"""
    _restriction = Restriction(base=r"xs:string", pattern=r"3\.00", enumeration=[])
    pass



class TDistDFe(Element):
    """Schema XML de validação da área de dados da mensagem da solicitação de distribuição de DF-e"""
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:  1 - Produção  2 - Homologação'])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que solicitou a distribuição de DF-e'])
    indDFe: str = Element(str, documentation=['Indicador de DF-e solicitados: \n0 - DF-e autorizados pela UF; \n1 - DF-e com carregamento na UF; \n2 – DF-e com descarregamento na UF;\n3 – DF-e com percurso pela UF; \n8 – DF-e carregados  (1), descarregados (2)  e que tiveram percurso na UF (3);\n9 - Todos DF-e que fazem referência a UF.\n'])
    indCompRet: str = Element(str, documentation=['Indicador de Compactação da Mensagem de retorno:  0 - sem compactação;  1 - compactação padrão gZip'])
    ultNSU: TNSU = Element(TNSU, documentation=['último NSU recebido, caso seja informado com zero, o Ambiente Autorizador tentará localizar o primeiro DF-e existente.'])
    versao: str = Attribute(TVerDFe)



class TVerDFe(str):
    """Tipo Versão"""
    _restriction = Restriction(base=r"xs:string", pattern=r"3\.00", enumeration=[])
    pass



class TLoteDistDFe(Element):
    """Schema XML de validação da área de dados descompactada"""

    class proc(ComplexType):
        schema: str = Attribute(string)
        NSU: str = Attribute(TNSU)
        ipTransmissor: str = Attribute(TIPv4)
    proc: proc = Element(proc)
    versao: str = Attribute(TVerDFe)



class TRetDistDFe(Element):
    """Schema XML de validação do lote de retorno de documentos ficais eletronicos"""
    _choice = [['loteDistMDFeComp', 'loteDistMDFe']]
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:  1 - Produção  2 - Homologação'])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que atendeu a pedido de distribuição de DF-e'])
    cStat: TStat = Element(TStat, documentation=['código do status de resultado da pesquisa'])
    xMotivo: TMotivo = Element(TMotivo, documentation=['descrição do resultado do pesquisa '])
    ultNSU: TNSU = Element(TNSU, documentation=['último NSU'])
    loteDistMDFeComp: base64Binary = Element(base64Binary)
    loteDistMDFe: TLoteDistDFe = Element(TLoteDistDFe)
    versao: str = Attribute(TVerDFe)


