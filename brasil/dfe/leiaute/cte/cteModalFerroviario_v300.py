from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v300 import *

from .cteTiposBasico_v300 import *



class TEnderFer(Element):
    """Tipo Dados do Endereço"""
    xLgr: str = Element(str, documentation=['Logradouro'])
    nro: str = Element(str, documentation=['Número'])
    xCpl: str = Element(str, documentation=['Complemento'])
    xBairro: str = Element(str, documentation=['Bairro'])
    cMun: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do município', ' Utilizar a tabela do IBGE\n\t\t\t\t\tInformar 9999999 para operações com o exterior.'])
    xMun: str = Element(str, documentation=['Nome do município', 'Informar EXTERIOR para operações com o exterior.'])
    CEP: str = Element(str, filter=str.isdigit, documentation=['CEP'])
    UF: TUf = Element(TUf, documentation=['Sigla da UF', 'Informar EX para operações com o exterior.'])



class ferrov(ComplexType):
    """Informações do modal Ferroviário"""
    tpTraf: str = Element(str, documentation=['Tipo de Tráfego', 'Preencher com:\n\t\t\t\t\t\t0-Próprio;\n\t\t\t\t\t\t1-Mútuo;\n\t\t\t\t\t\t2-Rodoferroviário;\n\t\t\t\t\t\t3-Rodoviário.'])

    class trafMut(ComplexType):
        """Detalhamento de informações para o tráfego mútuo"""
        respFat: str = Element(str, documentation=['Responsável pelo Faturamento', 'Preencher com: \n\t\t\t\t\t\t\t\t\t1-Ferrovia de origem; \n\t\t\t\t\t\t\t\t\t2-Ferrovia de destino'])
        ferrEmi: str = Element(str, documentation=['Ferrovia Emitente do CTe', 'Preencher com: \n\t\t\t\t\t\t\t\t\t1-Ferrovia de origem; \n\t\t\t\t\t\t\t\t\t2-Ferrovia de destino'])
        vFrete: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), documentation=['Valor do Frete do Tráfego Mútuo'])
        chCTeFerroOrigem: TChNFe = Element(TChNFe, documentation=['Chave de acesso do CT-e emitido pelo ferrovia de origem'])

        class ferroEnv(ComplexType):
            """Informações das Ferrovias Envolvidas"""
            _max_occurs = -1

            def add(self, CNPJ=None, cInt=None, IE=None, xNome=None, enderFerro=None) -> ferrov.trafMut.ferroEnv:
                return super().add(CNPJ=CNPJ, cInt=cInt, IE=IE, xNome=xNome, enderFerro=enderFerro)

            CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['Número do CNPJ', 'Informar o CNPJ da Ferrovia Envolvida. Caso a Ferrovia envolvida não seja inscrita no CNPJ o campo deverá preenchido com zeros.\nInformar os zeros não significativos.'])
            cInt: str = Element(str, documentation=['Código interno da Ferrovia envolvida', 'Uso da transportadora'])
            IE: TIe = Element(TIe, filter=str.isdigit, documentation=['Inscrição Estadual'])
            xNome: str = Element(str, documentation=['Razão Social ou Nome'])
            enderFerro: TEnderFer = Element(TEnderFer, documentation=['Dados do endereço da ferrovia envolvida'])
        ferroEnv: List[ferroEnv] = Element(ferroEnv, max_occurs=-1, documentation=['Informações das Ferrovias Envolvidas'])
    trafMut: trafMut = Element(trafMut, documentation=['Detalhamento de informações para o tráfego mútuo'])
    fluxo: str = Element(str, documentation=['Fluxo Ferroviário', 'Trata-se de um número identificador do contrato firmado com o cliente '])

ferrov: ferrov = Element(ferrov, documentation=['Informações do modal Ferroviário'])
