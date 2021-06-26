from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposBasico_v310 import *



class TEndereco(Element):
    """Tipo Dados do Endereço  // 24/10/08 - tamanho mínimo"""
    xLgr: str = Element(str, documentation=['Logradouro'])
    nro: str = Element(str, documentation=['Número'])
    xCpl: str = Element(str, documentation=['Complemento'])
    xBairro: str = Element(str, documentation=['Bairro'])
    cMun: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do município (utilizar a tabela do IBGE), informar 9999999 para operações com o exterior.'])
    xMun: str = Element(str, documentation=['Nome do município, informar EXTERIOR para operações com o exterior.'])
    UF: TUf = Element(TUf, documentation=['Sigla da UF, informar EX para operações com o exterior.'])
    CEP: str = Element(str, filter=str.isdigit, documentation=['CEP'])
    cPais: str = Element(str, documentation=['Código de Pais'])
    xPais: str = Element(str, documentation=['Nome do país'])
    fone: str = Element(str, filter=str.isdigit, documentation=['Telefone, preencher com Código DDD + número do telefone , nas operações com exterior é permtido informar o código do país + código da localidade + número do telefone'])



class TEnderEmi(Element):
    """Tipo Dados do Endereço do Emitente  // 24/10/08 - desmembrado / tamanho mínimo"""
    xLgr: str = Element(str, documentation=['Logradouro'])
    nro: str = Element(str, documentation=['Número'])
    xCpl: str = Element(str, documentation=['Complemento'])
    xBairro: str = Element(str, documentation=['Bairro'])
    cMun: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do município'])
    xMun: str = Element(str, documentation=['Nome do município'])
    UF: TUfEmi = Element(TUfEmi, documentation=['Sigla da UF'])
    CEP: str = Element(str, filter=str.isdigit, documentation=['CEP - NT 2011/004'])
    cPais: str = Element(str, documentation=['Código do país'])
    xPais: str = Element(str, documentation=['Nome do país'])
    fone: str = Element(str, filter=str.isdigit, documentation=['Preencher com Código DDD + número do telefone (v.2.0)'])



class TLocal(Element):
    """Tipo Dados do Local de Retirada ou Entrega // 24/10/08 - tamanho mínimo // v2.0"""
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
    CNPJ: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['CNPJ'])
    CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CPF (v2.0)'])
    xLgr: str = Element(str, documentation=['Logradouro'])
    nro: str = Element(str, documentation=['Número'])
    xCpl: str = Element(str, documentation=['Complemento'])
    xBairro: str = Element(str, documentation=['Bairro'])
    cMun: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do município (utilizar a tabela do IBGE)'])
    xMun: str = Element(str, documentation=['Nome do município'])
    UF: TUf = Element(TUf, documentation=['Sigla da UF'])



class TVeiculo(Element):
    """Tipo Dados do Veículo"""
    placa: str = Element(str, documentation=['Placa do veículo (NT2011/004)'])
    UF: TUf = Element(TUf, documentation=['Sigla da UF'])
    RNTC: str = Element(str, documentation=['Registro Nacional de Transportador de Carga (ANTT)'])



class Torig(str):
    """Tipo Origem da mercadoria CST ICMS  origem da mercadoria: 0-Nacional exceto as indicadas nos códigos 3, 4, 5 e 8;
1-Estrangeira - Importação direta; 2-Estrangeira - Adquirida no mercado interno; 3-Nacional, conteudo superior 40% e inferior ou igual a 70%; 4-Nacional, processos produtivos básicos; 5-Nacional, conteudo inferior 40%; 6-Estrangeira - Importação direta, com similar nacional, lista CAMEX; 7-Estrangeira - mercado interno, sem simular,lista CAMEX;8-Nacional, Conteúdo de Importação superior a 70%."""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['0', '1', '2', '3', '4', '5', '6', '7', '8'])
    pass



class TFinNFe(str):
    """Tipo Finalidade da NF-e (1=Normal; 2=Complementar; 3=Ajuste; 4=Devolução/Retorno)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1', '2', '3', '4'])
    pass



class TProcEmi(str):
    """Tipo processo de emissão da NF-e"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['0', '1', '2', '3'])
    pass



class TCListServ(str):
    """Tipo Código da Lista de Serviços LC 116/2003"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['01.01', '01.02', '01.03', '01.04', '01.05', '01.06', '01.07', '01.08', '02.01', '03.02', '03.03', '03.04', '03.05', '04.01', '04.02', '04.03', '04.04', '04.05', '04.06', '04.07', '04.08', '04.09', '04.10', '04.11', '04.12', '04.13', '04.14', '04.15', '04.16', '04.17', '04.18', '04.19', '04.20', '04.21', '04.22', '04.23', '05.01', '05.02', '05.03', '05.04', '05.05', '05.06', '05.07', '05.08', '05.09', '06.01', '06.02', '06.03', '06.04', '06.05', '07.01', '07.02', '07.03', '07.04', '07.05', '07.06', '07.07', '07.08', '07.09', '07.10', '07.11', '07.12', '07.13', '07.16', '07.17', '07.18', '07.19', '07.20', '07.21', '07.22', '08.01', '08.02', '09.01', '09.02', '09.03', '10.01', '10.02', '10.03', '10.04', '10.05', '10.06', '10.07', '10.08', '10.09', '10.10', '11.01', '11.02', '11.03', '11.04', '12.01', '12.02', '12.03', '12.04', '12.05', '12.06', '12.07', '12.08', '12.09', '12.10', '12.11', '12.12', '12.13', '12.14', '12.15', '12.16', '12.17', '13.02', '13.03', '13.04', '13.05', '14.01', '14.02', '14.03', '14.04', '14.05', '14.06', '14.07', '14.08', '14.09', '14.10', '14.11', '14.12', '14.13', '15.01', '15.02', '15.03', '15.04', '15.05', '15.06', '15.07', '15.08', '15.09', '15.10', '15.11', '15.12', '15.13', '15.14', '15.15', '15.16', '15.17', '15.18', '16.01', '17.01', '17.02', '17.03', '17.04', '17.05', '17.06', '17.08', '17.09', '17.10', '17.11', '17.12', '17.13', '17.14', '17.15', '17.16', '17.17', '17.18', '17.19', '17.20', '17.21', '17.22', '17.23', '17.24', '18.01', '19.01', '20.01', '20.02', '20.03', '21.01', '22.01', '23.01', '24.01', '25.01', '25.02', '25.03', '25.04', '26.01', '27.01', '28.01', '29.01', '30.01', '31.01', '32.01', '33.01', '34.01', '35.01', '36.01', '37.01', '38.01', '39.01', '40.01'])
    pass



class TVerNFe(str):
    """Tipo Versão da NF-e - 3.10"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"3\.10", enumeration=[])
    pass



class TGuid(str):
    """Identificador único (Globally Unique Identifier)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[A-F0-9]{8}-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{12}", enumeration=[])
    pass



class TIpi(Element):
    """Tipo: Dados do IPI"""
    _choice = [['IPITrib', 'IPINT']]
    clEnq: str = Element(str, documentation=['Classe de Enquadramento do IPI para Cigarros e Bebidas'])
    CNPJProd: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do produtor da mercadoria, quando diferente do emitente. Somente para os casos de exportação direta ou indireta.'])
    cSelo: str = Element(str, documentation=['Código do selo de controle do IPI '])
    qSelo: str = Element(str, documentation=['Quantidade de selo de controle do IPI'])
    cEnq: str = Element(str, documentation=['Código de Enquadramento Legal do IPI (tabela a ser criada pela RFB)'])

    class IPITrib(ComplexType):
        _choice = [[]]
        CST: str = Element(str, documentation=['Código da Situação Tributária do IPI:\n00-Entrada com recuperação de crédito\n49 - Outras entradas\n50-Saída tributada\n99-Outras saídas'])
        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do IPI'])
        pIPI: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do IPI'])
        qUnid: TDec_1204v = Element(TDec_1204v, tipo="N", tam=(12, 4), base_type=Decimal, documentation=['Quantidade total na unidade padrão para tributação '])
        vUnid: TDec_1104 = Element(TDec_1104, tipo="N", tam=(11, 4), base_type=Decimal, documentation=['Valor por Unidade Tributável. Informar o valor do imposto Pauta por unidade de medida.'])
        vIPI: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do IPI'])
    IPITrib: IPITrib = Element(IPITrib)

    class IPINT(ComplexType):
        CST: str = Element(str, documentation=['Código da Situação Tributária do IPI:\n01-Entrada tributada com alíquota zero\n02-Entrada isenta\n03-Entrada não-tributada\n04-Entrada imune\n05-Entrada com suspensão\n51-Saída tributada com alíquota zero\n52-Saída isenta\n53-Saída não-tributada\n54-Saída imune\n55-Saída com suspensão'])
    IPINT: IPINT = Element(IPINT)



class TNFe(Element):
    """Tipo Nota Fiscal Eletrônica"""

    class infNFe(ComplexType):
        """Informações da Nota Fiscal eletrônica"""

        class ide(ComplexType):
            """identificação da NF-e"""
            cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['Código da UF do emitente do Documento Fiscal. Utilizar a Tabela do IBGE.'])
            cNF: str = Element(str, documentation=['Código numérico que compõe a Chave de Acesso. Número aleatório gerado pelo emitente para cada NF-e.'])
            natOp: str = Element(str, documentation=['Descrição da Natureza da Operação'])
            indPag: str = Element(str, documentation=['Indicador da forma de pagamento:\n0 – pagamento à vista;\n1 – pagamento à prazo;\n2 – outros.'])
            mod: TMod = Element(TMod, documentation=['Código do modelo do Documento Fiscal. 55 = NF-e; 65 = NFC-e.'])
            serie: TSerie = Element(TSerie, documentation=['Série do Documento Fiscal\nsérie normal 0-889\nAvulsa Fisco 890-899\nSCAN 900-999'])
            nNF: TNF = Element(TNF, documentation=['Número do Documento Fiscal'])
            dhEmi: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e Hora de emissão do Documento Fiscal (AAAA-MM-DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00'])
            dhSaiEnt: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e Hora da saída ou de entrada da mercadoria / produto (AAAA-MM-DDTHH:mm:ssTZD)'])
            tpNF: str = Element(str, documentation=['Tipo do Documento Fiscal (0 - entrada; 1 - saída)'])
            idDest: str = Element(str, documentation=['Identificador de Local de destino da operação (1-Interna;2-Interestadual;3-Exterior)'])
            cMunFG: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do Município de Ocorrência do Fato Gerador (utilizar a tabela do IBGE)'])
            tpImp: str = Element(str, documentation=['Formato de impressão do DANFE (0-sem DANFE;1-DANFe Retrato; 2-DANFe Paisagem;3-DANFe Simplificado;\n\t\t\t\t\t\t\t\t\t\t\t4-DANFe NFC-e;5-DANFe NFC-e em mensagem eletrônica)\n\t\t\t\t\t\t\t\t\t\t\t'])
            tpEmis: str = Element(str, documentation=['Forma de emissão da NF-e\n1 - Normal;\n2 - Contingência FS\n3 - Contingência SCAN\n4 - Contingência DPEC\n5 - Contingência FSDA\n6 - Contingência SVC - AN\n7 - Contingência SVC - RS\n9 - Contingência off-line NFC-e'])
            cDV: str = Element(str, documentation=['Digito Verificador da Chave de Acesso da NF-e'])
            tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
            finNFe: TFinNFe = Element(TFinNFe, documentation=['Finalidade da emissão da NF-e:\n1 - NFe normal\n2 - NFe complementar\n3 - NFe de ajuste\n4 - Devolução/Retorno'])
            indFinal: str = Element(str, documentation=['Indica operação com consumidor final (0-Não;1-Consumidor Final)'])
            indPres: str = Element(str, documentation=['Indicador de presença do comprador no estabelecimento comercial no momento da oepração\n\t\t\t\t\t\t\t\t\t\t\t(0-Não se aplica (ex.: Nota Fiscal complementar ou de ajuste;1-Operação presencial;2-Não presencial, internet;3-Não presencial, teleatendimento;4-NFC-e entrega em domicílio;9-Não presencial, outros)'])
            procEmi: TProcEmi = Element(TProcEmi, documentation=['Processo de emissão utilizado com a seguinte codificação:\n0 - emissão de NF-e com aplicativo do contribuinte;\n1 - emissão de NF-e avulsa pelo Fisco;\n2 - emissão de NF-e avulsa, pelo contribuinte com seu certificado digital, através do site\ndo Fisco;\n3- emissão de NF-e pelo contribuinte com aplicativo fornecido pelo Fisco.'])
            verProc: str = Element(str, documentation=['versão do aplicativo utilizado no processo de\nemissão'])
            dhCont: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Informar a data e hora de entrada em contingência contingência no formato  (AAAA-MM-DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00.'])
            xJust: str = Element(str, documentation=['Informar a Justificativa da entrada'])

            class NFref(ComplexType):
                """Grupo de infromações da NF referenciada"""
                _max_occurs = 500
                _choice = [['refNFe', 'refNF', 'refNFP', 'refCTe', 'refECF']]

                def add(self, refNFe=None, refNF=None, refNFP=None, refCTe=None, refECF=None) -> TNFe.infNFe.ide.NFref:
                    return super().add(refNFe=refNFe, refNF=refNF, refNFP=refNFP, refCTe=refCTe, refECF=refECF)

                refNFe: TChNFe = Element(TChNFe, documentation=['Chave de acesso das NF-e referenciadas. Chave de acesso compostas por Código da UF (tabela do IBGE) + AAMM da emissão + CNPJ do Emitente + modelo, série e número da NF-e Referenciada + Código Numérico + DV.'])

                class refNF(ComplexType):
                    """Dados da NF modelo 1/1A referenciada"""
                    cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['Código da UF do emitente do Documento Fiscal. Utilizar a Tabela do IBGE.'])
                    AAMM: str = Element(str, documentation=['AAMM da emissão'])
                    CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do emitente do documento fiscal referenciado'])
                    mod: str = Element(str, documentation=['Código do modelo do Documento Fiscal. Utilizar 01 para NF modelo 1/1A'])
                    serie: TSerie = Element(TSerie, documentation=['Série do Documento Fiscal, informar zero se inexistente'])
                    nNF: TNF = Element(TNF, documentation=['Número do Documento Fiscal'])
                refNF: refNF = Element(refNF, documentation=['Dados da NF modelo 1/1A referenciada'])

                class refNFP(ComplexType):
                    """Grupo com as informações NF de produtor referenciada"""
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
                    cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['Código da UF do emitente do Documento FiscalUtilizar a Tabela do IBGE (Anexo IV - Tabela de UF, Município e País)'])
                    AAMM: str = Element(str, documentation=['AAMM da emissão da NF de produtor'])
                    CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do emitente da NF de produtor'])
                    CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CPF do emitente da NF de produtor'])
                    IE: TIeDest = Element(TIeDest, filter=str.isdigit, documentation=['IE do emitente da NF de Produtor'])
                    mod: str = Element(str, documentation=['Código do modelo do Documento Fiscal - utilizar 04 para NF de produtor  ou 01 para NF Avulsa'])
                    serie: TSerie = Element(TSerie, documentation=['Série do Documento Fiscal, informar zero se inexistentesérie'])
                    nNF: TNF = Element(TNF, documentation=['Número do Documento Fiscal - 1 – 999999999'])
                refNFP: refNFP = Element(refNFP, documentation=['Grupo com as informações NF de produtor referenciada'])
                refCTe: TChNFe = Element(TChNFe, documentation=['Utilizar esta TAG para referenciar um CT-e emitido anteriormente, vinculada a NF-e atual'])

                class refECF(ComplexType):
                    """Grupo do Cupom Fiscal vinculado à NF-e"""
                    mod: str = Element(str, documentation=['Código do modelo do Documento Fiscal \nPreencher com "2B", quando se tratar de Cupom Fiscal emitido por máquina registradora (não ECF), com "2C", quando se tratar de Cupom Fiscal PDV, ou "2D", quando se tratar de Cupom Fiscal (emitido por ECF)'])
                    nECF: str = Element(str, documentation=['Informar o número de ordem seqüencial do ECF que emitiu o Cupom Fiscal vinculado à NF-e'])
                    nCOO: str = Element(str, documentation=['Informar o Número do Contador de Ordem de Operação - COO vinculado à NF-e'])
                refECF: refECF = Element(refECF, documentation=['Grupo do Cupom Fiscal vinculado à NF-e'])
            NFref: List[NFref] = Element(NFref, max_occurs=500, documentation=['Grupo de infromações da NF referenciada'])
        ide: ide = Element(ide, documentation=['identificação da NF-e'])

        class emit(ComplexType):
            """Identificação do emitente"""
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
            CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['Número do CNPJ do emitente'])
            CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['Número do CPF do emitente'])
            xNome: str = Element(str, documentation=['Razão Social ou Nome do emitente'])
            xFant: str = Element(str, documentation=['Nome fantasia'])
            enderEmit: TEnderEmi = Element(TEnderEmi, documentation=['Endereço do emitente'])
            IE: TIe = Element(TIe, filter=str.isdigit, documentation=['Inscrição Estadual do Emitente'])
            IEST: TIeST = Element(TIeST, filter=str.isdigit, documentation=['Inscricao Estadual do Substituto Tributário'])
            IM: str = Element(str, documentation=['Inscrição Municipal'])
            CNAE: str = Element(str, documentation=['CNAE Fiscal'])
            CRT: str = Element(str, documentation=['Código de Regime Tributário. \nEste campo será obrigatoriamente preenchido com:\n1 – Simples Nacional;\n2 – Simples Nacional – excesso de sublimite de receita bruta;\n3 – Regime Normal.\n'])
        emit: emit = Element(emit, documentation=['Identificação do emitente'])

        class avulsa(ComplexType):
            """Emissão de avulsa, informar os dados do Fisco emitente"""
            CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do Órgão emissor'])
            xOrgao: str = Element(str, documentation=['Órgão emitente'])
            matr: str = Element(str, documentation=['Matrícula do agente'])
            xAgente: str = Element(str, documentation=['Nome do agente'])
            fone: str = Element(str, filter=str.isdigit, documentation=['Telefone'])
            UF: TUfEmi = Element(TUfEmi, documentation=['Sigla da Unidade da Federação'])
            nDAR: str = Element(str, documentation=['Número do Documento de Arrecadação de Receita'])
            dEmi: TData = Element(TData, base_type=date, documentation=['Data de emissão do DAR (AAAA-MM-DD)'])
            vDAR: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Total constante no DAR'])
            repEmi: str = Element(str, documentation=['Repartição Fiscal emitente'])
            dPag: TData = Element(TData, base_type=date, documentation=['Data de pagamento do DAR (AAAA-MM-DD)'])
        avulsa: avulsa = Element(avulsa, documentation=['Emissão de avulsa, informar os dados do Fisco emitente'])

        class dest(ComplexType):
            """Identificação do Destinatário"""
            _choice = [['CNPJ', 'CPF', 'idEstrangeiro']]
            CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['Número do CNPJ'])
            CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['Número do CPF'])
            idEstrangeiro: str = Element(str, documentation=['Identificador do destinatário, em caso de comprador estrangeiro'])
            xNome: str = Element(str, documentation=['Razão Social ou nome do destinatário'])
            enderDest: TEndereco = Element(TEndereco, documentation=['Dados do endereço'])
            indIEDest: str = Element(str, documentation=['Indicador da IE do destinatário:\n1 – Contribuinte ICMSpagamento à vista;\n2 – Contribuinte isento de inscrição;\n9 – Não Contribuinte'])
            IE: TIeDestNaoIsento = Element(TIeDestNaoIsento, filter=str.isdigit, documentation=['Inscrição Estadual (obrigatório nas operações com contribuintes do ICMS)'])
            ISUF: str = Element(str, documentation=['Inscrição na SUFRAMA (Obrigatório nas operações com as áreas com benefícios de incentivos fiscais sob controle da SUFRAMA) PL_005d - 11/08/09 - alterado para aceitar 8 ou 9 dígitos'])
            IM: str = Element(str, documentation=['Inscrição Municipal do tomador do serviço'])
            email: str = Element(str, documentation=['Informar o e-mail do destinatário. O campo pode ser utilizado para informar o e-mail\nde recepção da NF-e indicada pelo destinatário'])
        dest: dest = Element(dest, documentation=['Identificação do Destinatário  '])
        retirada: TLocal = Element(TLocal, documentation=['Identificação do Local de Retirada (informar apenas quando for diferente do endereço do remetente)'])
        entrega: TLocal = Element(TLocal, documentation=['Identificação do Local de Entrega (informar apenas quando for diferente do endereço do destinatário)'])

        class autXML(ComplexType):
            """Pessoas autorizadas para o download do XML da NF-e"""
            _max_occurs = 10
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

            def add(self, CNPJ=None, CPF=None) -> TNFe.infNFe.autXML:
                return super().add(CNPJ=CNPJ, CPF=CPF)

            CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ Autorizado'])
            CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CPF Autorizado'])
        autXML: List[autXML] = Element(autXML, max_occurs=10, documentation=['Pessoas autorizadas para o download do XML da NF-e'])

        class det(ComplexType):
            """Dados dos detalhes da NF-e"""
            _max_occurs = 990

            def add(self, prod=None, imposto=None, impostoDevol=None, infAdProd=None, nItem=None) -> TNFe.infNFe.det:
                return super().add(prod=prod, imposto=imposto, impostoDevol=impostoDevol, infAdProd=infAdProd, nItem=nItem)


            class prod(ComplexType):
                """Dados dos produtos e serviços da NF-e"""
                _choice = [['veicProd', 'med', 'arma', 'comb', 'nRECOPI']]
                cProd: str = Element(str, documentation=['Código do produto ou serviço. Preencher com CFOP caso se trate de itens não relacionados com mercadorias/produto e que o contribuinte não possua codificação própria\nFormato ”CFOP9999”.'])
                cEAN: str = Element(str, documentation=['GTIN (Global Trade Item Number) do produto, antigo código EAN ou código de barras'])
                xProd: str = Element(str, documentation=['Descrição do produto ou serviço'])
                NCM: str = Element(str, documentation=['Código NCM (8 posições), será permitida a informação do gênero (posição do capítulo do NCM) quando a operação não for de comércio exterior (importação/exportação) ou o produto não seja tributado pelo IPI. Em caso de item de serviço ou item que não tenham produto (Ex. transferência de crédito, crédito do ativo imobilizado, etc.), informar o código 00 (zeros) (v2.0)'])
                NVE: List[str] = Element(str, max_occurs=8, documentation=['Nomenclatura de Valor aduaneio e Estatístico'])
                CEST: str = Element(str, documentation=['Codigo especificador da Substuicao Tributaria - CEST, que identifica a mercadoria sujeita aos regimes de  substituicao tributária e de antecipação do recolhimento  do imposto\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t'])
                EXTIPI: str = Element(str, documentation=['Código EX TIPI (3 posições)'])
                CFOP: str = Element(str, documentation=['Cfop'])
                uCom: str = Element(str, documentation=['Unidade comercial'])
                qCom: TDec_1104v = Element(TDec_1104v, tipo="N", tam=(11, 4), base_type=Decimal, documentation=['Quantidade Comercial  do produto, alterado para aceitar de 0 a 4 casas decimais e 11 inteiros.'])
                vUnCom: TDec_1110v = Element(TDec_1110v, tipo="N", tam=(11, 10), base_type=Decimal, documentation=['Valor unitário de comercialização  - alterado para aceitar 0 a 10 casas decimais e 11 inteiros '])
                vProd: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor bruto do produto ou serviço.'])
                cEANTrib: str = Element(str, documentation=['GTIN (Global Trade Item Number) da unidade tributável, antigo código EAN ou código de barras'])
                uTrib: str = Element(str, documentation=['Unidade Tributável'])
                qTrib: TDec_1104v = Element(TDec_1104v, tipo="N", tam=(11, 4), base_type=Decimal, documentation=['Quantidade Tributável - alterado para aceitar de 0 a 4 casas decimais e 11 inteiros '])
                vUnTrib: TDec_1110v = Element(TDec_1110v, tipo="N", tam=(11, 10), base_type=Decimal, documentation=['Valor unitário de tributação - - alterado para aceitar 0 a 10 casas decimais e 11 inteiros '])
                vFrete: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor Total do Frete'])
                vSeg: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor Total do Seguro'])
                vDesc: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor do Desconto'])
                vOutro: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Outras despesas acessórias'])
                indTot: str = Element(str, documentation=['Este campo deverá ser preenchido com:\n 0 – o valor do item (vProd) não compõe o valor total da NF-e (vProd)\n 1  – o valor do item (vProd) compõe o valor total da NF-e (vProd)\n'])

                class DI(ComplexType):
                    """Delcaração de Importação
(NT 2011/004)"""
                    _max_occurs = 100

                    def add(self, nDI=None, dDI=None, xLocDesemb=None, UFDesemb=None, dDesemb=None, tpViaTransp=None, vAFRMM=None, tpIntermedio=None, CNPJ=None, UFTerceiro=None, cExportador=None, adi=None) -> TNFe.infNFe.det.prod.DI:
                        return super().add(nDI=nDI, dDI=dDI, xLocDesemb=xLocDesemb, UFDesemb=UFDesemb, dDesemb=dDesemb, tpViaTransp=tpViaTransp, vAFRMM=vAFRMM, tpIntermedio=tpIntermedio, CNPJ=CNPJ, UFTerceiro=UFTerceiro, cExportador=cExportador, adi=adi)

                    nDI: str = Element(str, documentation=['Numero do Documento de Importação DI/DSI/DA/DRI-E (DI/DSI/DA/DRI-E) (NT2011/004)'])
                    dDI: TData = Element(TData, base_type=date, documentation=['Data de registro da DI/DSI/DA (AAAA-MM-DD)'])
                    xLocDesemb: str = Element(str, documentation=['Local do desembaraço aduaneiro'])
                    UFDesemb: TUfEmi = Element(TUfEmi, documentation=['UF onde ocorreu o desembaraço aduaneiro'])
                    dDesemb: TData = Element(TData, base_type=date, documentation=['Data do desembaraço aduaneiro (AAAA-MM-DD)'])
                    tpViaTransp: str = Element(str, documentation=['Via de transporte internacional informada na DI\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1-Maritima;2-Fluvial;3-Lacustre;4-Aerea;5-Postal;6-Ferroviaria;7-Rodoviaria;8-Conduto;9-Meios Proprios;10-Entrada/Saida Ficta.'])
                    vAFRMM: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Adicional ao frete para renovação de marinha mercante'])
                    tpIntermedio: str = Element(str, documentation=['Forma de Importação quanto a intermediação \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1-por conta propria;2-por conta e ordem;3-encomenda'])
                    CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do adquirente ou do encomendante'])
                    UFTerceiro: TUfEmi = Element(TUfEmi, documentation=['Sigla da UF do adquirente ou do encomendante'])
                    cExportador: str = Element(str, documentation=['Código do exportador (usado nos sistemas internos de informação do emitente da NF-e)'])

                    class adi(ComplexType):
                        """Adições (NT 2011/004)"""
                        _max_occurs = 100

                        def add(self, nAdicao=None, nSeqAdic=None, cFabricante=None, vDescDI=None, nDraw=None) -> TNFe.infNFe.det.prod.DI.adi:
                            return super().add(nAdicao=nAdicao, nSeqAdic=nSeqAdic, cFabricante=cFabricante, vDescDI=vDescDI, nDraw=nDraw)

                        nAdicao: str = Element(str, documentation=['Número da Adição'])
                        nSeqAdic: str = Element(str, documentation=['Número seqüencial do item dentro da Adição'])
                        cFabricante: str = Element(str, documentation=['Código do fabricante estrangeiro (usado nos sistemas internos de informação do emitente da NF-e)'])
                        vDescDI: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor do desconto do item da DI – adição'])
                        nDraw: str = Element(str, documentation=['Número do ato concessório de Drawback'])
                    adi: List[adi] = Element(adi, max_occurs=100, documentation=['Adições (NT 2011/004)'])
                DI: List[DI] = Element(DI, max_occurs=100, documentation=['Delcaração de Importação\n(NT 2011/004)'])

                class detExport(ComplexType):
                    """Detalhe da exportação"""
                    _max_occurs = 500

                    def add(self, nDraw=None, exportInd=None) -> TNFe.infNFe.det.prod.detExport:
                        return super().add(nDraw=nDraw, exportInd=exportInd)

                    nDraw: str = Element(str, documentation=['Número do ato concessório de Drawback'])

                    class exportInd(ComplexType):
                        """Exportação indireta"""
                        nRE: str = Element(str, documentation=['Registro de exportação'])
                        chNFe: TChNFe = Element(TChNFe, documentation=['Chave de acesso da NF-e recebida para exportação'])
                        qExport: TDec_1104v = Element(TDec_1104v, tipo="N", tam=(11, 4), base_type=Decimal, documentation=['Quantidade do item efetivamente exportado'])
                    exportInd: exportInd = Element(exportInd, documentation=['Exportação indireta'])
                detExport: List[detExport] = Element(detExport, max_occurs=500, documentation=['Detalhe da exportação'])
                xPed: str = Element(str, documentation=['pedido de compra - Informação de interesse do emissor para controle do B2B.'])
                nItemPed: str = Element(str, documentation=['Número do Item do Pedido de Compra - Identificação do número do item do pedido de Compra'])
                nFCI: TGuid = Element(TGuid, documentation=['Número de controle da FCI - Ficha de Conteúdo de Importação.'])

                class veicProd(ComplexType):
                    """Veículos novos"""
                    tpOp: str = Element(str, documentation=['Tipo da Operação (1 - Venda concessionária; 2 - Faturamento direto; 3 - Venda direta; 0 - Outros)'])
                    chassi: str = Element(str, documentation=['Chassi do veículo - VIN (código-identificação-veículo)'])
                    cCor: str = Element(str, documentation=['Cor do veículo (código de cada montadora)'])
                    xCor: str = Element(str, documentation=['Descrição da cor'])
                    pot: str = Element(str, documentation=['Potência máxima do motor do veículo em cavalo vapor (CV). (potência-veículo)'])
                    cilin: str = Element(str, documentation=['Capacidade voluntária do motor expressa em centímetros cúbicos (CC). (cilindradas)'])
                    pesoL: str = Element(str, documentation=['Peso líquido'])
                    pesoB: str = Element(str, documentation=['Peso bruto'])
                    nSerie: str = Element(str, documentation=['Serial (série)'])
                    tpComb: str = Element(str, documentation=['Tipo de combustível-Tabela RENAVAM: 01-Álcool; 02-Gasolina; 03-Diesel; 16-Álcool/Gas.; 17-Gas./Álcool/GNV; 18-Gasolina/Elétrico'])
                    nMotor: str = Element(str, documentation=['Número do motor'])
                    CMT: str = Element(str, documentation=['CMT-Capacidade Máxima de Tração - em Toneladas 4 casas decimais'])
                    dist: str = Element(str, documentation=['Distância entre eixos'])
                    anoMod: str = Element(str, documentation=['Ano Modelo de Fabricação'])
                    anoFab: str = Element(str, documentation=['Ano de Fabricação'])
                    tpPint: str = Element(str, documentation=['Tipo de pintura'])
                    tpVeic: str = Element(str, documentation=['Tipo de veículo (utilizar tabela RENAVAM)'])
                    espVeic: str = Element(str, documentation=['Espécie de veículo (utilizar tabela RENAVAM)'])
                    VIN: str = Element(str, documentation=['Informa-se o veículo tem VIN (chassi) remarcado.\nR-Remarcado\nN-NormalVIN '])
                    condVeic: str = Element(str, documentation=['Condição do veículo (1 - acabado; 2 - inacabado; 3 - semi-acabado)'])
                    cMod: str = Element(str, documentation=['Código Marca Modelo (utilizar tabela RENAVAM)'])
                    cCorDENATRAN: str = Element(str, documentation=['Código da Cor Segundo as regras de pré-cadastro do DENATRAN: 01-AMARELO;02-AZUL;03-BEGE;04-BRANCA;05-CINZA;06-DOURADA;07-GRENA \n08-LARANJA;09-MARROM;10-PRATA;11-PRETA;12-ROSA;13-ROXA;14-VERDE;15-VERMELHA;16-FANTASIA'])
                    lota: str = Element(str, documentation=['Quantidade máxima de permitida de passageiros sentados, inclusive motorista.'])
                    tpRest: str = Element(str, documentation=['Restrição\n0 - Não há;\n1 - Alienação Fiduciária;\n2 - Arrendamento Mercantil;\n3 - Reserva de Domínio;\n4 - Penhor de Veículos;\n9 - outras.'])
                veicProd: veicProd = Element(veicProd, documentation=['Veículos novos'])

                class med(ComplexType):
                    """grupo do detalhamento de Medicamentos e de matérias-primas farmacêuticas"""
                    _max_occurs = 500

                    def add(self, nLote=None, qLote=None, dFab=None, dVal=None, vPMC=None) -> TNFe.infNFe.det.prod.med:
                        return super().add(nLote=nLote, qLote=qLote, dFab=dFab, dVal=dVal, vPMC=vPMC)

                    nLote: str = Element(str, documentation=['Número do lote do medicamento'])
                    qLote: TDec_0803v = Element(TDec_0803v, tipo="N", tam=(8, 3), base_type=Decimal, documentation=['Quantidade de produtos no lote'])
                    dFab: TData = Element(TData, base_type=date, documentation=['Data de Fabricação do medicamento (AAAA-MM-DD)'])
                    dVal: TData = Element(TData, base_type=date, documentation=['Data de validade do medicamento (AAAA-MM-DD)'])
                    vPMC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Preço Máximo ao Consumidor'])
                med: List[med] = Element(med, max_occurs=500, documentation=['grupo do detalhamento de Medicamentos e de matérias-primas farmacêuticas'])

                class arma(ComplexType):
                    """Armamentos"""
                    _max_occurs = 500

                    def add(self, tpArma=None, nSerie=None, nCano=None, descr=None) -> TNFe.infNFe.det.prod.arma:
                        return super().add(tpArma=tpArma, nSerie=nSerie, nCano=nCano, descr=descr)

                    tpArma: str = Element(str, documentation=['Indicador do tipo de arma de fogo (0 - Uso permitido; 1 - Uso restrito)'])
                    nSerie: str = Element(str, documentation=['Número de série da arma'])
                    nCano: str = Element(str, documentation=['Número de série do cano'])
                    descr: str = Element(str, documentation=['Descrição completa da arma, compreendendo: calibre, marca, capacidade, tipo de funcionamento, comprimento e demais elementos que permitam a sua perfeita identificação.'])
                arma: List[arma] = Element(arma, max_occurs=500, documentation=['Armamentos'])

                class comb(ComplexType):
                    """Informar apenas para operações com combustíveis líquidos"""
                    cProdANP: str = Element(str, documentation=['Código de produto da ANP. codificação de produtos do SIMP (http://www.anp.gov.br)'])
                    pMixGN: TDec_0204v = Element(TDec_0204v, tipo="N", tam=(2, 4), base_type=Decimal, documentation=['Percentual de gas natural para o produto GLP'])
                    CODIF: str = Element(str, documentation=['Código de autorização / registro do CODIF. Informar apenas quando a UF utilizar o CODIF (Sistema de Controle do \t\t\tDiferimento do Imposto nas Operações com AEAC - Álcool Etílico Anidro Combustível).'])
                    qTemp: TDec_1204temperatura = Element(TDec_1204temperatura, tipo="N", tam=(12, 4), base_type=Decimal, documentation=['Quantidade de combustível\nfaturada à temperatura ambiente.\nInformar quando a quantidade\nfaturada informada no campo\nqCom (I10) tiver sido ajustada para\numa temperatura diferente da\nambiente.'])
                    UFCons: TUf = Element(TUf, documentation=['Sigla da UF de Consumo'])

                    class CIDE(ComplexType):
                        """CIDE Combustíveis"""
                        qBCProd: TDec_1204v = Element(TDec_1204v, tipo="N", tam=(12, 4), base_type=Decimal, documentation=['BC do CIDE ( Quantidade comercializada) '])
                        vAliqProd: TDec_1104 = Element(TDec_1104, tipo="N", tam=(11, 4), base_type=Decimal, documentation=['Alíquota do CIDE  (em reais)'])
                        vCIDE: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do CIDE'])
                    CIDE: CIDE = Element(CIDE, documentation=['CIDE Combustíveis'])

                    class encerrante(ComplexType):
                        """Informações do grupo de \"encerrante\""""
                        nBico: str = Element(str, documentation=['Numero de identificação do Bico utilizado no abastecimento'])
                        nBomba: str = Element(str, documentation=['Numero de identificação da bomba ao qual o bico está interligado'])
                        nTanque: str = Element(str, documentation=['Numero de identificação do tanque ao qual o bico está interligado'])
                        vEncIni: TDec_1203 = Element(TDec_1203, tipo="N", tam=(12, 3), base_type=Decimal, documentation=['Valor do Encerrante no ínicio do abastecimento'])
                        vEncFin: TDec_1203 = Element(TDec_1203, tipo="N", tam=(12, 3), base_type=Decimal, documentation=['Valor do Encerrante no final do abastecimento'])
                    encerrante: encerrante = Element(encerrante, documentation=['Informações do grupo de "encerrante"'])
                comb: comb = Element(comb, documentation=['Informar apenas para operações com combustíveis líquidos'])
                nRECOPI: str = Element(str, documentation=['Número do RECOPI'])
            prod: prod = Element(prod, documentation=['Dados dos produtos e serviços da NF-e'])

            class imposto(ComplexType):
                """Tributos incidentes nos produtos ou serviços da NF-e"""
                _choice = [[]]
                vTotTrib: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor estimado total de impostos federais, estaduais e municipais'])

                class ICMS(ComplexType):
                    """Dados do ICMS Normal e ST"""
                    _choice = [['ICMS00', 'ICMS10', 'ICMS20', 'ICMS30', 'ICMS40', 'ICMS51', 'ICMS60', 'ICMS70', 'ICMS90', 'ICMSPart', 'ICMSST', 'ICMSSN101', 'ICMSSN102', 'ICMSSN201', 'ICMSSN202', 'ICMSSN500', 'ICMSSN900']]

                    class ICMS00(ComplexType):
                        """Tributação pelo ICMS
00 - Tributada integralmente"""
                        orig: Torig = Element(Torig, documentation=['origem da mercadoria: 0 - Nacional \n1 - Estrangeira - Importação direta \n2 - Estrangeira - Adquirida no mercado interno \n'])
                        CST: str = Element(str, documentation=['Tributção pelo ICMS\n00 - Tributada integralmente\n'])
                        modBC: str = Element(str, documentation=['Modalidade de determinação da BC do ICMS:\n0 - Margem Valor Agregado (%);\n1 - Pauta (valor);\n2 - Preço Tabelado Máximo (valor);\n3 - Valor da Operação.'])
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS'])
                        pICMS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do ICMS'])
                        vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS'])
                    ICMS00: ICMS00 = Element(ICMS00, documentation=['Tributação pelo ICMS\n00 - Tributada integralmente'])

                    class ICMS10(ComplexType):
                        """Tributação pelo ICMS
10 - Tributada e com cobrança do ICMS por substituição tributária"""
                        orig: Torig = Element(Torig, documentation=['origem da mercadoria: 0 - Nacional \n1 - Estrangeira - Importação direta \n2 - Estrangeira - Adquirida no mercado interno \n'])
                        CST: str = Element(str, documentation=['10 - Tributada e com cobrança do ICMS por substituição tributária '])
                        modBC: str = Element(str, documentation=['Modalidade de determinação da BC do ICMS:\n0 - Margem Valor Agregado (%);\n1 - Pauta (valor);\n2 - Preço Tabelado Máximo (valor);\n3 - Valor da Operação.'])
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS'])
                        pICMS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do ICMS'])
                        vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS'])
                        modBCST: str = Element(str, documentation=['Modalidade de determinação da BC do ICMS ST:\n0 – Preço tabelado ou máximo  sugerido;\n1 - Lista Negativa (valor);\n2 - Lista Positiva (valor);\n3 - Lista Neutra (valor);\n4 - Margem Valor Agregado (%);\n5 - Pauta (valor);'])
                        pMVAST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2), base_type=Decimal, optional=True, documentation=['Percentual da Margem de Valor Adicionado ICMS ST'])
                        pRedBCST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2), base_type=Decimal, optional=True, documentation=['Percentual de redução da BC ICMS ST '])
                        vBCST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS ST'])
                        pICMSST: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do ICMS ST'])
                        vICMSST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS ST'])
                    ICMS10: ICMS10 = Element(ICMS10, documentation=['Tributação pelo ICMS\n10 - Tributada e com cobrança do ICMS por substituição tributária '])

                    class ICMS20(ComplexType):
                        """Tributção pelo ICMS
20 - Com redução de base de cálculo"""
                        orig: Torig = Element(Torig, documentation=['origem da mercadoria: 0 - Nacional \n1 - Estrangeira - Importação direta \n2 - Estrangeira - Adquirida no mercado interno \n'])
                        CST: str = Element(str, documentation=['Tributção pelo ICMS\n20 - Com redução de base de cálculo'])
                        modBC: str = Element(str, documentation=['Modalidade de determinação da BC do ICMS:\n0 - Margem Valor Agregado (%);\n1 - Pauta (valor);\n2 - Preço Tabelado Máximo (valor);\n3 - Valor da Operação.'])
                        pRedBC: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Percentual de redução da BC'])
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS'])
                        pICMS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do ICMS'])
                        vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS'])
                        vICMSDeson: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS de desoneração'])
                        motDesICMS: str = Element(str, documentation=['Motivo da desoneração do ICMS:3-Uso na agropecuária;9-Outros;12-Fomento agropecuário'])
                    ICMS20: ICMS20 = Element(ICMS20, documentation=['Tributção pelo ICMS\n20 - Com redução de base de cálculo '])

                    class ICMS30(ComplexType):
                        """Tributação pelo ICMS
30 - Isenta ou não tributada e com cobrança do ICMS por substituição tributária"""
                        orig: Torig = Element(Torig, documentation=['origem da mercadoria: 0 - Nacional \n1 - Estrangeira - Importação direta \n2 - Estrangeira - Adquirida no mercado interno \n'])
                        CST: str = Element(str, documentation=['Tributção pelo ICMS\n30 - Isenta ou não tributada e com cobrança do ICMS por substituição tributária '])
                        modBCST: str = Element(str, documentation=['Modalidade de determinação da BC do ICMS ST:\n0 – Preço tabelado ou máximo  sugerido;\n1 - Lista Negativa (valor);\n2 - Lista Positiva (valor);\n3 - Lista Neutra (valor);\n4 - Margem Valor Agregado (%);\n5 - Pauta (valor).'])
                        pMVAST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2), base_type=Decimal, optional=True, documentation=['Percentual da Margem de Valor Adicionado ICMS ST'])
                        pRedBCST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2), base_type=Decimal, optional=True, documentation=['Percentual de redução da BC ICMS ST '])
                        vBCST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS ST'])
                        pICMSST: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do ICMS ST'])
                        vICMSST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS ST'])
                        vICMSDeson: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS de desoneração'])
                        motDesICMS: str = Element(str, documentation=['Motivo da desoneração do ICMS:6-Utilitários Motocicleta AÁrea Livre;7-SUFRAMA;9-Outros'])
                    ICMS30: ICMS30 = Element(ICMS30, documentation=['Tributação pelo ICMS\n30 - Isenta ou não tributada e com cobrança do ICMS por substituição tributária'])

                    class ICMS40(ComplexType):
                        """Tributação pelo ICMS
40 - Isenta 
41 - Não tributada 
50 - Suspensão"""
                        orig: Torig = Element(Torig, documentation=['origem da mercadoria: 0 - Nacional \n1 - Estrangeira - Importação direta \n2 - Estrangeira - Adquirida no mercado interno \n'])
                        CST: str = Element(str, documentation=['Tributação pelo ICMS \n40 - Isenta \n41 - Não tributada \n50 - Suspensão \n51 - Diferimento '])
                        vICMSDeson: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['O valor do ICMS será informado apenas nas operações com veículos beneficiados com a desoneração condicional do ICMS.'])
                        motDesICMS: str = Element(str, documentation=['Este campo será preenchido quando o campo anterior estiver preenchido.\nInformar o motivo da desoneração:\n1 – Táxi;\n3 – Produtor Agropecuário;\n4 – Frotista/Locadora;\n5 – Diplomático/Consular;\n6 – Utilitários e Motocicletas da Amazônia Ocidental e Áreas de Livre Comércio (Resolução 714/88 e 790/94 – CONTRAN e suas alterações);\n7 – SUFRAMA;\n8 - Venda a órgão Público;\n9 – Outros\n10- Deficiente Condutor\n11- Deficiente não condutor\n16 - Olimpíadas Rio 2016\n\t\t\t\t\t\t\t'])
                    ICMS40: ICMS40 = Element(ICMS40, documentation=['Tributação pelo ICMS\n40 - Isenta \n41 - Não tributada \n50 - Suspensão  '])

                    class ICMS51(ComplexType):
                        """Tributção pelo ICMS
51 - Diferimento
A exigência do preenchimento das informações do ICMS diferido fica à critério de cada UF."""
                        orig: Torig = Element(Torig, documentation=['origem da mercadoria: 0 - Nacional \n1 - Estrangeira - Importação direta \n2 - Estrangeira - Adquirida no mercado interno \n'])
                        CST: str = Element(str, documentation=['Tributção pelo ICMS\n20 - Com redução de base de cálculo'])
                        modBC: str = Element(str, documentation=['Modalidade de determinação da BC do ICMS:\n0 - Margem Valor Agregado (%);\n1 - Pauta (valor);\n2 - Preço Tabelado Máximo (valor);\n3 - Valor da Operação.'])
                        pRedBC: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Percentual de redução da BC'])
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS'])
                        pICMS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do ICMS'])
                        vICMSOp: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS da Operação'])
                        pDif: TDec_0302a04Max100 = Element(TDec_0302a04Max100, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Percentual do diferemento'])
                        vICMSDif: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS da diferido'])
                        vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS'])
                    ICMS51: ICMS51 = Element(ICMS51, documentation=['Tributção pelo ICMS\n51 - Diferimento\nA exigência do preenchimento das informações do ICMS diferido fica à critério de cada UF.'])

                    class ICMS60(ComplexType):
                        """Tributação pelo ICMS
60 - ICMS cobrado anteriormente por substituição tributária"""
                        orig: Torig = Element(Torig, documentation=['origem da mercadoria: 0 - Nacional \n1 - Estrangeira - Importação direta \n2 - Estrangeira - Adquirida no mercado interno \n'])
                        CST: str = Element(str, documentation=['Tributação pelo ICMS \n60 - ICMS cobrado anteriormente por substituição tributária '])
                        vBCSTRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS ST retido anteriormente'])
                        vICMSSTRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS ST retido anteriormente'])
                    ICMS60: ICMS60 = Element(ICMS60, documentation=['Tributação pelo ICMS\n60 - ICMS cobrado anteriormente por substituição tributária '])

                    class ICMS70(ComplexType):
                        """Tributação pelo ICMS 
70 - Com redução de base de cálculo e cobrança do ICMS por substituição tributária"""
                        orig: Torig = Element(Torig, documentation=['origem da mercadoria: 0 - Nacional \n1 - Estrangeira - Importação direta \n2 - Estrangeira - Adquirida no mercado interno \n'])
                        CST: str = Element(str, documentation=['Tributção pelo ICMS\n70 - Com redução de base de cálculo e cobrança do ICMS por substituição tributária '])
                        modBC: str = Element(str, documentation=['Modalidade de determinação da BC do ICMS:\n0 - Margem Valor Agregado (%);\n1 - Pauta (valor);\n2 - Preço Tabelado Máximo (valor);\n3 - Valor da Operação.'])
                        pRedBC: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Percentual de redução da BC'])
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS'])
                        pICMS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do ICMS'])
                        vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS'])
                        modBCST: str = Element(str, documentation=['Modalidade de determinação da BC do ICMS ST:\n0 – Preço tabelado ou máximo  sugerido;\n1 - Lista Negativa (valor);\n2 - Lista Positiva (valor);\n3 - Lista Neutra (valor);\n4 - Margem Valor Agregado (%);\n5 - Pauta (valor).'])
                        pMVAST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2), base_type=Decimal, optional=True, documentation=['Percentual da Margem de Valor Adicionado ICMS ST'])
                        pRedBCST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2), base_type=Decimal, optional=True, documentation=['Percentual de redução da BC ICMS ST '])
                        vBCST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS ST'])
                        pICMSST: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do ICMS ST'])
                        vICMSST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS ST'])
                        vICMSDeson: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS de desoneração'])
                        motDesICMS: str = Element(str, documentation=['Motivo da desoneração do ICMS:3-Uso na agropecuária;9-Outros;12-Fomento agropecuário'])
                    ICMS70: ICMS70 = Element(ICMS70, documentation=['Tributação pelo ICMS \n70 - Com redução de base de cálculo e cobrança do ICMS por substituição tributária '])

                    class ICMS90(ComplexType):
                        """Tributação pelo ICMS
90 - Outras"""
                        orig: Torig = Element(Torig, documentation=['origem da mercadoria: 0 - Nacional \n1 - Estrangeira - Importação direta \n2 - Estrangeira - Adquirida no mercado interno \n'])
                        CST: str = Element(str, documentation=['Tributção pelo ICMS\n90 - Outras'])
                        modBC: str = Element(str, documentation=['Modalidade de determinação da BC do ICMS: \n0 - Margem Valor Agregado (%);\n1 - Pauta (valor);\n2 - Preço Tabelado Máximo (valor);\n3 - Valor da Operação.'])
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS'])
                        pRedBC: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2), base_type=Decimal, optional=True, documentation=['Percentual de redução da BC'])
                        pICMS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do ICMS'])
                        vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS'])
                        modBCST: str = Element(str, documentation=['Modalidade de determinação da BC do ICMS ST:\n0 – Preço tabelado ou máximo  sugerido;\n1 - Lista Negativa (valor);\n2 - Lista Positiva (valor);\n3 - Lista Neutra (valor);\n4 - Margem Valor Agregado (%);\n5 - Pauta (valor).'])
                        pMVAST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2), base_type=Decimal, optional=True, documentation=['Percentual da Margem de Valor Adicionado ICMS ST'])
                        pRedBCST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2), base_type=Decimal, optional=True, documentation=['Percentual de redução da BC ICMS ST '])
                        vBCST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS ST'])
                        pICMSST: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do ICMS ST'])
                        vICMSST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS ST'])
                        vICMSDeson: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS de desoneração'])
                        motDesICMS: str = Element(str, documentation=['Motivo da desoneração do ICMS:3-Uso na agropecuária;9-Outros;12-Fomento agropecuário'])
                    ICMS90: ICMS90 = Element(ICMS90, documentation=['Tributação pelo ICMS\n90 - Outras'])

                    class ICMSPart(ComplexType):
                        """Partilha do ICMS entre a UF de origem e UF de destino ou a UF definida na legislação
Operação interestadual para consumidor final com partilha do ICMS  devido na operação entre a UF de origem e a UF do destinatário ou ou a UF definida na legislação. (Ex. UF da concessionária de entrega do  veículos)"""
                        orig: Torig = Element(Torig, documentation=['origem da mercadoria: 0 - Nacional \n1 - Estrangeira - Importação direta \n2 - Estrangeira - Adquirida no mercado interno \n'])
                        CST: str = Element(str, documentation=['Tributação pelo ICMS \n10 - Tributada e com cobrança do ICMS por substituição tributária;\n90 – Outros.'])
                        modBC: str = Element(str, documentation=['Modalidade de determinação da BC do ICMS: \n0 - Margem Valor Agregado (%);\n1 - Pauta (valor);\n2 - Preço Tabelado Máximo (valor);\n3 - Valor da Operação.'])
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS'])
                        pRedBC: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2), base_type=Decimal, optional=True, documentation=['Percentual de redução da BC'])
                        pICMS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do ICMS'])
                        vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS'])
                        modBCST: str = Element(str, documentation=['Modalidade de determinação da BC do ICMS ST:\n0 – Preço tabelado ou máximo  sugerido;\n1 - Lista Negativa (valor);\n2 - Lista Positiva (valor);\n3 - Lista Neutra (valor);\n4 - Margem Valor Agregado (%);\n5 - Pauta (valor).'])
                        pMVAST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2), base_type=Decimal, optional=True, documentation=['Percentual da Margem de Valor Adicionado ICMS ST'])
                        pRedBCST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2), base_type=Decimal, optional=True, documentation=['Percentual de redução da BC ICMS ST'])
                        vBCST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS ST'])
                        pICMSST: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do ICMS ST'])
                        vICMSST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS ST'])
                        pBCOp: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2), base_type=Decimal, optional=True, documentation=['Percentual para determinação do valor  da Base de Cálculo da operação própria.'])
                        UFST: TUf = Element(TUf, documentation=['Sigla da UF para qual é devido o ICMS ST da operação.'])
                    ICMSPart: ICMSPart = Element(ICMSPart, documentation=['Partilha do ICMS entre a UF de origem e UF de destino ou a UF definida na legislação\nOperação interestadual para consumidor final com partilha do ICMS  devido na operação entre a UF de origem e a UF do destinatário ou ou a UF definida na legislação. (Ex. UF da concessionária de entrega do  veículos)'])

                    class ICMSST(ComplexType):
                        """Grupo de informação do ICMSST devido para a UF de destino, nas operações interestaduais de produtos que tiveram retenção antecipada de ICMS por ST na UF do remetente. Repasse via Substituto Tributário."""
                        orig: Torig = Element(Torig, documentation=['origem da mercadoria: 0 - Nacional \n1 - Estrangeira - Importação direta \n2 - Estrangeira - Adquirida no mercado interno \n'])
                        CST: str = Element(str, documentation=['Tributção pelo ICMS\n41-Não Tributado'])
                        vBCSTRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Informar o valor da BC do ICMS ST retido na UF remetente'])
                        vICMSSTRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=[' Informar o valor do ICMS ST retido na UF remetente (iv2.0))'])
                        vBCSTDest: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=[' Informar o valor da BC do ICMS ST da UF destino'])
                        vICMSSTDest: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Informar o valor da BC do ICMS ST da UF destino (v2.0)'])
                    ICMSST: ICMSST = Element(ICMSST, documentation=['Grupo de informação do ICMSST devido para a UF de destino, nas operações interestaduais de produtos que tiveram retenção antecipada de ICMS por ST na UF do remetente. Repasse via Substituto Tributário.'])

                    class ICMSSN101(ComplexType):
                        """Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=101 (v.2.0)"""
                        orig: Torig = Element(Torig, documentation=['origem da mercadoria: 0 - Nacional \n1 - Estrangeira - Importação direta \n2 - Estrangeira - Adquirida no mercado interno \n(v2.0)'])
                        CSOSN: str = Element(str, documentation=['101- Tributada pelo Simples Nacional com permissão de crédito. (v.2.0)'])
                        pCredSN: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota aplicável de cálculo do crédito (Simples Nacional). (v2.0)'])
                        vCredICMSSN: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor crédito do ICMS que pode ser aproveitado nos termos do art. 23 da LC 123 (Simples Nacional) (v2.0)'])
                    ICMSSN101: ICMSSN101 = Element(ICMSSN101, documentation=['Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=101 (v.2.0)'])

                    class ICMSSN102(ComplexType):
                        """Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=102, 103, 300 ou 400 (v.2.0))"""
                        orig: Torig = Element(Torig, documentation=['origem da mercadoria: 0 - Nacional \n1 - Estrangeira - Importação direta \n2 - Estrangeira - Adquirida no mercado interno \n(v2.0)'])
                        CSOSN: str = Element(str, documentation=['102- Tributada pelo Simples Nacional sem permissão de crédito. \n103 – Isenção do ICMS  no Simples Nacional para faixa de receita bruta.\n300 – Imune.\n400 – Não tributda pelo Simples Nacional (v.2.0) (v.2.0)'])
                    ICMSSN102: ICMSSN102 = Element(ICMSSN102, documentation=['Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=102, 103, 300 ou 400 (v.2.0))'])

                    class ICMSSN201(ComplexType):
                        """Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=201 (v.2.0)"""
                        orig: Torig = Element(Torig, documentation=['Origem da mercadoria:\n0 – Nacional;\n1 – Estrangeira – Importação direta;\n2 – Estrangeira – Adquirida no mercado interno. (v2.0)'])
                        CSOSN: str = Element(str, documentation=['201- Tributada pelo Simples Nacional com permissão de crédito e com cobrança do ICMS por Substituição Tributária (v.2.0)'])
                        modBCST: str = Element(str, documentation=['Modalidade de determinação da BC do ICMS ST:\n0 – Preço tabelado ou máximo  sugerido;\n1 - Lista Negativa (valor);\n2 - Lista Positiva (valor);\n3 - Lista Neutra (valor);\n4 - Margem Valor Agregado (%);\n5 - Pauta (valor). (v2.0)'])
                        pMVAST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2), base_type=Decimal, optional=True, documentation=['Percentual da Margem de Valor Adicionado ICMS ST (v2.0)'])
                        pRedBCST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2), base_type=Decimal, optional=True, documentation=['Percentual de redução da BC ICMS ST  (v2.0)'])
                        vBCST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS ST (v2.0)'])
                        pICMSST: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do ICMS ST (v2.0)'])
                        vICMSST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS ST (v2.0)'])
                        pCredSN: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota aplicável de cálculo do crédito (Simples Nacional). (v2.0)'])
                        vCredICMSSN: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor crédito do ICMS que pode ser aproveitado nos termos do art. 23 da LC 123 (Simples Nacional) (v2.0)'])
                    ICMSSN201: ICMSSN201 = Element(ICMSSN201, documentation=['Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=201 (v.2.0)'])

                    class ICMSSN202(ComplexType):
                        """Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=202 ou 203 (v.2.0)"""
                        orig: Torig = Element(Torig, documentation=['Origem da mercadoria:\n0 – Nacional;\n1 – Estrangeira – Importação direta;\n2 – Estrangeira – Adquirida no mercado interno. (v2.0)'])
                        CSOSN: str = Element(str, documentation=['202- Tributada pelo Simples Nacional sem permissão de crédito e com cobrança do ICMS por Substituição Tributária;\n203-  Isenção do ICMS nos Simples Nacional para faixa de receita bruta e com cobrança do ICMS por Substituição Tributária (v.2.0)'])
                        modBCST: str = Element(str, documentation=['Modalidade de determinação da BC do ICMS ST:\n0 – Preço tabelado ou máximo  sugerido;\n1 - Lista Negativa (valor);\n2 - Lista Positiva (valor);\n3 - Lista Neutra (valor);\n4 - Margem Valor Agregado (%);\n5 - Pauta (valor). (v2.0)'])
                        pMVAST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2), base_type=Decimal, optional=True, documentation=['Percentual da Margem de Valor Adicionado ICMS ST (v2.0)'])
                        pRedBCST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2), base_type=Decimal, optional=True, documentation=['Percentual de redução da BC ICMS ST  (v2.0)'])
                        vBCST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS ST (v2.0)'])
                        pICMSST: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do ICMS ST (v2.0)'])
                        vICMSST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS ST (v2.0)'])
                    ICMSSN202: ICMSSN202 = Element(ICMSSN202, documentation=['Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=202 ou 203 (v.2.0)'])

                    class ICMSSN500(ComplexType):
                        """Tributação do ICMS pelo SIMPLES NACIONAL,CRT=1 – Simples Nacional e CSOSN=500 (v.2.0)"""
                        orig: Torig = Element(Torig, documentation=['origem da mercadoria: 0 - Nacional \n1 - Estrangeira - Importação direta \n2 - Estrangeira - Adquirida no mercado interno \n'])
                        CSOSN: str = Element(str, documentation=['500 – ICMS cobrado anterirmente por substituição tributária (substituído) ou por antecipação\n(v.2.0)'])
                        vBCSTRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS ST retido anteriormente (v2.0) '])
                        vICMSSTRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS ST retido anteriormente  (v2.0)'])
                    ICMSSN500: ICMSSN500 = Element(ICMSSN500, documentation=['Tributação do ICMS pelo SIMPLES NACIONAL,CRT=1 – Simples Nacional e CSOSN=500 (v.2.0)'])

                    class ICMSSN900(ComplexType):
                        """Tributação do ICMS pelo SIMPLES NACIONAL, CRT=1 – Simples Nacional e CSOSN=900 (v2.0)"""
                        orig: Torig = Element(Torig, documentation=['origem da mercadoria: 0 - Nacional \n1 - Estrangeira - Importação direta \n2 - Estrangeira - Adquirida no mercado interno \n'])
                        CSOSN: str = Element(str, documentation=['Tributação pelo ICMS 900 - Outros(v2.0)'])
                        modBC: str = Element(str, documentation=['Modalidade de determinação da BC do ICMS: \n0 - Margem Valor Agregado (%);\n1 - Pauta (valor);\n2 - Preço Tabelado Máximo (valor);\n3 - Valor da Operação.'])
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS'])
                        pRedBC: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2), base_type=Decimal, optional=True, documentation=['Percentual de redução da BC'])
                        pICMS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do ICMS'])
                        vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS'])
                        modBCST: str = Element(str, documentation=['Modalidade de determinação da BC do ICMS ST:\n0 – Preço tabelado ou máximo  sugerido;\n1 - Lista Negativa (valor);\n2 - Lista Positiva (valor);\n3 - Lista Neutra (valor);\n4 - Margem Valor Agregado (%);\n5 - Pauta (valor).'])
                        pMVAST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2), base_type=Decimal, optional=True, documentation=['Percentual da Margem de Valor Adicionado ICMS ST'])
                        pRedBCST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2), base_type=Decimal, optional=True, documentation=['Percentual de redução da BC ICMS ST '])
                        vBCST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS ST'])
                        pICMSST: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do ICMS ST'])
                        vICMSST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS ST'])
                        pCredSN: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota aplicável de cálculo do crédito (Simples Nacional). (v2.0)'])
                        vCredICMSSN: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor crédito do ICMS que pode ser aproveitado nos termos do art. 23 da LC 123 (Simples Nacional) (v2.0)'])
                    ICMSSN900: ICMSSN900 = Element(ICMSSN900, documentation=['Tributação do ICMS pelo SIMPLES NACIONAL, CRT=1 – Simples Nacional e CSOSN=900 (v2.0)'])
                ICMS: ICMS = Element(ICMS, documentation=['Dados do ICMS Normal e ST'])
                IPI: TIpi = Element(TIpi)

                class II(ComplexType):
                    """Dados do Imposto de Importação"""
                    vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Base da BC do Imposto de Importação'])
                    vDespAdu: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor das despesas aduaneiras'])
                    vII: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do Imposto de Importação'])
                    vIOF: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do Imposto sobre Operações Financeiras'])
                II: II = Element(II, documentation=['Dados do Imposto de Importação'])
                IPI: TIpi = Element(TIpi)

                class ISSQN(ComplexType):
                    """ISSQN"""
                    vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ISSQN'])
                    vAliq: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do ISSQN'])
                    vISSQN: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da do ISSQN'])
                    cMunFG: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Informar o município de ocorrência do fato gerador do ISSQN. Utilizar a Tabela do IBGE (Anexo VII - Tabela de UF, Município e País). “Atenção, não vincular com os campos B12, C10 ou E10” v2.0'])
                    cListServ: TCListServ = Element(TCListServ, documentation=['Informar o Item da lista de serviços da LC 116/03 em que se classifica o serviço.'])
                    vDeducao: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor dedução para redução da base de cálculo'])
                    vOutro: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor outras retenções'])
                    vDescIncond: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor desconto incondicionado'])
                    vDescCond: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor desconto condicionado'])
                    vISSRet: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor Retenção ISS'])
                    indISS: str = Element(str, documentation=['Exibilidade do ISS:1-Exigível;2-Não incidente;3-Isenção;4-Exportação;5-Imunidade;6-Exig.Susp. Judicial;7-Exig.Susp. ADM'])
                    cServico: str = Element(str, documentation=['Código do serviço prestado dentro do município'])
                    cMun: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do Município de Incidência do Imposto'])
                    cPais: str = Element(str, documentation=['Código de Pais'])
                    nProcesso: str = Element(str, documentation=['Número do Processo administrativo ou judicial de suspenção do processo'])
                    indIncentivo: str = Element(str, documentation=['Indicador de Incentivo Fiscal. 1=Sim; 2=Não'])
                ISSQN: ISSQN = Element(ISSQN, documentation=['ISSQN'])

                class PIS(ComplexType):
                    """Dados do PIS"""
                    _choice = [['PISAliq', 'PISQtde', 'PISNT', 'PISOutr']]

                    class PISAliq(ComplexType):
                        """Código de Situação Tributária do PIS.
 01 – Operação Tributável - Base de Cálculo = Valor da Operação Alíquota Normal (Cumulativo/Não Cumulativo);
02 - Operação Tributável - Base de Calculo = Valor da Operação (Alíquota Diferenciada);"""
                        CST: str = Element(str, documentation=['Código de Situação Tributária do PIS.\n 01 – Operação Tributável - Base de Cálculo = Valor da Operação Alíquota Normal (Cumulativo/Não Cumulativo);\n02 - Operação Tributável - Base de Calculo = Valor da Operação (Alíquota Diferenciada);'])
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do PIS'])
                        pPIS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do PIS (em percentual)'])
                        vPIS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do PIS'])
                    PISAliq: PISAliq = Element(PISAliq, documentation=['Código de Situação Tributária do PIS.\n 01 – Operação Tributável - Base de Cálculo = Valor da Operação Alíquota Normal (Cumulativo/Não Cumulativo);\n02 - Operação Tributável - Base de Calculo = Valor da Operação (Alíquota Diferenciada);'])

                    class PISQtde(ComplexType):
                        """Código de Situação Tributária do PIS.
03 - Operação Tributável - Base de Calculo = Quantidade Vendida x Alíquota por Unidade de Produto;"""
                        CST: str = Element(str, documentation=['Código de Situação Tributária do PIS.\n03 - Operação Tributável - Base de Calculo = Quantidade Vendida x Alíquota por Unidade de Produto;'])
                        qBCProd: TDec_1204v = Element(TDec_1204v, tipo="N", tam=(12, 4), base_type=Decimal, documentation=['Quantidade Vendida  (NT2011/004)'])
                        vAliqProd: TDec_1104v = Element(TDec_1104v, tipo="N", tam=(11, 4), base_type=Decimal, documentation=['Alíquota do PIS (em reais) (NT2011/004)'])
                        vPIS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do PIS'])
                    PISQtde: PISQtde = Element(PISQtde, documentation=['Código de Situação Tributária do PIS.\n03 - Operação Tributável - Base de Calculo = Quantidade Vendida x Alíquota por Unidade de Produto;'])

                    class PISNT(ComplexType):
                        """Código de Situação Tributária do PIS.
04 - Operação Tributável - Tributação Monofásica - (Alíquota Zero);
06 - Operação Tributável - Alíquota Zero;
07 - Operação Isenta da contribuição;
08 - Operação Sem Incidência da contribuição;
09 - Operação com suspensão da contribuição;"""
                        CST: str = Element(str, documentation=['Código de Situação Tributária do PIS.\n04 - Operação Tributável - Tributação Monofásica - (Alíquota Zero);\n05 - Operação Tributável (ST);\n06 - Operação Tributável - Alíquota Zero;\n07 - Operação Isenta da contribuição;\n08 - Operação Sem Incidência da contribuição;\n09 - Operação com suspensão da contribuição;'])
                    PISNT: PISNT = Element(PISNT, documentation=['Código de Situação Tributária do PIS.\n04 - Operação Tributável - Tributação Monofásica - (Alíquota Zero);\n06 - Operação Tributável - Alíquota Zero;\n07 - Operação Isenta da contribuição;\n08 - Operação Sem Incidência da contribuição;\n09 - Operação com suspensão da contribuição;'])

                    class PISOutr(ComplexType):
                        """Código de Situação Tributária do PIS.
99 - Outras Operações."""
                        _choice = [[]]
                        CST: str = Element(str, documentation=['Código de Situação Tributária do PIS.\n99 - Outras Operações.'])
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do PIS'])
                        pPIS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do PIS (em percentual)'])
                        qBCProd: TDec_1204v = Element(TDec_1204v, tipo="N", tam=(12, 4), base_type=Decimal, documentation=['Quantidade Vendida (NT2011/004) '])
                        vAliqProd: TDec_1104v = Element(TDec_1104v, tipo="N", tam=(11, 4), base_type=Decimal, documentation=['Alíquota do PIS (em reais) (NT2011/004)'])
                        vPIS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do PIS'])
                    PISOutr: PISOutr = Element(PISOutr, documentation=['Código de Situação Tributária do PIS.\n99 - Outras Operações.'])
                PIS: PIS = Element(PIS, documentation=['Dados do PIS'])

                class PISST(ComplexType):
                    """Dados do PIS Substituição Tributária"""
                    _choice = [[]]
                    vBC: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor da BC do PIS ST'])
                    pPIS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do PIS ST (em percentual)'])
                    qBCProd: TDec_1204 = Element(TDec_1204, tipo="N", tam=(12, 4), base_type=Decimal, documentation=['Quantidade Vendida '])
                    vAliqProd: TDec_1104 = Element(TDec_1104, tipo="N", tam=(11, 4), base_type=Decimal, documentation=['Alíquota do PIS ST (em reais)'])
                    vPIS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do PIS ST'])
                PISST: PISST = Element(PISST, documentation=['Dados do PIS Substituição Tributária'])

                class COFINS(ComplexType):
                    """Dados do COFINS"""
                    _choice = [['COFINSAliq', 'COFINSQtde', 'COFINSNT', 'COFINSOutr']]

                    class COFINSAliq(ComplexType):
                        """Código de Situação Tributária do COFINS.
 01 – Operação Tributável - Base de Cálculo = Valor da Operação Alíquota Normal (Cumulativo/Não Cumulativo);
02 - Operação Tributável - Base de Calculo = Valor da Operação (Alíquota Diferenciada);"""
                        CST: str = Element(str, documentation=['Código de Situação Tributária do COFINS.\n 01 – Operação Tributável - Base de Cálculo = Valor da Operação Alíquota Normal (Cumulativo/Não Cumulativo);\n02 - Operação Tributável - Base de Calculo = Valor da Operação (Alíquota Diferenciada);'])
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do COFINS'])
                        pCOFINS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do COFINS (em percentual)'])
                        vCOFINS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do COFINS'])
                    COFINSAliq: COFINSAliq = Element(COFINSAliq, documentation=['Código de Situação Tributária do COFINS.\n 01 – Operação Tributável - Base de Cálculo = Valor da Operação Alíquota Normal (Cumulativo/Não Cumulativo);\n02 - Operação Tributável - Base de Calculo = Valor da Operação (Alíquota Diferenciada);'])

                    class COFINSQtde(ComplexType):
                        """Código de Situação Tributária do COFINS.
03 - Operação Tributável - Base de Calculo = Quantidade Vendida x Alíquota por Unidade de Produto;"""
                        CST: str = Element(str, documentation=['Código de Situação Tributária do COFINS.\n03 - Operação Tributável - Base de Calculo = Quantidade Vendida x Alíquota por Unidade de Produto;'])
                        qBCProd: TDec_1204v = Element(TDec_1204v, tipo="N", tam=(12, 4), base_type=Decimal, documentation=['Quantidade Vendida (NT2011/004)'])
                        vAliqProd: TDec_1104v = Element(TDec_1104v, tipo="N", tam=(11, 4), base_type=Decimal, documentation=['Alíquota do COFINS (em reais) (NT2011/004)'])
                        vCOFINS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do COFINS'])
                    COFINSQtde: COFINSQtde = Element(COFINSQtde, documentation=['Código de Situação Tributária do COFINS.\n03 - Operação Tributável - Base de Calculo = Quantidade Vendida x Alíquota por Unidade de Produto;'])

                    class COFINSNT(ComplexType):
                        """Código de Situação Tributária do COFINS:
04 - Operação Tributável - Tributação Monofásica - (Alíquota Zero);
06 - Operação Tributável - Alíquota Zero;
07 - Operação Isenta da contribuição;
08 - Operação Sem Incidência da contribuição;
09 - Operação com suspensão da contribuição;"""
                        CST: str = Element(str, documentation=['Código de Situação Tributária do COFINS:\n04 - Operação Tributável - Tributação Monofásica - (Alíquota Zero);\n05 - Operação Tributável (ST);\n06 - Operação Tributável - Alíquota Zero;\n07 - Operação Isenta da contribuição;\n08 - Operação Sem Incidência da contribuição;\n09 - Operação com suspensão da contribuição;'])
                    COFINSNT: COFINSNT = Element(COFINSNT, documentation=['Código de Situação Tributária do COFINS:\n04 - Operação Tributável - Tributação Monofásica - (Alíquota Zero);\n06 - Operação Tributável - Alíquota Zero;\n07 - Operação Isenta da contribuição;\n08 - Operação Sem Incidência da contribuição;\n09 - Operação com suspensão da contribuição;'])

                    class COFINSOutr(ComplexType):
                        """Código de Situação Tributária do COFINS:
49 - Outras Operações de Saída
50 - Operação com Direito a Crédito - Vinculada Exclusivamente a Receita Tributada no Mercado Interno
51 - Operação com Direito a Crédito – Vinculada Exclusivamente a Receita Não Tributada no Mercado Interno
52 - Operação com Direito a Crédito - Vinculada Exclusivamente a Receita de Exportação
53 - Operação com Direito a Crédito - Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno
54 - Operação com Direito a Crédito - Vinculada a Receitas Tributadas no Mercado Interno e de Exportação
55 - Operação com Direito a Crédito - Vinculada a Receitas Não-Tributadas no Mercado Interno e de Exportação
56 - Operação com Direito a Crédito - Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno, e de Exportação
60 - Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita Tributada no Mercado Interno
61 - Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita Não-Tributada no Mercado Interno
62 - Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita de Exportação
63 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno
64 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas no Mercado Interno e de Exportação
65 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas Não-Tributadas no Mercado Interno e de Exportação
66 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno, e de Exportação
67 - Crédito Presumido - Outras Operações
70 - Operação de Aquisição sem Direito a Crédito
71 - Operação de Aquisição com Isenção
72 - Operação de Aquisição com Suspensão
73 - Operação de Aquisição a Alíquota Zero
74 - Operação de Aquisição sem Incidência da Contribuição
75 - Operação de Aquisição por Substituição Tributária
98 - Outras Operações de Entrada
99 - Outras Operações."""
                        _choice = [[]]
                        CST: str = Element(str, documentation=['Código de Situação Tributária do COFINS:\n49 - Outras Operações de Saída\n50 - Operação com Direito a Crédito - Vinculada Exclusivamente a Receita Tributada no Mercado Interno\n51 - Operação com Direito a Crédito – Vinculada Exclusivamente a Receita Não Tributada no Mercado Interno\n52 - Operação com Direito a Crédito - Vinculada Exclusivamente a Receita de Exportação\n53 - Operação com Direito a Crédito - Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno\n54 - Operação com Direito a Crédito - Vinculada a Receitas Tributadas no Mercado Interno e de Exportação\n55 - Operação com Direito a Crédito - Vinculada a Receitas Não-Tributadas no Mercado Interno e de Exportação\n56 - Operação com Direito a Crédito - Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno, e de Exportação\n60 - Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita Tributada no Mercado Interno\n61 - Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita Não-Tributada no Mercado Interno\n62 - Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita de Exportação\n63 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno\n64 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas no Mercado Interno e de Exportação\n65 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas Não-Tributadas no Mercado Interno e de Exportação\n66 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno, e de Exportação\n67 - Crédito Presumido - Outras Operações\n70 - Operação de Aquisição sem Direito a Crédito\n71 - Operação de Aquisição com Isenção\n72 - Operação de Aquisição com Suspensão\n73 - Operação de Aquisição a Alíquota Zero\n74 - Operação de Aquisição sem Incidência da Contribuição\n75 - Operação de Aquisição por Substituição Tributária\n98 - Outras Operações de Entrada\n99 - Outras Operações.'])
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do COFINS'])
                        pCOFINS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do COFINS (em percentual)'])
                        qBCProd: TDec_1204v = Element(TDec_1204v, tipo="N", tam=(12, 4), base_type=Decimal, documentation=['Quantidade Vendida (NT2011/004) '])
                        vAliqProd: TDec_1104v = Element(TDec_1104v, tipo="N", tam=(11, 4), base_type=Decimal, documentation=['Alíquota do COFINS (em reais) (NT2011/004)'])
                        vCOFINS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do COFINS'])
                    COFINSOutr: COFINSOutr = Element(COFINSOutr, documentation=['Código de Situação Tributária do COFINS:\n49 - Outras Operações de Saída\n50 - Operação com Direito a Crédito - Vinculada Exclusivamente a Receita Tributada no Mercado Interno\n51 - Operação com Direito a Crédito – Vinculada Exclusivamente a Receita Não Tributada no Mercado Interno\n52 - Operação com Direito a Crédito - Vinculada Exclusivamente a Receita de Exportação\n53 - Operação com Direito a Crédito - Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno\n54 - Operação com Direito a Crédito - Vinculada a Receitas Tributadas no Mercado Interno e de Exportação\n55 - Operação com Direito a Crédito - Vinculada a Receitas Não-Tributadas no Mercado Interno e de Exportação\n56 - Operação com Direito a Crédito - Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno, e de Exportação\n60 - Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita Tributada no Mercado Interno\n61 - Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita Não-Tributada no Mercado Interno\n62 - Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita de Exportação\n63 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno\n64 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas no Mercado Interno e de Exportação\n65 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas Não-Tributadas no Mercado Interno e de Exportação\n66 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno, e de Exportação\n67 - Crédito Presumido - Outras Operações\n70 - Operação de Aquisição sem Direito a Crédito\n71 - Operação de Aquisição com Isenção\n72 - Operação de Aquisição com Suspensão\n73 - Operação de Aquisição a Alíquota Zero\n74 - Operação de Aquisição sem Incidência da Contribuição\n75 - Operação de Aquisição por Substituição Tributária\n98 - Outras Operações de Entrada\n99 - Outras Operações.'])
                COFINS: COFINS = Element(COFINS, documentation=['Dados do COFINS'])

                class COFINSST(ComplexType):
                    """Dados do COFINS da
Substituição Tributaria;"""
                    _choice = [[]]
                    vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do COFINS ST'])
                    pCOFINS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do COFINS ST(em percentual)'])
                    qBCProd: TDec_1204 = Element(TDec_1204, tipo="N", tam=(12, 4), base_type=Decimal, documentation=['Quantidade Vendida '])
                    vAliqProd: TDec_1104 = Element(TDec_1104, tipo="N", tam=(11, 4), base_type=Decimal, documentation=['Alíquota do COFINS ST(em reais)'])
                    vCOFINS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do COFINS ST'])
                COFINSST: COFINSST = Element(COFINSST, documentation=['Dados do COFINS da\nSubstituição Tributaria;'])

                class ICMSUFDest(ComplexType):
                    """Grupo a ser informado nas vendas interestarduais para consumidor final, não contribuinte de ICMS"""
                    vBCUFDest: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da Base de Cálculo do ICMS na UF do destinatário. '])
                    pFCPUFDest: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Percentual adicional inserido na alíquota interna da UF de destino, relativo ao Fundo de Combate à Pobreza (FCP) naquela UF. '])
                    pICMSUFDest: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota adotada nas operações internas na UF do destinatário para o produto / mercadoria.'])
                    pICMSInter: str = Element(str, documentation=['Alíquota interestadual das UF envolvidas: - 4% alíquota interestadual para produtos importados; - 7% para os Estados de origem do Sul e Sudeste (exceto ES), destinado para os Estados do Norte e Nordeste  ou ES; - 12% para os demais casos.'])
                    pICMSInterPart: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Percentual de partilha para a UF do destinatário: - 40% em 2016; - 60% em 2017; - 80% em 2018; - 100% a partir de 2019.'])
                    vFCPUFDest: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) da UF de destino.'])
                    vICMSUFDest: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS de partilha para a UF do destinatário. '])
                    vICMSUFRemet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS de partilha para a UF do remetente. Nota: A partir de 2019, este valor será zero.'])
                ICMSUFDest: ICMSUFDest = Element(ICMSUFDest, documentation=['Grupo a ser informado nas vendas interestarduais para consumidor final, não contribuinte de ICMS'])
            imposto: imposto = Element(imposto, documentation=['Tributos incidentes nos produtos ou serviços da NF-e'])

            class impostoDevol(ComplexType):
                pDevol: TDec_0302Max100 = Element(TDec_0302Max100, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Percentual de mercadoria devolvida'])

                class IPI(ComplexType):
                    """Informação de IPI devolvido"""
                    vIPIDevol: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do IPI devolvido'])
                IPI: IPI = Element(IPI, documentation=['Informação de IPI devolvido'])
            impostoDevol: impostoDevol = Element(impostoDevol)
            infAdProd: str = Element(str, documentation=['Informações adicionais do produto (norma referenciada, informações complementares, etc)'])
            nItem: str = Attribute(None)
        det: List[det] = Element(det, max_occurs=990, documentation=['Dados dos detalhes da NF-e'])

        class total(ComplexType):
            """Dados dos totais da NF-e"""

            class ICMSTot(ComplexType):
                """Totais referentes ao ICMS"""
                vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['BC do ICMS'])
                vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Total do ICMS'])
                vICMSDeson: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Total do ICMS desonerado'])
                vFCPUFDest: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor total do ICMS relativo ao Fundo de Combate à Pobreza (FCP) para a UF de destino.'])
                vICMSUFDest: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor total do ICMS de partilha para a UF do destinatário'])
                vICMSUFRemet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor total do ICMS de partilha para a UF do remetente'])
                vBCST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['BC do ICMS ST'])
                vST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Total do ICMS ST'])
                vProd: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Total dos produtos e serviços'])
                vFrete: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Total do Frete'])
                vSeg: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Total do Seguro'])
                vDesc: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Total do Desconto'])
                vII: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Total do II'])
                vIPI: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Total do IPI'])
                vPIS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do PIS'])
                vCOFINS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do COFINS'])
                vOutro: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Outras Despesas acessórias'])
                vNF: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Total da NF-e'])
                vTotTrib: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor estimado total de impostos federais, estaduais e municipais'])
            ICMSTot: ICMSTot = Element(ICMSTot, documentation=['Totais referentes ao ICMS'])

            class ISSQNtot(ComplexType):
                """Totais referentes ao ISSQN"""
                vServ: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor Total dos Serviços sob não-incidência ou não tributados pelo ICMS '])
                vBC: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Base de Cálculo do ISS'])
                vISS: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor Total do ISS'])
                vPIS: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor do PIS sobre serviços'])
                vCOFINS: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor do COFINS sobre serviços'])
                dCompet: TData = Element(TData, base_type=date, documentation=['Data da prestação do serviço  (AAAA-MM-DD)'])
                vDeducao: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor dedução para redução da base de cálculo'])
                vOutro: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor outras retenções'])
                vDescIncond: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor desconto incondicionado'])
                vDescCond: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor desconto condicionado'])
                vISSRet: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor Total Retenção ISS'])
                cRegTrib: str = Element(str, documentation=['Código do regime especial de tributação'])
            ISSQNtot: ISSQNtot = Element(ISSQNtot, documentation=['Totais referentes ao ISSQN'])

            class retTrib(ComplexType):
                """Retenção de Tributos Federais"""
                vRetPIS: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor Retido de PIS'])
                vRetCOFINS: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor Retido de COFINS'])
                vRetCSLL: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor Retido de CSLL'])
                vBCIRRF: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Base de Cálculo do IRRF'])
                vIRRF: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor Retido de IRRF'])
                vBCRetPrev: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Base de Cálculo da Retenção da Previdêncica Social'])
                vRetPrev: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor da Retenção da Previdêncica Social'])
            retTrib: retTrib = Element(retTrib, documentation=['Retenção de Tributos Federais'])
        total: total = Element(total, documentation=['Dados dos totais da NF-e'])

        class transp(ComplexType):
            """Dados dos transportes da NF-e"""
            _choice = [['vagao', 'balsa']]
            modFrete: str = Element(str, documentation=['Modalidade do frete\n0- Por conta do emitente;\n1- Por conta do destinatário/remetente;\n2- Por conta de terceiros;\n9- Sem frete (v2.0)'])

            class transporta(ComplexType):
                """Dados do transportador"""
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
                CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do transportador'])
                CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CPF do transportador'])
                xNome: str = Element(str, documentation=['Razão Social ou nome do transportador'])
                IE: TIeDest = Element(TIeDest, filter=str.isdigit, documentation=['Inscrição Estadual (v2.0)'])
                xEnder: str = Element(str, documentation=['Endereço completo'])
                xMun: str = Element(str, documentation=['Nome do munícipio'])
                UF: TUf = Element(TUf, documentation=['Sigla da UF'])
            transporta: transporta = Element(transporta, documentation=['Dados do transportador'])

            class retTransp(ComplexType):
                """Dados da retenção  ICMS do Transporte"""
                vServ: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do Serviço'])
                vBCRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['BC da Retenção do ICMS'])
                pICMSRet: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota da Retenção'])
                vICMSRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS Retido'])
                CFOP: str = Element(str, documentation=['Código Fiscal de Operações e Prestações'])
                cMunFG: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do Município de Ocorrência do Fato Gerador (utilizar a tabela do IBGE)'])
            retTransp: retTransp = Element(retTransp, documentation=['Dados da retenção  ICMS do Transporte'])
            veicTransp: TVeiculo = Element(TVeiculo, documentation=['Dados do veículo'])
            reboque: List[TVeiculo] = Element(TVeiculo, max_occurs=5, documentation=['Dados do reboque/Dolly (v2.0)'])
            vagao: str = Element(str, documentation=['Identificação do vagão (v2.0)'])
            balsa: str = Element(str, documentation=['Identificação da balsa (v2.0)'])

            class vol(ComplexType):
                """Dados dos volumes"""
                _max_occurs = 5000

                def add(self, qVol=None, esp=None, marca=None, nVol=None, pesoL=None, pesoB=None, lacres=None) -> TNFe.infNFe.transp.vol:
                    return super().add(qVol=qVol, esp=esp, marca=marca, nVol=nVol, pesoL=pesoL, pesoB=pesoB, lacres=lacres)

                qVol: str = Element(str, documentation=['Quantidade de volumes transportados'])
                esp: str = Element(str, documentation=['Espécie dos volumes transportados'])
                marca: str = Element(str, documentation=['Marca dos volumes transportados'])
                nVol: str = Element(str, documentation=['Numeração dos volumes transportados'])
                pesoL: TDec_1203 = Element(TDec_1203, tipo="N", tam=(12, 3), base_type=Decimal, documentation=['Peso líquido (em kg)'])
                pesoB: TDec_1203 = Element(TDec_1203, tipo="N", tam=(12, 3), base_type=Decimal, documentation=['Peso bruto (em kg)'])

                class lacres(ComplexType):
                    _max_occurs = 5000

                    def add(self, nLacre=None) -> TNFe.infNFe.transp.vol.lacres:
                        return super().add(nLacre=nLacre)

                    nLacre: str = Element(str, documentation=['Número dos Lacres'])
                lacres: List[lacres] = Element(lacres, max_occurs=5000)
            vol: List[vol] = Element(vol, max_occurs=5000, documentation=['Dados dos volumes'])
        transp: transp = Element(transp, documentation=['Dados dos transportes da NF-e'])

        class cobr(ComplexType):
            """Dados da cobrança da NF-e"""

            class fat(ComplexType):
                """Dados da fatura"""
                nFat: str = Element(str, documentation=['Número da fatura'])
                vOrig: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor original da fatura'])
                vDesc: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor do desconto da fatura'])
                vLiq: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor líquido da fatura'])
            fat: fat = Element(fat, documentation=['Dados da fatura'])

            class dup(ComplexType):
                """Dados das duplicatas NT 2011/004"""
                _max_occurs = 120

                def add(self, nDup=None, dVenc=None, vDup=None) -> TNFe.infNFe.cobr.dup:
                    return super().add(nDup=nDup, dVenc=dVenc, vDup=vDup)

                nDup: str = Element(str, documentation=['Número da duplicata'])
                dVenc: TData = Element(TData, base_type=date, documentation=['Data de vencimento da duplicata (AAAA-MM-DD)'])
                vDup: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor da duplicata'])
            dup: List[dup] = Element(dup, max_occurs=120, documentation=['Dados das duplicatas NT 2011/004'])
        cobr: cobr = Element(cobr, documentation=['Dados da cobrança da NF-e'])

        class pag(ComplexType):
            """Dados de Pagamento. Obrigatório apenas para (NFC-e) NT 2012/004"""
            _max_occurs = 100

            def add(self, tPag=None, vPag=None, card=None) -> TNFe.infNFe.pag:
                return super().add(tPag=tPag, vPag=vPag, card=card)

            tPag: str = Element(str, documentation=['Forma de Pagamento:01-Dinheiro;02-Cheque;03-Cartão de Crédito;04-Cartão de Débito;05-Crédito Loja;10-Vale Alimentação;11-Vale Refeição;12-Vale Presente;13-Vale Combustível;99 - Outros'])
            vPag: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do Pagamento'])

            class card(ComplexType):
                """Grupo de Cartões"""
                tpIntegra: str = Element(str, documentation=['Tipo de Integração do processo de pagamento com o sistema de automação da empresa/ \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1=Pagamento integrado com o sistema de automação da empresa Ex. equipamento TEF , Comercio Eletronico\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t2=Pagamento não integrado com o sistema de automação da empresa Ex: equipamento POS\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t'])
                CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ da credenciadora de cartão de crédito/débito'])
                tBand: str = Element(str, documentation=['Bandeira da operadora de cartão de crédito/débito:01–Visa; 02–Mastercard; 03–American Express; 04–Sorocred; 99–Outros'])
                cAut: str = Element(str, documentation=['Número de autorização da operação cartão de crédito/débito'])
            card: card = Element(card, documentation=['Grupo de Cartões'])
        pag: List[pag] = Element(pag, max_occurs=100, documentation=['Dados de Pagamento. Obrigatório apenas para (NFC-e) NT 2012/004'])

        class infAdic(ComplexType):
            """Informações adicionais da NF-e"""
            infAdFisco: str = Element(str, documentation=['Informações adicionais de interesse do Fisco (v2.0)'])
            infCpl: str = Element(str, documentation=['Informações complementares de interesse do Contribuinte'])

            class obsCont(ComplexType):
                """Campo de uso livre do contribuinte
informar o nome do campo no atributo xCampo
e o conteúdo do campo no xTexto"""
                _max_occurs = 10

                def add(self, xTexto=None, xCampo=None) -> TNFe.infNFe.infAdic.obsCont:
                    return super().add(xTexto=xTexto, xCampo=xCampo)

                xTexto: str = Element(str)
                xCampo: str = Attribute(None)
            obsCont: List[obsCont] = Element(obsCont, max_occurs=10, documentation=['Campo de uso livre do contribuinte\ninformar o nome do campo no atributo xCampo\ne o conteúdo do campo no xTexto'])

            class obsFisco(ComplexType):
                """Campo de uso exclusivo do Fisco
informar o nome do campo no atributo xCampo
e o conteúdo do campo no xTexto"""
                _max_occurs = 10

                def add(self, xTexto=None, xCampo=None) -> TNFe.infNFe.infAdic.obsFisco:
                    return super().add(xTexto=xTexto, xCampo=xCampo)

                xTexto: str = Element(str)
                xCampo: str = Attribute(None)
            obsFisco: List[obsFisco] = Element(obsFisco, max_occurs=10, documentation=['Campo de uso exclusivo do Fisco\ninformar o nome do campo no atributo xCampo\ne o conteúdo do campo no xTexto'])

            class procRef(ComplexType):
                """Grupo de informações do  processo referenciado"""
                _max_occurs = 100

                def add(self, nProc=None, indProc=None) -> TNFe.infNFe.infAdic.procRef:
                    return super().add(nProc=nProc, indProc=indProc)

                nProc: str = Element(str, documentation=['Indentificador do processo ou ato\nconcessório'])
                indProc: str = Element(str, documentation=['Origem do processo, informar com:\n0 - SEFAZ;\n1 - Justiça Federal;\n2 - Justiça Estadual;\n3 - Secex/RFB;\n9 - Outros'])
            procRef: List[procRef] = Element(procRef, max_occurs=100, documentation=['Grupo de informações do  processo referenciado'])
        infAdic: infAdic = Element(infAdic, documentation=['Informações adicionais da NF-e'])

        class exporta(ComplexType):
            """Informações de exportação"""
            UFSaidaPais: TUfEmi = Element(TUfEmi, documentation=['Sigla da UF de Embarque ou de transposição de fronteira'])
            xLocExporta: str = Element(str, documentation=['Local de Embarque ou de transposição de fronteira'])
            xLocDespacho: str = Element(str, documentation=['Descrição do local de despacho'])
        exporta: exporta = Element(exporta, documentation=['Informações de exportação'])

        class compra(ComplexType):
            """Informações de compras  (Nota de Empenho, Pedido e Contrato)"""
            xNEmp: str = Element(str, documentation=['Informação da Nota de Empenho de compras públicas (NT2011/004)'])
            xPed: str = Element(str, documentation=['Informação do pedido'])
            xCont: str = Element(str, documentation=['Informação do contrato'])
        compra: compra = Element(compra, documentation=['Informações de compras  (Nota de Empenho, Pedido e Contrato)'])

        class cana(ComplexType):
            """Informações de registro aquisições de cana"""
            safra: str = Element(str, documentation=['Identificação da safra'])
            ref: str = Element(str, documentation=['Mês e Ano de Referência, formato: MM/AAAA'])

            class forDia(ComplexType):
                """Fornecimentos diários"""
                _max_occurs = 31

                def add(self, qtde=None, dia=None) -> TNFe.infNFe.cana.forDia:
                    return super().add(qtde=qtde, dia=dia)

                qtde: TDec_1110v = Element(TDec_1110v, tipo="N", tam=(11, 10), base_type=Decimal, documentation=['Quantidade em quilogramas - peso líquido'])
                dia: str = Attribute(None)
            forDia: List[forDia] = Element(forDia, max_occurs=31, documentation=['Fornecimentos diários'])
            qTotMes: TDec_1110v = Element(TDec_1110v, tipo="N", tam=(11, 10), base_type=Decimal, documentation=['Total do mês'])
            qTotAnt: TDec_1110v = Element(TDec_1110v, tipo="N", tam=(11, 10), base_type=Decimal, documentation=['Total Anterior'])
            qTotGer: TDec_1110v = Element(TDec_1110v, tipo="N", tam=(11, 10), base_type=Decimal, documentation=['Total Geral'])

            class deduc(ComplexType):
                """Deduções - Taxas e Contribuições"""
                _max_occurs = 10

                def add(self, xDed=None, vDed=None) -> TNFe.infNFe.cana.deduc:
                    return super().add(xDed=xDed, vDed=vDed)

                xDed: str = Element(str, documentation=['Descrição da Dedução'])
                vDed: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['valor da dedução'])
            deduc: List[deduc] = Element(deduc, max_occurs=10, documentation=['Deduções - Taxas e Contribuições'])
            vFor: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor  dos fornecimentos'])
            vTotDed: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Total das Deduções'])
            vLiqFor: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Líquido dos fornecimentos'])
        cana: cana = Element(cana, documentation=['Informações de registro aquisições de cana'])
        versao: str = Attribute(TVerNFe)
        Id: str = Attribute(None)
    infNFe: infNFe = Element(infNFe, documentation=['Informações da Nota Fiscal eletrônica'])

    class infNFeSupl(ComplexType):
        """Informações suplementares Nota Fiscal"""
        qrCode: str = Element(str, documentation=['Texto com o QR-Code impresso no DANFE NFC-e'])
    infNFeSupl: infNFeSupl = Element(infNFeSupl, documentation=['Informações suplementares Nota Fiscal'])
    Signature: Signature = Element(Signature)



class TProtNFe(Element):
    """Tipo Protocolo de status resultado do processamento da NF-e"""

    class infProt(ComplexType):
        """Dados do protocolo de status"""
        tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
        verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que processou a NF-e'])
        chNFe: TChNFe = Element(TChNFe, documentation=['Chaves de acesso da NF-e, compostas por: UF do emitente, AAMM da emissão da NFe, CNPJ do emitente, modelo, série e número da NF-e e código numérico+DV.'])
        dhRecbto: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e hora de processamento, no formato AAAA-MM-DDTHH:MM:SSTZD. Deve ser preenchida com data e hora da gravação no Banco em caso de Confirmação. Em caso de Rejeição, com data e hora do recebimento do Lote de NF-e enviado.'])
        nProt: TProt = Element(TProt, documentation=['Número do Protocolo de Status da NF-e. 1 posição (1 – Secretaria de Fazenda Estadual 2 – Receita Federal); 2 - códiga da UF - 2 posições ano; 10 seqüencial no ano.'])
        digVal: DigestValueType = Element(DigestValueType, documentation=['Digest Value da NF-e processada. Utilizado para conferir a integridade da NF-e original.'])
        cStat: TStat = Element(TStat, documentation=['Código do status da mensagem enviada.'])
        xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do serviço solicitado.'])
        Id: str = Attribute(ID)
    infProt: infProt = Element(infProt, documentation=['Dados do protocolo de status'])
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerNFe)



class TIdLote(str):
    """Tipo Identificação de Lote"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{1,15}", enumeration=[])
    pass



class TEnviNFe(Element):
    """Tipo Pedido de Concessão de Autorização da Nota Fiscal Eletrônica"""
    idLote: TIdLote = Element(TIdLote)
    indSinc: str = Element(str, documentation=['Indicador de processamento síncrono. 0=NÃO; 1=SIM=Síncrono'])
    NFe: List[TNFe] = Element(TNFe, max_occurs=50)
    versao: str = Attribute(TVerNFe)



class TRetEnviNFe(Element):
    """Tipo Retorno do Pedido de Autorização da Nota Fiscal Eletrônica"""
    _choice = [['infRec', 'protNFe']]
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que recebeu o Lote.'])
    cStat: TStat = Element(TStat, documentation=['Código do status da mensagem enviada.'])
    xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do serviço solicitado.'])
    cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['código da UF de atendimento'])
    dhRecbto: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e hora do recebimento, no formato AAAA-MM-DDTHH:MM:SSTZD'])

    class infRec(ComplexType):
        """Dados do Recibo do Lote"""
        nRec: TRec = Element(TRec, documentation=['Número do Recibo'])
        tMed: TMed = Element(TMed, documentation=['Tempo médio de resposta do serviço (em segundos) dos últimos 5 minutos'])
    infRec: infRec = Element(infRec, documentation=['Dados do Recibo do Lote'])
    protNFe: TProtNFe = Element(TProtNFe, documentation=['Protocolo de status resultado do processamento sincrono da NFC-e '])
    versao: str = Attribute(TVerNFe)



class TConsReciNFe(Element):
    """Tipo Pedido de Consulta do Recido do Lote de Notas Fiscais Eletrônicas"""
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    nRec: TRec = Element(TRec, documentation=['Número do Recibo'])
    versao: str = Attribute(TVerNFe)



class TRetConsReciNFe(Element):
    """Tipo Retorno do Pedido de  Consulta do Recido do Lote de Notas Fiscais Eletrônicas"""
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que processou a NF-e'])
    nRec: TRec = Element(TRec, documentation=['Número do Recibo Consultado'])
    cStat: TStat = Element(TStat, documentation=['Código do status da mensagem enviada.'])
    xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do serviço solicitado.'])
    cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['código da UF de atendimento'])
    dhRecbto: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e hora de processamento, no formato AAAA-MM-DDTHH:MM:SSTZD. Em caso de Rejeição, com data e hora do recebimento do Lote de NF-e enviado.\n\t\t\t\t\t'])
    cMsg: str = Element(str, documentation=['Código da Mensagem (v2.0) \nalterado para tamanho variavel 1-4. (NT2011/004)'])
    xMsg: str = Element(str, documentation=['Mensagem da SEFAZ para o emissor. (v2.0)'])
    protNFe: List[TProtNFe] = Element(TProtNFe, max_occurs=50, documentation=['Protocolo de status resultado do processamento da NF-e'])
    versao: str = Attribute(TVerNFe)



class TNfeProc(Element):
    """Tipo da NF-e processada"""
    NFe: TNFe = Element(TNFe)
    protNFe: TProtNFe = Element(TProtNFe)
    versao: str = Attribute(TVerNFe)


