from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralMDFe_v300 import *



class TRNTRC(TString):
    """Tipo RNTRC - Registro Nacional Transportadores Rodoviários de Carga"""
    _restriction = Restriction(base=r"TString", white_space=r"preserve", pattern=r"[0-9]{8}", enumeration=[])
    pass



class TCIOT(TString):
    """Tipo CIOT - Código Identificador da Operação de Transporte"""
    _restriction = Restriction(base=r"TString", white_space=r"preserve", pattern=r"[0-9]{12}", enumeration=[])
    pass



class rodo(ComplexType):
    """Informações do modal Rodoviário"""

    class infANTT(ComplexType):
        """Grupo de informações para Agência Reguladora"""
        RNTRC: TRNTRC = Element(TRNTRC, documentation=['Registro Nacional de Transportadores Rodoviários de Carga', 'Registro obrigatório do emitente do MDF-e junto à ANTT para exercer a atividade de transportador rodoviário de cargas por conta de terceiros e mediante remuneração.\n\t\t\t\t\t\t'])

        class infCIOT(ComplexType):
            """Dados do CIOT"""
            _max_occurs = -1
            _choice = [['CPF', 'CNPJ']]
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

            def add(self, CIOT=None, CPF=None, CNPJ=None) -> rodo.infANTT.infCIOT:
                return super().add(CIOT=CIOT, CPF=CPF, CNPJ=CNPJ)

            CIOT: str = Element(str, documentation=['Código Identificador da Operação de Transporte', 'Também Conhecido como conta frete'])
            CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['Número do CPF responsável pela geração do CIOT', 'Informar os zeros não significativos.'])
            CNPJ: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['Número do CNPJ responsável pela geração do CIOT', 'Informar os zeros não significativos.'])
        infCIOT: List[infCIOT] = Element(infCIOT, max_occurs=-1, documentation=['Dados do CIOT'])

        class valePed(ComplexType):
            """Informações de Vale Pedágio
Outras informações sobre Vale-Pedágio obrigatório que não tenham campos específicos devem ser informadas no campo de observações gerais de uso livre pelo contribuinte, visando atender as determinações legais vigentes."""

            class disp(ComplexType):
                """Informações dos dispositivos do Vale Pedágio"""
                _max_occurs = -1
                _choice = [['CNPJPg', 'CPFPg']]

                def add(self, CNPJForn=None, CNPJPg=None, CPFPg=None, nCompra=None, vValePed=None, tpValePed=None) -> rodo.infANTT.valePed.disp:
                    return super().add(CNPJForn=CNPJForn, CNPJPg=CNPJPg, CPFPg=CPFPg, nCompra=nCompra, vValePed=vValePed, tpValePed=tpValePed)

                CNPJForn: str = Element(str, documentation=['CNPJ da empresa fornecedora do Vale-Pedágio', '- CNPJ da Empresa Fornecedora do Vale-Pedágio, ou seja, empresa que fornece ao Responsável pelo Pagamento do Vale-Pedágio os dispositivos do Vale-Pedágio.\n\t\t\t\t\t\t\t\t\t- Informar os zeros não significativos.'])
                CNPJPg: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['CNPJ do responsável pelo pagamento do Vale-Pedágio', '- responsável pelo pagamento do Vale Pedágio. Informar somente quando o responsável não for o emitente do MDF-e.\n\t\t\t\t\t\t\t\t\t- Informar os zeros não significativos.'])
                CPFPg: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CNPJ do responsável pelo pagamento do Vale-Pedágio', 'Informar os zeros não significativos.'])
                nCompra: str = Element(str, documentation=['Número do comprovante de compra', 'Número de ordem do comprovante de compra do Vale-Pedágio fornecido para cada veículo ou combinação veicular, por viagem.'])
                vValePed: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do Vale-Pedagio', 'Valor do Vale-Pedágio obrigatório necessário à livre circulação, desde a origem da operação de transporte até o destino, do transportador contratado. '])
                tpValePed: str = Element(str, documentation=['Tipo do Vale Pedagio', '\n01 - TAG; 02 - Cupom; 03 - Cartão'])
            disp: List[disp] = Element(disp, max_occurs=-1, documentation=['Informações dos dispositivos do Vale Pedágio'])
            categCombVeic: str = Element(str, documentation=['Categoria de Combinação Veicular', 'Preencher com:\n\n02 Veículo Comercial 2 eixos;0\n4 Veículo Comercial 3 eixos;\n06 Veículo Comercial 4 eixos;0\n7 Veículo Comercial 5 eixos; 0\n8 Veículo Comercial 6 eixos;\n10 Veículo Comercial 7 eixos;\n11 Veículo Comercial 8 eixos;\n12 Veículo Comercial 9 eixos;\n13 Veículo Comercial 10 eixos;\n14 Veículo Comercial Acima de 10 eixos;'])
        valePed: valePed = Element(valePed, documentation=['Informações de Vale Pedágio', 'Outras informações sobre Vale-Pedágio obrigatório que não tenham campos específicos devem ser informadas no campo de observações gerais de uso livre pelo contribuinte, visando atender as determinações legais vigentes.'])

        class infContratante(ComplexType):
            """Grupo de informações dos contratantes do serviço de transporte"""
            _max_occurs = -1
            _choice = [['CPF', 'CNPJ', 'idEstrangeiro']]

            def add(self, xNome=None, CPF=None, CNPJ=None, idEstrangeiro=None, infContrato=None) -> rodo.infANTT.infContratante:
                return super().add(xNome=xNome, CPF=CPF, CNPJ=CNPJ, idEstrangeiro=idEstrangeiro, infContrato=infContrato)

            xNome: str = Element(str, documentation=['Razão social ou Nome do contratante'])
            CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['Número do CPF do contratante do serviço', 'Informar os zeros não significativos.'])
            CNPJ: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['Número do CNPJ do contratante do serviço', 'Informar os zeros não significativos.'])
            idEstrangeiro: str = Element(str, documentation=['Identificador do contratante em caso de contratante estrangeiro'])

            class infContrato(ComplexType):
                """Grupo de informações do contrato entre transportador e contratante"""
                NroContrato: str = Element(str, documentation=['Número do contrato do transportador com o contratante quando este existir para prestações continuadas'])
                vContratoGlobal: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor global do contrato'])
            infContrato: infContrato = Element(infContrato, documentation=['Grupo de informações do contrato entre transportador e contratante'])
        infContratante: List[infContratante] = Element(infContratante, max_occurs=-1, documentation=['Grupo de informações dos contratantes do serviço de transporte'])

        class infPag(ComplexType):
            """Informações do Pagamento do Frete"""
            _max_occurs = -1
            _choice = [['CPF', 'CNPJ', 'idEstrangeiro']]

            def add(self, xNome=None, CPF=None, CNPJ=None, idEstrangeiro=None, Comp=None, vContrato=None, indAltoDesemp=None, indPag=None, vAdiant=None, indAntecipaAdiant=None, infPrazo=None, tpAntecip=None, infBanc=None) -> rodo.infANTT.infPag:
                return super().add(xNome=xNome, CPF=CPF, CNPJ=CNPJ, idEstrangeiro=idEstrangeiro, Comp=Comp, vContrato=vContrato, indAltoDesemp=indAltoDesemp, indPag=indPag, vAdiant=vAdiant, indAntecipaAdiant=indAntecipaAdiant, infPrazo=infPrazo, tpAntecip=tpAntecip, infBanc=infBanc)

            xNome: str = Element(str, documentation=['Razão social ou Nome do respnsável pelo pagamento'])
            CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['Número do CPF do responsável pelo pgto', 'Informar os zeros não significativos.'])
            CNPJ: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['Número do CNPJ do responsável pelo pgto', 'Informar os zeros não significativos.'])
            idEstrangeiro: str = Element(str, documentation=['Identificador do responsável pelo pgto em caso de ser estrangeiro'])

            class Comp(ComplexType):
                """Componentes do Pagamentoi do Frete"""
                _max_occurs = -1

                def add(self, tpComp=None, vComp=None, xComp=None) -> rodo.infANTT.infPag.Comp:
                    return super().add(tpComp=tpComp, vComp=vComp, xComp=xComp)

                tpComp: str = Element(str, documentation=['Tipo do Componente', '\nPreencher com: 01 - Vale Pedágio; \n02 - Impostos, taxas e contribuições; \n03 - Despesas (bancárias, meios de pagamento, outras)\n; 99 - Outros'])
                vComp: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do componente'])
                xComp: str = Element(str, documentation=['Descrição do componente do tipo Outros'])
            Comp: List[Comp] = Element(Comp, max_occurs=-1, documentation=['Componentes do Pagamentoi do Frete'])
            vContrato: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Total do Contrato'])
            indAltoDesemp: str = Element(str, documentation=['Indicador de operação de transporte de alto desempenho', 'Operação de transporte com utilização de veículos de frotas dedicadas ou fidelizadas.\nPreencher com “1” para indicar operação de transporte de alto desempenho, demais casos não informar a tag\n'])
            indPag: str = Element(str, documentation=['Indicador da Forma de Pagamento:0-Pagamento à Vista;1-Pagamento à Prazo;'])
            vAdiant: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do Adiantamento (usar apenas em pagamento à Prazo'])
            indAntecipaAdiant: str = Element(str, documentation=['Indicador para declarar concordância em antecipar o adiantamento', 'Informar a tag somente se for autorizado antecipar o adiantamento'])

            class infPrazo(ComplexType):
                """Informações do pagamento a prazo.
Informar somente se indPag for à Prazo"""
                _max_occurs = -1

                def add(self, nParcela=None, dVenc=None, vParcela=None) -> rodo.infANTT.infPag.infPrazo:
                    return super().add(nParcela=nParcela, dVenc=dVenc, vParcela=vParcela)

                nParcela: str = Element(str, documentation=['Número da Parcela'])
                dVenc: TData = Element(TData, base_type=date, documentation=['Data de vencimento da Parcela (AAAA-MM-DD)'])
                vParcela: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor da Parcela'])
            infPrazo: List[infPrazo] = Element(infPrazo, max_occurs=-1, documentation=['Informações do pagamento a prazo. ', 'Informar somente se indPag for à Prazo'])
            tpAntecip: str = Element(str, documentation=['Tipo de Permissão em relação a antecipação das parcelas', '0 - Não permite antecipar\n\n1 - Permite antecipar as parcelas\n\n2 - Permite antecipar as parcelas mediante confirmação'])

            class infBanc(ComplexType):
                """Informações bancárias"""
                _choice = [['CNPJIPEF', 'PIX']]
                codBanco: str = Element(str, documentation=['Número do banco'])
                codAgencia: str = Element(str, documentation=['Número da agência bancária '])
                CNPJIPEF: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['Número do CNPJ da Instituição de Pagamento Eletrônico do Frete', 'Informar os zeros não significativos.'])
                PIX: str = Element(str, documentation=['Chave PIX ', 'Informar a chave PIX para recebimento do frete. \nPode ser email, CPF/ CNPJ (somente numeros), Telefone com a seguinte formatação (+5599999999999) ou a chave aleatória gerada pela instituição.'])
            infBanc: infBanc = Element(infBanc, documentation=['Informações bancárias'])
        infPag: List[infPag] = Element(infPag, max_occurs=-1, documentation=['Informações do Pagamento do Frete'])
    infANTT: infANTT = Element(infANTT, documentation=['Grupo de informações para Agência Reguladora'])

    class veicTracao(ComplexType):
        """Dados do Veículo com a Tração"""
        cInt: str = Element(str, documentation=['Código interno do veículo '])
        placa: str = Element(str, documentation=['Placa do veículo '])
        RENAVAM: str = Element(str, documentation=['RENAVAM do veículo '])
        tara: str = Element(str, documentation=['Tara em KG'])
        capKG: str = Element(str, documentation=['Capacidade em KG'])
        capM3: str = Element(str, documentation=['Capacidade em M3'])

        class prop(ComplexType):
            """Proprietário ou possuidor do Veículo.
Só preenchido quando o veículo não pertencer à empresa emitente do MDF-e"""
            _choice = [['CPF', 'CNPJ']]
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
            RNTRC: TRNTRC = Element(TRNTRC, documentation=['Registro Nacional dos Transportadores Rodoviários de Carga', 'Registro obrigatório do proprietário, co-proprietário ou arrendatário do veículo junto à ANTT para exercer a atividade de transportador rodoviário de cargas por conta de terceiros e mediante remuneração.'])
            xNome: str = Element(str, documentation=['Razão Social ou Nome do proprietário'])
            IE: str = Element(str, documentation=['Inscrição Estadual'])
            UF: TUf = Element(TUf, documentation=['UF'])
            tpProp: str = Element(str, documentation=['Tipo Proprietário ou possuidor', 'Preencher com:\n\t\t\t\t\t\t\t\t\t\t\t\t0-TAC Agregado;\n\t\t\t\t\t\t\t\t\t\t\t\t1-TAC Independente; \n\t\t\t\t\t\t\t\t\t\t\t\t2 – Outros.'])
        prop: prop = Element(prop, documentation=['Proprietário ou possuidor do Veículo.\nSó preenchido quando o veículo não pertencer à empresa emitente do MDF-e'])

        class condutor(ComplexType):
            """Informações do(s) Condutor(es) do veículo"""
            _max_occurs = 10

            def add(self, xNome=None, CPF=None) -> rodo.veicTracao.condutor:
                return super().add(xNome=xNome, CPF=CPF)

            xNome: str = Element(str, documentation=['Nome do Condutor'])
            CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CPF do Condutor'])
        condutor: List[condutor] = Element(condutor, max_occurs=10, documentation=['Informações do(s) Condutor(es) do veículo'])
        tpRod: str = Element(str, documentation=['Tipo de Rodado', 'Preencher com:\n\t\t\t\t\t\t\t\t\t01 - Truck;\n\t\t\t\t\t\t\t\t\t02 - Toco;\n\t\t\t\t\t\t\t\t\t03 - Cavalo Mecânico;\n\t\t\t\t\t\t\t\t\t04 - VAN;\n\t\t\t\t\t\t\t\t\t05 - Utilitário;\n\t\t\t\t\t\t\t\t\t06 - Outros.'])
        tpCar: str = Element(str, documentation=['Tipo de Carroceria', 'Preencher com:\n\t\t\t\t\t\t\t\t\t00 - não aplicável;\n\t\t\t\t\t\t\t\t\t01 - Aberta;\n\t\t\t\t\t\t\t\t\t02 - Fechada/Baú;\n\t\t\t\t\t\t\t\t\t03 - Granelera;\n\t\t\t\t\t\t\t\t\t04 - Porta Container;\n\t\t\t\t\t\t\t\t\t05 - Sider'])
        UF: TUf = Element(TUf, documentation=['UF em que veículo está licenciado', 'Sigla da UF de licenciamento do veículo.'])
    veicTracao: veicTracao = Element(veicTracao, documentation=['Dados do Veículo com a Tração'])

    class veicReboque(ComplexType):
        """Dados dos reboques
"""
        _max_occurs = 3

        def add(self, cInt=None, placa=None, RENAVAM=None, tara=None, capKG=None, capM3=None, prop=None, tpCar=None, UF=None) -> rodo.veicReboque:
            return super().add(cInt=cInt, placa=placa, RENAVAM=RENAVAM, tara=tara, capKG=capKG, capM3=capM3, prop=prop, tpCar=tpCar, UF=UF)

        cInt: str = Element(str, documentation=['Código interno do veículo '])
        placa: str = Element(str, documentation=['Placa do veículo '])
        RENAVAM: str = Element(str, documentation=['RENAVAM do veículo '])
        tara: str = Element(str, documentation=['Tara em KG'])
        capKG: str = Element(str, documentation=['Capacidade em KG'])
        capM3: str = Element(str, documentation=['Capacidade em M3'])

        class prop(ComplexType):
            """Proprietários ou possuidor do Veículo.
Só preenchido quando o veículo não pertencer à empresa emitente do MDF-e"""
            _choice = [['CPF', 'CNPJ']]
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
            RNTRC: TRNTRC = Element(TRNTRC, documentation=['Registro Nacional dos Transportadores Rodoviários de Carga', 'Registro obrigatório do proprietário, co-proprietário ou arrendatário do veículo junto à ANTT para exercer a atividade de transportador rodoviário de cargas por conta de terceiros e mediante remuneração.'])
            xNome: str = Element(str, documentation=['Razão Social ou Nome do proprietário'])
            IE: str = Element(str, documentation=['Inscrição Estadual'])
            UF: TUf = Element(TUf, documentation=['UF'])
            tpProp: str = Element(str, documentation=['Tipo Proprietário ou possuidor', 'Preencher com:\n\t\t\t\t\t\t\t\t\t\t\t\t0-TAC Agregado;\n\t\t\t\t\t\t\t\t\t\t\t\t1-TAC Independente;  \n\t\t\t\t\t\t\t\t\t\t\t\t2 – Outros.'])
        prop: prop = Element(prop, documentation=['Proprietários ou possuidor do Veículo.\nSó preenchido quando o veículo não pertencer à empresa emitente do MDF-e'])
        tpCar: str = Element(str, documentation=['Tipo de Carroceria', 'Preencher com:\n\t\t\t\t\t\t\t\t\t00 - não aplicável;\n\t\t\t\t\t\t\t\t\t01 - Aberta;\n\t\t\t\t\t\t\t\t\t02 - Fechada/Baú;\n\t\t\t\t\t\t\t\t\t03 - Granelera;\n\t\t\t\t\t\t\t\t\t04 - Porta Container;\n\t\t\t\t\t\t\t\t\t05 - Sider'])
        UF: TUf = Element(TUf, documentation=['UF em que veículo está licenciado', 'Sigla da UF de licenciamento do veículo.'])
    veicReboque: List[veicReboque] = Element(veicReboque, max_occurs=3, documentation=['Dados dos reboques', None])
    codAgPorto: str = Element(str, documentation=['Código de Agendamento no porto'])

    class lacRodo(ComplexType):
        """Lacres"""
        _max_occurs = -1

        def add(self, nLacre=None) -> rodo.lacRodo:
            return super().add(nLacre=nLacre)

        nLacre: str = Element(str, documentation=['Número do Lacre'])
    lacRodo: List[lacRodo] = Element(lacRodo, max_occurs=-1, documentation=['Lacres'])

rodo: rodo = Element(rodo, documentation=['Informações do modal Rodoviário'])
