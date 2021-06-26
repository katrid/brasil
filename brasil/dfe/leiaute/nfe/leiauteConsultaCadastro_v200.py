from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *



class TUfCons(token):
    """Tipo Sigla da UF consultada"""
    _restriction = Restriction(base=r"xs:token", enumeration=['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO', 'SU'])
    pass



class TVerConsCad(token):
    """Tipo Versão do Leiaute da Consulta Cadastro 2.00"""
    _restriction = Restriction(base=r"xs:token", pattern=r"2\.00", enumeration=[])
    pass



class TConsCad(Element):
    """Tipo Pedido de Consulta de cadastro de contribuintes"""

    class infCons(ComplexType):
        """Dados do Pedido de Consulta de cadastro de contribuintes"""
        _choice = [['IE', 'CNPJ', 'CPF']]
        xServ: str = Element(str, documentation=['Serviço Solicitado'])
        UF: TUfCons = Element(TUfCons, documentation=['sigla da UF consultada, utilizar SU para SUFRAMA'])
        IE: TIe = Element(TIe, filter=str.isdigit, documentation=['Inscrição Estadual do contribuinte '])
        CNPJ: TCnpjVar = Element(TCnpjVar, documentation=['CNPJ do contribuinte'])
        CPF: TCpfVar = Element(TCpfVar, documentation=['CPF do contribuinte'])
    infCons: infCons = Element(infCons, documentation=['Dados do Pedido de Consulta de cadastro de contribuintes'])
    versao: str = Attribute(TVerConsCad)



class TEndereco(Element):
    """Tipo Dados do Endereço"""
    xLgr: str = Element(str, documentation=['Logradouro'])
    nro: str = Element(str, documentation=['Número'])
    xCpl: str = Element(str, documentation=['Complemento'])
    xBairro: str = Element(str, documentation=['Bairro'])
    cMun: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do município (utilizar a tabela do IBGE), informar 9999999 para operações com o exterior.'])
    xMun: str = Element(str, documentation=['Nome do município'])
    CEP: str = Element(str, filter=str.isdigit, documentation=['CEP'])



class TRetConsCad(Element):
    """Tipo Retorno Pedido de Consulta de cadastro de contribuintes"""

    class infCons(ComplexType):
        """Dados do Resultado doDados do Pedido de Consulta de cadastro de contribuintes"""
        _choice = [['IE', 'CNPJ', 'CPF']]
        verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que processou o pedido de consulta de cadastro'])
        cStat: TStat = Element(TStat, documentation=['Código do status da mensagem enviada.'])
        xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do serviço solicitado.'])
        UF: TUfCons = Element(TUfCons, documentation=['sigla da UF consultada, utilizar SU para SUFRAMA'])
        IE: TIe = Element(TIe, filter=str.isdigit, documentation=['Inscrição Estadual do contribuinte '])
        CNPJ: TCnpjVar = Element(TCnpjVar, documentation=['CNPJ do contribuinte'])
        CPF: TCpfVar = Element(TCpfVar, documentation=['CPF do contribuinte'])
        dhCons: dateTime = Element(dateTime, documentation=['Data da Consulta'])
        cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['código da UF de atendimento'])

        class infCad(ComplexType):
            """Informações cadastrais do contribuinte consultado"""
            _max_occurs = -1
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

            def add(self, IE=None, CNPJ=None, CPF=None, UF=None, cSit=None, indCredNFe=None, indCredCTe=None, xNome=None, xFant=None, xRegApur=None, CNAE=None, dIniAtiv=None, dUltSit=None, dBaixa=None, IEUnica=None, IEAtual=None, ender=None) -> TRetConsCad.infCons.infCad:
                return super().add(IE=IE, CNPJ=CNPJ, CPF=CPF, UF=UF, cSit=cSit, indCredNFe=indCredNFe, indCredCTe=indCredCTe, xNome=xNome, xFant=xFant, xRegApur=xRegApur, CNAE=CNAE, dIniAtiv=dIniAtiv, dUltSit=dUltSit, dBaixa=dBaixa, IEUnica=IEUnica, IEAtual=IEAtual, ender=ender)

            IE: TIe = Element(TIe, filter=str.isdigit, documentation=['Número da Inscrição Estadual do contribuinte'])
            CNPJ: TCnpjVar = Element(TCnpjVar, documentation=['Número do CNPJ  do contribuinte'])
            CPF: TCpfVar = Element(TCpfVar, documentation=['Número do CPF do contribuinte'])
            UF: TUf = Element(TUf, documentation=['Sigla da UF de localização do contribuinte. Em algumas situações, a UF de localização pode ser diferente da UF consultada. Ex. IE de Substituto Tributário.'])
            cSit: str = Element(str, documentation=['Situação cadastral do contribuinte:\n0 - não habilitado\n1 - habilitado'])
            indCredNFe: str = Element(str, documentation=['Indicador de contribuinte credenciado a emitir NF-e.\n0 - Não credenciado para emissão da NF-e;\n1 - Credenciado;\n2 - Credenciado com obrigatoriedade para todas operações;\n3 - Credenciado com obrigatoriedade parcial;\n4 – a SEFAZ não fornece a informação.\nEste indicador significa apenas que o contribuinte é credenciado para emitir NF-e na SEFAZ consultada.'])
            indCredCTe: str = Element(str, documentation=['Indicador de contribuinte credenciado a emitir CT-e.\n0 - Não credenciado para emissão da CT-e;\n1 - Credenciado;\n2 - Credenciado com obrigatoriedade para todas operações;\n3 - Credenciado com obrigatoriedade parcial;\n4 – a SEFAZ não fornece a informação.\nEste indicador significa apenas que o contribuinte é credenciado para emitir CT-e na SEFAZ consultada.'])
            xNome: str = Element(str, documentation=['Razão Social ou nome do contribuinte'])
            xFant: str = Element(str, documentation=['Razão Social ou nome do contribuinte'])
            xRegApur: str = Element(str, documentation=['Regime de Apuração do ICMS'])
            CNAE: str = Element(str, documentation=['CNAE Fiscal do contribuinte'])
            dIniAtiv: date = Element(date, documentation=['Data de início de atividades do contribuinte'])
            dUltSit: date = Element(date, documentation=['Data da última modificação da situação cadastral do contribuinte.'])
            dBaixa: date = Element(date, documentation=['Data de ocorrência da baixa do contribuinte.'])
            IEUnica: TIe = Element(TIe, filter=str.isdigit, documentation=['Inscrição Estadual Única'])
            IEAtual: TIe = Element(TIe, filter=str.isdigit, documentation=['Inscrição Estadual atual'])
            ender: TEndereco = Element(TEndereco, documentation=['Endereço'])
        infCad: List[infCad] = Element(infCad, max_occurs=-1, documentation=['Informações cadastrais do contribuinte consultado'])
    infCons: infCons = Element(infCons, documentation=['Dados do Resultado doDados do Pedido de Consulta de cadastro de contribuintes'])
    versao: str = Attribute(TVerConsCad)


