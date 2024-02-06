from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoMDFeTiposBasico_v300 import *



class evAlteracaoPagtoServMDFe(ComplexType):
    """Schema XML de validação do evento de alteração do pagamento do serviçp de transporte 110118"""
    descEvento: str = Element(str, documentation=['Descrição do Evento - “Alteração Pagamento Serviço MDFe”'])
    nProt: TProt = Element(TProt, documentation=['Número do Protocolo de Status do MDF-e. '])

    class infPag(ComplexType):
        """Informações do Pagamento do Frete"""
        _max_occurs = -1
        _choice = [['CPF', 'CNPJ', 'idEstrangeiro']]

        def add(self, xNome=None, CPF=None, CNPJ=None, idEstrangeiro=None, Comp=None, vContrato=None, indPag=None, vAdiant=None, indAntecipaAdiant=None, infPrazo=None, tpAntecip=None, infBanc=None) -> evAlteracaoPagtoServMDFe.infPag:
            return super().add(xNome=xNome, CPF=CPF, CNPJ=CNPJ, idEstrangeiro=idEstrangeiro, Comp=Comp, vContrato=vContrato, indPag=indPag, vAdiant=vAdiant, indAntecipaAdiant=indAntecipaAdiant, infPrazo=infPrazo, tpAntecip=tpAntecip, infBanc=infBanc)

        xNome: str = Element(str, documentation=['Razão social ou Nome do responsavel pelo pagamento'])
        CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['Número do CPF do responsável pelo pgto', 'Informar os zeros não significativos.'])
        CNPJ: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['Número do CNPJ do responsável pelo pgto', 'Informar os zeros não significativos.'])
        idEstrangeiro: str = Element(str, documentation=['Identificador do responsável pelo pgto em caso de ser estrangeiro'])

        class Comp(ComplexType):
            """Componentes do Pagamentoi do Frete"""
            _max_occurs = -1

            def add(self, tpComp=None, vComp=None, xComp=None) -> evAlteracaoPagtoServMDFe.infPag.Comp:
                return super().add(tpComp=tpComp, vComp=vComp, xComp=xComp)

            tpComp: str = Element(str, documentation=['Tipo do Componente', '\n01 - Vale Pedágio; \n02 - Impostos, taxas e contribuições; \n03 - Despesas (bancárias, meios de pagamento, outras)\n; 99 - Outros'])
            vComp: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do componente'])
            xComp: str = Element(str, documentation=['Descrição do componente do tipo Outros'])
        Comp: List[Comp] = Element(Comp, max_occurs=-1, documentation=['Componentes do Pagamentoi do Frete'])
        vContrato: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Total do Contrato'])
        indPag: str = Element(str, documentation=['Indicador da Forma de Pagamento:0-Pagamento à Vista;1-Pagamento à Prazo;'])
        vAdiant: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do Adiantamento (usar apenas em pagamento à Prazo'])
        indAntecipaAdiant: str = Element(str, documentation=['Indicador para declarar concordância em antecipar o adiantamento', 'Operação de transporte com utilização de veículos de frotas dedicadas ou fidelizadas.\nPreencher com “1” para indicar operação de transporte de alto desempenho, demais casos não informar a tag\n'])

        class infPrazo(ComplexType):
            """Informações do pagamento a prazo.
Informar somente se indPag for à Prazo"""
            _max_occurs = -1

            def add(self, nParcela=None, dVenc=None, vParcela=None) -> evAlteracaoPagtoServMDFe.infPag.infPrazo:
                return super().add(nParcela=nParcela, dVenc=dVenc, vParcela=vParcela)

            nParcela: str = Element(str, documentation=['Número da Parcela'])
            dVenc: TData = Element(TData, base_type=date, documentation=['Data de vencimento da Parcela (AAAA-MM-DD)'])
            vParcela: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor da Parcela'])
        infPrazo: List[infPrazo] = Element(infPrazo, max_occurs=-1, documentation=['Informações do pagamento a prazo. ', 'Informar somente se indPag for à Prazo'])
        tpAntecip: str = Element(str, documentation=['Tipo de Permissão em relação a antecipação das parcelas', '0 - Não permite antecipar\n1 - Permite antecipar as parcelas\n2 - Permite antecipar as parcelas mediante confirmação'])

        class infBanc(ComplexType):
            """Informações bancárias"""
            _choice = [['CNPJIPEF', 'PIX']]
            codBanco: str = Element(str, documentation=['Número do banco'])
            codAgencia: str = Element(str, documentation=['Número da agência bancária '])
            CNPJIPEF: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['Número do CNPJ da Instituição de Pagamento Eletrônico do Frete', 'Informar os zeros não significativos.'])
            PIX: str = Element(str, documentation=['Chave PIX ', 'Informar a chave PIX para recebimento do frete. \nPode ser email, CPF/ CNPJ (somente numeros), Telefone com a seguinte formatação (+5599999999999) ou a chave aleatória gerada pela instituição.'])
        infBanc: infBanc = Element(infBanc, documentation=['Informações bancárias'])
    infPag: List[infPag] = Element(infPag, max_occurs=-1, documentation=['Informações do Pagamento do Frete'])

evAlteracaoPagtoServMDFe: evAlteracaoPagtoServMDFe = Element(evAlteracaoPagtoServMDFe, documentation=['Schema XML de validação do evento de alteração do pagamento do serviçp de transporte 110118'])
