from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v400 import *



class evEPECCTe(ComplexType):
    """Schema XML de validação do evento de emissão prévia de emissão em contingência 
110113"""
    descEvento: str = Element(str, documentation=['Descrição do Evento - “EPEC”'])
    xJust: TJust = Element(TJust, documentation=['Justificativa da Entrada em Contingencia'])
    vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS'])
    vICMSST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS ST'])
    vTPrest: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Total da Prestação do Serviço', 'Pode conter zeros quando o CT-e for de complemento de ICMS'])
    vCarga: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor total da carga', 'Dever ser informado para todos os modais, com exceção para o Dutoviário.'])

    class toma4(ComplexType):
        """Indicador do \"papel\" do tomador do serviço no CT-e"""
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
        toma: str = Element(str, documentation=['Tomador do Serviço', 'Preencher com: \n0-Remetente;\n1-Expedidor;2-Recebedor;3-Destinatário\n;4 - Outros'])
        UF: TUf = Element(TUf, documentation=['UF do tomador do serviço', "Informar 'EX' para operações com o exterior."])
        CNPJ: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['Número do CNPJ', 'Em caso de empresa não estabelecida no Brasil, será informado o CNPJ com zeros.\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\nInformar os zeros não significativos.'])
        CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['Número do CPF', 'Informar os zeros não significativos.'])
        IE: TIeDest = Element(TIeDest, filter=str.isdigit, documentation=['Inscrição Estadual', 'Informar a IE do tomador ou ISENTO se tomador é contribuinte do ICMS isento de inscrição no cadastro de contribuintes do ICMS. Caso o tomador não seja contribuinte do ICMS não informar o conteúdo.'])
    toma4: toma4 = Element(toma4, documentation=['Indicador do "papel" do tomador do serviço no CT-e'])
    modal: TModTransp = Element(TModTransp, documentation=['Modal', 'Preencher com:\n \n01-Rodoviário;\n\n02-Aéreo;\n03-Aquaviário;\n\n04-Ferroviário;\n\n05-Dutoviário;\n06-Multimodal;'])
    UFIni: TUf = Element(TUf, documentation=['UF do início da prestação', "Informar 'EX' para operações com o exterior."])
    UFFim: TUf = Element(TUf, documentation=['UF do término da prestação', "Informar 'EX' para operações com o exterior."])
    tpCTe: str = Element(str, documentation=['Tipo do CT-e - Aceitar apenas Tipo Normal = 0', 'Preencher com:\n\t0 - CT-e Normal;\n 1 - CT-e de Complemento de Valores;\t2 - CT-e de Anulação;\n 3 - CT-e Substituto'])
    dhEmi: str = Element(str, documentation=['Data e hora de emissão do CT-e', 'Formato AAAA-MM-DDTHH:MM:DD TZD'])

evEPECCTe: evEPECCTe = Element(evEPECCTe, documentation=['Schema XML de validação do evento de emissão prévia de emissão em contingência \n110113'])
