from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposGeralMDFe_v300 import *



class TEmail(str):
    """Tipo Email"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[^@]+@[^\.]+\..+", min_length=r"6", max_length=r"60", enumeration=[])
    pass



class TEndeEmi(Element):
    """Tipo Dados do Endereço"""
    xLgr: str = Element(str, documentation=['Logradouro'])
    nro: str = Element(str, documentation=['Número'])
    xCpl: str = Element(str, documentation=['Complemento'])
    xBairro: str = Element(str, documentation=['Bairro'])
    cMun: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do município (utilizar a tabela do IBGE), informar 9999999 para operações com o exterior.'])
    xMun: str = Element(str, documentation=['Nome do município, , informar EXTERIOR para operações com o exterior.'])
    CEP: str = Element(str, filter=str.isdigit, documentation=['CEP', 'Informar zeros não significativos'])
    UF: TUf = Element(TUf, documentation=['Sigla da UF, , informar EX para operações com o exterior.'])
    fone: str = Element(str, filter=str.isdigit, documentation=['Telefone'])
    email: TEmail = Element(TEmail, documentation=['Endereço de E-mail'])



class TContainer(str):
    """Tipo Número do Container"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[A-Z0-9]+", min_length=r"1", max_length=r"20", enumeration=[])
    pass



class TUnidCarga(Element):
    """Tipo Dados Unidade de Carga"""
    tpUnidCarga: TtipoUnidCarga = Element(TtipoUnidCarga, documentation=['Tipo da Unidade de Carga', '1 - Container;\n\n2 - ULD;\n\n3 - Pallet;\n\n4 - Outros;'])
    idUnidCarga: TContainer = Element(TContainer, documentation=['Identificação da Unidade de Carga', 'Informar a identificação da unidade de carga, por exemplo: número do container.'])

    class lacUnidCarga(ComplexType):
        """Lacres das Unidades de Carga"""
        _max_occurs = -1

        def add(self, nLacre=None) -> TUnidCarga.lacUnidCarga:
            return super().add(nLacre=nLacre)

        nLacre: str = Element(str, documentation=['Número do lacre'])
    lacUnidCarga: List[lacUnidCarga] = Element(lacUnidCarga, max_occurs=-1, documentation=['Lacres das Unidades de Carga'])
    qtdRat: str = Element(str, documentation=['Quantidade rateada (Peso,Volume)'])



class TUnidadeTransp(Element):
    """Tipo Dados Unidade de Transporte"""
    tpUnidTransp: TtipoUnidTransp = Element(TtipoUnidTransp, documentation=['Tipo da Unidade de Transporte', '1 - Rodoviário Tração;\n\n2 - Rodoviário Reboque;\n\n3 - Navio;\n\n4 - Balsa;\n\n5 - Aeronave;\n\n6 - Vagão;\n\n7 - Outros'])
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



class TRespTec(Element):
    """Tipo Dados da Responsável Técnico"""
    CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ da pessoa jurídica responsável técnica pelo sistema utilizado na emissão do documento fiscal eletrônico', 'Informar o CNPJ da pessoa jurídica desenvolvedora do sistema utilizado na emissão do documento fiscal eletrônico.'])
    xContato: str = Element(str, documentation=['Nome da pessoa a ser contatada', 'Informar o nome da pessoa a ser contatada na empresa desenvolvedora do sistema utilizado na emissão do documento fiscal eletrônico. No caso de pessoa física, informar o respectivo nome.'])
    email: TEmail = Element(TEmail, documentation=['Email da pessoa jurídica a ser contatada'])
    fone: str = Element(str, filter=str.isdigit, documentation=['Telefone da pessoa jurídica a ser contatada', 'Preencher com o Código DDD + número do telefone.'])
    idCSRT: str = Element(str, documentation=['Identificador do código de segurança do responsável técnico', 'Identificador do CSRT utilizado para geração do hash'])
    hashCSRT: str = Element(str, documentation=['Hash do token do código de segurança do responsável técnico', 'O hashCSRT é o resultado das funções SHA-1 e base64 do token CSRT fornecido pelo fisco + chave de acesso do DF-e. (Implementação em futura NT)\n\nObservação: 28 caracteres são representados no schema como 20 bytes do tipo base64Binary'])



class TModalMD(str):
    """Tipo Modal Manifesto"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1', '2', '3', '4'])
    pass



class TVerMDe(str):
    """Tipo Versão do MDF-e - 3.00"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"3\.00", enumeration=[])
    pass



class TMDFe(Element):
    """Tipo Manifesto de Documentos Fiscais Eletrônicos"""

    @property
    def chave(self):
        if self.infMDFe.Id:
            return self.infMDFe.Id[4:]

    @chave.setter
    def chave(self, value):
        self.infMDFe.ide.cDV = value[-1]
        self.infMDFe.Id = 'MDFe' + value

    class infMDFe(ComplexType):
        """Informações do MDF-e"""

        class ide(ComplexType):
            """Identificação do MDF-e"""
            cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['Código da UF do emitente do MDF-e', 'Código da UF do emitente do Documento Fiscal. Utilizar a\nTabela do IBGE de código de unidades da federação.'])
            tpAmb: TAmb = Element(TAmb, documentation=['Tipo do Ambiente', '1 - Produção\n2 - Homologação'])
            tpEmit: TEmit = Element(TEmit, documentation=['Tipo do Emitente\n', '1 - Prestador de serviço de transporte \n2 - Transportador de Carga Própria 3 - Prestador de serviço de transporte que emitirá CT-e Globalizado \n\nOBS: Deve ser preenchido com 2 para emitentes de NF-e e pelas transportadoras quando estiverem fazendo transporte de carga própria. Deve ser preenchido com 3 para transportador de carga que emitirá à posteriori CT-e Globalizado relacionando as NF-e.'])
            tpTransp: TTransp = Element(TTransp, documentation=['Tipo do Transportador', '1 - ETC\n\n2 - TAC\n\n3 - CTC'])
            mod: TModMD = Element(TModMD, documentation=['Modelo do Manifesto Eletrônico', 'Utilizar o código 58 para identificação do MDF-e'])
            serie: TSerie = Element(TSerie, documentation=['Série do Manifesto', 'Informar a série do documento fiscal (informar zero se inexistente).\nSérie na faixa [920-969]: Reservada para emissão por contribuinte pessoa física com inscrição estadual.'])
            nMDF: TNF = Element(TNF, documentation=['Número do Manifesto', 'Número que identifica o Manifesto. 1 a 999999999.'])
            cMDF: str = Element(str, documentation=['Código numérico que compõe a Chave de Acesso. ', 'Código aleatório gerado pelo emitente, com o objetivo de evitar acessos indevidos ao documento.'])
            cDV: str = Element(str, documentation=['Digito verificador da chave de acesso do Manifesto', 'Informar o dígito  de controle da chave de acesso do MDF-e, que deve ser calculado com a aplicação do algoritmo módulo 11 (base 2,9) da chave de acesso. '])
            modal: TModalMD = Element(TModalMD, documentation=['Modalidade de transporte', '1 - Rodoviário;\n2 - Aéreo; 3 - Aquaviário; 4 - Ferroviário.'])
            dhEmi: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e hora de emissão do Manifesto', 'Formato AAAA-MM-DDTHH:MM:DD TZD'])
            tpEmis: str = Element(str, documentation=['Forma de emissão do Manifesto', '1 - Normal\n; 2 - Contingência; 3-Regime Especial NFF'])
            procEmi: str = Element(str, documentation=['Identificação do processo de emissão do Manifesto', '0 - emissão de MDF-e com aplicativo do contribuinte'])
            verProc: str = Element(str, documentation=['Versão do processo de emissão', 'Informar a versão do aplicativo emissor de MDF-e.'])
            UFIni: TUf = Element(TUf, documentation=['Sigla da UF do Carregamento', "Utilizar a Tabela do IBGE de código de unidades da federação.\nInformar 'EX' para operações com o exterior."])
            UFFim: TUf = Element(TUf, documentation=['Sigla da UF do Descarregamento', "Utilizar a Tabela do IBGE de código de unidades da federação.\nInformar 'EX' para operações com o exterior."])

            class infMunCarrega(ComplexType):
                """Informações dos Municípios de Carregamento"""
                _max_occurs = 50

                def add(self, cMunCarrega=None, xMunCarrega=None) -> TMDFe.infMDFe.ide.infMunCarrega:
                    return super().add(cMunCarrega=cMunCarrega, xMunCarrega=xMunCarrega)

                cMunCarrega: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do Município de Carregamento'])
                xMunCarrega: str = Element(str, documentation=['Nome do Município de Carregamento'])
            infMunCarrega: List[infMunCarrega] = Element(infMunCarrega, max_occurs=50, documentation=['Informações dos Municípios de Carregamento'])

            class infPercurso(ComplexType):
                """Informações do Percurso do MDF-e"""
                _max_occurs = 25

                def add(self, UFPer=None) -> TMDFe.infMDFe.ide.infPercurso:
                    return super().add(UFPer=UFPer)

                UFPer: TUf = Element(TUf, documentation=['Sigla das Unidades da Federação do percurso do veículo.', 'Não é necessário repetir as UF de Início e Fim'])
            infPercurso: List[infPercurso] = Element(infPercurso, max_occurs=25, documentation=['Informações do Percurso do MDF-e'])
            dhIniViagem: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e hora previstos de inicio da viagem', 'Formato AAAA-MM-DDTHH:MM:DD TZD'])
            indCanalVerde: str = Element(str, documentation=['Indicador de participação do Canal Verde'])
            indCarregaPosterior: str = Element(str, documentation=['Indicador de MDF-e com inclusão da Carga posterior a emissão por evento de inclusão de DF-e'])
        ide: ide = Element(ide, documentation=['Identificação do MDF-e'])

        class emit(ComplexType):
            """Identificação do Emitente do Manifesto"""
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
            CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do emitente', 'Informar zeros não significativos'])
            CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CPF do emitente', 'Informar zeros não significativos.\n\nUsar com série específica 920-969 para emitente pessoa física com inscrição estadual.\nPoderá ser usado também para emissão do Regime Especial da Nota Fiscal Fácil'])
            IE: str = Element(str, documentation=['Inscrição Estadual do emitemte'])
            xNome: str = Element(str, documentation=['Razão social ou Nome do emitente'])
            xFant: str = Element(str, documentation=['Nome fantasia do emitente'])
            enderEmit: TEndeEmi = Element(TEndeEmi, documentation=['Endereço do emitente'])
        emit: emit = Element(emit, documentation=['Identificação do Emitente do Manifesto'])

        class infModal(ComplexType):
            """Informações do modal"""
            versaoModal: str = Attribute(None, default='3.00')
            from .mdfeModalRodoviario_v300 import rodo
            rodo: rodo = Element(rodo, documentation=['Informações do modal Rodoviário'])
        infModal: infModal = Element(infModal, documentation=['Informações do modal'])

        class infDoc(ComplexType):
            """Informações dos Documentos fiscais vinculados ao manifesto"""

            class infMunDescarga(ComplexType):
                """Informações dos Municípios de descarregamento"""
                _max_occurs = 1000

                def add(self, cMunDescarga=None, xMunDescarga=None, infCTe=None, infNFe=None, infMDFeTransp=None) -> TMDFe.infMDFe.infDoc.infMunDescarga:
                    return super().add(cMunDescarga=cMunDescarga, xMunDescarga=xMunDescarga, infCTe=infCTe, infNFe=infNFe, infMDFeTransp=infMDFeTransp)

                cMunDescarga: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do Município de Descarregamento'])
                xMunDescarga: str = Element(str, documentation=['Nome do Município de Descarregamento'])

                class infCTe(ComplexType):
                    """Conhecimentos de Tranporte - usar este grupo quando for prestador de serviço de transporte"""
                    _max_occurs = 10000

                    def add(self, chCTe=None, SegCodBarra=None, indReentrega=None, infUnidTransp=None, peri=None, infEntregaParcial=None) -> TMDFe.infMDFe.infDoc.infMunDescarga.infCTe:
                        return super().add(chCTe=chCTe, SegCodBarra=SegCodBarra, indReentrega=indReentrega, infUnidTransp=infUnidTransp, peri=peri, infEntregaParcial=infEntregaParcial)

                    chCTe: TChCTe = Element(TChCTe, documentation=['Conhecimento Eletrônico - Chave de Acesso'])
                    SegCodBarra: TSegCodBarra = Element(TSegCodBarra, documentation=['Segundo código de barras'])
                    indReentrega: str = Element(str, documentation=['Indicador de Reentrega'])
                    infUnidTransp: List[TUnidadeTransp] = Element(TUnidadeTransp, max_occurs=-1, documentation=['Informações das Unidades de Transporte (Carreta/Reboque/Vagão)', 'Deve ser preenchido com as informações das unidades de transporte utilizadas.'])

                    class peri(ComplexType):
                        """Preenchido quando for  transporte de produtos classificados pela ONU como perigosos."""
                        _max_occurs = -1

                        def add(self, nONU=None, xNomeAE=None, xClaRisco=None, grEmb=None, qTotProd=None, qVolTipo=None) -> TMDFe.infMDFe.infDoc.infMunDescarga.infCTe.peri:
                            return super().add(nONU=nONU, xNomeAE=xNomeAE, xClaRisco=xClaRisco, grEmb=grEmb, qTotProd=qTotProd, qVolTipo=qVolTipo)

                        nONU: str = Element(str, documentation=['Número ONU/UN', 'Ver a legislação de transporte de produtos perigosos aplicadas ao modal  '])
                        xNomeAE: str = Element(str, documentation=['Nome apropriado para embarque do produto', 'Ver a legislação de transporte de produtos perigosos aplicada ao modo de transporte'])
                        xClaRisco: str = Element(str, documentation=['Classe ou subclasse/divisão, e risco subsidiário/risco secundário', 'Ver a legislação de transporte de produtos perigosos aplicadas ao modal'])
                        grEmb: str = Element(str, documentation=['Grupo de Embalagem', 'Ver a legislação de transporte de produtos perigosos aplicadas ao modal\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPreenchimento obrigatório para o modal aéreo.\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tA legislação para o modal rodoviário e ferroviário não atribui grupo de embalagem para todos os produtos, portanto haverá casos de não preenchimento desse campo.'])
                        qTotProd: str = Element(str, documentation=['Quantidade total por produto', 'Preencher conforme a legislação de transporte de produtos perigosos aplicada ao modal'])
                        qVolTipo: str = Element(str, documentation=['Quantidade e Tipo de volumes', 'Preencher conforme a legislação de transporte de produtos perigosos aplicada ao modal'])
                    peri: List[peri] = Element(peri, max_occurs=-1, documentation=['Preenchido quando for  transporte de produtos classificados pela ONU como perigosos.'])

                    class infEntregaParcial(ComplexType):
                        """Grupo de informações da Entrega Parcial (Corte de Voo)"""
                        qtdTotal: TDec_1104 = Element(TDec_1104, tipo="N", tam=(11, 4), base_type=Decimal, documentation=['Quantidade total de volumes'])
                        qtdParcial: TDec_1104 = Element(TDec_1104, tipo="N", tam=(11, 4), base_type=Decimal, documentation=['Quantidade de volumes enviados no MDF-e'])
                    infEntregaParcial: infEntregaParcial = Element(infEntregaParcial, documentation=['Grupo de informações da Entrega Parcial (Corte de Voo)'])
                infCTe: List[infCTe] = Element(infCTe, max_occurs=10000, documentation=['Conhecimentos de Tranporte - usar este grupo quando for prestador de serviço de transporte'])

                class infNFe(ComplexType):
                    """Nota Fiscal Eletronica"""
                    _max_occurs = 10000

                    def add(self, chNFe=None, SegCodBarra=None, indReentrega=None, infUnidTransp=None, peri=None) -> TMDFe.infMDFe.infDoc.infMunDescarga.infNFe:
                        return super().add(chNFe=chNFe, SegCodBarra=SegCodBarra, indReentrega=indReentrega, infUnidTransp=infUnidTransp, peri=peri)

                    chNFe: TChNFe = Element(TChNFe, documentation=['Nota Fiscal Eletrônica'])
                    SegCodBarra: TSegCodBarra = Element(TSegCodBarra, documentation=['Segundo código de barras'])
                    indReentrega: str = Element(str, documentation=['Indicador de Reentrega'])
                    infUnidTransp: List[TUnidadeTransp] = Element(TUnidadeTransp, max_occurs=-1, documentation=['Informações das Unidades de Transporte (Carreta/Reboque/Vagão)', 'Deve ser preenchido com as informações das unidades de transporte utilizadas.'])

                    class peri(ComplexType):
                        """Preenchido quando for  transporte de produtos classificados pela ONU como perigosos."""
                        _max_occurs = -1

                        def add(self, nONU=None, xNomeAE=None, xClaRisco=None, grEmb=None, qTotProd=None, qVolTipo=None) -> TMDFe.infMDFe.infDoc.infMunDescarga.infNFe.peri:
                            return super().add(nONU=nONU, xNomeAE=xNomeAE, xClaRisco=xClaRisco, grEmb=grEmb, qTotProd=qTotProd, qVolTipo=qVolTipo)

                        nONU: str = Element(str, documentation=['Número ONU/UN', 'Ver a legislação de transporte de produtos perigosos aplicadas ao modal  '])
                        xNomeAE: str = Element(str, documentation=['Nome apropriado para embarque do produto', 'Ver a legislação de transporte de produtos perigosos aplicada ao modo de transporte'])
                        xClaRisco: str = Element(str, documentation=['Classe ou subclasse/divisão, e risco subsidiário/risco secundário', 'Ver a legislação de transporte de produtos perigosos aplicadas ao modal'])
                        grEmb: str = Element(str, documentation=['Grupo de Embalagem', 'Ver a legislação de transporte de produtos perigosos aplicadas ao modal\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPreenchimento obrigatório para o modal aéreo.\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tA legislação para o modal rodoviário e ferroviário não atribui grupo de embalagem para todos os produtos, portanto haverá casos de não preenchimento desse campo.'])
                        qTotProd: str = Element(str, documentation=['Quantidade total por produto', 'Preencher conforme a legislação de transporte de produtos perigosos aplicada ao modal'])
                        qVolTipo: str = Element(str, documentation=['Quantidade e Tipo de volumes', 'Preencher conforme a legislação de transporte de produtos perigosos aplicada ao modal'])
                    peri: List[peri] = Element(peri, max_occurs=-1, documentation=['Preenchido quando for  transporte de produtos classificados pela ONU como perigosos.'])
                infNFe: List[infNFe] = Element(infNFe, max_occurs=10000, documentation=['Nota Fiscal Eletronica'])

                class infMDFeTransp(ComplexType):
                    """Manifesto Eletrônico de Documentos Fiscais. Somente para modal Aquaviário (vide regras MOC)"""
                    _max_occurs = 10000

                    def add(self, chMDFe=None, indReentrega=None, infUnidTransp=None, peri=None) -> TMDFe.infMDFe.infDoc.infMunDescarga.infMDFeTransp:
                        return super().add(chMDFe=chMDFe, indReentrega=indReentrega, infUnidTransp=infUnidTransp, peri=peri)

                    chMDFe: TChNFe = Element(TChNFe, documentation=['Manifesto Eletrônico de Documentos Fiscais'])
                    indReentrega: str = Element(str, documentation=['Indicador de Reentrega'])
                    infUnidTransp: List[TUnidadeTransp] = Element(TUnidadeTransp, max_occurs=-1, documentation=['Informações das Unidades de Transporte (Carreta/Reboque/Vagão)', 'Dispositivo de carga utilizada (Unit Load Device - ULD) significa todo tipo de contêiner de carga, vagão, contêiner de avião, palete de aeronave com rede ou palete de aeronave com rede sobre um iglu. '])

                    class peri(ComplexType):
                        """Preenchido quando for  transporte de produtos classificados pela ONU como perigosos."""
                        _max_occurs = -1

                        def add(self, nONU=None, xNomeAE=None, xClaRisco=None, grEmb=None, qTotProd=None, qVolTipo=None) -> TMDFe.infMDFe.infDoc.infMunDescarga.infMDFeTransp.peri:
                            return super().add(nONU=nONU, xNomeAE=xNomeAE, xClaRisco=xClaRisco, grEmb=grEmb, qTotProd=qTotProd, qVolTipo=qVolTipo)

                        nONU: str = Element(str, documentation=['Número ONU/UN', 'Ver a legislação de transporte de produtos perigosos aplicadas ao modal  '])
                        xNomeAE: str = Element(str, documentation=['Nome apropriado para embarque do produto', 'Ver a legislação de transporte de produtos perigosos aplicada ao modo de transporte'])
                        xClaRisco: str = Element(str, documentation=['Classe ou subclasse/divisão, e risco subsidiário/risco secundário', 'Ver a legislação de transporte de produtos perigosos aplicadas ao modal'])
                        grEmb: str = Element(str, documentation=['Grupo de Embalagem', 'Ver a legislação de transporte de produtos perigosos aplicadas ao modal\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPreenchimento obrigatório para o modal aéreo.\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tA legislação para o modal rodoviário e ferroviário não atribui grupo de embalagem para todos os produtos, portanto haverá casos de não preenchimento desse campo.'])
                        qTotProd: str = Element(str, documentation=['Quantidade total por produto', 'Preencher conforme a legislação de transporte de produtos perigosos aplicada ao modal'])
                        qVolTipo: str = Element(str, documentation=['Quantidade e Tipo de volumes', 'Preencher conforme a legislação de transporte de produtos perigosos aplicada ao modal'])
                    peri: List[peri] = Element(peri, max_occurs=-1, documentation=['Preenchido quando for  transporte de produtos classificados pela ONU como perigosos.'])
                infMDFeTransp: List[infMDFeTransp] = Element(infMDFeTransp, max_occurs=10000, documentation=['Manifesto Eletrônico de Documentos Fiscais. Somente para modal Aquaviário (vide regras MOC)'])
            infMunDescarga: List[infMunDescarga] = Element(infMunDescarga, max_occurs=1000, documentation=['Informações dos Municípios de descarregamento'])
        infDoc: infDoc = Element(infDoc, documentation=['Informações dos Documentos fiscais vinculados ao manifesto'])

        class seg(ComplexType):
            """Informações de Seguro da Carga"""
            _max_occurs = -1

            def add(self, infResp=None, infSeg=None, nApol=None, nAver=None) -> TMDFe.infMDFe.seg:
                return super().add(infResp=infResp, infSeg=infSeg, nApol=nApol, nAver=nAver)


            class infResp(ComplexType):
                """Informações do responsável pelo seguro da carga"""
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
                respSeg: str = Element(str, documentation=['Responsável pelo seguro', 'Preencher com:\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1- Emitente do MDF-e;\n\t\t\t\t\t\t\n22 - Responsável pela contratação do serviço de transporte (contratante)\t\n\n\nDados obrigatórios apenas no modal Rodoviário, depois da lei 11.442/07. Para os demais modais esta informação é opcional.'])
                CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['Número do CNPJ do responsável pelo seguro', 'Obrigatório apenas se responsável pelo seguro for (2) responsável pela contratação do transporte - pessoa jurídica'])
                CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['Número do CPF do responsável pelo seguro', 'Obrigatório apenas se responsável pelo seguro for (2) responsável pela contratação do transporte - pessoa física'])
            infResp: infResp = Element(infResp, documentation=['Informações do responsável pelo seguro da carga'])

            class infSeg(ComplexType):
                """Informações da seguradora"""
                xSeg: str = Element(str, documentation=['Nome da Seguradora'])
                CNPJ: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['Número do CNPJ da seguradora', 'Obrigatório apenas se responsável pelo seguro for (2) responsável pela contratação do transporte - pessoa jurídica'])
            infSeg: infSeg = Element(infSeg, documentation=['Informações da seguradora'])
            nApol: str = Element(str, documentation=['Número da Apólice', 'Obrigatório pela lei 11.442/07 (RCTRC)'])
            nAver: List[str] = Element(str, max_occurs=-1, documentation=['Número da Averbação', 'Informar as averbações do seguro'])
        seg: List[seg] = Element(seg, max_occurs=-1, documentation=['Informações de Seguro da Carga'])

        class prodPred(ComplexType):
            """Produto predominante
Informar a descrição do produto predominante"""
            tpCarga: str = Element(str, documentation=['Tipo de Carga', 'Conforme Resolução ANTT nº.  5.849/2019.\n\n01-Granel sólido;\n02-Granel líquido;\n03-Frigorificada;\n04-Conteinerizada;\n05-Carga Geral;\n06-Neogranel;\n07-Perigosa (granel sólido);\n08-Perigosa (granel líquido);\n09-Perigosa (carga frigorificada);\n10-Perigosa (conteinerizada);\n11-Perigosa (carga geral).'])
            xProd: str = Element(str, documentation=['Descrição do produto '])
            cEAN: str = Element(str, documentation=['GTIN (Global Trade Item Number) do produto, antigo código EAN ou código de barras'])
            NCM: str = Element(str, documentation=['Código NCM '])

            class infLotacao(ComplexType):
                """Informações da carga lotação. Informar somente quando MDF-e for de carga lotação"""

                class infLocalCarrega(ComplexType):
                    """Informações da localização de carregamento do MDF-e de carga lotação"""
                    _choice = [['CEP']]
                    CEP: str = Element(str, filter=str.isdigit, documentation=['CEP onde foi carregado o MDF-e', 'Informar zeros não significativos'])
                    latitude: TLatitude = Element(TLatitude, documentation=['Latitude do ponto geográfico onde foi carregado o MDF-e'])
                    longitude: TLongitude = Element(TLongitude, documentation=['Latitude do ponto geográfico onde foi carregado o MDF-e'])
                infLocalCarrega: infLocalCarrega = Element(infLocalCarrega, documentation=['Informações da localização de carregamento do MDF-e de carga lotação'])

                class infLocalDescarrega(ComplexType):
                    """Informações da localização de descarregamento do MDF-e de carga lotação"""
                    _choice = [['CEP']]
                    CEP: str = Element(str, filter=str.isdigit, documentation=['CEP onde foi descarregado o MDF-e', 'Informar zeros não significativos'])
                    latitude: TLatitude = Element(TLatitude, documentation=['Latitude do ponto geográfico onde foi descarregado o MDF-e'])
                    longitude: TLongitude = Element(TLongitude, documentation=['Latitude do ponto geográfico onde foi descarregado o MDF-e'])
                infLocalDescarrega: infLocalDescarrega = Element(infLocalDescarrega, documentation=['Informações da localização de descarregamento do MDF-e de carga lotação'])
            infLotacao: infLotacao = Element(infLotacao, documentation=['Informações da carga lotação. Informar somente quando MDF-e for de carga lotação'])
        prodPred: prodPred = Element(prodPred, documentation=['Produto predominante', 'Informar a descrição do produto predominante'])

        class tot(ComplexType):
            """Totalizadores da carga transportada e seus documentos fiscais"""
            qCTe: str = Element(str, documentation=['Quantidade total de CT-e relacionados no Manifesto'])
            qNFe: str = Element(str, documentation=['Quantidade total de NF-e relacionadas no Manifesto'])
            qMDFe: str = Element(str, documentation=['Quantidade total de MDF-e relacionados no Manifesto Aquaviário'])
            vCarga: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor total da carga / mercadorias transportadas'])
            cUnid: str = Element(str, documentation=['Código da unidade de medida do Peso Bruto da Carga / Mercadorias transportadas', '01 – KG;  02 - TON'])
            qCarga: TDec_1104 = Element(TDec_1104, tipo="N", tam=(11, 4), base_type=Decimal, documentation=['Peso Bruto Total da Carga / Mercadorias transportadas'])
        tot: tot = Element(tot, documentation=['Totalizadores da carga transportada e seus documentos fiscais'])

        class lacres(ComplexType):
            """Lacres do MDF-e
Preechimento opcional para os modais Rodoviário e Ferroviário"""
            _max_occurs = -1

            def add(self, nLacre=None) -> TMDFe.infMDFe.lacres:
                return super().add(nLacre=nLacre)

            nLacre: str = Element(str, documentation=['número do lacre'])
        lacres: List[lacres] = Element(lacres, max_occurs=-1, documentation=['Lacres do MDF-e', 'Preechimento opcional para os modais Rodoviário e Ferroviário'])

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

            def add(self, CNPJ=None, CPF=None) -> TMDFe.infMDFe.autXML:
                return super().add(CNPJ=CNPJ, CPF=CPF)

            CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do autorizado', 'Informar zeros não significativos'])
            CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CPF do autorizado', 'Informar zeros não significativos'])
        autXML: List[autXML] = Element(autXML, max_occurs=10, documentation=['Autorizados para download do XML do DF-e', 'Informar CNPJ ou CPF. Preencher os zeros não significativos.'])

        class infAdic(ComplexType):
            """Informações Adicionais"""
            infAdFisco: str = Element(str, documentation=['Informações adicionais de interesse do Fisco', 'Norma referenciada, informações complementares, etc'])
            infCpl: str = Element(str, documentation=['Informações complementares de interesse do Contribuinte'])
        infAdic: infAdic = Element(infAdic, documentation=['Informações Adicionais'])
        infRespTec: TRespTec = Element(TRespTec, documentation=['Informações do Responsável Técnico pela emissão do DF-e'])

        class infSolicNFF(ComplexType):
            """Grupo de informações do pedido de emissão da Nota Fiscal Fácil"""
            xSolic: str = Element(str, documentation=['Solicitação do pedido de emissão da NFF.', 'Será preenchido com a totalidade de campos informados no aplicativo emissor serializado.'])
        infSolicNFF: infSolicNFF = Element(infSolicNFF, documentation=['Grupo de informações do pedido de emissão da Nota Fiscal Fácil'])

        class infPAA(ComplexType):
            """Grupo de Informação do Provedor de Assinatura e Autorização"""
            CNPJPAA: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do Provedor de Assinatura e Autorização'])

            class PAASignature(ComplexType):
                """Assinatura RSA do Emitente para DFe gerados por PAA"""
                SignatureValue: base64Binary = Element(base64Binary, documentation=['Assinatura digital padrão RSA', 'Converter o atributo Id do DFe para array de bytes e assinar com a chave privada do RSA com algoritmo SHA1 gerando um valor no formato base64.'])
                RSAKeyValue: TRSAKeyValueType = Element(TRSAKeyValueType, documentation=['Chave Publica no padrão XML RSA Key'])
            PAASignature: PAASignature = Element(PAASignature, documentation=['Assinatura RSA do Emitente para DFe gerados por PAA'])
        infPAA: infPAA = Element(infPAA, documentation=['Grupo de Informação do Provedor de Assinatura e Autorização'])
        versao: str = Attribute(TVerMDe)
        Id: str = Attribute(None)
    infMDFe: infMDFe = Element(infMDFe, documentation=['Informações do MDF-e'])

    class infMDFeSupl(ComplexType):
        """Informações suplementares do MDF-e"""
        qrCodMDFe: str = Element(str, documentation=['Texto com o QR-Code para consulta do MDF-e'])
    infMDFeSupl: infMDFeSupl = Element(infMDFeSupl, documentation=['Informações suplementares do MDF-e'])
    Signature: Signature = Element(Signature)



class TIdLote(str):
    """Tipo Identificador de controle do envio do lote. Número seqüencial auto-incremental, de controle correspondente ao identificador único do lote enviado. A responsabilidade de gerar e controlar esse número é do próprio contribuinte."""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{1,15}", enumeration=[])
    pass



class TEnviMDFe(Element):
    """Tipo Pedido de Autorização Assíncrona de MDF-e"""
    idLote: TIdLote = Element(TIdLote)
    MDFe: TMDFe = Element(TMDFe)
    versao: str = Attribute(TVerMDe)



class TProtMDFe(Element):
    """Tipo Protocolo de status resultado do processamento do MDF-e"""

    class infProt(ComplexType):
        """Dados do protocolo de status"""
        tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
        verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que processou a NF-3e'])
        chMDFe: TChMDFe = Element(TChMDFe, documentation=['Chave de acesso do MDF-e'])
        dhRecbto: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e hora de processamento, no formato AAAA-MM-DDTHH:MM:SS TZD.'])
        nProt: TProt = Element(TProt, documentation=['Número do Protocolo de Status do MDF-e'])
        digVal: DigestValueType = Element(DigestValueType, documentation=['Digest Value do MDF-e processado. Utilizado para conferir a integridade do MDF-e original.'])
        cStat: str = Element(str, documentation=['Código do status do MDF-e'])
        xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do MDF-e.'])
        Id: str = Attribute(ID)
    infProt: infProt = Element(infProt, documentation=['Dados do protocolo de status'])

    class infFisco(ComplexType):
        """Mensagem do Fisco"""
        cMsg: str = Element(str, documentation=['Código do status da mensagem do fisco'])
        xMsg: TMotivo = Element(TMotivo, documentation=['Mensagem do Fisco'])
    infFisco: infFisco = Element(infFisco, documentation=['Mensagem do Fisco'])
    Signature: Signature = Element(Signature)
    versao: str = Attribute(TVerMDe)



class TRetMDFe(Element):
    """Tipo Retorno do Pedido de Autorização do MDF-e"""
    tpAmb: str = Element(str, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['Identificação da UF'])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que recebeu o Arquivo.'])
    cStat: TStat = Element(TStat, documentation=['Código do status da mensagem enviada.'])
    xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do serviço solicitado.'])
    protMDFe: TProtMDFe = Element(TProtMDFe, documentation=['Dados do Recibo do Arquivo'])
    versao: str = Attribute(TVerMDe)



class TRetEnviMDFe(Element):
    """Tipo Retorno do Recibo do Pedido de Autorização do MDF-e"""
    tpAmb: str = Element(str, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    cUF: TCodUfIBGE = Element(TCodUfIBGE, documentation=['Identificação da UF'])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que recebeu o Arquivo.'])
    cStat: TStat = Element(TStat, documentation=['Código do status da mensagem enviada.'])
    xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do serviço solicitado.'])

    class infRec(ComplexType):
        """Dados do Recibo do Arquivo"""
        nRec: TRec = Element(TRec, documentation=['Número do Recibo'])
        dhRecbto: dateTime = Element(dateTime, documentation=['Data e hora do recebimento, no formato AAAA-MM-DDTHH:MM:SS'])
        tMed: str = Element(str, documentation=['Tempo médio de resposta do serviço (em segundos) dos últimos 5 minutos'])
    infRec: infRec = Element(infRec, documentation=['Dados do Recibo do Arquivo'])
    versao: str = Attribute(TVerMDe)



class TEndereco(Element):
    """Tipo Dados do Endereço"""
    xLgr: str = Element(str, documentation=['Logradouro'])
    nro: str = Element(str, documentation=['Número'])
    xCpl: str = Element(str, documentation=['Complemento'])
    xBairro: str = Element(str, documentation=['Bairro'])
    cMun: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do município (utilizar a tabela do IBGE), informar 9999999 para operações com o exterior.'])
    xMun: str = Element(str, documentation=['Nome do município, informar EXTERIOR para operações com o exterior.'])
    CEP: str = Element(str, filter=str.isdigit, documentation=['CEP', 'Informar os zeros não significativos'])
    UF: TUf = Element(TUf, documentation=['Sigla da UF, informar EX para operações com o exterior.'])
    cPais: str = Element(str, documentation=['Código do país', 'Utilizar a tabela do BACEN'])
    xPais: str = Element(str, documentation=['Nome do país'])



class TEndernac(Element):
    """Tipo Dados do Endereço"""
    xLgr: str = Element(str, documentation=['Logradouro'])
    nro: str = Element(str, documentation=['Número'])
    xCpl: str = Element(str, documentation=['Complemento'])
    xBairro: str = Element(str, documentation=['Bairro'])
    cMun: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do município (utilizar a tabela do IBGE), informar 9999999 para operações com o exterior.'])
    xMun: str = Element(str, documentation=['Nome do município, , informar EXTERIOR para operações com o exterior.'])
    CEP: str = Element(str, filter=str.isdigit, documentation=['CEP'])
    UF: TUf = Element(TUf, documentation=['Sigla da UF, , informar EX para operações com o exterior.'])



class TEnderFer(Element):
    """Tipo Dados do Endereço"""
    xLgr: str = Element(str, documentation=['Logradouro'])
    nro: str = Element(str, documentation=['Número'])
    xCpl: str = Element(str, documentation=['Complemento'])
    xBairro: str = Element(str, documentation=['Bairro'])
    cMun: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do município (utilizar a tabela do IBGE), informar 9999999 para operações com o exterior.'])
    xMun: str = Element(str, documentation=['Nome do município, , informar EXTERIOR para operações com o exterior.'])
    CEP: str = Element(str, filter=str.isdigit, documentation=['CEP'])
    UF: TUf = Element(TUf, documentation=['Sigla da UF, , informar EX para operações com o exterior.'])



class TEndOrg(Element):
    """Tipo Dados do Endereço"""
    xLgr: str = Element(str, documentation=['Logradouro'])
    nro: str = Element(str, documentation=['Número'])
    xCpl: str = Element(str, documentation=['Complemento'])
    xBairro: str = Element(str, documentation=['Bairro'])
    cMun: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do município (utilizar a tabela do IBGE), informar 9999999 para operações com o exterior.'])
    xMun: str = Element(str, documentation=['Nome do município, , informar EXTERIOR para operações com o exterior.'])
    CEP: str = Element(str, filter=str.isdigit, documentation=['CEP'])
    UF: TUf = Element(TUf, documentation=['Sigla da UF, , informar EX para operações com o exterior.'])
    cPais: str = Element(str, documentation=['Código do país'])
    xPais: str = Element(str, documentation=['Nome do país'])
    fone: str = Element(str, filter=str.isdigit, documentation=['Telefone'])



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
    cMun: TCodMunIBGE = Element(TCodMunIBGE, documentation=['Código do município (utilizar a tabela do IBGE), informar 9999999 para operações com o exterior.'])
    xMun: str = Element(str, documentation=['Nome do município, , informar EXTERIOR para operações com o exterior.'])
    UF: TUf = Element(TUf, documentation=['Sigla da UF, , informar EX para operações com o exterior.'])



class TPIN(str):
    """Tipo Dados PIN (SUFRAMA)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[1-9]{1}[0-9]{1,8}", min_length=r"2", max_length=r"9", enumeration=[])
    pass



class TNFeNF(Element):
    """Tipo  de Dados das Notas Fiscais Papel e Eletrônica"""
    _choice = [['infNFe', 'infNF']]

    class infNFe(ComplexType):
        """Informações da NF-e"""
        chNFe: TChNFe = Element(TChNFe, documentation=['Chave de acesso da NF-e'])
        PIN: TPIN = Element(TPIN, documentation=['PIN SUFRAMA', 'PIN atribuído pela SUFRAMA para a operação.'])
    infNFe: infNFe = Element(infNFe, documentation=['Informações da NF-e'])

    class infNF(ComplexType):
        """Informações da NF mod 1 e 1A"""

        class emi(ComplexType):
            """Informações do Emitente da NF"""
            CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do emitente', None])
            xNome: str = Element(str, documentation=['Razão Social ou Nome '])
            UF: TUf = Element(TUf, documentation=['UF do Emitente', "Informar 'EX' para operações com o exterior."])
        emi: emi = Element(emi, documentation=['Informações do Emitente da NF'])

        class dest(ComplexType):
            """Informações do Destinatário da NF"""
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
            CNPJ: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['CNPJ do Destinatário', 'Informar o CNPJ ou o CPF do destinatário, preenchendo os\nzeros não significativos.\nNão informar o conteúdo da TAG se a operação for realizada com o Exterior.'])
            CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CPF do Destinatário', 'Informar os zeros não significativos.\n'])
            xNome: str = Element(str, documentation=['Razão Social ou Nome '])
            UF: TUf = Element(TUf, documentation=['UF do Destinatário', "Informar 'EX' para operações com o exterior."])
        dest: dest = Element(dest, documentation=['Informações do Destinatário da NF'])
        serie: str = Element(str, documentation=['Série'])
        nNF: str = Element(str, documentation=['Número '])
        dEmi: TData = Element(TData, base_type=date, documentation=['Data de Emissão', 'Formato AAAA-MM-DD'])
        vNF: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor Total da NF'])
        PIN: TPIN = Element(TPIN, documentation=['PIN SUFRAMA', 'PIN atribuído pela SUFRAMA para a operação.'])
    infNF: infNF = Element(infNF, documentation=['Informações da NF mod 1 e 1A'])



class TProcEmi(str):
    """Tipo processo de emissão do MDF-e"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['0'])
    pass



class TModDoc(str):
    """Tipo Modelo do Documento"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['01', '1B', '02', '2D', '2E', '04', '06', '07', '08', '8B', '09', '10', '11', '13', '14', '15', '16', '17', '18', '20', '21', '22', '23', '24', '25', '26', '27', '28', '55'])
    pass



class TTime(str):
    """Tipo hora"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])", enumeration=[])
    pass


