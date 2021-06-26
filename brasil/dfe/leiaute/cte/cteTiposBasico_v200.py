from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposGeralCTe_v200 import *



class TEndeEmi(Element):
    """Tipo Dados do Endereço"""
    xLgr: str = Element(str, documentation=['Logradouro'])
    nro: str = Element(str, documentation=['Número'])
    xCpl: str = Element(str, documentation=['Complemento'])
    xBairro: str = Element(str, documentation=['Bairro'])
    cMun: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do município (utilizar a tabela do IBGE)'])
    xMun: str = Element(str, documentation=['Nome do município'])
    CEP: str = Element(str, filter=str.isdigit, documentation=['CEP', 'Informar zeros não significativos'])
    UF: TUF_sem_EX = Element(TUF_sem_EX, documentation=['Sigla da UF'])
    fone: TFone = Element(TFone, filter=str.isdigit, documentation=['Telefone'])



class TEndereco(Element):
    """Tipo Dados do Endereço"""
    xLgr: str = Element(str, documentation=['Logradouro'])
    nro: str = Element(str, documentation=['Número'])
    xCpl: str = Element(str, documentation=['Complemento'])
    xBairro: str = Element(str, documentation=['Bairro'])
    cMun: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do município (utilizar a tabela do IBGE)', 'Informar 9999999 para operações com o exterior.'])
    xMun: str = Element(str, documentation=['Nome do município', 'Informar EXTERIOR para operações com o exterior.'])
    CEP: str = Element(str, filter=str.isdigit, documentation=['CEP', 'Informar os zeros não significativos'])
    UF: TUf = Element(TUf, documentation=['Sigla da UF', 'Informar EX para operações com o exterior.'])
    cPais: str = Element(str, documentation=['Código do país', 'Utilizar a tabela do BACEN'])
    xPais: str = Element(str, documentation=['Nome do país'])



class TImp(Element):
    """Tipo Dados do Imposto"""
    _choice = [['ICMS00', 'ICMS20', 'ICMS45', 'ICMS60', 'ICMS90', 'ICMSOutraUF', 'ICMSSN']]

    class ICMS00(ComplexType):
        """Prestação sujeito à tributação normal do ICMS"""
        CST: str = Element(str, documentation=['classificação Tributária do Serviço', '00 - tributação normal ICMS'])
        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS'])
        pICMS: TDec_0302 = Element(TDec_0302, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do ICMS'])
        vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS'])
    ICMS00: ICMS00 = Element(ICMS00, documentation=['Prestação sujeito à tributação normal do ICMS'])

    class ICMS20(ComplexType):
        """Prestação sujeito à tributação com redução de BC do ICMS"""
        CST: str = Element(str, documentation=['Classificação Tributária do serviço', '20 - tributação com BC reduzida do ICMS'])
        pRedBC: TDec_0302Opc = Element(TDec_0302Opc, tipo="N", tam=(3, 2), base_type=Decimal, optional=True, documentation=['Percentual de redução da BC'])
        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS'])
        pICMS: TDec_0302 = Element(TDec_0302, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do ICMS'])
        vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS'])
    ICMS20: ICMS20 = Element(ICMS20, documentation=['Prestação sujeito à tributação com redução de BC do ICMS'])

    class ICMS45(ComplexType):
        """ICMS  Isento, não Tributado ou diferido"""
        CST: str = Element(str, documentation=['Classificação Tributária do Serviço', 'Preencher com:\n\t\t\t\t\t\t\t\t40 - ICMS isenção;\n\t\t\t\t\t\t\t\t41 - ICMS não tributada;\n\t\t\t\t\t\t\t\t51 - ICMS diferido'])
    ICMS45: ICMS45 = Element(ICMS45, documentation=['ICMS  Isento, não Tributado ou diferido'])

    class ICMS60(ComplexType):
        """Tributação pelo ICMS60 - ICMS cobrado por substituição tributária.Responsabilidade do recolhimento do ICMS atribuído ao tomador ou 3º por ST"""
        CST: str = Element(str, documentation=['Classificação Tributária do Serviço', '60 - ICMS cobrado anteriormente por substituição tributária '])
        vBCSTRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS ST retido'])
        vICMSSTRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS ST retido'])
        pICMSSTRet: TDec_0302 = Element(TDec_0302, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do ICMS'])
        vCred: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do Crédito outorgado/Presumido'])
    ICMS60: ICMS60 = Element(ICMS60, documentation=['Tributação pelo ICMS60 - ICMS cobrado por substituição tributária.Responsabilidade do recolhimento do ICMS atribuído ao tomador ou 3º por ST'])

    class ICMS90(ComplexType):
        """ICMS Outros"""
        CST: str = Element(str, documentation=['Classificação Tributária do Serviço', ' 90 - Outros'])
        pRedBC: TDec_0302Opc = Element(TDec_0302Opc, tipo="N", tam=(3, 2), base_type=Decimal, optional=True, documentation=['Percentual de redução da BC'])
        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS'])
        pICMS: TDec_0302 = Element(TDec_0302, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do ICMS'])
        vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS'])
        vCred: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do Crédito Outorgado/Presumido'])
    ICMS90: ICMS90 = Element(ICMS90, documentation=['ICMS Outros'])

    class ICMSOutraUF(ComplexType):
        """ICMS devido à UF de origem da prestação, quando  diferente da UF do emitente"""
        CST: str = Element(str, documentation=['Classificação Tributária do Serviço', '90 - ICMS Outra UF'])
        pRedBCOutraUF: TDec_0302Opc = Element(TDec_0302Opc, tipo="N", tam=(3, 2), base_type=Decimal, optional=True, documentation=['Percentual de redução da BC'])
        vBCOutraUF: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS'])
        pICMSOutraUF: TDec_0302 = Element(TDec_0302, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota do ICMS'])
        vICMSOutraUF: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS devido outra UF'])
    ICMSOutraUF: ICMSOutraUF = Element(ICMSOutraUF, documentation=['ICMS devido à UF de origem da prestação, quando  diferente da UF do emitente'])

    class ICMSSN(ComplexType):
        """Simples Nacional"""
        indSN: str = Element(str, documentation=['Indica se o contribuinte é Simples Nacional\t\t\t1=Sim'])
    ICMSSN: ICMSSN = Element(ICMSSN, documentation=['Simples Nacional'])



class TContainer(str):
    """Tipo Número do Container"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[A-Z0-9]+", min_length=r"1", max_length=r"20", enumeration=[])
    pass



class TUnidCarga(Element):
    """Tipo Dados Unidade de Carga"""
    tpUnidCarga: TtipoUnidCarga = Element(TtipoUnidCarga, documentation=['Tipo da Unidade de Carga', '1 - Container\n2 - ULD\n3 - Pallet\n4 - Outros'])
    idUnidCarga: TContainer = Element(TContainer, documentation=['Identificação da Unidade de Carga', 'Informar a identificação da unidade de carga, por exemplo: número do container.'])

    class lacUnidCarga(ComplexType):
        """Lacres das Unidades de Carga"""
        _max_occurs = -1

        def add(self, nLacre=None) -> TUnidCarga.lacUnidCarga:
            return super().add(nLacre=nLacre)

        nLacre: str = Element(str, documentation=['Número do lacre'])
    lacUnidCarga: List[lacUnidCarga] = Element(lacUnidCarga, max_occurs=-1, documentation=['Lacres das Unidades de Carga'])
    qtdRat: TDec_0302_0303 = Element(TDec_0302_0303, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Quantidade rateada (Peso,Volume)'])



class TUnidadeTransp(Element):
    """Tipo Dados Unidade de Transporte"""
    tpUnidTransp: TtipoUnidTransp = Element(TtipoUnidTransp, documentation=['Tipo da Unidade de Transporte', '1 - Rodoviário Tração\n2 - Rodoviário Reboque\n3 - Navio\n4 - Balsa\n5 - Aeronave\n6 - Vagão\n7 - Outros'])
    idUnidTransp: TContainer = Element(TContainer, documentation=['Identificação da Unidade de Transporte', 'Informar a identificação conforme o tipo de unidade de transporte.\nPor exemplo: para rodoviário tração ou reboque deverá preencher com a placa do veículo.\n'])

    class lacUnidTransp(ComplexType):
        """Lacres das Unidades de Transporte"""
        _max_occurs = -1

        def add(self, nLacre=None) -> TUnidadeTransp.lacUnidTransp:
            return super().add(nLacre=nLacre)

        nLacre: str = Element(str, documentation=['Número do lacre'])
    lacUnidTransp: List[lacUnidTransp] = Element(lacUnidTransp, max_occurs=-1, documentation=['Lacres das Unidades de Transporte'])
    infUnidCarga: List[TUnidCarga] = Element(TUnidCarga, max_occurs=-1, documentation=['Informações das Unidades de Carga (Containeres/ULD/Outros)', 'Dispositivo de carga utilizada (Unit Load Device - ULD) significa todo tipo de contêiner de carga, vagão, contêiner de avião, palete de aeronave com rede ou palete de aeronave com rede sobre um iglu. '])
    qtdRat: TDec_0302_0303 = Element(TDec_0302_0303, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Quantidade rateada (Peso,Volume)'])



class TCfop(str):
    """Tipo CFOP"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[123567][0-9]([0-9][1-9]|[1-9][0-9])", enumeration=[])
    pass



class TDocAssoc(str):
    """Tipo Documento Associado"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '99'])
    pass



class TEmail(str):
    """Tipo Email"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[^@]+@[^\.]+\..+", min_length=r"1", max_length=r"60", enumeration=[])
    pass



class TFinCTe(str):
    """Tipo Finalidade da CT-e"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['0', '1', '2', '3'])
    pass



class TModDoc(str):
    """Tipo Modelo do Documento"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['01', '1B', '02', '2D', '2E', '04', '06', '07', '08', '8B', '09', '10', '11', '13', '14', '15', '16', '17', '18', '20', '21', '22', '23', '24', '25', '26', '27', '28', '55'])
    pass



class TModTransp(str):
    """Tipo Modal transporte"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['01', '02', '03', '04', '05', '06'])
    pass



class TProcEmi(str):
    """Tipo processo de emissão do CT-e"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['0', '1', '2', '3'])
    pass



class TTime(str):
    """Tipo hora"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])", enumeration=[])
    pass



class TCTe(Element):
    """Tipo Conhecimento de Transporte Eletrônico"""

    class infCte(ComplexType):
        """Informações do CT-e"""
        _choice = [['infCTeNorm', 'infCteComp', 'infCteAnu']]

        class ide(ComplexType):
            """Identificação do CT-e"""
            _choice = [['toma03', 'toma4']]
            cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['Código da UF do emitente do CT-e.', 'Utilizar a Tabela do IBGE.'])
            cCT: str = Element(str, documentation=['Código numérico que compõe a Chave de Acesso. ', 'Número aleatório gerado pelo emitente para cada CT-e, com o objetivo de evitar acessos indevidos ao documento.'])
            CFOP: TCfop = Element(TCfop, documentation=['Código Fiscal de Operações e Prestações'])
            natOp: str = Element(str, documentation=['Natureza da Operação'])
            forPag: str = Element(str, documentation=['Forma de pagamento do serviço *** TAG OBSOLETA - Será retirada em versão futura', 'Preencher com: \n\t\t\t\t\t\t\t\t\t\t\t0 - Pago;\n\t\t\t\t\t\t\t\t\t\t\t1 - A pagar;\n\t\t\t\t\t\t\t\t\t\t\t2 - Outros'])
            mod: TModCT = Element(TModCT, documentation=['Modelo do documento fiscal', 'Utilizar o código 57 para identificação do CT-e, emitido em substituição aos modelos de conhecimentos em papel.'])
            serie: str = Element(str, documentation=['Série do CT-e', 'Preencher com "0" no caso de série única'])
            nCT: TNF = Element(TNF, documentation=['Número do CT-e'])
            dhEmi: str = Element(str, documentation=['Data e hora de emissão do CT-e ', 'Formato AAAA-MM-DDTHH:MM:DD'])
            tpImp: str = Element(str, documentation=['Formato de impressão do DACTE', 'Preencher com: 1 - Retrato; 2 - Paisagem.'])
            tpEmis: str = Element(str, documentation=['Forma de emissão do CT-e', 'Preencher com:\n1 - Normal;\n 4-EPEC pela SVC; 5 - Contingência FSDA;\n\t7 - Autorização pela SVC-RS;\n 8 - Autorização pela SVC-SP'])
            cDV: str = Element(str, documentation=['Digito Verificador da chave de acesso do CT-e', 'Informar o dígito  de controle da chave de acesso do CT-e, que deve ser calculado com a aplicação do algoritmo módulo 11 (base 2,9) da chave de acesso. '])
            tpAmb: TAmb = Element(TAmb, documentation=['Tipo do Ambiente', 'Preencher com:1 - Produção; 2 - Homologação'])
            tpCTe: TFinCTe = Element(TFinCTe, documentation=['Tipo do CT-e', 'Preencher com:\n\t0 - CT-e Normal;\n 1 - CT-e de Complemento de Valores;\t2 - CT-e de Anulação;\n 3 - CT-e Substituto'])
            procEmi: TProcEmi = Element(TProcEmi, documentation=['Identificador do processo de emissão do CT-e', 'Preencher com: \n\t\t\t\t\t\t\t\t\t\t\t0 - emissão de CT-e com aplicativo do contribuinte;\n\t\t\t\t\t\t\t\t\t\t\t1 - emissão de CT-e avulsa pelo Fisco;\n\t\t\t\t\t\t\t\t\t\t\t2 - emissão de CT-e avulsa, pelo contribuinte com seu certificado digital, através do site do Fisco;\n\t\t\t\t\t\t\t\t\t\t\t3- emissão CT-e pelo contribuinte com aplicativo fornecido pelo Fisco.'])
            verProc: str = Element(str, documentation=['Versão do processo de emissão', 'Iinformar a versão do aplicativo emissor de CT-e.'])
            refCTE: TChNFe = Element(TChNFe, documentation=['Chave de acesso do CT-e referenciado'])
            cMunEnv: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do Município de envio do CT-e (de onde o documento foi transmitido)', 'Utilizar a tabela do IBGE. Informar 9999999 para as operações com o exterior.'])
            xMunEnv: str = Element(str, documentation=['Nome do Município de envio do CT-e (de onde o documento foi transmitido)', 'Informar PAIS/Municipio para as operações com o exterior.'])
            UFEnv: TUf = Element(TUf, documentation=['Sigla da UF de envio do CT-e (de onde o documento foi transmitido)', "Informar 'EX' para operações com o exterior."])
            modal: TModTransp = Element(TModTransp, documentation=['Modal', 'Preencher com:01-Rodoviário;\n02-Aéreo;03-Aquaviário;04-Ferroviário;05-Dutoviário;06-Multimodal;'])
            tpServ: str = Element(str, documentation=['Tipo do Serviço', 'Preencher com: \n0 - Normal;1 - Subcontratação;\n2 - Redespacho;3 - Redespacho Intermediário; 4 - Serviço Vinculado a Multimodal'])
            cMunIni: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do Município de início da prestação', 'Utilizar a tabela do IBGE. Informar 9999999 para operações com o exterior.'])
            xMunIni: str = Element(str, documentation=['Nome do Município do início da prestação', "Informar 'EXTERIOR' para operações com o exterior."])
            UFIni: TUf = Element(TUf, documentation=['UF do início da prestação', "Informar 'EX' para operações com o exterior."])
            cMunFim: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do Município de término da prestação', 'Utilizar a tabela do IBGE. Informar 9999999 para operações com o exterior.'])
            xMunFim: str = Element(str, documentation=['Nome do Município do término da prestação', "Informar 'EXTERIOR' para operações com o exterior."])
            UFFim: TUf = Element(TUf, documentation=['UF do término da prestação', "Informar 'EX' para operações com o exterior."])
            retira: str = Element(str, documentation=['Indicador se o Recebedor retira no Aeroporto, Filial, Porto ou Estação de Destino?', 'Preencher com: 0 - sim; 1 - não'])
            xDetRetira: str = Element(str, documentation=['Detalhes do retira'])

            class toma03(ComplexType):
                """Indicador do \"papel\" do tomador do serviço no CT-e"""
                toma: str = Element(str, documentation=['Tomador do Serviço', 'Preencher com:\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t0-Remetente;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1-Expedidor;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t2-Recebedor;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t3-Destinatário\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tSerão utilizadas as informações contidas no respectivo grupo, conforme indicado pelo conteúdo deste campo'])
            toma03: toma03 = Element(toma03, documentation=['Indicador do "papel" do tomador do serviço no CT-e'])

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
                toma: str = Element(str, documentation=['Tomador do Serviço', 'Preencher com: \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t4 - Outros\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tObs: Informar os dados cadastrais do tomador do serviço'])
                CNPJ: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['Número do CNPJ', 'Em caso de empresa não estabelecida no Brasil, será informado o CNPJ com zeros.\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\nInformar os zeros não significativos.'])
                CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['Número do CPF', 'Informar os zeros não significativos.'])
                IE: TIeDest = Element(TIeDest, filter=str.isdigit, documentation=['Inscrição Estadual', 'Informar a IE do tomador ou ISENTO se tomador é contribuinte do ICMS isento de inscrição no cadastro de contribuintes do ICMS. Caso o tomador não seja contribuinte do ICMS não informar o conteúdo.'])
                xNome: str = Element(str, documentation=['Razão Social ou Nome'])
                xFant: str = Element(str, documentation=['Nome Fantasia'])
                fone: TFone = Element(TFone, filter=str.isdigit, documentation=['Telefone'])
                enderToma: TEndereco = Element(TEndereco, documentation=['Dados do endereço'])
                email: TEmail = Element(TEmail, documentation=['Endereço de email'])
            toma4: toma4 = Element(toma4, documentation=['Indicador do "papel" do tomador do serviço no CT-e'])
            dhCont: str = Element(str, documentation=['Data e Hora da entrada em contingência', 'Informar a data e hora no formato AAAA-MM-DDTHH:MM:SS'])
            xJust: str = Element(str, documentation=['Justificativa da entrada em contingência'])
        ide: ide = Element(ide, documentation=['Identificação do CT-e'])

        class compl(ComplexType):
            """Dados complementares do CT-e para fins operacionais ou comerciais"""
            xCaracAd: str = Element(str, documentation=['Característica adicional do transporte', 'Texto livre:\nREENTREGA; DEVOLUÇÃO; REFATURAMENTO; etc'])
            xCaracSer: str = Element(str, documentation=['Característica adicional do serviço', 'Texto livre:\n\t\t\t\t\t\t\t\t\t\t\tENTREGA EXPRESSA; LOGÍSTICA REVERSA; CONVENCIONAL; EMERGENCIAL; etc'])
            xEmi: str = Element(str, documentation=['Funcionário emissor do CTe'])

            class fluxo(ComplexType):
                """Previsão do fluxo da carga
Preenchimento obrigatório para o modal aéreo."""
                xOrig: str = Element(str, documentation=['Sigla ou código interno da Filial/Porto/Estação/ Aeroporto de Origem', 'Observações para o modal aéreo:\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Preenchimento obrigatório para o modal aéreo.\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t- O código de três letras IATA do aeroporto de partida deverá ser incluído como primeira anotação. Quando não for possível, utilizar a sigla OACI.'])

                class pass_(ComplexType):
                    _max_occurs = -1

                    def add(self, xPass=None) -> TCTe.infCte.compl.fluxo.pass_:
                        return super().add(xPass=xPass)

                    xPass: str = Element(str, documentation=['Sigla ou código interno da Filial/Porto/Estação/Aeroporto de Passagem', 'Observação para o modal aéreo:\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t- O código de três letras IATA, referente ao aeroporto de transferência, deverá ser incluído, quando for o caso. Quando não for possível,  utilizar a sigla OACI. Qualquer solicitação de itinerário deverá ser incluída.'])
                pass_: List[pass_] = Element(pass_, max_occurs=-1)
                xDest: str = Element(str, documentation=['Sigla ou código interno da Filial/Porto/Estação/Aeroporto de Destino', 'Observações para o modal aéreo:\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Preenchimento obrigatório para o modal aéreo.\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t- Deverá ser incluído o código de três letras IATA do aeroporto de destino. Quando não for possível, utilizar a sigla OACI.'])
                xRota: str = Element(str, documentation=['Código da Rota de Entrega'])
            fluxo: fluxo = Element(fluxo, documentation=['Previsão do fluxo da carga', 'Preenchimento obrigatório para o modal aéreo.'])

            class Entrega(ComplexType):
                """Informações ref. a previsão de entrega"""
                _choice = [['semData', 'comData', 'noPeriodo'], ['semHora', 'comHora', 'noInter']]

                class semData(ComplexType):
                    """Entrega sem data definida
Esta opção é proibida para o modal aéreo."""
                    tpPer: str = Element(str, documentation=['Tipo de data/período programado para entrega', '0- Sem data definida'])
                semData: semData = Element(semData, documentation=['Entrega sem data definida', 'Esta opção é proibida para o modal aéreo.'])

                class comData(ComplexType):
                    """Entrega com data definida"""
                    tpPer: str = Element(str, documentation=['Tipo de data/período programado para entrega', 'Preencher com:\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1-Na data;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t2-Até a data;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t3-A partir da data'])
                    dProg: TData = Element(TData, base_type=date, documentation=['Data programada ', 'Formato AAAA-MM-DD'])
                comData: comData = Element(comData, documentation=['Entrega com data definida'])

                class noPeriodo(ComplexType):
                    """Entrega no período definido"""
                    tpPer: str = Element(str, documentation=['Tipo período', '4-no período'])
                    dIni: TData = Element(TData, base_type=date, documentation=['Data inicial ', 'Formato AAAA-MM-DD'])
                    dFim: TData = Element(TData, base_type=date, documentation=['Data final ', 'Formato AAAA-MM-DD'])
                noPeriodo: noPeriodo = Element(noPeriodo, documentation=['Entrega no período definido'])

                class semHora(ComplexType):
                    """Entrega sem hora definida"""
                    tpHor: str = Element(str, documentation=['Tipo de hora', '0- Sem hora definida'])
                semHora: semHora = Element(semHora, documentation=['Entrega sem hora definida'])

                class comHora(ComplexType):
                    """Entrega com hora definida"""
                    tpHor: str = Element(str, documentation=['Tipo de hora', 'Preencher com:\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1--No horário;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t2-Até o horário;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t3-A partir do horário'])
                    hProg: TTime = Element(TTime, documentation=['Hora programada ', 'Formato HH:MM:SS'])
                comHora: comHora = Element(comHora, documentation=['Entrega com hora definida'])

                class noInter(ComplexType):
                    """Entrega no intervalo de horário definido"""
                    tpHor: str = Element(str, documentation=[' Tipo de hora', '4 - No intervalo de tempo'])
                    hIni: TTime = Element(TTime, documentation=['Hora inicial ', 'Formato HH:MM:SS'])
                    hFim: TTime = Element(TTime, documentation=['Hora final ', 'Formato HH:MM:SS'])
                noInter: noInter = Element(noInter, documentation=['Entrega no intervalo de horário definido'])
            Entrega: Entrega = Element(Entrega, documentation=['Informações ref. a previsão de entrega'])
            origCalc: str = Element(str, documentation=['Município de origem para efeito de cálculo do frete'])
            destCalc: str = Element(str, documentation=['Município de destino para efeito de cálculo do frete'])
            xObs: str = Element(str, documentation=['Observações Gerais'])

            class ObsCont(ComplexType):
                """Campo de uso livre do contribuinte
Informar o nome do campo no atributo xCampo e o conteúdo do campo no XTexto"""
                _max_occurs = 10

                def add(self, xTexto=None, xCampo=None) -> TCTe.infCte.compl.ObsCont:
                    return super().add(xTexto=xTexto, xCampo=xCampo)

                xTexto: str = Element(str, documentation=['Conteúdo do campo'])
                xCampo: str = Attribute(None)
            ObsCont: List[ObsCont] = Element(ObsCont, max_occurs=10, documentation=['Campo de uso livre do contribuinte', 'Informar o nome do campo no atributo xCampo e o conteúdo do campo no XTexto'])

            class ObsFisco(ComplexType):
                """Campo de uso livre do contribuinte
Informar o nome do campo no atributo xCampo e o conteúdo do campo no XTexto"""
                _max_occurs = 10

                def add(self, xTexto=None, xCampo=None) -> TCTe.infCte.compl.ObsFisco:
                    return super().add(xTexto=xTexto, xCampo=xCampo)

                xTexto: str = Element(str, documentation=['Conteúdo do campo'])
                xCampo: str = Attribute(None)
            ObsFisco: List[ObsFisco] = Element(ObsFisco, max_occurs=10, documentation=['Campo de uso livre do contribuinte', 'Informar o nome do campo no atributo xCampo e o conteúdo do campo no XTexto'])
        compl: compl = Element(compl, documentation=['Dados complementares do CT-e para fins operacionais ou comerciais'])

        class emit(ComplexType):
            """Identificação do Emitente do CT-e"""
            CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do emitente', 'Informar zeros não significativos'])
            IE: str = Element(str, documentation=['Inscrição Estadual do Emitente'])
            xNome: str = Element(str, documentation=['Razão social ou Nome do emitente'])
            xFant: str = Element(str, documentation=['Nome fantasia'])
            enderEmit: TEndeEmi = Element(TEndeEmi, documentation=['Endereço do emitente'])
        emit: emit = Element(emit, documentation=['Identificação do Emitente do CT-e'])

        class rem(ComplexType):
            """Informações do Remetente das mercadorias transportadas pelo CT-e
Poderá não ser informado para os CT-e de redespacho intermediário. Nos demais casos deverá sempre ser informado."""
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
            CNPJ: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['Número do CNPJ', 'Em caso de empresa não estabelecida no Brasil, será informado o CNPJ com zeros.\n\t\t\t\t\t\t\t\t\t\t\t\tInformar os zeros não significativos.'])
            CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['Número do CPF', 'Informar os zeros não significativos.'])
            IE: TIeDest = Element(TIeDest, filter=str.isdigit, documentation=['Inscrição Estadual', 'Informar a IE do remetente ou ISENTO se remetente é contribuinte do ICMS isento de inscrição no cadastro de contribuintes do ICMS. Caso o remetente não seja contribuinte do ICMS não informar o conteúdo.'])
            xNome: str = Element(str, documentation=['Razão social ou nome do remetente'])
            xFant: str = Element(str, documentation=['Nome fantasia'])
            fone: TFone = Element(TFone, filter=str.isdigit, documentation=['Telefone'])
            enderReme: TEndereco = Element(TEndereco, documentation=['Dados do endereço'])
            email: str = Element(str, documentation=['Endereço de email'])
        rem: rem = Element(rem, documentation=['Informações do Remetente das mercadorias transportadas pelo CT-e', 'Poderá não ser informado para os CT-e de redespacho intermediário. Nos demais casos deverá sempre ser informado.'])

        class exped(ComplexType):
            """Informações do Expedidor da Carga"""
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
            CNPJ: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['Número do CNPJ', 'Em caso de empresa não estabelecida no Brasil, será informado o CNPJ com zeros.\n\t\t\t\t\t\t\t\t\t\t\t\tInformar os zeros não significativos.'])
            CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['Número do CPF', 'Informar os zeros não significativos.'])
            IE: TIeDest = Element(TIeDest, filter=str.isdigit, documentation=['Inscrição Estadual', 'Informar a IE do expedidor ou ISENTO se expedidor é contribuinte do ICMS isento de inscrição no cadastro de contribuintes do ICMS. Caso o expedidor não seja contribuinte do ICMS não informar o conteúdo.'])
            xNome: str = Element(str, documentation=['Razão Social ou Nome'])
            fone: TFone = Element(TFone, filter=str.isdigit, documentation=['Telefone'])
            enderExped: TEndereco = Element(TEndereco, documentation=['Dados do endereço'])
            email: TEmail = Element(TEmail, documentation=['Endereço de email'])
        exped: exped = Element(exped, documentation=['Informações do Expedidor da Carga'])

        class receb(ComplexType):
            """Informações do Recebedor da Carga"""
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
            CNPJ: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['Número do CNPJ', 'Em caso de empresa não estabelecida no Brasil, será informado o CNPJ com zeros.\n\t\t\t\t\t\t\t\t\t\t\t\tInformar os zeros não significativos.'])
            CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['Número do CPF', 'Informar os zeros não significativos.'])
            IE: TIeDest = Element(TIeDest, filter=str.isdigit, documentation=['Inscrição Estadual', 'Informar a IE do recebedor ou ISENTO se recebedor é contribuinte do ICMS isento de inscrição no cadastro de contribuintes do ICMS. Caso o recebedor não seja contribuinte do ICMS não informar o conteúdo.'])
            xNome: str = Element(str, documentation=['Razão Social ou Nome '])
            fone: TFone = Element(TFone, filter=str.isdigit, documentation=['Telefone'])
            enderReceb: TEndereco = Element(TEndereco, documentation=['Dados do endereço'])
            email: TEmail = Element(TEmail, documentation=['Endereço de email'])
        receb: receb = Element(receb, documentation=['Informações do Recebedor da Carga'])

        class dest(ComplexType):
            """Informações do Destinatário do CT-e
Só pode ser omitido em caso de redespacho intermediário"""
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
            CNPJ: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['Número do CNPJ', 'Em caso de empresa não estabelecida no Brasil, será informado o CNPJ com zeros.\n\t\t\t\t\t\t\t\t\t\t\t\tInformar os zeros não significativos.'])
            CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['Número do CPF', 'Informar os zeros não significativos.'])
            IE: str = Element(str, documentation=['Inscrição Estadual', 'Informar a IE do destinatário ou ISENTO se destinatário é contribuinte do ICMS isento de inscrição no cadastro de contribuintes do ICMS. Caso o destinatário não seja contribuinte do ICMS não informar o conteúdo.'])
            xNome: str = Element(str, documentation=['Razão Social ou Nome do destinatário'])
            fone: TFone = Element(TFone, filter=str.isdigit, documentation=['Telefone'])
            ISUF: str = Element(str, documentation=['Inscrição na SUFRAMA', '(Obrigatório nas operações com as áreas com benefícios de incentivos fiscais sob controle da SUFRAMA)'])
            enderDest: TEndereco = Element(TEndereco, documentation=['Dados do endereço'])
            email: TEmail = Element(TEmail, documentation=['Endereço de email'])
        dest: dest = Element(dest, documentation=['Informações do Destinatário do CT-e', 'Só pode ser omitido em caso de redespacho intermediário'])

        class vPrest(ComplexType):
            """Valores da Prestação de Serviço"""
            vTPrest: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Total da Prestação do Serviço', 'Pode conter zeros quando o CT-e for de complemento de ICMS'])
            vRec: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor a Receber'])

            class Comp(ComplexType):
                """Componentes do Valor da Prestação"""
                _max_occurs = -1

                def add(self, xNome=None, vComp=None) -> TCTe.infCte.vPrest.Comp:
                    return super().add(xNome=xNome, vComp=vComp)

                xNome: str = Element(str, documentation=['Nome do componente', 'Exxemplos: FRETE PESO, FRETE VALOR, SEC/CAT, ADEME, AGENDAMENTO, etc'])
                vComp: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do componente'])
            Comp: List[Comp] = Element(Comp, max_occurs=-1, documentation=['Componentes do Valor da Prestação'])
        vPrest: vPrest = Element(vPrest, documentation=['Valores da Prestação de Serviço'])

        class imp(ComplexType):
            """Informações relativas aos Impostos"""
            ICMS: TImp = Element(TImp, documentation=['Informações relativas ao ICMS', None])
            vTotTrib: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Total dos Tributos'])
            infAdFisco: str = Element(str, documentation=['Informações adicionais de interesse do Fisco', 'Norma referenciada, informações complementares, etc'])

            class ICMSUFFim(ComplexType):
                """Informações do ICMS de partilha com a UF de término do serviço de transporte na operação interestadual
Grupo a ser informado nas prestações interestaduais para consumidor final, não contribuinte do ICMS"""
                vBCUFFim: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da BC do ICMS na UF de término da prestação do serviço de transporte'])
                pFCPUFFim: TDec_0302 = Element(TDec_0302, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Percentual do ICMS relativo ao Fundo de Combate à pobreza (FCP) na UF de término da prestação do serviço de transporte', 'Alíquota adotada nas operações internas na UF do destinatário'])
                pICMSUFFim: TDec_0302 = Element(TDec_0302, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota interna da UF de término da prestação do serviço de transporte', 'Alíquota adotada nas operações internas na UF do destinatário'])
                pICMSInter: TDec_0302 = Element(TDec_0302, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Alíquota interestadual das UF envolvidas', 'Alíquota interestadual das UF envolvidas\n'])
                pICMSInterPart: TDec_0302 = Element(TDec_0302, tipo="N", tam=(3, 2), base_type=Decimal, documentation=['Percentual provisório de partilha entre os estados', 'Percentual de partilha para a UF do destinatário:\n- 40% em 2016;\n- 60% em 2017;\n- 80% em 2018;\n- 100% a partir de 2019.'])
                vFCPUFFim: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS relativo ao Fundo de Combate á Pobreza (FCP) da UF de término da prestação'])
                vICMSUFFim: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS de partilha para a UF de término da prestação do serviço de transporte'])
                vICMSUFIni: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do ICMS de partilha para a UF de início da prestação do serviço de transporte'])
            ICMSUFFim: ICMSUFFim = Element(ICMSUFFim, documentation=['Informações do ICMS de partilha com a UF de término do serviço de transporte na operação interestadual', 'Grupo a ser informado nas prestações interestaduais para consumidor final, não contribuinte do ICMS'])
        imp: imp = Element(imp, documentation=['Informações relativas aos Impostos'])

        class infCTeNorm(ComplexType):
            """Grupo de informações do CT-e Normal e Substituto"""

            class infCarga(ComplexType):
                """Informações da Carga do CT-e"""
                vCarga: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor total da carga', 'Dever ser informado para todos os modais, com exceção para o Dutoviário.'])
                proPred: str = Element(str, documentation=['Produto predominante', 'Informar a descrição do produto predominante'])
                xOutCat: str = Element(str, documentation=['Outras características da carga', '"FRIA", "GRANEL", "REFRIGERADA", "Medidas: 12X12X12"'])

                class infQ(ComplexType):
                    """Informações de quantidades da Carga do CT-e
Para o Aéreo é obrigatório o preenchimento desse campo da seguinte forma.
1 - Peso Bruto, sempre em quilogramas (obrigatório);
2 - Peso Cubado; sempre em quilogramas;
3 - Quantidade de volumes, sempre em unidades (obrigatório);
4 - Cubagem, sempre em metros cúbicos (obrigatório apenas quando for impossível preencher as dimensões da(s) embalagem(ens) na tag xDime do leiaute do Aéreo)."""
                    _max_occurs = -1

                    def add(self, cUnid=None, tpMed=None, qCarga=None) -> TCTe.infCte.infCTeNorm.infCarga.infQ:
                        return super().add(cUnid=cUnid, tpMed=tpMed, qCarga=qCarga)

                    cUnid: str = Element(str, documentation=['Código da Unidade de Medida ', 'Preencher com:\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t00-M3;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t01-KG;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t02-TON;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t03-UNIDADE;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t04-LITROS;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t05-MMBTU'])
                    tpMed: str = Element(str, documentation=['Tipo da Medida', 'Exemplos:\nPESO BRUTO, PESO DECLARADO, PESO CUBADO, PESO AFORADO, PESO AFERIDO, PESO BASE DE CÁLCULO, LITRAGEM, CAIXAS e etc'])
                    qCarga: TDec_1104 = Element(TDec_1104, tipo="N", tam=(11, 4), base_type=Decimal, documentation=['Quantidade'])
                infQ: List[infQ] = Element(infQ, max_occurs=-1, documentation=['Informações de quantidades da Carga do CT-e', 'Para o Aéreo é obrigatório o preenchimento desse campo da seguinte forma.\n1 - Peso Bruto, sempre em quilogramas (obrigatório);\n2 - Peso Cubado; sempre em quilogramas;\n3 - Quantidade de volumes, sempre em unidades (obrigatório);\n4 - Cubagem, sempre em metros cúbicos (obrigatório apenas quando for impossível preencher as dimensões da(s) embalagem(ens) na tag xDime do leiaute do Aéreo).'])
            infCarga: infCarga = Element(infCarga, documentation=['Informações da Carga do CT-e'])

            class infDoc(ComplexType):
                """Informações dos documentos transportados pelo CT-e
Opcional para Redespacho Intermediario e Serviço vinculado a multimodal.
Poderá não ser informado para os CT-e de redespacho intermediário. Nos demais casos deverá sempre ser informado."""
                _choice = [['infNF', 'infNFe', 'infOutros']]

                class infNF(ComplexType):
                    """Informações das NF
Este grupo deve ser informado quando o documento originário for NF"""
                    _max_occurs = -1
                    _choice = [['infUnidTransp', 'infUnidCarga']]

                    def add(self, nRoma=None, nPed=None, mod=None, serie=None, nDoc=None, dEmi=None, vBC=None, vICMS=None, vBCST=None, vST=None, vProd=None, vNF=None, nCFOP=None, nPeso=None, PIN=None, dPrev=None, infUnidTransp=None, infUnidCarga=None) -> TCTe.infCte.infCTeNorm.infDoc.infNF:
                        return super().add(nRoma=nRoma, nPed=nPed, mod=mod, serie=serie, nDoc=nDoc, dEmi=dEmi, vBC=vBC, vICMS=vICMS, vBCST=vBCST, vST=vST, vProd=vProd, vNF=vNF, nCFOP=nCFOP, nPeso=nPeso, PIN=PIN, dPrev=dPrev, infUnidTransp=infUnidTransp, infUnidCarga=infUnidCarga)

                    nRoma: str = Element(str, documentation=['Número do Romaneio da NF'])
                    nPed: str = Element(str, documentation=['Número do Pedido da NF'])
                    mod: TModNF = Element(TModNF, documentation=['Modelo da Nota Fiscal', 'Preencher com: \n01 - NF Modelo 01/1A e Avulsa; \n04 - NF de Produtor'])
                    serie: str = Element(str, documentation=['Série'])
                    nDoc: str = Element(str, documentation=['Número '])
                    dEmi: TData = Element(TData, base_type=date, documentation=['Data de Emissão', 'Formato AAAA-MM-DD'])
                    vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da Base de Cálculo do ICMS'])
                    vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Total do ICMS'])
                    vBCST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da Base de Cálculo do ICMS ST'])
                    vST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Total do ICMS ST'])
                    vProd: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Total dos Produtos'])
                    vNF: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Total da NF'])
                    nCFOP: TCfop = Element(TCfop, documentation=['CFOP Predominante', 'CFOP da NF ou, na existência de mais de um, predominância pelo critério de valor econômico.'])
                    nPeso: TDec_1203Opc = Element(TDec_1203Opc, tipo="N", tam=(12, 3), base_type=Decimal, optional=True, documentation=['Peso total em Kg'])
                    PIN: str = Element(str, documentation=['PIN SUFRAMA', 'PIN atribuído pela SUFRAMA para a operação.'])
                    dPrev: TData = Element(TData, base_type=date, documentation=['Data prevista de entrega', 'Formato AAAA-MM-DD'])
                    infUnidTransp: List[TUnidadeTransp] = Element(TUnidadeTransp, max_occurs=-1, documentation=['Informações das Unidades de Transporte (Carreta/Reboque/Vagão)', 'Deve ser preenchido com as informações das unidades de transporte utilizadas.'])
                    infUnidCarga: List[TUnidCarga] = Element(TUnidCarga, max_occurs=-1, documentation=['Informações das Unidades de Carga (Containeres/ULD/Outros)', 'Dispositivo de carga utilizada (Unit Load Device - ULD) significa todo tipo de contêiner de carga, vagão, contêiner de avião, palete de aeronave com rede ou palete de aeronave com rede sobre um iglu. '])
                infNF: List[infNF] = Element(infNF, max_occurs=-1, documentation=['Informações das NF', 'Este grupo deve ser informado quando o documento originário for NF '])

                class infNFe(ComplexType):
                    """Informações das NF-e"""
                    _max_occurs = -1
                    _choice = [['infUnidTransp', 'infUnidCarga']]

                    def add(self, chave=None, PIN=None, dPrev=None, infUnidTransp=None, infUnidCarga=None) -> TCTe.infCte.infCTeNorm.infDoc.infNFe:
                        return super().add(chave=chave, PIN=PIN, dPrev=dPrev, infUnidTransp=infUnidTransp, infUnidCarga=infUnidCarga)

                    chave: TChNFe = Element(TChNFe, documentation=['Chave de acesso da NF-e'])
                    PIN: str = Element(str, documentation=['PIN SUFRAMA', 'PIN atribuído pela SUFRAMA para a operação.'])
                    dPrev: TData = Element(TData, base_type=date, documentation=['Data prevista de entrega', 'Formato AAAA-MM-DD'])
                    infUnidTransp: List[TUnidadeTransp] = Element(TUnidadeTransp, max_occurs=-1, documentation=['Informações das Unidades de Transporte (Carreta/Reboque/Vagão)', 'Deve ser preenchido com as informações das unidades de transporte utilizadas.'])
                    infUnidCarga: List[TUnidCarga] = Element(TUnidCarga, max_occurs=-1, documentation=['Informações das Unidades de Carga (Containeres/ULD/Outros)', 'Dispositivo de carga utilizada (Unit Load Device - ULD) significa todo tipo de contêiner de carga, vagão, contêiner de avião, palete de aeronave com rede ou palete de aeronave com rede sobre um iglu. '])
                infNFe: List[infNFe] = Element(infNFe, max_occurs=-1, documentation=['Informações das NF-e'])

                class infOutros(ComplexType):
                    """Informações dos demais documentos"""
                    _max_occurs = -1
                    _choice = [['infUnidTransp', 'infUnidCarga']]

                    def add(self, tpDoc=None, descOutros=None, nDoc=None, dEmi=None, vDocFisc=None, dPrev=None, infUnidTransp=None, infUnidCarga=None) -> TCTe.infCte.infCTeNorm.infDoc.infOutros:
                        return super().add(tpDoc=tpDoc, descOutros=descOutros, nDoc=nDoc, dEmi=dEmi, vDocFisc=vDocFisc, dPrev=dPrev, infUnidTransp=infUnidTransp, infUnidCarga=infUnidCarga)

                    tpDoc: str = Element(str, documentation=['Tipo de documento originário', 'Preencher com:\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t00 - Declaração;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t10 - Dutoviário;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t99 - Outros'])
                    descOutros: str = Element(str, documentation=['Descrição quando se tratar de 99-Outros'])
                    nDoc: str = Element(str, documentation=['Número '])
                    dEmi: TData = Element(TData, base_type=date, documentation=['Data de Emissão', 'Formato AAAA-MM-DD'])
                    vDocFisc: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor do documento'])
                    dPrev: TData = Element(TData, base_type=date, documentation=['Data prevista de entrega', 'Formato AAAA-MM-DD'])
                    infUnidTransp: List[TUnidadeTransp] = Element(TUnidadeTransp, max_occurs=-1, documentation=['Informações das Unidades de Transporte (Carreta/Reboque/Vagão)', 'Deve ser preenchido com as informações das unidades de transporte utilizadas.'])
                    infUnidCarga: List[TUnidCarga] = Element(TUnidCarga, max_occurs=-1, documentation=['Informações das Unidades de Carga (Containeres/ULD/Outros)', 'Dispositivo de carga utilizada (Unit Load Device - ULD) significa todo tipo de contêiner de carga, vagão, contêiner de avião, palete de aeronave com rede ou palete de aeronave com rede sobre um iglu. '])
                infOutros: List[infOutros] = Element(infOutros, max_occurs=-1, documentation=['Informações dos demais documentos'])
            infDoc: infDoc = Element(infDoc, documentation=['Informações dos documentos transportados pelo CT-e\nOpcional para Redespacho Intermediario e Serviço vinculado a multimodal.', 'Poderá não ser informado para os CT-e de redespacho intermediário. Nos demais casos deverá sempre ser informado.'])

            class docAnt(ComplexType):
                """Documentos de Transporte Anterior"""

                class emiDocAnt(ComplexType):
                    """Emissor do documento anterior"""
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

                    def add(self, CNPJ=None, CPF=None, IE=None, UF=None, xNome=None, idDocAnt=None) -> TCTe.infCte.infCTeNorm.docAnt.emiDocAnt:
                        return super().add(CNPJ=CNPJ, CPF=CPF, IE=IE, UF=UF, xNome=xNome, idDocAnt=idDocAnt)

                    CNPJ: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['Número do CNPJ', 'Em caso de empresa não estabelecida no Brasil, será informado o CNPJ com zeros.\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tInformar os zeros não significativos.'])
                    CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['Número do CPF', 'Informar os zeros não significativos.'])
                    IE: TIe = Element(TIe, filter=str.isdigit, documentation=['Inscrição Estadual'])
                    UF: TUf = Element(TUf, documentation=['Sigla da UF', 'Informar EX para operações com o exterior.'])
                    xNome: str = Element(str, documentation=['Razão Social ou Nome do expedidor'])

                    class idDocAnt(ComplexType):
                        """Informações de identificação dos documentos de Transporte Anterior"""
                        _max_occurs = 2
                        _choice = [['idDocAntPap', 'idDocAntEle']]

                        def add(self, idDocAntPap=None, idDocAntEle=None) -> TCTe.infCte.infCTeNorm.docAnt.emiDocAnt.idDocAnt:
                            return super().add(idDocAntPap=idDocAntPap, idDocAntEle=idDocAntEle)


                        class idDocAntPap(ComplexType):
                            """Documentos de transporte anterior em papel"""
                            _max_occurs = -1

                            def add(self, tpDoc=None, serie=None, subser=None, nDoc=None, dEmi=None) -> TCTe.infCte.infCTeNorm.docAnt.emiDocAnt.idDocAnt.idDocAntPap:
                                return super().add(tpDoc=tpDoc, serie=serie, subser=subser, nDoc=nDoc, dEmi=dEmi)

                            tpDoc: TDocAssoc = Element(TDocAssoc, documentation=['Tipo do Documento de Transporte Anterior', 'Preencher com:\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t00-CTRC;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t01-CTAC;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t02-ACT;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t03 - NF Modelo 7;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t04 - NF Modelo 27;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t05-Conhecimento Aéreo Nacional;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t06-CTMC;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t07-ATRE;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t08-DTA (Despacho de Transito Aduaneiro);\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t09-Conhecimento Aéreo Internacional;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t10 – Conhecimento - Carta de Porte Internacional;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t11 – Conhecimento Avulso;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t12-TIF (Transporte Internacional Ferroviário);\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t99 - outros'])
                            serie: str = Element(str, documentation=['Série do Documento Fiscal'])
                            subser: str = Element(str, documentation=['Série do Documento Fiscal'])
                            nDoc: str = Element(str, documentation=['Número do Documento Fiscal'])
                            dEmi: TData = Element(TData, base_type=date, documentation=['Data de emissão (AAAA-MM-DD)'])
                        idDocAntPap: List[idDocAntPap] = Element(idDocAntPap, max_occurs=-1, documentation=['Documentos de transporte anterior em papel'])

                        class idDocAntEle(ComplexType):
                            """Documentos de transporte anterior eletrônicos"""
                            _max_occurs = -1

                            def add(self, chave=None) -> TCTe.infCte.infCTeNorm.docAnt.emiDocAnt.idDocAnt.idDocAntEle:
                                return super().add(chave=chave)

                            chave: TChNFe = Element(TChNFe, documentation=['Chave de acesso do CT-e'])
                        idDocAntEle: List[idDocAntEle] = Element(idDocAntEle, max_occurs=-1, documentation=['Documentos de transporte anterior eletrônicos'])
                    idDocAnt: List[idDocAnt] = Element(idDocAnt, max_occurs=2, documentation=['Informações de identificação dos documentos de Transporte Anterior'])
                emiDocAnt: List[emiDocAnt] = Element(emiDocAnt, max_occurs=-1, documentation=['Emissor do documento anterior'])
            docAnt: docAnt = Element(docAnt, documentation=['Documentos de Transporte Anterior'])

            class seg(ComplexType):
                """Informações de Seguro da Carga"""
                _max_occurs = -1

                def add(self, respSeg=None, xSeg=None, nApol=None, nAver=None, vCarga=None) -> TCTe.infCte.infCTeNorm.seg:
                    return super().add(respSeg=respSeg, xSeg=xSeg, nApol=nApol, nAver=nAver, vCarga=vCarga)

                respSeg: str = Element(str, documentation=['Responsável pelo seguro', 'Preencher com:\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t0- Remetente;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1- Expedidor;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t2 - Recebedor;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t3 - Destinatário;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t4 - Emitente do CT-e;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t5 - Tomador de Serviço.\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tDados obrigatórios apenas no modal Rodoviário, depois da lei 11.442/07. Para os demais modais esta informação é opcional.'])
                xSeg: str = Element(str, documentation=['Nome da Seguradora'])
                nApol: str = Element(str, documentation=['Número da Apólice', 'Obrigatório pela lei 11.442/07 (RCTRC)'])
                nAver: str = Element(str, documentation=['Número da Averbação', 'Não é obrigatório, pois muitas averbações ocorrem aapós a emissão do CT, mensalmente, por exemplo.'])
                vCarga: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor da Carga para efeito de averbação', 'Normalmente igual ao valor declarado da mercadoria, diferente por exemplo, quando a mercadoria transportada é isenta de tributos nacionais para exportação, onde é preciso averbar um valor maior, pois no caso de indenização, o valor a ser pago será maior'])
            seg: List[seg] = Element(seg, max_occurs=-1, documentation=['Informações de Seguro da Carga'])

            class infModal(ComplexType):
                """Informações do modal"""
                versaoModal: str = Attribute(None)
            infModal: infModal = Element(infModal, documentation=['Informações do modal'])

            class peri(ComplexType):
                """Preenchido quando for  transporte de produtos classificados pela ONU como perigosos.
Não deve ser preenchido para modal dutoviário.
												Observação para o modal aéreo:
												- O preenchimento desses campos não desobriga a empresa aérea de emitir os demais documentos que constam na legislação vigente."""
                _max_occurs = -1

                def add(self, nONU=None, xNomeAE=None, xClaRisco=None, grEmb=None, qTotProd=None, qVolTipo=None, pontoFulgor=None) -> TCTe.infCte.infCTeNorm.peri:
                    return super().add(nONU=nONU, xNomeAE=xNomeAE, xClaRisco=xClaRisco, grEmb=grEmb, qTotProd=qTotProd, qVolTipo=qVolTipo, pontoFulgor=pontoFulgor)

                nONU: str = Element(str, documentation=['Número ONU/UN', 'Ver a legislação de transporte de produtos perigosos aplicadas ao modal  '])
                xNomeAE: str = Element(str, documentation=['Nome apropriado para embarque do produto', 'Ver a legislação de transporte de produtos perigosos aplicada ao modo de transporte'])
                xClaRisco: str = Element(str, documentation=['Classe ou subclasse/divisão, e risco subsidiário/risco secundário', 'Ver a legislação de transporte de produtos perigosos aplicadas ao modal'])
                grEmb: str = Element(str, documentation=['Grupo de Embalagem', 'Ver a legislação de transporte de produtos perigosos aplicadas ao modal\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPreenchimento obrigatório para o modal aéreo.\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tA legislação para o modal rodoviário e ferroviário não atribui grupo de embalagem para todos os produtos, portanto haverá casos de não preenchimento desse campo.'])
                qTotProd: str = Element(str, documentation=['Quantidade total por produto', 'Preencher conforme a legislação de transporte de produtos perigosos aplicada ao modal'])
                qVolTipo: str = Element(str, documentation=['Quantidade e Tipo de volumes', 'Preencher conforme a legislação de transporte de produtos perigosos aplicada ao modal'])
                pontoFulgor: str = Element(str, documentation=['Ponto de Fulgor', 'Preencher conforme a legislação de transporte de produtos perigosos aplicada ao modal. \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tNo caso de transporte rodoviário e ferroviário, este campo não é exigido.'])
            peri: List[peri] = Element(peri, max_occurs=-1, documentation=['Preenchido quando for  transporte de produtos classificados pela ONU como perigosos.', 'Não deve ser preenchido para modal dutoviário.\n\t\t\t\t\t\t\t\t\t\t\t\tObservação para o modal aéreo:\n\t\t\t\t\t\t\t\t\t\t\t\t- O preenchimento desses campos não desobriga a empresa aérea de emitir os demais documentos que constam na legislação vigente.'])

            class veicNovos(ComplexType):
                """informações dos veículos transportados"""
                _max_occurs = -1

                def add(self, chassi=None, cCor=None, xCor=None, cMod=None, vUnit=None, vFrete=None) -> TCTe.infCte.infCTeNorm.veicNovos:
                    return super().add(chassi=chassi, cCor=cCor, xCor=xCor, cMod=cMod, vUnit=vUnit, vFrete=vFrete)

                chassi: str = Element(str, documentation=['Chassi do veículo'])
                cCor: str = Element(str, documentation=['Cor do veículo', 'Código de cada montadora'])
                xCor: str = Element(str, documentation=['Descrição da cor'])
                cMod: str = Element(str, documentation=['Código Marca Modelo', 'Utilizar tabela RENAVAM'])
                vUnit: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Unitário do Veículo'])
                vFrete: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Frete Unitário'])
            veicNovos: List[veicNovos] = Element(veicNovos, max_occurs=-1, documentation=['informações dos veículos transportados'])

            class cobr(ComplexType):
                """Dados da cobrança do CT-e"""

                class fat(ComplexType):
                    """Dados da fatura"""
                    nFat: str = Element(str, documentation=['Número da fatura'])
                    vOrig: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor original da fatura'])
                    vDesc: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor do desconto da fatura'])
                    vLiq: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor líquido da fatura'])
                fat: fat = Element(fat, documentation=['Dados da fatura'])

                class dup(ComplexType):
                    """Dados das duplicatas"""
                    _max_occurs = -1

                    def add(self, nDup=None, dVenc=None, vDup=None) -> TCTe.infCte.infCTeNorm.cobr.dup:
                        return super().add(nDup=nDup, dVenc=dVenc, vDup=vDup)

                    nDup: str = Element(str, documentation=['Número da duplicata'])
                    dVenc: TData = Element(TData, base_type=date, documentation=['Data de vencimento da duplicata (AAAA-MM-DD)'])
                    vDup: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2), base_type=Decimal, optional=True, documentation=['Valor da duplicata'])
                dup: List[dup] = Element(dup, max_occurs=-1, documentation=['Dados das duplicatas'])
            cobr: cobr = Element(cobr, documentation=['Dados da cobrança do CT-e'])

            class infCteSub(ComplexType):
                """Informações do CT-e de substituição"""
                _choice = [['tomaICMS', 'tomaNaoICMS']]
                chCte: str = Element(str, documentation=['Chave de acesso do CT-e a ser substituído (original)'])

                class tomaICMS(ComplexType):
                    """Tomador é contribuinte do ICMS"""
                    _choice = [['refNFe', 'refNF', 'refCte']]
                    refNFe: TChNFe = Element(TChNFe, documentation=['Chave de acesso da NF-e emitida pelo Tomador'])

                    class refNF(ComplexType):
                        """Informação da NF ou CT emitido pelo Tomador"""
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
                        CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do Emitente', 'Informar o CNPJ do emitente do Documento Fiscal'])
                        CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['Número do CPF', 'Informar o CPF do emitente do documento fiscal'])
                        mod: TModDoc = Element(TModDoc, documentation=['Modelo do Documento Fiscal'])
                        serie: TSerie = Element(TSerie, documentation=['Serie do documento fiscal'])
                        subserie: TSerie = Element(TSerie, documentation=['Subserie do documento fiscal'])
                        nro: str = Element(str, documentation=['Número do documento fiscal'])
                        valor: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do documento fiscal.'])
                        dEmi: TData = Element(TData, base_type=date, documentation=['Data de emissão do documento fiscal.'])
                    refNF: refNF = Element(refNF, documentation=['Informação da NF ou CT emitido pelo Tomador'])
                    refCte: TChNFe = Element(TChNFe, documentation=['Chave de acesso do CT-e emitido pelo Tomador'])
                tomaICMS: tomaICMS = Element(tomaICMS, documentation=['Tomador é contribuinte do ICMS'])

                class tomaNaoICMS(ComplexType):
                    """Tomador não é contribuinte do ICMS"""
                    refCteAnu: str = Element(str, documentation=['Chave de acesso do CT-e de Anulação'])
                tomaNaoICMS: tomaNaoICMS = Element(tomaNaoICMS, documentation=['Tomador não é contribuinte do ICMS'])
            infCteSub: infCteSub = Element(infCteSub, documentation=['Informações do CT-e de substituição '])
        infCTeNorm: infCTeNorm = Element(infCTeNorm, documentation=['Grupo de informações do CT-e Normal e Substituto'])

        class infCteComp(ComplexType):
            """Detalhamento do CT-e complementado"""
            chave: TChNFe = Element(TChNFe, documentation=['Chave do CT-e complementado'])
        infCteComp: infCteComp = Element(infCteComp, documentation=['Detalhamento do CT-e complementado'])

        class infCteAnu(ComplexType):
            """Detalhamento do CT-e do tipo Anulação"""
            chCte: str = Element(str, documentation=['Chave de acesso do CT-e original a ser anulado e substituído'])
            dEmi: TData = Element(TData, base_type=date, documentation=['Data de emissão da declaração do tomador não contribuinte do ICMS'])
        infCteAnu: infCteAnu = Element(infCteAnu, documentation=['Detalhamento do CT-e do tipo Anulação'])

        class autXML(ComplexType):
            """Autorizados para download do XML do DF-e
Informar CNPJ ou CPF. Preencher os zeros não significativos."""
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

            def add(self, CNPJ=None, CPF=None) -> TCTe.infCte.autXML:
                return super().add(CNPJ=CNPJ, CPF=CPF)

            CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do autorizado', 'Informar zeros não significativos'])
            CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CPF do autorizado', 'Informar zeros não significativos'])
        autXML: List[autXML] = Element(autXML, max_occurs=10, documentation=['Autorizados para download do XML do DF-e', 'Informar CNPJ ou CPF. Preencher os zeros não significativos.'])
        versao: str = Attribute(None)
        Id: str = Attribute(None)
    infCte: infCte = Element(infCte, documentation=['Informações do CT-e'])
    Signature: Signature = Element(Signature)



class TIdLote(str):
    """Tipo Identificador de controle do envio do lote. Número seqüencial auto-incremental, de controle correspondente ao identificador único do lote enviado. A responsabilidade de gerar e controlar esse número é do próprio contribuinte."""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{1,15}", enumeration=[])
    pass



class TVerCTe(str):
    """Tipo Versão do CT-e - 2.00"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"2\.00", enumeration=[])
    pass



class TEnviCTe(Element):
    """Tipo Pedido de Concessão de Autorização da CT-e"""
    idLote: TIdLote = Element(TIdLote)
    CTe: List[TCTe] = Element(TCTe, max_occurs=50)
    versao: str = Attribute(TVerCTe)



class TRetEnviCTe(Element):
    """Tipo Retorno do Pedido de Concessão de Autorização da CT-e"""
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:1 - Produção; 2 - Homologação'])
    cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['Identificação da UF'])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que recebeu o Lote.'])
    cStat: TStat = Element(TStat, documentation=['Código do status da mensagem enviada.'])
    xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do serviço solicitado.'])

    class infRec(ComplexType):
        """Dados do Recibo do Lote"""
        nRec: TRec = Element(TRec, documentation=['Número do Recibo'])
        dhRecbto: dateTime = Element(dateTime, documentation=['Data e hora do recebimento, no formato AAAA-MM-DDTHH:MM:SS'])
        tMed: str = Element(str, documentation=['Tempo médio de resposta do serviço (em segundos) dos últimos 5 minutos'])
    infRec: infRec = Element(infRec, documentation=['Dados do Recibo do Lote'])
    versao: str = Attribute(TVerCTe)



class TEndernac(Element):
    """Tipo Dados do Endereço"""
    xLgr: str = Element(str, documentation=['Logradouro'])
    nro: str = Element(str, documentation=['Número'])
    xCpl: str = Element(str, documentation=['Complemento'])
    xBairro: str = Element(str, documentation=['Bairro'])
    cMun: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do município (utilizar a tabela do IBGE), informar 9999999 para operações com o exterior.'])
    xMun: str = Element(str, documentation=['Nome do município, , informar EXTERIOR para operações com o exterior.'])
    CEP: str = Element(str, filter=str.isdigit, documentation=['CEP'])
    UF: TUf = Element(TUf, documentation=['Sigla da UF', 'Informar EX para operações com o exterior.'])



class TEndOrg(Element):
    """Tipo Dados do Endereço"""
    xLgr: str = Element(str, documentation=['Logradouro'])
    nro: str = Element(str, documentation=['Número'])
    xCpl: str = Element(str, documentation=['Complemento'])
    xBairro: str = Element(str, documentation=['Bairro'])
    cMun: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do município (utilizar a tabela do IBGE), informar 9999999 para operações com o exterior.'])
    xMun: str = Element(str, documentation=['Nome do município', 'Informar EXTERIOR para operações com o exterior.'])
    CEP: str = Element(str, filter=str.isdigit, documentation=['CEP'])
    UF: TUf = Element(TUf, documentation=['Sigla da UF', 'Informar EX para operações com o exterior.'])
    cPais: str = Element(str, documentation=['Código do país'])
    xPais: str = Element(str, documentation=['Nome do país'])
    fone: TFone = Element(TFone, filter=str.isdigit, documentation=['Telefone'])



class TLocal(Element):
    """Tipo Dados do Local de Origem ou Destino"""
    cMun: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do município (utilizar a tabela do IBGE)'])
    xMun: str = Element(str, documentation=['Nome do município'])
    UF: TUf = Element(TUf, documentation=['Sigla da UF'])



class TEndReEnt(Element):
    """Tipo Dados do Local de Retirada ou Entrega"""
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
    CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['Número do CNPJ'])
    CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['Número do CPF'])
    xNome: str = Element(str, documentation=['Razão Social ou Nome'])
    xLgr: str = Element(str, documentation=['Logradouro'])
    nro: str = Element(str, documentation=['Número'])
    xCpl: str = Element(str, documentation=['Complemento'])
    xBairro: str = Element(str, documentation=['Bairro'])
    cMun: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do município (utilizar a tabela do IBGE) ', 'Informar 9999999 para operações com o exterior.'])
    xMun: str = Element(str, documentation=['Nome do município', 'Informar EXTERIOR para operações com o exterior.'])
    UF: TUf = Element(TUf, documentation=['Sigla da UF', 'Informar EX para operações com o exterior.'])



class TCListServ(str):
    """Tipo Código da Lista de Serviços LC 116/2003"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['101', '102', '103', '104', '105', '106', '107', '108', '201', '302', '303', '304', '305', '401', '402', '403', '404', '405', '406', '407', '408', '409', '410', '411', '412', '413', '414', '415', '416', '417', '418', '419', '420', '421', '422', '423', '501', '502', '503', '504', '505', '506', '507', '508', '509', '601', '602', '603', '604', '605', '701', '702', '703', '704', '705', '706', '707', '708', '709', '710', '711', '712', '713', '716', '717', '718', '719', '720', '721', '722', '801', '802', '901', '902', '903', '1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1009', '1010', '1101', '1102', '1103', '1104', '1201', '1202', '1203', '1204', '1205', '1206', '1207', '1208', '1209', '1210', '1211', '1212', '1213', '1214', '1215', '1216', '1217', '1302', '1303', '1304', '1305', '1401', '1402', '1403', '1404', '1405', '1406', '1407', '1408', '1409', '1410', '1411', '1412', '1413', '1501', '1502', '1503', '1504', '1505', '1506', '1507', '1508', '1509', '1510', '1511', '1512', '1513', '1514', '1515', '1516', '1517', '1518', '1601', '1701', '1702', '1703', '1704', '1705', '1706', '1708', '1709', '1710', '1711', '1712', '1713', '1714', '1715', '1716', '1717', '1718', '1719', '1720', '1721', '1722', '1723', '1724', '1801', '1901', '2001', '2002', '2003', '2101', '2201', '2301', '2401', '2501', '2502', '2503', '2504', '2601', '2701', '2801', '2901', '3001', '3101', '3201', '3301', '3401', '3501', '3601', '3701', '3801', '3901', '4001'])
    pass


