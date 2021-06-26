from __future__ import annotations
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
        xServ: str = Element(str)
        UF: TUfCons = Element(TUfCons)
        IE: TIe = Element(TIe)
        CNPJ: TCnpjVar = Element(TCnpjVar)
        CPF: TCpfVar = Element(TCpfVar)
    infCons: infCons = Element(infCons)
    versao: str = Attribute(TVerConsCad)



class TEndereco(Element):
    """Tipo Dados do Endereço"""
    xLgr: str = Element(str)
    nro: str = Element(str)
    xCpl: str = Element(str)
    xBairro: str = Element(str)
    cMun: TCodMunIBGE = Element(TCodMunIBGE)
    xMun: str = Element(str)
    CEP: str = Element(str)



class TRetConsCad(Element):
    """Tipo Retorno Pedido de Consulta de cadastro de contribuintes"""

    class infCons(ComplexType):
        """Dados do Resultado doDados do Pedido de Consulta de cadastro de contribuintes"""
        _choice = [['IE', 'CNPJ', 'CPF']]
        verAplic: TVerAplic = Element(TVerAplic)
        cStat: TStat = Element(TStat)
        xMotivo: TMotivo = Element(TMotivo)
        UF: TUfCons = Element(TUfCons)
        IE: TIe = Element(TIe)
        CNPJ: TCnpjVar = Element(TCnpjVar)
        CPF: TCpfVar = Element(TCpfVar)
        dhCons: dateTime = Element(dateTime)
        cUF: TCodUfIBGE = Element(TCodUfIBGE)

        class infCad(ComplexType):
            """Informações cadastrais do contribuinte consultado"""
            _max_occurs = -1
            _choice = [['CNPJ', 'CPF']]

            def add(self, IE=None, CNPJ=None, CPF=None, UF=None, cSit=None, indCredNFe=None, indCredCTe=None, xNome=None, xFant=None, xRegApur=None, CNAE=None, dIniAtiv=None, dUltSit=None, dBaixa=None, IEUnica=None, IEAtual=None, ender=None) -> TRetConsCad.infCons.infCad:
                return super().add(IE=IE, CNPJ=CNPJ, CPF=CPF, UF=UF, cSit=cSit, indCredNFe=indCredNFe, indCredCTe=indCredCTe, xNome=xNome, xFant=xFant, xRegApur=xRegApur, CNAE=CNAE, dIniAtiv=dIniAtiv, dUltSit=dUltSit, dBaixa=dBaixa, IEUnica=IEUnica, IEAtual=IEAtual, ender=ender)

            IE: TIe = Element(TIe)
            CNPJ: TCnpjVar = Element(TCnpjVar)
            CPF: TCpfVar = Element(TCpfVar)
            UF: TUf = Element(TUf)
            cSit: str = Element(str)
            indCredNFe: str = Element(str)
            indCredCTe: str = Element(str)
            xNome: str = Element(str)
            xFant: str = Element(str)
            xRegApur: str = Element(str)
            CNAE: str = Element(str)
            dIniAtiv: date = Element(date)
            dUltSit: date = Element(date)
            dBaixa: date = Element(date)
            IEUnica: TIe = Element(TIe)
            IEAtual: TIe = Element(TIe)
            ender: TEndereco = Element(TEndereco)
        infCad: List[infCad] = Element(infCad, max_occurs=-1)
    infCons: infCons = Element(infCons)
    versao: str = Attribute(TVerConsCad)


