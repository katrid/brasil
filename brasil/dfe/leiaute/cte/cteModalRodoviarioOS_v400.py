from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v400 import *

from .cteTiposBasico_v400 import *



class TTermoAutFreta(str):
    """Tipo Termo  de Autorização de Fretamento – TAF"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{12}", max_length=r"12", enumeration=[])
    pass



class TNroRegEstadual(str):
    """Tipo Número de Registro Estadual"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{25}", max_length=r"25", enumeration=[])
    pass



class rodoOS(ComplexType):
    """Informações do modal Rodoviário"""
    _choice = [['TAF', 'NroRegEstadual']]
    TAF: TTermoAutFreta = Element(TTermoAutFreta, documentation=['Termo de Autorização de Fretamento – TAF', 'Registro obrigatório do emitente do CT-e OS junto à ANTT, de acordo com a Resolução ANTT nº 4.777/2015'])
    NroRegEstadual: TNroRegEstadual = Element(TNroRegEstadual, documentation=['Número do Registro Estadual ', 'Registro obrigatório do emitente do CT-e OS junto à Agência Reguladora  Estadual.\t\t\t\t\t'])

    class veic(ComplexType):
        """Dados do Veículo"""
        placa: str = Element(str, documentation=['Placa do veículo '])
        RENAVAM: str = Element(str, documentation=['RENAVAM do veículo '])

        class prop(ComplexType):
            """Proprietário ou possuidor do Veículo.
Só preenchido quando o veículo não pertencer à empresa emitente do CT-e OS"""
            _choice = [['CPF', 'CNPJ'], ['TAF', 'NroRegEstadual']]
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
            CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['Número do CPF', 'Informar os zeros não significativos.'])
            CNPJ: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['Número do CNPJ', 'Informar os zeros não significativos.'])
            TAF: TTermoAutFreta = Element(TTermoAutFreta, documentation=['Termo de Autorização de Fretamento – TAF', 'De acordo com a Resolução ANTT nº 4.777/2015\t\t\t\t\t\t'])
            NroRegEstadual: TNroRegEstadual = Element(TNroRegEstadual, documentation=['Número do Registro Estadual ', 'Registro obrigatório do emitente do CT-e OS junto à Agência Reguladora  Estadual\t\t\t\t\t\t'])
            xNome: str = Element(str, documentation=['Razão Social ou Nome do proprietário'])
            IE: str = Element(str, documentation=['Inscrição Estadual'])
            UF: TUf = Element(TUf, documentation=['UF'])
            tpProp: str = Element(str, documentation=['Tipo Proprietário ou possuidor', 'Preencher com:\n\t\t\t\t\t\t\t\t\t\t\t\t0-TAC – Agregado;\n\t\t\t\t\t\t\t\t\t\t\t\t1-TAC Independente; ou \n\t\t\t\t\t\t\t\t\t\t\t\t2 – Outros.'])
        prop: prop = Element(prop, documentation=['Proprietário ou possuidor do Veículo.\nSó preenchido quando o veículo não pertencer à empresa emitente do CT-e OS'])
        UF: TUf = Element(TUf, documentation=['UF em que veículo está licenciado', 'Sigla da UF de licenciamento do veículo.'])
    veic: veic = Element(veic, documentation=['Dados do Veículo'])

    class infFretamento(ComplexType):
        """Dados do fretamento (apenas para Transporte de Pessoas)"""
        tpFretamento: str = Element(str, documentation=['Tipo Fretamento', 'Preencher com:\n 1 - Eventual 2 - Continuo\t\t\t\t\t\t\t\t'])
        dhViagem: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e hora da viagem (Apenas para fretamento eventual)', 'Formato AAAA-MM-DDTHH:MM:DD TZD'])
    infFretamento: infFretamento = Element(infFretamento, documentation=['Dados do fretamento (apenas para Transporte de Pessoas)'])

rodoOS: rodoOS = Element(rodoOS, documentation=['Informações do modal Rodoviário'])
