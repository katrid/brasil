from typing import List, Required, Annotated
import enum
from datetime import date
from decimal import Decimal

from brasil.sped.registro import BlockList, Registro, BlocoSPED


class IndMov(enum.StrEnum):
    ComDados = "0"  # 0- Bloco com dados informados;
    SemDados = "1"  # 1- Bloco sem dados informados.


class IndPerfil(enum.StrEnum):
    PerfilA = "A"  # A  Perfil A
    PerfilB = "B"  # B  Perfil B
    PerfilC = "C"  # C  Perfil C
    PerfilD = "D"  # D  Perfil D
    Nenhum = ""  # Nenhum


class IndAtiv(enum.StrEnum):
    Industrial = "0"  # 0  Industrial ou equiparado a industrial
    Outros = "1"  # 1  Outros.


class VersaoLeiauteSPEDFiscal(enum.StrEnum):
    Versao100 = "001"  # Código 001 - Versão 100 Ato COTEPE 01/01/2008
    Versao101 = "002"  # Código 002 - Versão 101 Ato COTEPE 01/01/2009
    Versao102 = "003"  # Código 003 - Versão 102 Ato COTEPE 01/01/2010
    Versao103 = "004"  # Código 004 - Versão 103 Ato COTEPE 01/01/2011
    Versao104 = "005"  # Código 005 - Versão 104 Ato COTEPE 01/07/2012
    Versao105 = "006"  # Código 006 - Versão 105 Ato COTEPE 01/07/2012
    Versao106 = "007"  # Código 007 - Versão 106 Ato COTEPE 01/07/2013
    Versao107 = "008"  # Código 008 - Versão 107 Ato COTEPE 01/07/2014
    Versao108 = "009"  # Código 009 - Versão 108 Ato COTEPE 01/07/2015
    Versao109 = "010"  # Código 010 - Versão 109 Ato COTEPE 01/07/2016
    Versao110 = "011"  # Código 011 - Versão 110 Ato COTEPE 01/01/2017
    Versao111 = "012"  # Código 012 - Versão 111 Ato COTEPE 01/01/2018
    Versao112 = "013"  # Código 013 - Versão 112 Ato COTEPE 01/01/2019
    Versao113 = "014"  # Código 014 - Versão 113 Ato COTEPE 01/01/2020
    Versao114 = "015"  # Código 015 - Versão 114 Ato COTEPE 01/01/2021
    Versao115 = "016"  # Código 016 - Versão 115 Ato COTEPE 01/01/2022
    Versao116 = "017"  # Código 017 - Versão 116 Ato COTEPE 01/01/2023
    Versao117 = "018"  # Código 018 - Versão 117 Ato COTEPE 01/01/2024
    Versao118 = "019"  # Código 019 - Versão 118 Ato COTEPE 01/01/2025


class CodFin(enum.StrEnum):
    Original = "0"  # 0 - Remessa do arquivo original
    Substituto = "1"  # 1 - Remessa do arquivo substituto


class TipoItem(enum.StrEnum):
    MercadoriaRevenda = "00"  # 00  Mercadoria para Revenda
    MateriaPrima = "01"  # 01  Matéria-Prima;
    Embalagem = "02"  # 02  Embalagem;
    ProdutoProcesso = "03"  # 03  Produto em Processo;
    ProdutoAcabado = "04"  # 04  Produto Acabado;
    Subproduto = "05"  # 05  Subproduto;
    ProdutoIntermediario = "06"  # 06  Produto Intermediário;
    MaterialConsumo = "07"  # 07  Material de Uso e Consumo;
    AtivoImobilizado = "08"  # 08  Ativo Imobilizado;
    Servicos = "09"  # 09  Serviços;
    OutrosInsumos = "10"  # 10  Outros Insumos;
    Outras = "99"  # 99  Outras


class IndOper(enum.StrEnum):
    EntradaAquisicao = "0"  # 0 - Entrada
    SaidaPrestacao = "1"  # 1 - Saída


class IndEmit(enum.StrEnum):
    EmissaoPropria = "0"  # 0 - Emissão própria
    Terceiros = "1"  # 1 - Terceiro


class IndPgto(enum.StrEnum):
    Vista = "0"  # 0 - À Vista
    Prazo = "1"  # 1 - A Prazo
    Outros = "2"  # 2 - Outros
    SemPagamento = "9"  # 9 - Sem pagamento
    Nenhum = ""  # Preencher vazio


class IndFrt(enum.StrEnum):
    PorContaEmitente = "0"  # 0 - Contratação do Frete por conta do Remetente (CIF)
    PorContaDestinatario = "1"  # 1 - Contratação do Frete por conta do Destinatário (FOB)
    PorContaTerceiros = "2"  # 2 - Contratação do Frete por conta de Terceiros
    ProprioPorContaRemetente = "3"  # 3 - Transporte Próprio por conta do Remetente
    ProprioPorContaDestinatario = "4"  # 4 - Transporte Próprio por conta do Destinatário
    SemCobrancaFrete = "9"  # 9 - Sem Ocorrência de Transporte
    Nenhum = ""  # Preencher vazio


class TipoFreteRedespacho(enum.StrEnum):
    SemRedespacho = "0"  # 0  Sem redespacho
    PorContaEmitente = "1"  # 1 - Por conta do emitente
    PorContaDestinatario = "2"  # 2 - Por conta do destinatário
    Outros = "9"  # 9  Outros
    Nenhum = ""  # Preencher vazio


class OrigemProcesso(enum.StrEnum):
    Sefaz = "0"  # 0 - Sefaz
    JusticaFederal = "1"  # 1 - Justiça Federal
    JusticaEstadual = "2"  # 2 - Justiça Estadual
    SecexRFB = "3"  # 3 - Secex/RFB
    Outros = "9"  # 9 - Outros
    Nenhum = ""  # Preencher vazio


class IndTipoOperacaoST(enum.StrEnum):
    CombustiveisLubrificantes = "0"  # 0 - Combustíveis e Lubrificantes
    LeasingVeiculos = "1"  # 1 - leasing de veículos ou faturamento direto
    RecusadeRecebimento = "2"  # 2 - Recusa de recebimento (de acordo com as condições descritas nas instruções do Registro


class DoctoArrecada(enum.StrEnum):
    EstadualArrecadacao = "0"  # 0 - Documento Estadual de Arrecadação
    GNRE = "1"  # 1 - GNRE


class TipoTransporte(enum.StrEnum):
    Rodoviario = "0"  # 0  Rodoviário
    Ferroviario = "1"  # 1  Ferroviário
    RodoFerroviario = "2"  # 2  Rodo-Ferroviário
    Aquaviario = "3"  # 3  Aquaviário
    Dutoviario = "4"  # 4  Dutoviário
    Aereo = "5"  # 5  Aéreo
    Outros = "9"  # 9  Outros


class DoctoImporta(enum.StrEnum):
    Importacao = "0"  # 0  Declaração de Importação
    SimplificadaImport = "1"  # 1  Declaração Simplificada de Importação


class TipoTitulo(enum.StrEnum):
    Duplicata = "00"  # 00- Duplicata
    Cheque = "01"  # 01- Cheque
    Promissoria = "02"  # 02- Promissória
    Recibo = "03"  # 03- Recibo
    Outros = "99"  # 99- Outros (descrever)


class IndMovFisica(enum.StrEnum):
    Sim = "0"  # 0 - Sim
    Nao = "1"  # 1 - Não


class ApuracaoIPI(enum.StrEnum):
    Mensal = "0"  # 0 - Mensal
    Decendial = "1"  # 1 - Decendial
    Nenhum = ""  # Vazio


class TipoBaseMedicamento(enum.StrEnum):
    CalcTabeladoSugerido = "0"  # 0 - Base de cálculo referente ao preço tabelado ou preço máximo sugerido;
    CalMargemAgregado = "1"  # 1 - Base cálculo  Margem de valor agregado;
    CalListNegativa = "2"  # 2 - Base de cálculo referente à Lista Negativa;
    CalListaPositiva = "3"  # 3 - Base de cálculo referente à Lista Positiva;
    CalListNeutra = "4"  # 4 - Base de cálculo referente à Lista Neutra


class TipoProduto(enum.StrEnum):
    Similar = "0"  # 0 - Similar
    Generico = "1"  # 1 - Genérico
    Marca = "2"  # 2 - Ético ou de Marca


class TipoArmaFogo(enum.StrEnum):
    Permitido = "0"  # 0 - Permitido
    Restrito = "1"  # 1 - Restrito


class IndVeicOper(enum.StrEnum):
    VendaPConcess = "0"  # 0 - Venda para concessionária
    FaturaDireta = "1"  # 1 - Faturamento direto
    VendaDireta = "2"  # 2 - Venda direta
    VendaDConcess = "3"  # 3 - Venda da concessionária
    VendaOutros = "9"  # 9 - Outros


class IndRec(enum.StrEnum):
    Propria = "0"  # 0 - Receita própria
    Terceiro = "1"  # 1 - Receita de terceiros


class TipoVeiculo(enum.StrEnum):
    Embarcacao = "0"  # 0 - Embarcação
    EmpuradorRebocador = "1"  # 1 - Empurrador/rebocador


class TipoNavegacao(enum.StrEnum):
    Interior = "0"  # 0 - Interior
    Cabotagem = "1"  # 1 - Cabotagem


class CodSit(enum.StrEnum):
    Regular = "00"  # 00 - Documento regular
    ExtempRegular = "01"  # 01 - Escrituração extemporânea de documento regular
    Cancelado = "02"  # 02 - Documento cancelado
    CanceladoExtemp = "03"  # 03 - Escrituração extemporânea de documento cancelado
    DoctoDenegado = "04"  # 04 - NF-e ou CT-e - denegado
    DoctoNumInutilizada = "05"  # 05 - NF-e ou CT-e - Numeração inutilizada
    FiscalCompl = "06"  # 06 - Documento Fiscal Complementar
    ExtempCompl = "07"  # 07 - Escrituração extemporânea de documento complementar
    RegimeEspecNEsp = "08"  # 08 - Documento Fiscal emitido com base em Regime Especial ou Norma Específica


class TipoTarifa(enum.StrEnum):
    Exp = "0"  # 0 - Exp
    Enc = "1"  # 1 - Enc
    CI = "2"  # 2 - CI
    Outra = "9"  # 9 - Outra


class NaturezaFrete(enum.StrEnum):
    Negociavel = "0"  # 0 - Negociavel
    NaoNegociavel = "1"  # 1 - Não Negociavel


class IndReceita(enum.StrEnum):
    ServicoPrestado = "0"  # 0 - Receita própria - serviços prestados;
    CobrancaDebitos = "1"  # 1 - Receita própria - cobrança de débitos;
    VendaMerc = "2"  # 2 - Receita própria - venda de mercadorias;
    ServicoPrePago = "3"  # 3 - Receita própria - venda de serviço pré-pago;
    OutrasProprias = "4"  # 4 - Outras receitas próprias;
    TerceiroCoFaturamento = "5"  # 5 - Receitas de terceiros (co-faturamento);
    TerceiroOutras = "9"  # 9 - Outras receitas de terceiros


class ServicoPrestado(enum.StrEnum):
    Telefonia = "0"  # 0- Telefonia;
    ComunicacaoDados = "1"  # 1- Comunicação de dados;
    TVAssinatura = "2"  # 2- TV por assinatura;
    AcessoInternet = "3"  # 3- Provimento de acesso à Internet;
    Multimidia = "4"  # 4- Multimídia;
    Outros = "9"  # 9- Outros


class MovimentoST(enum.StrEnum):
    SemOperacaoST = "0"  # 0 - Sem operações com ST
    ComOperacaoST = "1"  # 1 - Com operações de ST


class TipoAjuste(enum.StrEnum):
    Debito = "0"  # 0 - Ajuste a débito;
    Credito = "1"  # 1- Ajuste a crédito


class OrigemDocto(enum.StrEnum):
    PorcessoJudicial = "0"  # 0 - Processo Judicial;
    ProcessoAdminist = "1"  # 1 - Processo Administrativo;
    PerDcomp = "2"  # 2 - PER/DCOMP;
    DocumentoFiscal = "3"  # 3 - Documento Fiscal
    Outros = "9"  # 9  Outros.


class IndProp(enum.StrEnum):
    Informante = "0"  # 0- Item de propriedade do informante e em seu poder;
    InformanteNoTerceiro = "1"  # 1- Item de propriedade do informante em posse de terceiros;
    TerceiroNoInformante = "2"  # 2- Item de propriedade de terceiros em posse do informante


class TipoDocto(enum.StrEnum):
    DeclaracaoExportacao = "0"  # 0 - Declaração de Exportação;
    DeclaracaoSimplesExportacao = "1"  # 1 - Declaração Simplificada de Exportação;
    DeclaracaoUnicaExportacao = "2"  # 2 - Declaração Única de Exportação.


class Exportacao(enum.StrEnum):
    Direta = "0"  # 0 - Exportação Direta
    Indireta = "1"  # 1 - Exportação Indireta


class IndTipoLeiaute(enum.StrEnum):
    Simplificado = "0"  # 0 = Leiaute simplificado
    Completo = "1"  # 1 = Leiaute completo
    RestritoSaldoEstoque = "2"  # 2 = Leiaute restrito aos saldos de estoque


class IndEstoque(enum.StrEnum):
    PropInformantePoder = "0"  # 0 = Estoque de propriedade do informante e em seu poder
    PropInformanteTerceiros = "1"  # 1 = Estoque de propriedade do informante e em posse de terceiros;
    PropTerceirosInformante = "2"  # 2 = Estoque de propriedade de terceiros e em posse do informante


class ConhecEmbarque(enum.StrEnum):
    AWB = "01"  # 01  AWB;
    MAWB = "02"  # 02  MAWB;
    HAWB = "03"  # 03  HAWB;
    COMAT = "04"  # 04  COMAT;
    RExpressas = "06"  # 06  R. EXPRESSAS;
    EtiqREspressas = "07"  # 07  ETIQ. REXPRESSAS;
    HrExpressas = "08"  # 08  HR. EXPRESSAS;
    AV7 = "09"  # 09  AV7;
    BL = "10"  # 10  BL;
    MBL = "11"  # 11  MBL;
    HBL = "12"  # 12  HBL;
    CTR = "13"  # 13  CRT;
    DSIC = "14"  # 14  DSIC;
    ComatBL = "16"  # 16  COMAT BL;
    RWB = "17"  # 17  RWB;
    HRWB = "18"  # 18  HRWB;
    TifDta = "19"  # 19  TIF/DTA;
    CP2 = "20"  # 20  CP2;
    NaoIATA = "91"  # 91  NÂO IATA;
    MNaoIATA = "92"  # 92  MNAO IATA;
    HNaoIATA = "93"  # 93  HNAO IATA;
    COutros = "99"  # 99  OUTROS.


class Medicao(enum.StrEnum):
    Analogico = "0"  # 0 - analógico;
    Digital = "1"  # 1  digital


class MovimentoBens(enum.StrEnum):
    SI = "SI"  # SI = Saldo inicial de bens imobilizados
    IM = "IM"  # IM = Imobilização de bem individual
    IA = "IA"  # IA = Imobilização em Andamento - Componente
    CI = "CI"  # CI = Conclusão de Imobilização em Andamento  Bem Resultante
    MC = "MC"  # MC = Imobilização oriunda do Ativo Circulante
    BA = "BA"  # BA = Baixa do Saldo de ICMS - Fim do período de apropriação
    AT = "AT"  # AT = Alienação ou Transferência
    PE = "PE"  # PE = Perecimento, Extravio ou Deterioração
    OT = "OT"  # OT = Outras Saídas do Imobilizado


class GrupoTensao(enum.StrEnum):
    Nenhum = ""  # '' - Vazio. Para uso quando o documento for cancelado.
    A1 = "01"  # 01 - A1 - Alta Tensão (230kV ou mais)
    A2 = "02"  # 02 - A2 - Alta Tensão (88 a 138kV)
    A3 = "03"  # 03 - A3 - Alta Tensão (69kV)
    A3a = "04"  # 04 - A3a - Alta Tensão (30kV a 44kV)
    A4 = "05"  # 05 - A4 - Alta Tensão (2,3kV a 25kV)
    AS = "06"  # 06 - AS - Alta Tensão Subterrâneo 06
    B107 = "07"  # 07 - B1 - Residencial 07
    B108 = "08"  # 08 - B1 - Residencial Baixa Renda 08
    B209 = "09"  # 09 - B2 - Rural 09
    B2Rural = "10"  # 10 - B2 - Cooperativa de Eletrificação Rural
    B2Irrigacao = "11"  # 11 - B2 - Serviço Público de Irrigação
    B3 = "12"  # 12 - B3 - Demais Classes
    B4a = "13"  # 13 - B4a - Iluminação Pública - rede de distribuição
    B4b = "14"  # 14 - B4b - Iluminação Pública - bulbo de lâmpada


class ClasseConsumo(enum.StrEnum):
    Comercial = "01"  # 01 - Comercial
    ConsumoProprio = "02"  # 02 - Consumo Próprio
    IluminacaoPublica = "03"  # 03 - Iluminação Pública
    Industrial = "04"  # 04 - Industrial
    PoderPublico = "05"  # 05 - Poder Público
    Residencial = "06"  # 06 - Residencial
    Rural = "07"  # 07 - Rural
    ServicoPublico = "08"  # 08 -Serviço Público


class TpLigacao(enum.StrEnum):
    Nenhum = ""  # '' - Para uso quando o documento for cancelado
    Monofasico = "1"  # 1 - Monofásico
    Bifasico = "2"  # 2 - Bifásico
    Trifasico = "3"  # 3 - Trifásico


class Dispositivo(enum.StrEnum):
    FormSeguranca = "00"  # 00 - Formulário de Segurança
    FSDA = "01"  # 01 - FS-DA  Formulário de Segurança para Impressão de DANFE
    NFe = "02"  # 02  Formulário de segurança - NF-e
    FormContinuo = "03"  # 03 - Formulário Contínuo
    Blocos = "04"  # 04  Blocos
    JogosSoltos = "05"  # 05 - Jogos Soltos


class TpAssinante(enum.StrEnum):
    Nenhum = ""  # Preencher vazio
    ComercialIndustrial = "1"  # 1 - Comercial/Industrial
    PodrPublico = "2"  # 2 - Poder Público
    Residencial = "3"  # 3 - Residencial/Pessoa física
    Publico = "4"  # 4 - Público
    SemiPublico = "5"  # 5 - Semi-Público
    Outros = "6"  # 6 - Outros


class MotInv(enum.StrEnum):
    FinalPeriodo = "01"
    MudancaTributacao = "02"
    BaixaCadastral = "03"
    RegimePagamento = "04"
    DeterminacaoFiscos = "05"
    ControleMercadoriaSujeitaST = "06"


class CstIcms(enum.StrEnum):
    Nenhum = ""
    TributadaIntegralmente = "000"  # '000' //	Tributada integralmente
    TributadaComCobracaPorST = "010"  # '010' //	Tributada e com cobrança do ICMS por substituição tributária
    ComReducao = "020"  # '020' //	Com redução de base de cálculo
    IsentaComCobracaPorST = "030"  # '030' //	Isenta ou não tributada e com cobrança do ICMS por substituição tributária
    Isenta = "040"  # '040' //	Isenta
    NaoTributada = "041"  # '041' //	Não tributada
    Suspensao = "050"  # '050' //	Suspensão
    Diferimento = "051"  # '051' //	Diferimento
    CobradoAnteriormentePorST = "060"  # '060' //	ICMS cobrado anteriormente por substituição tributária
    ComReducaoPorST = "070"  # '070' //	Com redução de base de cálculo e cobrança do ICMS por substituição tributária
    Outros = "090"  # '090' //	Outros
    EstrangeiraImportacaoDiretaTributadaIntegralmente = "100"  # '100' // Estrangeira - Importação direta - Tributada integralmente
    EstrangeiraImportacaoDiretaTributadaComCobracaPorST = "110"  # '110' // Estrangeira - Importação direta - Tributada e com cobrança do ICMS por substituição tributária
    EstrangeiraImportacaoDiretaComReducao = "120"  # '120' // Estrangeira - Importação direta - Com redução de base de cálculo
    EstrangeiraImportacaoDiretaIsentaComCobracaPorST = "130"  # '130' // Estrangeira - Importação direta - Isenta ou não tributada e com cobrança do ICMS por substituição tributária
    EstrangeiraImportacaoDiretaIsenta = "140"  # '140' // Estrangeira - Importação direta - Isenta
    EstrangeiraImportacaoDiretaNaoTributada = "141"  # '141' // Estrangeira - Importação direta - Não tributada
    EstrangeiraImportacaoDiretaSuspensao = "150"  # '150' // Estrangeira - Importação direta - Suspensão
    EstrangeiraImportacaoDiretaDiferimento = "151"  # '151' // Estrangeira - Importação direta - Diferimento
    EstrangeiraImportacaoDiretaCobradoAnteriormentePorST = "160"  # '160' // Estrangeira - Importação direta - ICMS cobrado anteriormente por substituição tributária
    EstrangeiraImportacaoDiretaComReducaoPorST = "170"  # '170' // Estrangeira - Importação direta - Com redução de base de cálculo e cobrança do ICMS por substituição tributária
    EstrangeiraImportacaoDiretaOutros = "190"  # '190' // Estrangeira - Importação direta - Outras
    EstrangeiraAdqMercIntTributadaIntegralmente = "200"  # '200' // Estrangeira - Adquirida no mercado interno - Tributada integralmente
    EstrangeiraAdqMercIntTributadaComCobracaPorST = "210"  # '210' // Estrangeira - Adquirida no mercado interno - Tributada e com cobrança do ICMS por substituição tributária
    EstrangeiraAdqMercIntComReducao = "220"  # '220' // Estrangeira - Adquirida no mercado interno - Com redução de base de cálculo
    EstrangeiraAdqMercIntIsentaComCobracaPorST = "230"  # '230' // Estrangeira - Adquirida no mercado interno - Isenta ou não tributada e com cobrança do ICMS por substituição tributária
    EstrangeiraAdqMercIntIsenta = "240"  # '240' // Estrangeira - Adquirida no mercado interno - Isenta
    EstrangeiraAdqMercIntNaoTributada = "241"  # '241' // Estrangeira - Adquirida no mercado interno - Não tributada
    EstrangeiraAdqMercIntSuspensao = "250"  # '250' // Estrangeira - Adquirida no mercado interno - Suspensão
    EstrangeiraAdqMercIntDiferimento = "251"  # '251' // Estrangeira - Adquirida no mercado interno - Diferimento
    EstrangeiraAdqMercIntCobradoAnteriormentePorST = "260"  # '260' // Estrangeira - Adquirida no mercado interno - ICMS cobrado anteriormente por substituição tributária
    EstrangeiraAdqMercIntComReducaoPorST = "270"  # '270' // Estrangeira - Adquirida no mercado interno - Com redução de base de cálculo e cobrança do ICMS por substituição tributária
    EstrangeiraAdqMercIntOutros = "290"  # '290' // Estrangeira - Adquirida no mercado interno - Outras
    CSTICMS300 = "300"  # '300' // Estrangeira - Adquirida no mercado interno - Tributada integralmente
    CSTICMS310 = "310"  # '310' // Estrangeira - Adquirida no mercado interno - Tributada e com cobrança do ICMS por substituição tributária
    CSTICMS320 = "320"  # '320' // Estrangeira - Adquirida no mercado interno - Com redução de base de cálculo
    CSTICMS330 = "330"  # '330' // Estrangeira - Adquirida no mercado interno - Isenta ou não tributada e com cobrança do ICMS por substituição tributária
    CSTICMS340 = "340"  # '340' // Estrangeira - Adquirida no mercado interno - Isenta
    CSTICMS341 = "341"  # '341' // Estrangeira - Adquirida no mercado interno - Não tributada
    CSTICMS350 = "350"  # '350' // Estrangeira - Adquirida no mercado interno - Suspensão
    CSTICMS351 = "351"  # '351' // Estrangeira - Adquirida no mercado interno - Diferimento
    CSTICMS360 = "360"  # '360' // Estrangeira - Adquirida no mercado interno - ICMS cobrado anteriormente por substituição tributária
    CSTICMS370 = "370"  # '370' // Estrangeira - Adquirida no mercado interno - Com redução de base de cálculo e cobrança do ICMS por substituição tributária
    CSTICMS390 = "390"  # '390' // Estrangeira - Adquirida no mercado interno - Outras
    CSTICMS400 = "400"  # '400' // Estrangeira - Adquirida no mercado interno - Tributada integralmente
    CSTICMS410 = "410"  # '410' // Estrangeira - Adquirida no mercado interno - Tributada e com cobrança do ICMS por substituição tributária
    CSTICMS420 = "420"  # '420' // Estrangeira - Adquirida no mercado interno - Com redução de base de cálculo
    CSTICMS430 = "430"  # '430' // Estrangeira - Adquirida no mercado interno - Isenta ou não tributada e com cobrança do ICMS por substituição tributária
    CSTICMS440 = "440"  # '440' // Estrangeira - Adquirida no mercado interno - Isenta
    CSTICMS441 = "441"  # '441' // Estrangeira - Adquirida no mercado interno - Não tributada
    CSTICMS450 = "450"  # '450' // Estrangeira - Adquirida no mercado interno - Suspensão
    CSTICMS451 = "451"  # '451' // Estrangeira - Adquirida no mercado interno - Diferimento
    CSTICMS460 = "460"  # '460' // Estrangeira - Adquirida no mercado interno - ICMS cobrado anteriormente por substituição tributária
    CSTICMS470 = "470"  # '470' // Estrangeira - Adquirida no mercado interno - Com redução de base de cálculo e cobrança do ICMS por substituição tributária
    CSTICMS490 = "490"  # '490' // Estrangeira - Adquirida no mercado interno - Outras
    CSTICMS500 = "500"  # '500' // Estrangeira - Adquirida no mercado interno - Tributada integralmente
    CSTICMS510 = "510"  # '510' // Estrangeira - Adquirida no mercado interno - Tributada e com cobrança do ICMS por substituição tributária
    CSTICMS520 = "520"  # '520' // Estrangeira - Adquirida no mercado interno - Com redução de base de cálculo
    CSTICMS530 = "530"  # '530' // Estrangeira - Adquirida no mercado interno - Isenta ou não tributada e com cobrança do ICMS por substituição tributária
    CSTICMS540 = "540"  # '540' // Estrangeira - Adquirida no mercado interno - Isenta
    CSTICMS541 = "541"  # '541' // Estrangeira - Adquirida no mercado interno - Não tributada
    CSTICMS550 = "550"  # '550' // Estrangeira - Adquirida no mercado interno - Suspensão
    CSTICMS551 = "551"  # '551' // Estrangeira - Adquirida no mercado interno - Diferimento
    CSTICMS560 = "560"  # '560' // Estrangeira - Adquirida no mercado interno - ICMS cobrado anteriormente por substituição tributária
    CSTICMS570 = "570"  # '570' // Estrangeira - Adquirida no mercado interno - Com redução de base de cálculo e cobrança do ICMS por substituição tributária
    CSTICMS590 = "590"  # '590' // Estrangeira - Adquirida no mercado interno - Outras
    CSTICMS600 = "600"  # '600' // Estrangeira - Adquirida no mercado interno - Tributada integralmente
    CSTICMS610 = "610"  # '610' // Estrangeira - Adquirida no mercado interno - Tributada e com cobrança do ICMS por substituição tributária
    CSTICMS620 = "620"  # '620' // Estrangeira - Adquirida no mercado interno - Com redução de base de cálculo
    CSTICMS630 = "630"  # '630' // Estrangeira - Adquirida no mercado interno - Isenta ou não tributada e com cobrança do ICMS por substituição tributária
    CSTICMS640 = "640"  # '640' // Estrangeira - Adquirida no mercado interno - Isenta
    CSTICMS641 = "641"  # '641' // Estrangeira - Adquirida no mercado interno - Não tributada
    CSTICMS650 = "650"  # '650' // Estrangeira - Adquirida no mercado interno - Suspensão
    CSTICMS651 = "651"  # '651' // Estrangeira - Adquirida no mercado interno - Diferimento
    CSTICMS660 = "660"  # '660' // Estrangeira - Adquirida no mercado interno - ICMS cobrado anteriormente por substituição tributária
    CSTICMS670 = "670"  # '670' // Estrangeira - Adquirida no mercado interno - Com redução de base de cálculo e cobrança do ICMS por substituição tributária
    CSTICMS690 = "690"  # '690' // Estrangeira - Adquirida no mercado interno - Outras
    CSTICMS700 = "700"  # '700' // Estrangeira - Adquirida no mercado interno - Tributada integralmente
    CSTICMS710 = "710"  # '710' // Estrangeira - Adquirida no mercado interno - Tributada e com cobrança do ICMS por substituição tributária
    CSTICMS720 = "720"  # '720' // Estrangeira - Adquirida no mercado interno - Com redução de base de cálculo
    CSTICMS730 = "730"  # '730' // Estrangeira - Adquirida no mercado interno - Isenta ou não tributada e com cobrança do ICMS por substituição tributária
    CSTICMS740 = "740"  # '740' // Estrangeira - Adquirida no mercado interno - Isenta
    CSTICMS741 = "741"  # '741' // Estrangeira - Adquirida no mercado interno - Não tributada
    CSTICMS750 = "750"  # '750' // Estrangeira - Adquirida no mercado interno - Suspensão
    CSTICMS751 = "751"  # '751' // Estrangeira - Adquirida no mercado interno - Diferimento
    CSTICMS760 = "760"  # '760' // Estrangeira - Adquirida no mercado interno - ICMS cobrado anteriormente por substituição tributária
    CSTICMS770 = "770"  # '770' // Estrangeira - Adquirida no mercado interno - Com redução de base de cálculo e cobrança do ICMS por substituição tributária
    CSTICMS790 = "790"  # '790' // Estrangeira - Adquirida no mercado interno - Outras
    CSTICMS800 = "800"  # '800' // Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% (setenta por cento) - Tributada integralmente
    CSTICMS810 = "810"  # '810' // Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% (setenta por cento) - Tributada e com cobrança do ICMS por substituição tributária
    CSTICMS820 = "820"  # '820' // Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% (setenta por cento) - Com redução de base de cálculo
    CSTICMS830 = "830"  # '830' // Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% (setenta por cento) - Isenta ou não tributada e com cobrança do ICMS por substituição tributária
    CSTICMS840 = "840"  # '840' // Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% (setenta por cento) - Isenta
    CSTICMS841 = "841"  # '841' // Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% (setenta por cento) - Não tributada
    CSTICMS850 = "850"  # '850' // Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% (setenta por cento) - Suspensão
    CSTICMS851 = "851"  # '851' // Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% (setenta por cento) - Diferimento
    CSTICMS860 = "860"  # '860' // Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% (setenta por cento) - ICMS cobrado anteriormente por substituição tributária
    CSTICMS870 = "870"  # '870' // Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% (setenta por cento) - Com redução de base de cálculo e cobrança do ICMS por substituição tributária
    CSTICMS890 = "890"  # '890' // Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% (setenta por cento) - Outras
    SimplesNacionalTributadaComPermissaoCredito = "101"  # '101' // Simples Nacional - Tributada pelo Simples Nacional com permissão de crédito
    SimplesNacionalTributadaSemPermissaoCredito = "102"  # '102' // Simples Nacional - Tributada pelo Simples Nacional sem permissão de crédito
    SimplesNacionalIsencaoPorFaixaReceitaBruta = "103"  # '103' // Simples Nacional - Isenção do ICMS no Simples Nacional para faixa de receita bruta
    SimplesNacionalTributadaComPermissaoCreditoComST = "201"  # '201' // Simples Nacional - Tributada pelo Simples Nacional com permissão de crédito e com cobrança do ICMS por substituição tributária
    SimplesNacionalTributadaSemPermissaoCreditoComST = "202"  # '202' // Simples Nacional - Tributada pelo Simples Nacional sem permissão de crédito e com cobrança do ICMS por substituição tributária
    SimplesNacionalIsencaoPorFaixaReceitaBrutaComST = "203"  # '203' // Simples Nacional - Isenção do ICMS no Simples Nacional para faixa de receita bruta e com cobrança do ICMS por substituição tributária
    SimplesNacionalImune = "300"  # '300' // Simples Nacional - Imune
    SimplesNacionalNaoTributada = "400"  # '400' // Simples Nacional - Não tributada pelo Simples Nacional
    SimplesNacionalCobradoAnteriormentePorST = "500"  # '500' // Simples Nacional - ICMS cobrado anteriormente por substituição tributária (substituído) ou por antecipação
    SimplesNacionalOutros = "900"  # '900' // Simples Nacional - Outros
    TributacaoMonofasicaPropriaCombustives = "002"  # '002' // Tributação Monofásica Própria do ICMS nas operações com combustíveis
    TributacaoMonofasicaPropriacomRetencaoCombustiveis = "015"  # '015' // Tributação Monofásica Própria e com responsabilidade pela retenção do ICMS nas operações com combustíveis
    TributacaoMonofasicaRecolhimentoDiferidoCombustiveis = "053"  # '053' // Tributação Monofásica com recolhimento diferido do ICMS nas operações com combustíveis
    TributacaoMonofasicaCombustiveisCobradoAnteriormente = "061"  # '061' // Tributação Monofásica sobre combustíveis com ICMS cobrado anteriormente


class MovimentoDIFAL(enum.StrEnum):
    DifalSemOperacaoICMS = "0"  # 0 - Sem operações com ICMS Diferencial de Alíquota da UF
    DifalComOperacaoICMS = "1"  # 1 - Com operações com ICMS Diferencial de Alíquota da UF


class NaturezaConta(enum.StrEnum):
    Ativo = "01"  # 01 - Contas de ativo
    Passivo = "02"  # 02 - Contas de passivo
    Liquido = "03"  # 03 - Patrimônio líquido
    Resultado = "04"  # 04 - Contas de resultado
    Compensacao = "05"  # 05 - Contas de compensação
    Outras = "09"  # 09 - Outras


class IndCTA(enum.StrEnum):
    CTASintetica = "S"  # S Sintética
    CTAnalitica = "A"  # A Analitica


class CstPisCofins(enum.StrEnum):
    OperTribuComAliqBasica = "01"  # 01 Operação Tributável com Alíquota Básica
    OperTribuAliqZero = "06"  # 06 Operação Tributável a Alíquota Zero
    OperIsentaContribuicao = "07"  # 07 Operação Isenta da Contribuição
    OperSemIncidenciaContribuicao = "08"  # 08 Operação sem Incidência da Contribuição
    OperComSuspensaoContribuicao = "09"  # 09 Operação com Suspensão da Contribuição
    OutrasOperacoesSaida = "49"  # 49 Outras Operações de Saída
    OutrasDespesas = "99"  # 99 Outras Operações
    Nenhum = ""


class CstIpi(enum.StrEnum):
    EntradaRecuperacaoCredito = "00"  # '00' // Entrada com recuperação de crédito
    EntradaTributradaZero = "01"  # '01' // Entrada tributada com alíquota zero
    EntradaIsenta = "02"  # '02' // Entrada isenta
    EntradaNaoTributada = "03"  # '03' // Entrada não-tributada
    EntradaImune = "04"  # '04' // Entrada imune
    EntradaComSuspensao = "05"  # '05' // Entrada com suspensão
    OutrasEntradas = "49"  # '49' // Outras entradas
    SaidaTributada = "50"  # '50' // Saída tributada
    SaidaTributadaZero = "51"  # '51' // Saída tributada com alíquota zero
    SaidaIsenta = "52"  # '52' // Saída isenta
    SaidaNaoTributada = "53"  # '53' // Saída não-tributada
    SaidaImune = "54"  # '54' // Saída imune
    SaidaComSuspensao = "55"  # '55' // Saída com suspensão
    OutrasSaidas = "99"  # '99' // Outras saídas
    Vazio = ""


class CstPis(enum.StrEnum):
    ValorAliquotaNormal = "01"  # '01' // Operação Tributável com Alíquota Básica   // valor da operação alíquota normal (cumulativo/não cumulativo)).
    ValorAliquotaDiferenciada = "02"  # '02' // Operação Tributável com Alíquota Diferenciada // valor da operação (alíquota diferenciada)).
    QtdeAliquotaUnidade = "03"  # '03' // Operação Tributável com Alíquota por Unidade de Medida de Produto // quantidade vendida x alíquota por unidade de produto).
    MonofaticaAliquotaZero = "04"  # '04' // Operação Tributável Monofásica - Revenda a Alíquota Zero
    ValorAliquotaPorST = "05"  # '05' // Operação Tributável por Substituição Tributária
    AliquotaZero = "06"  # '06' // Operação Tributável a Alíquota Zero
    IsentaContribuicao = "07"  # '07' // Operação Isenta da Contribuição
    SemIncidenciaContribuicao = "08"  # '08' // Operação sem Incidência da Contribuição
    SuspensaoContribuicao = "09"  # '09' // Operação com Suspensão da Contribuição
    OutrasOperacoesSaida = "49"  # '49' // Outras Operações de Saída
    OperCredExcRecTribMercInt = "50"  # '50' // Operação com Direito a Crédito - Vinculada Exclusivamente a Receita Tributada no Mercado Interno
    OperCredExcRecNaoTribMercInt = "51"  # '51' // Operação com Direito a Crédito  Vinculada Exclusivamente a Receita Não Tributada no Mercado Interno
    OperCredExcRecExportacao = "52"  # '52' // Operação com Direito a Crédito - Vinculada Exclusivamente a Receita de Exportação
    OperCredRecTribNaoTribMercInt = "53"  # '53' // Operação com Direito a Crédito - Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno
    OperCredRecTribMercIntEExportacao = "54"  # '54' // Operação com Direito a Crédito - Vinculada a Receitas Tributadas no Mercado Interno e de Exportação
    OperCredRecNaoTribMercIntEExportacao = "55"  # '55' // Operação com Direito a Crédito - Vinculada a Receitas Não-Tributadas no Mercado Interno e de Exportação
    OperCredRecTribENaoTribMercIntEExportacao = "56"  # '56' // Operação com Direito a Crédito - Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno, e de Exportação
    CredPresAquiExcRecTribMercInt = "60"  # '60' // Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita Tributada no Mercado Interno
    CredPresAquiExcRecNaoTribMercInt = "61"  # '61' // Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita Não-Tributada no Mercado Interno
    CredPresAquiExcExcRecExportacao = "62"  # '62' // Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita de Exportação
    CredPresAquiRecTribNaoTribMercInt = "63"  # '63' // Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno
    CredPresAquiRecTribMercIntEExportacao = "64"  # '64' // Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas no Mercado Interno e de Exportação
    CredPresAquiRecNaoTribMercIntEExportacao = "65"  # '65' // Crédito Presumido - Operação de Aquisição Vinculada a Receitas Não-Tributadas no Mercado Interno e de Exportação
    CredPresAquiRecTribENaoTribMercIntEExportacao = "66"  # '66' // Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno, e de Exportação
    OutrasOperacoes_CredPresumido = "67"  # '67' // Crédito Presumido - Outras Operações
    OperAquiSemDirCredito = "70"  # '70' // Operação de Aquisição sem Direito a Crédito
    OperAquiComIsensao = "71"  # '71' // Operação de Aquisição com Isenção
    OperAquiComSuspensao = "72"  # '72' // Operação de Aquisição com Suspensão
    OperAquiAliquotaZero = "73"  # '73' // Operação de Aquisição a Alíquota Zero
    OperAqui_SemIncidenciaContribuicao = "74"  # '74' // Operação de Aquisição sem Incidência da Contribuição
    OperAquiPorST = "75"  # '75' // Operação de Aquisição por Substituição Tributária
    OutrasOperacoesEntrada = "98"  # '98' // Outras Operações de Entrada
    OutrasOperacoes = "99"  # '99' // Outras Operações
    Nenhum = "00"  # '00' // Nenhum


class CstCofins(enum.StrEnum):
    ValorAliquotaNormal = "01"  # '01' // Operação Tributável com Alíquota Básica                           // valor da operação alíquota normal (cumulativo/não cumulativo)).
    ValorAliquotaDiferenciada = "02"  # '02' // Operação Tributável com Alíquota Diferenciada                     // valor da operação (alíquota diferenciada)).
    QtdeAliquotaUnidade = "03"  # '03' // Operação Tributável com Alíquota por Unidade de Medida de Produto // quantidade vendida x alíquota por unidade de produto).
    MonofaticaAliquotaZero = "04"  # '04' // Operação Tributável Monofásica - Revenda a Alíquota Zero
    ValorAliquotaPorST = "05"  # '05' // Operação Tributável por Substituição Tributária
    AliquotaZero = "06"  # '06' // Operação Tributável a Alíquota Zero
    IsentaContribuicao = "07"  # '07' // Operação Isenta da Contribuição
    SemIncidenciaContribuicao = "08"  # '08' // Operação sem Incidência da Contribuição
    SuspensaoContribuicao = "09"  # '09' // Operação com Suspensão da Contribuição
    OutrasOperacoesSaida = "49"  # '49' // Outras Operações de Saída
    OperCredExcRecTribMercInt = "50"  # '50' // Operação com Direito a Crédito - Vinculada Exclusivamente a Receita Tributada no Mercado Interno
    OperCredExcRecNaoTribMercInt = "51"  # '51' // Operação com Direito a Crédito - Vinculada Exclusivamente a Receita Não-Tributada no Mercado Interno
    OperCredExcRecExportacao = "52"  # '52' // Operação com Direito a Crédito - Vinculada Exclusivamente a Receita de Exportação
    OperCredRecTribNaoTribMercInt = "53"  # '53' // Operação com Direito a Crédito - Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno
    OperCredRecTribMercIntEExportacao = "54"  # '54' // Operação com Direito a Crédito - Vinculada a Receitas Tributadas no Mercado Interno e de Exportação
    OperCredRecNaoTribMercIntEExportacao = "55"  # '55' // Operação com Direito a Crédito - Vinculada a Receitas Não Tributadas no Mercado Interno e de Exportação
    OperCredRecTribENaoTribMercIntEExportacao = "56"  # '56' // Operação com Direito a Crédito - Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno e de Exportação
    CredPresAquiExcRecTribMercInt = "60"  # '60' // Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita Tributada no Mercado Interno
    CredPresAquiExcRecNaoTribMercInt = "61"  # '61' // Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita Não-Tributada no Mercado Interno
    CredPresAquiExcExcRecExportacao = "62"  # '62' // Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita de Exportação
    CredPresAquiRecTribNaoTribMercInt = "63"  # '63' // Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno
    CredPresAquiRecTribMercIntEExportacao = "64"  # '64' // Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas no Mercado Interno e de Exportação
    CredPresAquiRecNaoTribMercIntEExportacao = "65"  # '65' // Crédito Presumido - Operação de Aquisição Vinculada a Receitas Não-Tributadas no Mercado Interno e de Exportação
    CredPresAquiRecTribENaoTribMercIntEExportacao = "66"  # '66' // Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno e de Exportação
    OutrasOperacoes_CredPresumido = "67"  # '67' // Crédito Presumido - Outras Operações
    OperAquiSemDirCredito = "70"  # '70' // Operação de Aquisição sem Direito a Crédito
    OperAquiComIsensao = "71"  # '71' // Operação de Aquisição com Isenção
    OperAquiComSuspensao = "72"  # '72' // Operação de Aquisição com Suspensão
    OperAquiAliquotaZero = "73"  # '73' // Operação de Aquisição a Alíquota Zero
    OperAqui_SemIncidenciaContribuicao = "74"  # '74' // Operação de Aquisição sem Incidência da Contribuição
    OperAquiPorST = "75"  # '75' // Operação de Aquisição por Substituição Tributária
    OutrasOperacoesEntrada = "98"  # '98' // Outras Operações de Entrada
    OutrasOperacoes = "99"  # '99' // Outras Operações
    Nenhum = "00"  # '00' // Nenhum


class MotivoRessarcimento(enum.StrEnum):
    VendaOutraUF = "1"
    SaidaInsetaNaoIncidencia = "2"
    PerdaDeterioracao = "3"
    FurtoRoubo = "4"
    Exportacao = "5"
    VendaSimpleNacional = "6"
    Outros = "9"
    Nenhum = "0"


class IndicadorDeducao(enum.StrEnum):
    CompensacaoISS = "0"  # 0- Compensação do ISS calculado a maior;
    BeneficioFiscal = "1"  # 1- Benefício fiscal por incentivo à cultura;
    DecisaoAdministrativa = "2"  # 2- Decisão administrativa ou judicial;
    Outros = "9"  # 9- Outros;


class IndicadorProcesso(enum.StrEnum):
    Sefin = "0"  # 0- Sefin;
    JusticaFederal = "1"  # 1- Justiça Federal;
    JusticaEstadual = "2"  # 2- Justiça Estadual;
    Outros = "9"  # 9- Outros;


class IndicadorObrigacao(enum.StrEnum):
    ISSProprio = "0"  # 0 - ISS Próprio;
    ISSSubstituto = "1"  # 1 - ISS Substituto (devido pelas aquisições de serviços do declarante).
    ISSUniprofissionais = "2"  # 2 - ISS Uniprofissionais


class FinalidadeEmissaoDocumentoEletronico(enum.StrEnum):
    NaoDefinida = ""
    Normal = "1"  # 1  Normal
    Substituicao = "2"  # 2  Substituição
    NormalComAjuste = "3"  # 3  Normal com ajuste


class IndicadorDestinatarioAcessante(enum.StrEnum):
    ContribuinteICMS = "1"  # 1  Contribuinte do ICMS
    ContribuinteIsentoInscricaoCadastroICMS = "2"  # 2  Contribuinte Isento de Inscrição no Cadastro de Contribuintes do ICMS
    NaoContribuinte = "9"  # 9  Não Contribuinte


class FinEmissaoFaturaEletronica(enum.StrEnum):
    NaoDefinida = ""
    Normal = "0"
    Substituicao = "3"
    Ajuste = "4"


class TipoFaturamentoDocumentoEletronico(enum.StrEnum):
    FaturamentoNormal = "0"  # 0 - Faturamento Normal
    FaturamentoCentralizado = "1"  # 1 - Faturamento Centralizado
    Cofaturamento = "2"  # 2 - Cofaturamento


class IndicadorFormaPagto(enum.StrEnum):
    PrePago = "0"  # 0  Pré pago
    PosPago = "1"  # 1 - Pós pago


class TipoResiduo(enum.StrEnum):
    BagacodeCana = "01"  # 01 - Bagaço de cana
    DDG = "02"  # 02 - DDG
    WDG = "03"  # 03  WDG
    DDGWDG = "04"  # 04 - DDG + WDG


class BlocoInicial(Registro, abstract=True):
    IND_MOV: IndMov  # /// Indicador de movimento: 0- Bloco com dados informados, 1- Bloco sem dados informados.


class RegistroB025(Registro):
    VL_CONT_P: Decimal  # /// Parcela correspondente ao "Valor Contábil" referente à combinação da alíquota e item da lista
    VL_BC_ISS_P: Decimal  # /// Parcela correspondente ao "Valor da base de cálculo do ISS" referente à combinação da alíquota e item da lista
    ALIQ_ISS: Decimal  # /// Alíquota do ISS
    VL_ISS_P: Decimal  # /// Parcela correspondente ao "Valor do ISS" referente à combinação da alíquota e item da lista
    VL_ISNT_ISS_P: Decimal  # /// Parcela correspondente ao "Valor das operações isentas ou nãotributadas pelo ISS" referente à combinação da alíquota e item da lista
    COD_SERV: str  # /// Item da lista de serviços, conforme Tabela 4.6.3


class RegistroB020(Registro):
    IND_OPER: IndOper  # /// Indicador do tipo de operação: 0- Aquisição; 1- Prestação
    IND_EMIT: IndEmit  # /// Indicador do emitente do documento fiscal: 0- Emissão própria; 1- Terceiros
    COD_PART: str  # /// Código do participante (campo 02 do Registro 0150):
    COD_MOD: str  # /// Código do modelo do documento fiscal, conforme a Tabela 4.1.3
    COD_SIT: CodSit  # /// Código da situação do documento fiscal, conforme a Tabela 4.1.2
    SER: str  # /// Série do documento fiscal
    NUM_DOC: str  # /// Número do documento fiscal
    CHV_NFE: str  # /// Chave da Nota Fiscal Eletrônica
    DT_DOC: date  # /// Data da emissão do documento fiscal
    COD_MUN_SERV: str  # /// Código do município onde o serviço foi prestado,conforme a tabela IBGE.
    VL_CONT: Decimal  # /// Valor contábil (valor total do documento)
    VL_MAT_TERC: Decimal  # /// Valor do material fornecido por terceiros na prestação do serviço
    VL_SUB: Decimal  # /// Valor da subempreitada
    VL_ISNT_ISS: Decimal  # /// Valor das operações isentas ou não-tributadas pelo ISS
    VL_DED_BC: Decimal  # /// Valor da dedução da base de cálculo
    VL_BC_ISS: Decimal  # /// Valor da base de cálculo do ISS
    VL_BC_ISS_RT: Decimal  # /// Valor da base de cálculo de retenção do ISS
    VL_ISS_RT: Decimal  # /// Valor do ISS retido pelo tomador
    VL_ISS: Decimal  # /// Valor do ISS destacado
    COD_INF_OBS: str  # /// Código da observação do lançamento fiscal(campo 02 do Registro 0460)
    RegistroB025: BlockList[RegistroB025]  # /// Bloco b - Lista de RegistroB025 (FILHO)


class RegistroB035(Registro):
    VL_CONT_P: Decimal  # /// Parcela correspondente ao "Valor Contábil" referente à combinação da alíquota e item da lista
    VL_BC_ISS_P: Decimal  # /// Parcela correspondente ao "Valor da base de cálculo do ISS" referente à combinação da alíquota e item da lista
    ALIQ_ISS: Decimal  # /// Alíquota do ISS
    VL_ISS_P: Decimal  # /// Parcela correspondente ao "Valor do ISS" referente à combinação da alíquota e item da lista
    VL_ISNT_ISS_P: Decimal  # /// Parcela correspondente ao "Valor das operações isentas ou nãotributadas pelo ISS" referente à combinação da alíquota e item da lista
    COD_SERV: str  # /// Item da lista de serviços, conforme Tabela 4.6.3


class RegistroB030(Registro):
    COD_MOD: str  # /// Código do modelo do documento fiscal, conforme a Tabela 4.1.3
    SER: str  # /// Série do documento fiscal
    NUM_DOC_INI: str  # /// Número do primeiro documento fiscal emitido no dia
    NUM_DOC_FIN: str  # /// Número do último documento fiscal emitido no dia
    DT_DOC: date  # /// Data da emissão do documento fiscal
    QTD_CANC: Decimal  # /// Quantidade de documentos cancelados
    VL_CONT: Decimal  # /// Valor contábil (valor total do documento)
    VL_ISNT_ISS: Decimal  # /// Valor das operações isentas ou não-tributadas pelo ISS
    VL_BC_ISS: Decimal  # /// Valor da base de cálculo do ISS
    VL_ISS: Decimal  # /// Valor do ISS destacado
    COD_INF_OBS: str  # /// Código da observação do lançamento fiscal(campo 02 do Registro 0460)
    RegistroB035: BlockList[RegistroB035]  # /// Bloco b - Lista de RegistroB035 (FILHO)


class RegistroB350(Registro):
    COD_CTD: str  # /// Código da conta do plano de contas
    CTA_ISS: str  # /// Descrição da conta no plano de contas
    CTA_COSIF: str  # /// Código COSIF a que está subordinada a conta do ISS das instituições financeiras
    QTD_OCOR: Decimal  # /// Quantidade de ocorrências na conta
    COD_SERV: str  # /// Item da lista de serviços, conforme Tabela 4.6.3.
    VL_CONT: Decimal  # /// Valor contábil
    VL_BC_ISS: Decimal  # /// Valor da base de cálculo do ISS
    ALIQ_ISS: Decimal  # /// Alíquota do ISS
    VL_ISS: Decimal  # /// Valor do ISS
    COD_INF_OBS: str  # /// Código da observação do lançamento fiscal (campo 02 do Registro 0460)


class RegistroB420(Registro):
    VL_CONT: Decimal  # /// Totalização do Valor Contábil das prestações do declarante referente à combinação da alíquota e item da lista
    VL_BC_ISS: Decimal  # /// Totalização do Valor da base de cálculo do ISS das prestações do declarante referente à combinação da alíquota e item da lista
    ALIQ_ISS: Decimal  # /// Alíquota do ISS
    VL_ISNT_ISS: Decimal  # /// Totalização do valor das operações isentas ou não-tributadas pelo ISS referente à combinação da alíquota e item da lista
    VL_ISS: Decimal  # /// Totalização, por combinação da alíquota e item da lista, do Valor do ISS
    COD_SERV: str  # /// Item da lista de serviços, conforme Tabela 4.6.3.


class RegistroB440(Registro):
    IND_OPER: IndOper  # /// Indicador do tipo de operação: 0- Aquisição; 1- Prestação
    COD_PART: str  # /// Código do participante (campo 02 do Registro 0150):- do prestador, no caso de aquisição de serviço pelo declarante; - do tomador, no caso de prestação de serviço pelo declarante
    VL_CONT_RT: Decimal  # /// Totalização do Valor Contábil das prestações e/ou aquisições do declarante pela combinação de tipo de operação e participante.
    VL_BC_ISS_RT: Decimal  # /// Totalização do Valor da base de cálculo de retenção do ISS das prestações e/ou aquisições do declarante pela combinação de tipo de operação e participante.
    VL_ISS_RT: Decimal  # /// Totalização do Valor do ISS retido pelo tomador das prestações e/ou aquisições do declarante pela combinação de tipo de operação e participante.


class RegistroB460(Registro):
    IND_DED: IndicadorDeducao  # /// Indicador do tipo de dedução: 0- Compensação do ISS calculado a maior; 1- Benefício fiscal por incentivo à cultura; 2- Decisão administrativa ou judicial; 9- Outros
    VL_DED: Decimal  # /// Valor da dedução
    NUM_PROC: str  # /// Número do processo ao qual o ajuste está vinculado, se houver
    IND_PROC: IndicadorProcesso  # /// Indicador da origem do processo: 0- Sefin; 1- Justiça Federal; 2- Justiça Estadual; 9- Outros
    PROC: str  # /// Descrição do processo que embasou o lançamento
    COD_INF_OBS: str  # /// Código da observação do lançamento fiscal (campo 02 do Registro 0460)
    IND_OBR: IndicadorObrigacao  # /// Indicador da obrigação onde será aplicada a dedução: 0 - ISS Próprio; 1 - ISS Substituto (devido pelas aquisições de serviços do declarante).2 - ISS Uniprofissionais.


class RegistroB470(Registro):
    VL_CONT: Decimal  # /// A - Valor total referente às prestações de serviço do período
    VL_MAT_TERC: Decimal  # /// B - Valor total do material fornecido por terceiros na prestação do serviço
    VL_MAT_PROP: Decimal  # /// C - Valor do material próprio utilizado na prestação do serviço
    VL_SUB: Decimal  # /// D - Valor total das subempreitadas N - 02 O
    VL_ISNT: Decimal  # /// E - Valor total das operações isentas ou não-tributadas pelo ISS
    VL_DED_BC: Decimal  # /// F - Valor total das deduções da base de cálculo (B + C + D + E)
    VL_BC_ISS: Decimal  # /// G - Valor total da base de cálculo do ISS N - 02 O
    VL_BC_ISS_RT: Decimal  # /// H - Valor total da base de cálculo de retenção do ISS referente às prestações do declarante.
    VL_ISS: Decimal  # /// I - Valor total do ISS destacado N - 02 O
    VL_ISS_RT: Decimal  # /// J - Valor total do ISS retido pelo tomador nas prestações do declarante
    VL_DED: Decimal  # /// K - Valor total das deduções do ISS próprio
    VL_ISS_REC: Decimal  # /// L - Valor total apurado do ISS próprio a recolher (I - J - K)
    VL_ISS_ST: Decimal  # /// M - Valor total do ISS substituto a recolher pelas aquisições do declarante(tomador)
    VL_ISS_REC_UNI: Decimal  # /// U Valor do ISS próprio a recolher pela Sociedade Uniprofissional


class RegistroB510(Registro):
    IND_PROF: str  # /// Indicador de habilitação: 0- Profissional habilitado 1- Profissional não habilitado
    IND_ESC: str  # /// Indicador de escolaridade: 0- Nível superior 1- Nível médio
    IND_SOC: str  # /// Indicador de participação societária: 0- Sócio 1- Não sócio
    CPF: str  # /// Número de inscrição do profissional no CPF.
    NOME: str  # /// Nome do profissional


class RegistroB500(Registro):
    VL_REC: Decimal  # ///Valor mensal das receitas auferidas pela sociedade uniprofissional
    QTD_PROF: Decimal  # ///Quantidade de profissionais habilitados
    VL_OR: Decimal  # //Valor do ISS devido
    RegistroB510: BlockList[RegistroB510]


class RegistroB001(BlocoInicial):
    RegistroB020: BlockList[RegistroB020]
    RegistroB030: BlockList[RegistroB030]
    RegistroB350: BlockList[RegistroB350]
    RegistroB420: BlockList[RegistroB420]
    RegistroB440: BlockList[RegistroB440]
    RegistroB460: BlockList[RegistroB460]
    RegistroB470: BlockList[RegistroB470]
    RegistroB500: BlockList[RegistroB500]


class RegistroB990(Registro):
    QTD_LIN_B: int  # /// Quantidade total de linhas do Bloco B


class RegistroC101(Registro):
    VL_FCP_UF_DEST: Decimal  # // VLR FUNDO DE COMBATE A POBREZA UF DE DESTINO
    VL_ICMS_UF_DEST: Decimal  # // VLR TOTAL ICMS INTERESTADUAL PARA A UF DE DESTINO
    VL_ICMS_UF_REM: Decimal  # // VLR TOTAL ICMS INTERESTADUAL PARA A UF DO REMETENTE


class RegistroC105(Registro):
    OPER: IndTipoOperacaoST  # /// Indicador do tipo de operação. 0- Combustíveis e Lubrificantes; 1- leasing de veículos ou faturamento direto.
    UF: str  # /// Sigla da UF de destino do ICMS_ST


class RegistroC111(Registro):
    NUM_PROC: str
    IND_PROC: OrigemProcesso


class RegistroC112(Registro):
    COD_DA: DoctoArrecada
    UF: str
    NUM_DA: str
    COD_AUT: str
    VL_DA: Decimal
    DT_VCTO: date
    DT_PGTO: date


class RegistroC113(Registro):
    IND_OPER: IndOper  # /// Indicador do tipo de operação: 0 - Entrada/aquisição; 1- Saída/prestação
    IND_EMIT: IndEmit  # /// Indicador do emitente do título: 0 - Emissão própria; 1- Terceiros
    COD_PART: str  # /// Código do participante emitente (campo 02 do Registro 0150)  do documento referenciado.
    COD_MOD: str  # /// Código do documento fiscal, conforme a Tabela 4.1.1
    SER: str  # /// Série do documento fiscal
    SUB: str  # /// Subsérie do documento fiscal
    NUM_DOC: str  # /// Número do documento fiscal
    DT_DOC: date  # /// Data da emissão do documento fiscal.
    CHV_DOCe: str  # /// Chave do Documento Eletrônico


class RegistroC114(Registro):
    COD_MOD: str
    ECF_FAB: str
    ECF_CX: str
    NUM_DOC: str
    DT_DOC: date


class RegistroC115(Registro):
    IND_CARGA: TipoTransporte
    CNPJ_COL: str
    IE_COL: str
    CPF_COL: str
    COD_MUN_COL: str
    CNPJ_ENTG: str
    IE_ENTG: str
    CPF_ENTG: str
    COD_MUN_ENTG: str


class RegistroC116(Registro):
    COD_MOD: str
    NR_SAT: str
    CHV_CFE: str
    NUM_CFE: str
    DT_DOC: date


class RegistroC110(Registro):
    COD_INF: str
    TXT_COMPL: str
    RegistroC111: BlockList[RegistroC111]  # /// BLOCO C - Lista de RegistroC111 (FILHO fo FILHO)
    RegistroC112: BlockList[RegistroC112]  # /// BLOCO C - Lista de RegistroC111 (FILHO fo FILHO)
    RegistroC113: BlockList[RegistroC113]  # /// BLOCO C - Lista de RegistroC111 (FILHO fo FILHO)
    RegistroC114: BlockList[RegistroC114]  # /// BLOCO C - Lista de RegistroC111 (FILHO fo FILHO)
    RegistroC115: BlockList[RegistroC115]  # /// BLOCO C - Lista de RegistroC111 (FILHO fo FILHO)
    RegistroC116: BlockList[
        RegistroC116]  # /// BLOCO C - Lista de RegistroC111 (FILHO fo FILHO) {Alteração Versão 2.0.4 03Mar2011}


class RegistroC120(Registro):
    COD_DOC_IMP: DoctoImporta
    NUM_DOC__IMP: str
    PIS_IMP: Decimal
    COFINS_IMP: Decimal
    NUM_ACDRAW: str  # /// Numero do Ato Concessório ro regime Drawback public


class RegistroC130(Registro):
    VL_SERV_NT: Decimal
    VL_BC_ISSQN: Decimal
    VL_ISSQN: Decimal
    VL_BC_IRRF: Decimal
    VL_IRRF: Decimal
    VL_BC_PREV: Decimal
    VL_PREV: Decimal


class RegistroC141(Registro):
    NUM_PARC: str
    DT_VCTO: date
    VL_PARC: Decimal


class RegistroC140(Registro):
    IND_EMIT: IndEmit
    IND_TIT: TipoTitulo
    DESC_TIT: str
    NUM_TIT: str
    QTD_PARC: int
    VL_TIT: Decimal
    RegistroC141: BlockList[RegistroC141]  # /// BLOCO C - Lista de RegistroC141 (FILHO fo FILHO)


class RegistroC160(Registro):
    COD_PART: str
    VEIC_ID: str
    QTD_VOL: int
    PESO_BRT: Decimal
    PESO_LIQ: Decimal
    UF_ID: str


class RegistroC165(Registro):
    COD_PART: str
    VEIC_ID: str
    COD_AUT: str
    NR_PASSE: str
    HORA: str
    TEMPER: str
    QTD_VOL: int
    PESO_BRT: Decimal
    PESO_LIQ: Decimal
    NOM_MOT: str
    CPF: str
    UF_ID: str


class RegistroC171(Registro):
    NUM_TANQUE: str
    QTDE: float


class RegistroC172(Registro):
    VL_BC_ISSQN: Decimal
    ALIQ_ISSQN: Decimal
    VL_ISSQN: Decimal


class RegistroC173(Registro):
    LOTE_MED: str
    QTD_ITEM: float
    DT_FAB: date
    DT_VAL: date
    IND_MED: TipoBaseMedicamento
    TP_PROD: TipoProduto
    VL_TAB_MAX: Decimal


class RegistroC174(Registro):
    IND_ARM: TipoArmaFogo
    NUM_ARM: str
    DESCR_COMPL: str


class RegistroC175(Registro):
    IND_VEIC_OPER: IndVeicOper
    CNPJ: str
    UF: str
    CHASSI_VEIC: str


class RegistroC176(Registro):
    COD_MOD_ULT_E: str
    NUM_DOC_ULT_E: str
    SER_ULT_E: str
    DT_ULT_E: date
    COD_PART_ULT_E: str
    QUANT_ULT_E: float
    VL_UNIT_ULT_E: float
    VL_UNIT_BC_ST: float
    CHAVE_NFE_ULT_E: str  # /// Número completo da chave da NFe relativo à última entrada
    NUM_ITEM_ULT_E: str  # /// Número sequencial do item na NF entrada que corresponde à mercadoria objeto de pedido de ressarcimento
    VL_UNIT_BC_ICMS_ULT_E: Decimal  # /// Valor unitário da base de cálculo da operação própria do remetente sob o regime comum de tributação
    ALIQ_ICMS_ULT_E: Decimal  # /// Alíquota do ICMS aplicável à última entrada da mercadoria
    VL_UNIT_LIMITE_BC_ICMS_ULT_E: Decimal  # /// Valor unitário da base de cálculo do ICMS relativo à última entrada da mercadoria, limitado ao valor da BC da retenção (corresponde ao menor valor entre os campos VL_UNIT_BC_ST e VL_UNIT_BC_ICMS_ULT_E )
    VL_UNIT_ICMS_ULT_E: Decimal  # /// Valor unitário do crédito de ICMS sobre operações próprias do remetente, relativo à última entrada da mercadoria, decorrente da quebra da ST  equivalente a multiplicação entre os campos 13 e 14
    ALIQ_ST_ULT_E: Decimal  # /// Alíquota do ICMS ST relativa à última entrada da mercadoria
    VL_UNIT_RES: Decimal  # /// Valor unitário do ressarcimento (parcial ou completo) de ICMS decorrente da quebra da ST
    COD_RESP_RET: str  # /// Código que indica o responsável pela retenção do ICMS-ST: 1-Remetente Direto 2-Remetente Indireto 3-Próprio declarante
    COD_MOT_RES: MotivoRessarcimento  # /// Código do motivo do ressarcimento 1  Venda para outra UF; 2  Saída amparada por isenção ou não incidência; 3  Perda ou deterioração; 4  Furto ou roubo 5  Exportação 6  Venda interna para Simples Nacional 9 - Outros
    CHAVE_NFE_RET: str  # /// Número completo da chave da NF-e emitida pelo substituto, na qual consta o valor do ICMS-ST retido
    COD_PART_NFE_RET: str  # /// Código do participante do emitente da NF-e em que houve a retenção do ICMS-ST  campo 02 do registro 0150
    SER_NFE_RET: str  # /// Série da NF-e em que houve a retenção do ICMSST
    NUM_NFE_RET: str  # /// Número da NF-e em que houve a retenção do ICMS-ST
    ITEM_NFE_RET: str  # /// Número sequencial do item na NF-e em que houve a retenção do ICMS-ST, que corresponde à mercadoria objeto de pedido de ressarcimento
    COD_DA: str  # /// Código do modelo do documento de arrecadação : 0 - documento estadual de arrecadação 1  GNRE
    NUM_DA: str  # /// Número do documento de arrecadação estadual, se houver
    VL_UNIT_RES_FCP_ST: Decimal  # /// Valor unitário do ressarcimento (parcial ou completo) de FCP decorrente da quebra da ST


class RegistroC177(Registro):
    COD_SELO_IPI: str
    QT_SELO_IPI: Decimal
    COD_INF_ITEM: str  # //Código da informação adicional de acordo com tabela a ser publicada pelas SEFAZ, conforme tabela definida no item 5.6.


class RegistroC178(Registro):
    CL_ENQ: str
    VL_UNID: Decimal
    QUANT_PAD: float


class RegistroC179(Registro):
    BC_ST_ORIG_DEST: Decimal
    ICMS_ST_REP: Decimal
    ICMS_ST_COMPL: Decimal
    BC_RET: Decimal
    ICMS_RET: Decimal


class RegistroC180(Registro):
    COD_RESP_RET: str  # /// Código que indica o responsável pela retenção do ICMS-ST: 1-Remetente Direto / 2-Remetente Indireto / 3-Próprio declarante.
    QUANT_CONV: float  # /// Quantidade do item convertida na unidade de controle de estoque informada no registro 0200 ou a unidade de comercialização, a critério de cada UF.
    UNID: str  # /// Unidade adotada para informar o campo QUANT_CONV.
    VL_UNIT_CONV: float  # /// Valor unitário da mercadoria, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_OP_CONV: float  # /// Valor unitário do ICMS operação própria que o informante teria direito ao crédito caso a mercadoria estivesse sob o regime comum de tributação, considerando unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_BC_ICMS_ST_CONV: float  # /// Valor unitário da base de cálculo do imposto pago ou retido anteriormente por substituição, considerando a unidade utilizada para informar o campo QUANT_CONV, aplicando-se redução, se houver.
    VL_UNIT_ICMS_ST_CONV: float  # /// Valor unitário do imposto pago ou retido anteriormente por substituição, inclusive FCP se devido, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_FCP_ST_CONV: float  # /// Valor unitário do FCP_ST agregado ao valor informado no campo VL_UNIT_ICMS_ST_CONV.
    COD_DA: str  # /// Código do modelo do documento de arrecadação: 0  Documento estadual de arrecadação / 1  GNRE.
    NUM_DA: str  # /// Número do documento de arrecadação estadual, se houver.


class RegistroC181(Registro):
    COD_MOT_REST_COMPL: str  # /// Código do motivo da restituição ou complementação conforme Tabela 5.7
    QUANT_CONV: float  # /// Quantidade do item
    UNID: str  # /// Unidade adotada para informar o campoQUANT_CONV.
    COD_MOD_SAIDA: str  # /// Código do modelo do documento fiscal de saída, conforme a tabela indicada no item 4.1.1
    SERIE_SAIDA: str  # /// Número de série do documento de saída em papel
    ECF_FAB_SAIDA: str  # /// Número de série de fabricação do equipamento ECF
    NUM_DOC_SAIDA: str  # /// Número do documento fiscal de saída
    CHV_DFE_SAIDA: str  # /// Chave do documento fiscal eletrônico de saída
    DT_DOC_SAIDA: date  # /// Data da emissão do documento fiscal de saída
    NUM_ITEM_SAIDA: str  # /// Número do item em que foi escriturada a saída em um registro C185, C380, C480 ou C815 quando o contribuinte informar a saída em um arquivo de perfil A.
    VL_UNIT_CONV_SAIDA: float  # /// Valor unitário da mercadoria, considerando a unidade utilizada para informar o campo QUANT_CONV, correspondente ao valor do campo VL_UNIT_CONV, preenchido na ocasião da saída
    VL_UNIT_ICMS_OP_ESTOQUE_CONV_SAIDA: Decimal  # /// Valor médio unitário do ICMS OP, das mercadorias em estoque, correspondente ao valor do campo VL_UNIT_ICMS_OP_ESTOQUE_CONV, preenchido na ocasião da saída
    VL_UNIT_ICMS_ST_ESTOQUE_CONV_SAIDA: Decimal  # /// Valor médio unitário do ICMS ST, incluindo FCP ST, das mercadorias em estoque, correspondente ao valor do campo VL_UNIT_ICMS_ST_ESTOQUE_CONV, preenchido na ocasião da saída
    VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV_SAIDA: Decimal  # /// Valor médio unitário do FCP ST agregado ao ICMS das mercadorias em estoque, correspondente ao valor do campo VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV, preenchido na ocasião da saída
    VL_UNIT_ICMS_NA_OPERACAO_CONV_SAIDA: Decimal  # /// Valor unitário para o ICMS na operação, correspondente ao valor do campo VL_UNIT_ICMS_NA_OPERACAO_CONV, preenchido na ocasião da saída
    VL_UNIT_ICMS_OP_CONV_SAIDA: Decimal  # /// Valor unitário do ICMS correspondente ao valor do campo VL_UNIT_ICMS_OP_CONV, preenchido na ocasião da saída
    VL_UNIT_ICMS_ST_CONV_REST: Decimal  # /// Valor unitário do total do ICMS ST, incluindo FCP ST, a ser restituído/ressarcido, correspondente ao estorno do complemento apurado na operação de saída.
    VL_UNIT_FCP_ST_CONV_REST: Decimal  # /// Valor unitário correspondente à parcela de ICMS FCP ST que compõe o campo VL_UNIT_ICMS_ST_CONV_REST, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_ST_CONV_COMPL: Decimal  # /// Valor unitário do estorno do ressarcimento/restituição, incluindo FCP ST, apurado na operação de saída.
    VL_UNIT_FCP_ST_CONV_COMPL: Decimal  # /// Valor unitário correspondente à parcela de ICMS FCP ST que compõe o campo VL_UNIT_ICMS_ST_CONV_COMPL, considerando unidade utilizada para informar o campo QUANT_CONV.


class RegistroC170(Registro):
    NUM_ITEM: str
    COD_ITEM: str
    DESCR_COMPL: str
    QTD: float
    UNID: str
    VL_ITEM: Decimal
    VL_DESC: Decimal
    IND_MOV: IndMovFisica
    CST_ICMS: str
    CFOP: str
    COD_NAT: str
    VL_BC_ICMS: Decimal
    ALIQ_ICMS: Decimal
    VL_ICMS: Decimal
    VL_BC_ICMS_ST: Decimal
    ALIQ_ST: Decimal
    VL_ICMS_ST: Decimal
    IND_APUR: ApuracaoIPI
    CST_IPI: str
    COD_ENQ: str
    VL_BC_IPI: Decimal
    ALIQ_IPI: Decimal
    VL_IPI: Decimal
    CST_PIS: str
    VL_BC_PIS: Decimal
    ALIQ_PIS_PERC: Decimal
    QUANT_BC_PIS: float
    ALIQ_PIS_R: float
    VL_PIS: Decimal
    CST_COFINS: str
    VL_BC_COFINS: Decimal
    ALIQ_COFINS_PERC: Decimal
    QUANT_BC_COFINS: float
    ALIQ_COFINS_R: float
    VL_COFINS: Decimal
    COD_CTA: str
    VL_ABAT_NT: Decimal
    RegistroC171: BlockList[RegistroC171]  # /// BLOCO C - Lista de RegistroC171 (FILHO fo FILHO)
    RegistroC172: BlockList[RegistroC172]  # /// BLOCO C - Lista de RegistroC172 (FILHO fo FILHO)
    RegistroC173: BlockList[RegistroC173]  # /// BLOCO C - Lista de RegistroC173 (FILHO fo FILHO)
    RegistroC174: BlockList[RegistroC174]  # /// BLOCO C - Lista de RegistroC174 (FILHO fo FILHO)
    RegistroC175: BlockList[RegistroC175]  # /// BLOCO C - Lista de RegistroC175 (FILHO fo FILHO)
    RegistroC176: BlockList[RegistroC176]  # /// BLOCO C - Lista de RegistroC176 (FILHO fo FILHO)
    RegistroC177: BlockList[RegistroC177]  # /// BLOCO C - Lista de RegistroC177 (FILHO fo FILHO)
    RegistroC178: BlockList[RegistroC178]  # /// BLOCO C - Lista de RegistroC178 (FILHO fo FILHO)
    RegistroC179: BlockList[RegistroC179]  # /// BLOCO C - Lista de RegistroC179 (FILHO fo FILHO)
    RegistroC180: BlockList[RegistroC180]  # /// BLOCO C - Lista de RegistroC180 (FILHO fo FILHO)
    RegistroC181: BlockList[RegistroC181]  # /// BLOCO C - Lista de RegistroC181 (FILHO fo FILHO)


class RegistroC185(Registro):
    NUM_ITEM: str  # /// Número sequencial do item no documento fiscal.
    COD_ITEM: str  # /// Código do item (campo 02 do Registro 0200).
    CST_ICMS: str  # /// Código da Situação Tributária referente ao ICMS.
    CFOP: str  # /// Código Fiscal de Operação e Prestação.
    COD_MOT_REST_COMPL: str  # /// Código do motivo da restituição ou complementação conforme Tabela 5.7.
    QUANT_CONV: float  # /// Quantidade do item.
    UNID: str  # /// Unidade adotada para informar o campo QUANT_CONV.
    VL_UNIT_CONV: float  # /// Valor unitário da mercadoria, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_NA_OPERACAO_CONV: Decimal  # /// Valor unitário para o ICMS na operação, caso não houvesse a ST, considerando unidade utilizada para informar o campo QUANT_CONV, considerando redução da base de cálculo do ICMS ST na tributação, se houver.
    VL_UNIT_ICMS_OP_CONV: Decimal  # /// Valor unitário do ICMS que o contribuinte teria se creditado, ou pode se creditar, referente à operação de entrada da mercadoria, caso estivesse submetida ao regime comum de tributação, no desfazimento da substituição tributária, calculado conforme a legislação de cada UF, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_OP_ESTOQUE_CONV: Decimal  # /// Valor médio unitário do ICMS que o contribuinte teria se creditado referente à operação de entrada das mercadorias em estoque caso estivesse submetida ao regime comum de tributação, calculado conforme a legislação de cada UF, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_ST_ESTOQUE_CONV: Decimal  # /// Valor médio unitário do ICMS/ST, incluindo FCP ST, das mercadorias em estoque, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV: Decimal  # /// Valor médio unitário do FCP ST agregado ao ICMS das mercadorias em estoque, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_ST_CONV_REST: Decimal  # /// Valor unitário do total do ICMS/ST, incluindo FCP ST, a ser restituído/ressarcido, calculado conforme a legislação de cada UF, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_FCP_ST_CONV_REST: Decimal  # /// Valor unitário correspondente à parcela de ICMS FCP ST que compõe o campo VL_UNIT_ICMS_ST_CONV_REST, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_ST_CONV_COMPL: Decimal  # ///  Valor unitário do complemento do ICMS, incluindo FCP ST, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_FCP_ST_CONV_COMPL: Decimal  # /// Valor unitário correspondente à parcela de ICMS FCP ST que compõe o campo VL_UNIT_ICMS_ST_CONV_COMPL, considerando unidade utilizada para informar o campo QUANT_CONV.


class RegistroC186(Registro):
    NUM_ITEM: str  # /// Número sequencial do item no documento fiscal.
    COD_ITEM: str  # /// Código do item (campo 02 do Registro 0200).
    CST_ICMS: str  # /// Código da Situação Tributária referente ao ICMS.
    CFOP: str  # /// Código Fiscal de Operação e Prestação.
    COD_MOT_REST_COMPL: str  # /// Código do motivo da restituição ou complementação conforme Tabela 5.7.
    QUANT_CONV: float  # /// Quantidade do item.
    UNID: str  # /// Unidade adotada para informar o campo QUANT_CONV.
    COD_MOD_ENTRADA: str  # /// Código do modelo do documento fiscal de entrada, conforme a tabela indicada no item 4.1.1
    SERIE_ENTRADA: str  # ///  Número de série do documento de entrada em papel
    NUM_DOC_ENTRADA: str  # /// Número do documento fiscal de entrada
    CHV_DFE_ENTRADA: str  # /// Chave do documento fiscal eletrônico de entrada
    DT_DOC_ENTRADA: date  # /// Data da emissão do documento fiscal de entrada
    NUM_ITEM_ENTRADA: str  # /// Item do documento fiscal de entrada
    VL_UNIT_CONV_ENTRADA: float  # /// Valor unitário da mercadoria, considerando a unidade utilizada para informar o campo QUANT_CONV, correspondente ao valor do campo VL_UNIT_CONV, preenchido na ocasião da entrada
    VL_UNIT_ICMS_OP_CONV_ENTRADA: float  # /// Valor unitário do ICMS correspondente ao valor do campo VL_UNIT_ICMS_OP_CONV, preenchido na ocasião da entrada
    VL_UNIT_BC_ICMS_ST_CONV_ENTRADA: float  # /// Valor unitário da base de cálculo do imposto pago ou retido anteriormente por substituição, correspondente ao valor do campo VL_UNIT_BC_ICMS_ST_CONV, preenchido na ocasião da entrada
    VL_UNIT_ICMS_ST_CONV_ENTRADA: float  # ///  Valor unitário do imposto pago ou retido anteriormente por substituição, inclusive FCP se devido, correspondente ao valor do campo VL_UNIT_ICMS_ST_CONV, preenchido na ocasião da entrada
    VL_UNIT_FCP_ST_CONV_ENTRADA: float  # /// Valor unitário do FCP_ST, correspondente ao valor do campo VL_UNIT_FCP_ST_CONV, preenchido na ocasião da entrada


class RegistroC191(Registro):
    VL_FCP_OP: Decimal  # //Valor do Fundo de Combate à Pobreza (FCP) vinculado à operação própria, na combinação de CST_ICMS, CFOP e alíquota do ICMS
    VL_FCP_ST: Decimal  # //Valor do Fundo de Combate à Pobreza (FCP) vinculado à operação de substituição tributária, na combinação de CST_ICMS, CFOP e alíquota do ICMS.
    VL_FCP_RET: Decimal  # //Valor relativo ao Fundo de Combate à Pobreza (FCP) retido anteriormente nas operações com Substituição Tributárias, na combinação de CST_ICMS, CFOP e alíquota do ICMS


class RegistroC190(Registro):
    CST_ICMS: str
    CFOP: str
    ALIQ_ICMS: Decimal
    VL_OPR: Decimal
    VL_BC_ICMS: Decimal
    VL_ICMS: Decimal
    VL_BC_ICMS_ST: Decimal
    VL_ICMS_ST: Decimal
    VL_RED_BC: Decimal
    VL_IPI: Decimal
    COD_OBS: str
    RegistroC191: BlockList[RegistroC191]  # /// BLOCO C - Lista de RegistroC191 (FILHO)


class RegistroC197(Registro):
    COD_AJ: str
    DESCR_COMPL_AJ: str
    COD_ITEM: str
    VL_BC_ICMS: Decimal
    ALIQ_ICMS: Decimal
    VL_ICMS: Decimal
    VL_OUTROS: Decimal


class RegistroC195(Registro):
    COD_OBS: str
    TXT_COMPL: str
    RegistroC197: BlockList[RegistroC197]


class RegistroC100(Registro):
    IND_OPER: IndOper
    IND_EMIT: IndEmit
    COD_PART: str
    COD_MOD: str
    COD_SIT: CodSit
    SER: str
    NUM_DOC: str
    CHV_NFE: str
    DT_DOC: date
    DT_E_S: date
    VL_DOC: Decimal
    IND_PGTO: IndPgto
    VL_DESC: Decimal
    VL_ABAT_NT: Decimal
    VL_MERC: Decimal
    IND_FRT: IndFrt
    VL_FRT: Decimal
    VL_SEG: Decimal
    VL_OUT_DA: Decimal
    VL_BC_ICMS: Decimal
    VL_ICMS: Decimal
    VL_BC_ICMS_ST: Decimal
    VL_ICMS_ST: Decimal
    VL_IPI: Decimal
    VL_PIS: Decimal
    VL_COFINS: Decimal
    VL_PIS_ST: Decimal
    VL_COFINS_ST: Decimal
    RegistroC101: BlockList[RegistroC101]  # /// BLOCO C - Lista de RegistroC105 (FILHO)
    RegistroC105: BlockList[RegistroC105]  # /// BLOCO C - Lista de RegistroC105 (FILHO)
    RegistroC110: BlockList[RegistroC110]  # /// BLOCO C - Lista de RegistroC110 (FILHO)
    RegistroC120: BlockList[RegistroC120]  # /// BLOCO C - Lista de RegistroC120 (FILHO)
    RegistroC130: BlockList[RegistroC130]  # /// BLOCO C - Lista de RegistroC130 (FILHO)
    RegistroC140: BlockList[RegistroC140]  # /// BLOCO C - Lista de RegistroC140 (FILHO)
    RegistroC160: BlockList[RegistroC160]  # /// BLOCO C - Lista de RegistroC160 (FILHO)
    RegistroC165: BlockList[RegistroC165]  # /// BLOCO C - Lista de RegistroC165 (FILHO)
    RegistroC170: BlockList[RegistroC170]  # /// BLOCO C - Lista de RegistroC170 (FILHO)
    RegistroC185: BlockList[RegistroC185]  # /// BLOCO C - Lista de RegistroC185 (FILHO)
    RegistroC186: BlockList[RegistroC186]  # /// BLOCO C - Lista de RegistroC186 (FILHO)
    RegistroC190: BlockList[RegistroC190]  # /// BLOCO C - Lista de RegistroC190 (FILHO)
    RegistroC195: BlockList[RegistroC195]  # /// BLOCO C - Lista de RegistroC195 (FILHO)


class RegistroC310(Registro):
    NUM_DOC_CANC: str  # /// Número do documento fiscal cancelado


class RegistroC330(Registro):
    COD_MOT_REST_COMPL: str  # /// Código do motivo da restituição ou complementação conforme Tabela 5.7.
    QUANT_CONV: Decimal  # /// Quantidade do item.
    UNID: str  # /// Unidade adotada para informar o campo QUANT_CONV.
    VL_UNIT_CONV: Decimal  # /// Valor unitário da mercadoria, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_NA_OPERACAO_CONV: Decimal  # /// Valor unitário para o ICMS na operação, caso não houvesse a ST, considerando unidade utilizada para informar o campo QUANT_CONV, aplicando-se a mesma redução da base de cálculo do ICMS ST na tributação, se houver.
    VL_UNIT_ICMS_OP_CONV: Decimal  # /// Valor unitário correspondente ao ICMS OP utilizado no cálculo do ressarcimento / restituição, no desfazimento da substituição tributária, calculado conforme a legislação de cada UF, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_OP_ESTOQUE_CONV: Decimal  # /// Valor médio unitário do ICMS que o contribuinte teria se creditado referente à operação de entrada das mercadorias em estoque caso estivesse submetida ao regime comum de tributação, calculado conforme a legislação de cada UF, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_ST_ESTOQUE_CONV: Decimal  # /// Valor médio unitário do ICMS/ST, incluindo FCP ST, das mercadorias em estoque, considerando unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV: Decimal  # /// Valor médio unitário do ICMS/ST, incluindo FCP ST, das mercadorias em estoque, considerando unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_ST_CONV_REST: Decimal  # /// Valor unitário do total do ICMS/ST, incluindo FCP ST, a ser restituído/ressarcido, calculado conforme a legislação de cada UF, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_FCP_ST_CONV_REST: Decimal  # /// Valor unitário correspondente à parcela de ICMS FCP ST que compõe o campo VL_UNIT_ICMS_ST_CONV_REST, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_ST_CONV_COMPL: Decimal  # /// Valor unitário do complemento do ICMS, incluindo FCP ST, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_FCP_ST_CONV_COMPL: Decimal  # /// Valor unitário correspondente à parcela de ICMS FCP ST que compõe o campo VL_UNIT_ICMS_ST_CONV_COMPL, considerando unidade utilizada para informar o campo QUANT_CONV.


class RegistroC321(Registro):
    COD_ITEM: str
    QTD: float
    UNID: str
    VL_ITEM: Decimal
    VL_DESC: Decimal
    VL_BC_ICMS: Decimal
    VL_ICMS: Decimal
    VL_PIS: Decimal
    VL_COFINS: Decimal
    RegistroC330: BlockList[RegistroC330]


class RegistroC320(Registro):
    CST_ICMS: str  # /// Código da Situação Tributária, conforme a Tabela indicada no item 4.3.1
    CFOP: str  # /// Código Fiscal de Operação e Prestação
    ALIQ_ICMS: Decimal  # /// Alíquota do ICMS
    VL_OPR: Decimal  # /// Valor total acumulado das operações correspondentes à combinação de CST_ICMS, CFOP e alíquota do ICMS, incluídas as despesas acessórias e acréscimos.
    VL_BC_ICMS: Decimal  # /// Valor acumulado da base de cálculo do ICMS, referente à combinação de CST_ICMS, CFOP, e alíquota do ICMS.
    VL_ICMS: Decimal  # /// Valor acumulado do ICMS, referente à combinação de CST_ICMS, CFOP e alíquota do ICMS.
    VL_RED_BC: Decimal  # /// Valor não tributado em função da redução da base de cálculo do ICMS, referente à combinação de CST_ICMS, CFOP, e alíquota do ICMS.
    COD_OBS: str  # /// Código da observação do lançamento fiscal (campo 02 do Registro 0460)
    RegistroC321: BlockList[RegistroC321]


class RegistroC300(Registro):
    COD_MOD: str  # /// Código do modelo do documento fiscal, conforme a Tabela 4.1.1
    SER: str  # /// Série do documento fiscal
    SUB: str  # /// Subsérie do documento fiscal
    NUM_DOC_INI: str  # /// Número do documento fiscal inicial
    NUM_DOC_FIN: str  # /// Número do documento fiscal final
    DT_DOC: date  # /// Data da emissão dos documentos fiscais
    VL_DOC: Decimal  # /// Valor total dos documentos
    VL_PIS: Decimal  # /// Valor total do PIS
    VL_COFINS: Decimal  # /// Valor total da COFINS
    COD_CTA: str  # /// Código da conta analítica contábil debitada/creditada
    RegistroC310: BlockList[RegistroC310]
    RegistroC320: BlockList[RegistroC320]


class RegistroC380(Registro):
    COD_MOT_REST_COMPL: str  # /// Código do motivo da restituição ou complementação conforme Tabela 5.7.
    QUANT_CONV: Decimal  # ///Quantidade do item.
    UNID: str  # /// Unidade adotada para informar o campo QUANT_CONV.
    VL_UNIT_CONV: Decimal  # /// Valor unitário da mercadoria, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_NA_OPERACAO_CONV: Decimal  # /// Valor unitário para o ICMS na operação, caso não houvesse a ST, considerando unidade utilizada para informar o campo QUANT_CONV, aplicando-se a mesma redução da base de cálculo do ICMS ST na tributação, se houver.
    VL_UNIT_ICMS_OP_CONV: Decimal  # /// Valor unitário correspondente ao ICMS OP utilizado no cálculo do ressarcimento / restituição, no desfazimento da substituição tributária, calculado conforme a legislação de cada UF, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_OP_ESTOQUE_CONV: Decimal  # /// Valor médio unitário do ICMS que o contribuinte teria se creditado referente à operação de entrada das mercadorias em estoque caso estivesse submetida ao regime comum de tributação, calculado conforme a legislação de cada UF, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_ST_ESTOQUE_CONV: Decimal  # /// Valor médio unitário do ICMS/ST, incluindo FCP ST, das mercadorias em estoque, considerando unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV: Decimal  # /// Valor médio unitário do FCP ST agregado ao ICMS das mercadorias em estoque, considerando unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_ST_CONV_REST: Decimal  # /// Valor unitário do total do ICMS/ST, incluindo FCP ST, a ser restituído/ressarcido, calculado conforme a legislação de cada UF, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_FCP_ST_CONV_REST: Decimal  # /// Valor unitário correspondente à parcela de ICMS FCP ST que compõe o campo VL_UNIT_ICMS_ST_CONV_REST, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_ST_CONV_COMPL: Decimal  # /// Valor unitário do complemento do ICMS, incluindo FCP ST, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_FCP_ST_CONV_COMPL: Decimal  # /// Valor unitário correspondente à parcela de ICMS FCP ST que compõe o campo VL_UNIT_ICMS_ST_CONV_COMPL, considerando unidade utilizada para informar o campo QUANT_CONV.
    CST_ICMS: str  # ///Código da Situação Tributária referente ao ICMS.
    CFOP: str  # /// Código Fiscal de Operação e Prestação.


class RegistroC370(Registro):
    NUM_ITEM: str
    COD_ITEM: str
    QTD: float
    UNID: str
    VL_ITEM: Decimal
    VL_DESC: Decimal
    RegistroC380: BlockList[RegistroC380]


class RegistroC390(Registro):
    CST_ICMS: str
    CFOP: str
    ALIQ_ICMS: Decimal
    VL_OPR: Decimal
    VL_BC_ICMS: Decimal
    VL_ICMS: Decimal
    VL_RED_BC: Decimal
    COD_OBS: str


class RegistroC350(Registro):
    SER: str
    SUB_SER: str
    NUM_DOC: str
    DT_DOC: date
    CNPJ_CPF: str
    VL_MERC: Decimal
    VL_DOC: Decimal
    VL_DESC: Decimal
    VL_PIS: Decimal
    VL_COFINS: Decimal
    COD_CTA: str
    RegistroC370: BlockList[RegistroC370]  # /// BLOCO C - Lista de RegistroC370 (FILHO)
    RegistroC390: BlockList[RegistroC390]  # /// BLOCO C - Lista de RegistroC390 (FILHO)


class RegistroC410(Registro):
    VL_PIS: Decimal
    VL_COFINS: Decimal


class RegistroC430(Registro):
    COD_MOT_REST_COMPL: str  # /// Código do motivo da restituição ou complementação conforme Tabela 5.7.
    QUANT_CONV: Decimal  # /// Quantidade do item.
    UNID: str  # /// Unidade adotada para informar o campo QUANT_CONV.
    VL_UNIT_CONV: Decimal  # /// Valor unitário da mercadoria, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_NA_OPERACAO_CONV: Decimal  # /// Valor unitário para o ICMS na operação, caso não houvesse a ST, considerando unidade utilizada para informar o campo QUANT_CONV, considerando redução da base de cálculo do ICMS ST na tributação, se houver.
    VL_UNIT_ICMS_OP_CONV: Decimal  # /// Valor unitário do ICMS que o contribuinte teria se creditado, ou pode se creditar, referente à operação de entrada da mercadoria, caso estivesse submetida ao regime comum de tributação, no desfazimento da substituição tributária, calculado conforme a legislação de cada UF, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_OP_ESTOQUE_CONV: Decimal  # /// Valor médio unitário do ICMS que o contribuinte teria se creditado referente à operação de entrada das mercadorias em estoque caso estivesse submetida ao regime comum de tributação, calculado conforme a legislação de cada UF, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_ST_ESTOQUE_CONV: Decimal  # /// Valor médio unitário do ICMS/ST, incluindo FCP ST, das mercadorias em estoque, considerando unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV: Decimal  # /// Valor médio unitário do FCP ST agregado ao ICMS das mercadorias em estoque, considerando unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_ST_CONV_REST: Decimal  # /// Valor unitário do total do ICMS/ST, incluindo FCP ST, a ser restituído/ressarcido, calculado conforme a legislação de cada UF, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_FCP_ST_CONV_REST: Decimal  # /// Valor unitário correspondente à parcela de ICMS FCP ST que compõe o campo VL_UNIT_ICMS_ST_CONV_REST, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_ST_CONV_COMPL: Decimal  # /// Valor unitário do complemento do ICMS, incluindo FCP ST, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_FCP_ST_CONV_COMPL: Decimal  # /// Valor unitário correspondente à parcela de ICMS FCP ST que compõe o campo VL_UNIT_ICMS_ST_CONV_COMPL, considerando unidade utilizada para informar o campo QUANT_CONV.
    CST_ICMS: str  # /// Código da Situação Tributária referente ao ICMS.
    CFOP: str  # /// Código Fiscal de Operação e Prestação


class RegistroC425(Registro):
    COD_ITEM: str
    QTD: float
    UNID: str
    VL_ITEM: Decimal
    VL_PIS: Decimal  # /// Valor do PIS
    VL_COFINS: Decimal  # /// Valor da COFINS
    RegistroC430: BlockList[RegistroC430]  # /// BLOCO C - Lista de RegistroC430 (FILHO)


class RegistroC420(Registro):
    COD_TOT_PAR: str  # /// Código do totalizador, conforme Tabela 4.4.6
    VLR_ACUM_TOT: Decimal  # /// Valor acumulado no totalizador, relativo à respectiva Redução Z.
    NR_TOT: int  # /// Número do totalizador quando ocorrer mais de uma situação com a mesma carga tributária efetiva.
    DESCR_NR_TOT: str  # /// Descrição da situação tributária relativa ao totalizador parcial, quando houver mais de um com a mesma carga tributária efetiva.
    RegistroC425: BlockList[RegistroC425]  # /// BLOCO C - Lista de RegistroC425 (FILHO)


class RegistroC465(Registro):
    CHV_CFE: str
    NUM_CCF: str


class RegistroC480(Registro):
    COD_MOT_REST_COMPL: str  # /// Código do motivo da restituição ou complementação conforme Tabela 5.7.
    QUANT_CONV: Decimal  # /// Quantidade do item.
    UNID: str  # /// Unidade adotada para informar o campo QUANT_CONV.
    VL_UNIT_CONV: Decimal  # /// Valor unitário da mercadoria, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_NA_OPERACAO_CONV: Decimal  # /// Valor unitário para o ICMS na operação, caso não houvesse a ST, considerando unidade utilizada para informar o campo QUANT_CONV, aplicando-se a mesma redução da base de cálculo do ICMS ST na tributação, se houver.
    VL_UNIT_ICMS_OP_CONV: Decimal  # /// Valor unitário correspondente ao ICMS OP utilizado no cálculo do ressarcimento / restituição, no desfazimento da substituição tributária, calculado conforme a legislação de cada UF, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_OP_ESTOQUE_CONV: Decimal  # /// Valor médio unitário do ICMS que o contribuinte teria se creditado referente à operação de entrada das mercadorias em estoque caso estivesse submetida ao regime comum de tributação, calculado conforme a legislação de cada UF, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_ST_ESTOQUE_CONV: Decimal  # /// Valor médio unitário do ICMS/ST, incluindo FCP ST, das mercadorias em estoque, considerando unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV: Decimal  # /// Valor médio unitário do FCP ST agregado ao ICMS das mercadorias em estoque, considerando unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_ST_CONV_REST: Decimal  # /// Valor unitário do total do ICMS/ST, incluindo FCP ST, a ser restituído/ressarcido, calculado conforme a legislação de cada UF, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_FCP_ST_CONV_REST: Decimal  # /// Valor unitário correspondente à parcela de ICMS FCP ST que compõe o campo VL_UNIT_ICMS_ST_CONV_REST, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_ICMS_ST_CONV_COMPL: Decimal  # /// Valor unitário do complemento do ICMS, incluindo FCP ST, considerando a unidade utilizada para informar o campo QUANT_CONV.
    VL_UNIT_FCP_ST_CONV_COMPL: Decimal  # /// Valor unitário correspondente à parcela de ICMS FCP ST que compõe o campo VL_UNIT_ICMS_ST_CONV_COMPL, considerando unidade utilizada para informar o campo QUANT_CONV.
    CST_ICMS: str  # /// Código da Situação Tributária referente ao ICMS.
    CFOP: str  # /// Código Fiscal de Operação e Prestação.


class RegistroC470(Registro):
    COD_ITEM: str
    QTD: float
    QTD_CANC: float
    UNID: str
    VL_ITEM: Decimal
    CST_ICMS: str  # /// Código da Situação Tributária, conforme a Tabela indicada no item 4.3.1.
    CFOP: str  # /// Código Fiscal de Operação e Prestação
    ALIQ_ICMS: Decimal  # /// Alíquota do ICMS - Carga tributária efetiva em percentual
    VL_PIS: Decimal  # /// Valor do PIS
    VL_COFINS: Decimal  # /// Valor da COFINS
    RegistroC480: BlockList[RegistroC480]


class RegistroC460(Registro):
    COD_MOD: str  # /// Código do modelo do documento fiscal, conforme a Tabela 4.1.1
    COD_SIT: CodSit  # /// Código da situação do documento fiscal, conforme a Tabela 4.1.2
    NUM_DOC: str  # /// Número do documento fiscal (COO)
    DT_DOC: date  # /// Data da emissão do documento fiscal
    VL_DOC: Decimal  # /// Valor total do documento fiscal
    VL_PIS: Decimal  # /// Valor do PIS
    VL_COFINS: Decimal  # /// Valor da COFINS
    CPF_CNPJ: str  # /// CPF ou CNPJ do adquirente
    NOM_ADQ: str  # /// Nome do adquirente
    RegistroC465: BlockList[RegistroC465]
    RegistroC470: BlockList[RegistroC470]  # /// BLOCO C - Lista de RegistroC460 (FILHO)


class RegistroC490(Registro):
    CST_ICMS: str
    CFOP: str
    ALIQ_ICMS: Decimal
    VL_OPR: Decimal
    VL_BC_ICMS: Decimal
    VL_ICMS: Decimal
    COD_OBS: str


class RegistroC405(Registro):
    DT_DOC: date  # /// Data do movimento a que se refere a Redução Z
    CRO: int  # /// Posição do Contador de Reinício de Operação
    CRZ: int  # /// Posição do Contador de Redução Z
    NUM_COO_FIN: int  # /// Número do Contador de Ordem de Operação do último documento emitido no dia. (Número do COO na Redução Z)
    GT_FIN: Decimal  # /// Valor do Grande Total final
    VL_BRT: Decimal  # /// Valor da venda bruta
    RegistroC410: BlockList[RegistroC410]  # /// BLOCO C - Lista de RegistroC410 (FILHO)
    RegistroC420: BlockList[RegistroC420]  # /// BLOCO C - Lista de RegistroC420 (FILHO)
    RegistroC460: BlockList[RegistroC460]  # /// BLOCO C - Lista de RegistroC460 (FILHO)
    RegistroC490: BlockList[RegistroC490]  # /// BLOCO C - Lista de RegistroC490 (FILHO)


class RegistroC400(Registro):
    COD_MOD: str  # /// Código do modelo do documento fiscal, conforme a Tabela 4.1.1
    ECF_MOD: str  # /// Modelo do equipamento
    ECF_FAB: str  # /// Número de série de fabricação do ECF
    ECF_CX: str  # /// Número do caixa atribuído ao ECF
    RegistroC405: BlockList[RegistroC405]  # /// BLOCO C - Lista de RegistroC405 (FILHO)


class RegistroC495(Registro):
    ALIQ_ICMS: Decimal
    COD_ITEM: str
    QTD: float
    QTD_CANC: float
    UNID: str
    VL_ITEM: Decimal
    VL_DESC: Decimal
    VL_CANC: Decimal
    VL_ACMO: Decimal
    VL_BC_ICMS: Decimal
    VL_ICMS: Decimal
    VL_ISEN: Decimal
    VL_NT: Decimal
    VL_ICMS_ST: Decimal


class RegistroC510(Registro):
    NUM_ITEM: str  # /// Número seqüencial do item no documento fiscal
    COD_ITEM: str  # /// Código do item (campo 02 do Registro 0200)
    COD_CLASS: str  # /// Código de classificação do item de energia elétrica, conforme a Tabela 4.4.1
    QTD: float  # /// Quantidade do item
    UNID: str  # /// Unidade do item (Campo 02 do registro 0190)
    VL_ITEM: Decimal  # /// Valor do item
    VL_DESC: Decimal  # /// Valor total do desconto
    CST_ICMS: str  # /// Código da Situação Tributária, conforme a Tabela indicada no item 4.3.1
    CFOP: str  # /// Código Fiscal de Operação e Prestação
    VL_BC_ICMS: Decimal  # /// Valor da base de cálculo do ICMS
    ALIQ_ICMS: Decimal  # /// Alíquota do ICMS
    VL_ICMS: Decimal  # /// Valor do ICMS creditado/debitado
    VL_BC_ICMS_ST: Decimal  # /// Valor da base de cálculo referente à substituição tributária
    ALIQ_ST: Decimal  # /// Alíquota do ICMS da substituição tributária na unidade da federação de destino
    VL_ICMS_ST: Decimal  # /// Valor do ICMS referente à substituição tributária
    IND_REC: IndReceita  # /// Indicador do tipo de receita: 0- Receita própria; 1- Receita de terceiros
    COD_PART: str  # /// Código do participante receptor da receita, terceiro da operação (campo 02 do Registro 0150)
    VL_PIS: Decimal  # /// Valor do PIS
    VL_COFINS: Decimal  # /// Valor da COFINS
    COD_CTA: str  # /// Código da conta analítica contábil debitada/creditada


class RegistroC591(Registro):
    VL_FCP_OP: Decimal  # /// Valor do Fundo de Combate à Pobreza (FCP) vinculado à operação própria, na combinação de CST_ICMS, CFOP e alíquota do ICMS
    VL_FCP_ST: Decimal  # /// Valor do Fundo de Combate à Pobreza (FCP) vinculado à operação de substituição tributária, na combinação de CST_ICMS, CFOP e alíquota do ICMS.


class RegistroC590(Registro):
    CST_ICMS: str  # /// Código da Situação Tributária, conforme a Tabela indicada no item 4.3.1.
    CFOP: str  # /// Código Fiscal de Operação e Prestação do agrupamento de itens
    ALIQ_ICMS: Decimal  # /// Alíquota do ICMS
    VL_OPR: Decimal  # /// Valor da operação correspondente à combinação de CST_ICMS, CFOP, e alíquota do ICMS.
    VL_BC_ICMS: Decimal  # /// Parcela correspondente ao "Valor da base de cálculo do ICMS" referente à combinação de CST_ICMS, CFOP e alíquota do ICMS.
    VL_ICMS: Decimal  # /// Parcela correspondente ao "Valor do ICMS" referente à combinação de CST_ICMS, CFOP e alíquota do ICMS.
    VL_BC_ICMS_ST: Decimal  # /// Parcela correspondente ao "Valor da base de cálculo do ICMS" da substituição tributária referente à combinação de CST_ICMS, CFOP e alíquota do ICMS.
    VL_ICMS_ST: Decimal  # /// Parcela correspondente ao valor creditado/debitado do ICMS da substituição tributária, referente à combinação de CST_ICMS,  CFOP, e alíquota do ICMS.
    VL_RED_BC: Decimal  # /// Valor não tributado em função da redução da base de cálculo do ICMS, referente à combinação de CST_ICMS, CFOP e alíquota do ICMS.
    COD_OBS: str  # /// Código da observação do lançamento fiscal (campo 02 do Registro 0460)
    RegistroC591: BlockList[RegistroC591]


class RegistroC597(Registro):
    COD_AJ: str  # /// Código do ajustes/benefício/incentivo, conforme tabela indicada no item 5.3.
    DESCR_COMPL_AJ: str  # /// Descrição complementar do ajuste do documento fiscal
    COD_ITEM: str  # /// Código do item (campo 02 do Registro 0200).
    VL_BC_ICMS: Decimal  # /// Base de cálculo do ICMS ou do ICMS ST.
    ALIQ_ICMS: Decimal  # /// Alíquota do ICMS.
    VL_ICMS: Decimal  # /// Valor do ICMS ou do ICMS.
    VL_OUTROS: Decimal  # /// Outros valores.


class RegistroC595(Registro):
    COD_OBS: str  # /// Código da observação do lançamento fiscal (campo 02 do Registro 0460).
    TXT_COMPL: str  # /// Descrição complementar do código de observação.
    RegistroC597: BlockList[RegistroC597]


class RegistroC500(Registro):
    IND_OPER: IndOper  # /// Indicador do tipo de operação: 0 - Entrada; 1- Saída
    IND_EMIT: IndEmit  # /// Indicador do emitente do documento fiscal: 0- Emissão própria; 1- Terceiros
    COD_PART: str  # /// Código do participante (campo 02 do Registro 0150): - do adquirente, no caso das saídas; - do fornecedor no caso de entradas
    COD_MOD: str  # /// Código do modelo do documento fiscal, conforme a Tabela 4.1.1
    COD_SIT: CodSit  # /// Código da situação do documento fiscal, conforme a Tabela 4.1.2
    SER: str  # /// Série do documento fiscal
    SUB: str  # /// Subsérie do documento fiscal
    COD_CONS: str  # /// Código de classe de consumo de energia elétrica, conforme a Tabela 4.4.5 ou Código da classe de consumo de gás canalizado conforme Tabela 4.4.3.
    NUM_DOC: str  # /// Número do documento fiscal
    DT_DOC: date  # /// Data da emissão do documento fiscal
    DT_E_S: date  # /// Data da entrada ou da saída
    VL_DOC: Decimal  # /// Valor total do documento fiscal
    VL_DESC: Decimal  # /// Valor total do desconto
    VL_FORN: Decimal  # /// Valor total fornecido/consumido
    VL_SERV_NT: Decimal  # /// Valor total dos serviços não-tributados pelo ICMS
    VL_TERC: Decimal  # /// Valor total cobrado em nome de terceiros
    VL_DA: Decimal  # /// Valor total de despesas acessórias indicadas no documento fiscal
    VL_BC_ICMS: Decimal  # /// Valor acumulado da base de cálculo do ICMS
    VL_ICMS: Decimal  # /// Valor acumulado do ICMS
    VL_BC_ICMS_ST: Decimal  # /// Valor acumulado da base de cálculo do ICMS substituição tributária
    VL_ICMS_ST: Decimal  # /// Valor acumulado do ICMS retido por substituição tributária
    COD_INF: str  # /// Código da informação complementar do documento fiscal (campo 02 do Registro 0450)
    VL_PIS: Decimal  # /// Valor do PIS
    VL_COFINS: Decimal  # /// Valor da COFINS
    TP_LIGACAO: TpLigacao  # /// Código de tipo de Ligação [ 1 - Monofásico 2 - Bifásico 3 - Trifásico ]
    COD_GRUPO_TENSAO: GrupoTensao  # /// Código de grupo de tensão: Vide Manual Registro C500 Campo 27
    CHV_DOCe: str  # /// Chave da Nota Fiscal de Energia Elétrica Eletrônica
    FIN_DOCe: FinalidadeEmissaoDocumentoEletronico  # /// Finalidade da emissão do documento eletrônico
    CHV_DOCe_REF: str  # /// Chave da nota referenciada.
    IND_DEST: IndicadorDestinatarioAcessante  # /// Indicador do Destinatário/Acessante:
    COD_MUN_DEST: str  # /// Código do município do destinatário conforme a tabela do IBGE.
    COD_CTA: str  # /// Código da conta analítica contábil debitada/creditada
    COD_MOD_DOC_REF: str  # /// Código do modelo do documento fiscal referenciado, conforme a Tabela 4.1.1
    HASH_DOC_REF: str  # /// Código de autenticação digital do registro (Convênio 115/2003).
    SER_DOC_REF: str  # /// Série do documento fiscal referenciado.
    NUM_DOC_REF: str  # /// Número do documento fiscal referenciado.
    MES_DOC_REF: str  # /// Mês e ano da emissão do documento fiscal referenciado.
    ENER_INJET: Decimal  # /// Outras deduções
    OUTRAS_DED: Decimal  # /// Energia injetada
    RegistroC510: BlockList[RegistroC510]  # /// BLOCO C - Lista de RegistroC510 (FILHO)
    RegistroC590: BlockList[RegistroC590]  # /// BLOCO C - Lista de RegistroC590 (FILHO)
    RegistroC595: BlockList[RegistroC595]  # /// BLOCO C - Lista de RegistroC595 (FILHO)


class RegistroC601(Registro):
    NUM_DOC_CANC: str


class RegistroC610(Registro):
    COD_CLASS: str
    COD_ITEM: str
    QTD: float
    UNID: str
    VL_ITEM: Decimal
    VL_DESC: Decimal
    CST_ICMS: str
    CFOP: str
    ALIQ_ICMS: Decimal
    VL_BC_ICMS: Decimal
    VL_ICMS: Decimal
    VL_BC_ICMS_ST: Decimal
    VL_ICMS_ST: Decimal
    VL_PIS: Decimal
    VL_COFINS: Decimal
    COD_CTA: str


class RegistroC690(Registro):
    CST_ICMS: str
    CFOP: str
    ALIQ_ICMS: Decimal
    VL_OPR: Decimal
    VL_BC_ICMS: Decimal
    VL_ICMS: Decimal
    VL_RED_BC: Decimal
    VL_BC_ICMS_ST: Decimal
    VL_ICMS_ST: Decimal
    COD_OBS: str


class RegistroC600(Registro):
    COD_MOD: str  # /// Código do modelo do documento fiscal, conforme a Tabela 4.1.1
    COD_MUN: str  # /// Código do município dos pontos de consumo, conforme a tabela IBGE
    SER: str  # /// Série do documento fiscal
    SUB: str  # /// Subsérie do documento fiscal
    COD_CONS: str  # /// Código de classe de consumo de energia elétrica, conforme a Tabela 4.4.5, ou Código de Consumo de Fornecimento Dágua - Tabela 4.4.2 ou Código da classe de consumo de gás canalizado   conforme Tabela 4.4.3.
    QTD_CONS: int  # /// Quantidade de documentos consolidados neste registro
    QTD_CANC: int  # /// Quantidade de documentos cancelados
    DT_DOC: date  # /// Data dos documentos consolidados
    VL_DOC: Decimal  # /// Valor total dos documentos
    VL_DESC: Decimal  # /// Valor acumulado dos descontos
    CONS: int  # /// Consumo total acumulado, em kWh (Código 06)
    VL_FORN: Decimal  # /// Valor acumulado do fornecimento
    VL_SERV_NT: Decimal  # /// Valor acumulado dos serviços não-tributados pelo ICMS
    VL_TERC: Decimal  # /// Valores cobrados em nome de terceiros
    VL_DA: Decimal  # /// Valor acumulado das despesas acessórias
    VL_BC_ICMS: Decimal  # /// Valor acumulado da base de cálculo do ICMS
    VL_ICMS: Decimal  # /// Valor acumulado do ICMS
    VL_BC_ICMS_ST: Decimal  # /// Valor acumulado da base de cálculo do ICMS substituição tributária
    VL_ICMS_ST: Decimal  # /// Valor acumulado do ICMS retido por substituição tributária
    VL_PIS: Decimal  # /// Valor acumulado do PIS
    VL_COFINS: Decimal  # /// Valor acumulado COFINS
    RegistroC601: BlockList[RegistroC601]
    RegistroC610: BlockList[RegistroC610]
    RegistroC690: BlockList[RegistroC690]


class RegistroC791(Registro):
    UF: str
    VL_BC_ICMS_ST: Decimal
    VL_ICMS_ST: Decimal


class RegistroC790(Registro):
    CST_ICMS: str
    CFOP: str
    ALIQ_ICMS: Decimal
    VL_OPR: Decimal
    VL_BC_ICMS: Decimal
    VL_ICMS: Decimal
    VL_BC_ICMS_ST: Decimal
    VL_ICMS_ST: Decimal
    VL_RED_BC: Decimal
    COD_OBS: str
    RegistroC791: BlockList[RegistroC791]  # /// Código da observação do lançamento fiscal (campo 02 do Registro 0460)


class RegistroC700(Registro):
    COD_MOD: str  # /// Código do modelo d documento fiscal, conforme a Tabela 4.1.1
    SER: str  # /// Série do documento fiscal
    NRO_ORD_INI: int  # /// Número de ordem inicial
    NRO_ORD_FIN: int  # /// Número de ordem final
    DT_DOC_INI: date  # /// Data de emissão inicial dos documentos
    DT_DOC_FIN: date  # /// Data de emissão final dos documentos
    NOM_MEST: str  # /// Nome do arquivo Mestre de Documento Fiscal
    CHV_COD_DIG: str  # /// Chave de codificação digital do arquivo Mestre de Documento Fiscal
    RegistroC790: BlockList[RegistroC790]


class RegistroC815(Registro):
    COD_MOT_REST_COMPL: str
    QUANT_CONV: Decimal
    UNID: str
    VL_UNIT_CONV: Decimal
    VL_UNIT_ICMS_NA_OPERACAO_CONV: Decimal
    VL_UNIT_ICMS_OP_CONV: Decimal
    VL_UNIT_ICMS_OP_ESTOQUE_CONV: Decimal
    VL_UNIT_ICMS_ST_ESTOQUE_CONV: Decimal
    VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV: Decimal
    VL_UNIT_ICMS_ST_CONV_REST: Decimal
    VL_UNIT_FCP_ST_CONV_REST: Decimal
    VL_UNIT_ICMS_ST_CONV_COMPL: Decimal
    VL_UNIT_FCP_ST_CONV_COMPL: Decimal


class RegistroC810(Registro):
    NUM_ITEM: str
    COD_ITEM: str
    QTD: Decimal
    UNID: str
    VL_ITEM: Decimal
    CST_ICMS: str
    CFOP: str
    RegistroC815: RegistroC815


class RegistroC850(Registro):
    CST_ICMS: str
    CFOP: str
    ALIQ_ICMS: Decimal
    VL_OPR: Decimal
    VL_BC_ICMS: Decimal
    VL_ICMS: Decimal
    COD_OBS: str


class RegistroC857(Registro):
    COD_AJ: str  # // Código do ajustes/benefício/incentivo
    DESCR_COMPL_AJ: str  # // Descrição complementar do ajuste do documento fiscal
    COD_ITEM: str  # // Código do item
    VL_BC_ICMS: Decimal  # // Base de cálculo do ICMS
    ALIQ_ICMS: Decimal  # // Alíquota do ICMS
    VL_ICMS: Decimal  # // Valor do ICMS
    VL_OUTROS: Decimal  # // Outros valores


class RegistroC855(Registro):
    COD_OBS: str  # // Código da observação do lançamento fiscal (campo 02 do Registro 0460)
    TXT_COMPL: str  # // Descrição complementar do código de observação.
    RegistroC857: BlockList[RegistroC857]


class RegistroC800(Registro):
    COD_MOD: str
    COD_SIT: CodSit
    NUM_CFE: str
    DT_DOC: date
    VL_CFE: Decimal
    VL_PIS: Decimal
    VL_COFINS: Decimal
    CNPJ_CPF: str
    NR_SAT: str
    CHV_CFE: str
    VL_DESC: Decimal
    VL_MERC: Decimal
    VL_OUT_DA: Decimal
    VL_ICMS: Decimal
    VL_PIS_ST: Decimal
    VL_COFINS_ST: Decimal
    RegistroC810: BlockList[RegistroC810]
    RegistroC850: BlockList[RegistroC850]  # /// BLOCO C - Lista de RegistroC850 (FILHO)
    RegistroC855: BlockList[RegistroC855]


class RegistroC880(Registro):
    COD_MOT_REST_COMPL: str
    QUANT_CONV: Decimal
    UNID: str
    VL_UNIT_CONV: Decimal
    VL_UNIT_ICMS_NA_OPERACAO_CONV: Decimal
    VL_UNIT_ICMS_OP_CONV: Decimal
    VL_UNIT_ICMS_OP_ESTOQUE_CONV: Decimal
    VL_UNIT_ICMS_ST_ESTOQUE_CONV: Decimal
    VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV: Decimal
    VL_UNIT_ICMS_ST_CONV_REST: Decimal
    VL_UNIT_FCP_ST_CONV_REST: Decimal
    VL_UNIT_ICMS_ST_CONV_COMPL: Decimal
    VL_UNIT_FCP_ST_CONV_COMPL: Decimal


class RegistroC870(Registro):
    COD_ITEM: str
    QTD: Decimal
    UNID: str
    CST_ICMS: str
    CFOP: str
    RegistroC880: RegistroC880


class RegistroC890(Registro):
    CST_ICMS: str
    CFOP: str
    ALIQ_ICMS: Decimal
    VL_OPR: Decimal
    VL_BC_ICMS: Decimal
    VL_ICMS: Decimal
    COD_OBS: str


class RegistroC897(Registro):
    COD_AJ: str  # // Código do ajustes/benefício/incentivo
    DESCR_COMPL_AJ: str  # // Descrição complementar do ajuste do documento fiscal
    COD_ITEM: str  # // Código do item
    VL_BC_ICMS: Decimal  # // Base de cálculo do ICMS
    ALIQ_ICMS: Decimal  # // Alíquota do ICMS
    VL_ICMS: Decimal  # // Valor do ICMS
    VL_OUTROS: Decimal  # // Outros valores


class RegistroC895(Registro):
    COD_OBS: str  # // Código da observação do lançamento fiscal (campo 02 do Registro 0460)
    TXT_COMPL: str  # // Descrição complementar do código de observação.
    RegistroC897: BlockList[RegistroC897]


class RegistroC860(Registro):
    COD_MOD: str
    NR_SAT: str
    DT_DOC: date
    DOC_INI: str  # /// Número do documento inicial
    DOC_FIN: str  # /// Número do documento final
    RegistroC870: BlockList[RegistroC870]
    RegistroC890: BlockList[RegistroC890]  # /// BLOCO C - Lista de RegistroC890 (FILHO)
    RegistroC895: BlockList[RegistroC895]


class RegistroC001(BlocoInicial):
    RegistroC100: BlockList[RegistroC100]
    RegistroC300: BlockList[RegistroC300]
    RegistroC350: BlockList[RegistroC350]
    RegistroC400: BlockList[RegistroC400]
    RegistroC495: BlockList[RegistroC495]
    RegistroC500: BlockList[RegistroC500]
    RegistroC600: BlockList[RegistroC600]
    RegistroC700: BlockList[RegistroC700]
    RegistroC800: BlockList[RegistroC800]
    RegistroC860: BlockList[RegistroC860]


class RegistroC990(Registro):
    QTD_LIN_C: int  # /// Quantidade total de linhas do Bloco C


class Registro0000(Registro):
    COD_VER: VersaoLeiauteSPEDFiscal
    COD_FIN: CodFin
    DT_INI: date
    DT_FIN: date
    NOME: str
    CNPJ: str
    CPF: str
    UF: str
    IE: str
    COD_MUN: int
    IM: str
    SUFRAMA: str
    IND_PERFIL: IndPerfil
    IND_ATIV: IndAtiv


class Registro0005(Registro):
    FANTASIA: str  # /// Nome de fantasia associado:
    CEP: str
    END: str
    NUM: str
    COMPL: str
    BAIRRO: str
    FONE: str
    FAX: str
    EMAIL: str


class Registro0015(Registro):
    UF_ST: str
    IE_ST: str


class Registro0100(Registro):
    NOME: str
    CPF: str
    CRC: str
    CNPJ: str
    CEP: str
    ENDERECO: str
    NUM: str
    COMPL: str
    BAIRRO: str
    FONE: str
    FAX: str
    EMAIL: str
    COD_MUN: int


class Registro0175(Registro):
    DT_ALT: date
    NR_CAMPO: str
    CONT_ANT: str


class Registro0150(Registro):
    COD_PART: str
    NOME: str
    COD_PAIS: str
    CNPJ: str
    CPF: str
    IE: str
    COD_MUN: int
    SUFRAMA: str
    END: str
    NUM: str
    COMPL: str
    BAIRRO: str
    Registro0175: BlockList[Registro0175]  # /// BLOCO C - Lista de Registro0175 (FILHO)


class Registro0190(Registro):
    UNID: str
    DESCR: str


class Registro0205(Registro):
    DESCR_ANT_ITEM: str
    DT_INI: date
    DT_FIN: date
    COD_ANT_ITEM: str


class Registro0206(Registro):
    COD_COMB: str


class Registro0210(Registro):
    COD_ITEM_COMP: str
    QTD_COMP: float
    PERDA: float


class Registro0220(Registro):
    UNID_CONV: str
    FAT_CONV: float
    COD_BARRA: str  # ///   Representação alfanumérica do código de barra da unidade comercial do produto, se houver


class Registro0221(Registro):
    COD_ITEM_ATOMICO: str  # /// Informar o código do item atômico contido no item informado no 0200 Pai.
    QTDE_CONTIDA: float  # /// Informar quantos itens atômicos estão contidos no item informado no 0200 Pai.


class Registro0200(Registro):
    COD_ITEM: str
    DESCR_ITEM: str
    COD_BARRA: str
    COD_ANT_ITEM: str
    UNID_INV: str
    TIPO_ITEM: TipoItem
    COD_NCM: str
    EX_IPI: str
    COD_GEN: str
    COD_LST: str
    ALIQ_ICMS: Decimal
    CEST: str
    Registro0205: BlockList[Registro0205]  # /// BLOCO 0 - Lista de Registro0205 (FILHO)
    Registro0206: BlockList[Registro0206]  # /// BLOCO 0 - Lista de Registro0206 (FILHO)
    Registro0210: BlockList[Registro0210]
    Registro0220: BlockList[Registro0220]  # /// BLOCO 0 - Lista de Registro0220 (FILHO)
    Registro0221: BlockList[Registro0221]  # /// BLOCO 0 - Lista de Registro0221 (FILHO)


class Registro0305(Registro):
    COD_CCUS: str  # /// Código do centro de custo onde o bem está sendo ou será utilizado (campo 03 do Registro 0600)
    FUNC: str  # /// Descrição sucinta da função do bem na atividade do estabelecimento
    VIDA_UTIL: int  # /// Vida útil estimada do bem, em número de meses


class Registro0300(Registro):
    COD_IND_BEM: str  # /// Código individualizado do bem ou componente adotado no controle patrimonial do estabelecimento informante
    IDENT_MERC: int  # /// Identificação do tipo de mercadoria: 1 = bem; 2 = componente.
    DESCR_ITEM: str  # /// Descrição do bem ou componente (modelo, marca e outras características necessárias a sua individualização)
    COD_PRNC: str  # /// Código de cadastro do bem principal nos casos em que o bem ou componente ( campo 02) esteja vinculado a um bem principal.
    COD_CTA: str  # /// Código da conta analítica de contabilização do bem ou componente (campo 06 do Registro 0500)
    NR_PARC: float  # /// Número total de parcelas a serem apropriadas, segundo a legislação de cada unidade federada
    Registro0305: Registro0305  # /// BLOCO 0 - Registro0305 (FILHO)


class Registro0400(Registro):
    COD_NAT: str
    DESCR_NAT: str


class Registro0450(Registro):
    COD_INF: str
    TXT: str


class Registro0460(Registro):
    COD_OBS: str
    TXT: str


class Registro0500(Registro):
    DT_ALT: date
    COD_NAT_CC: str
    IND_CTA: str
    NIVEL: str
    COD_CTA: str
    NOME_CTA: str


class Registro0600(Registro):
    DT_ALT: date
    COD_CCUS: str
    CCUS: str


class Registro0001(BlocoInicial):
    Registro0005: Registro0005
    Registro0015: BlockList[Registro0015]
    Registro0100: Registro0100
    Registro0150: BlockList[Registro0150]
    Registro0190: BlockList[Registro0190]
    Registro0200: BlockList[Registro0200]
    Registro0300: BlockList[Registro0300]
    Registro0400: BlockList[Registro0400]
    Registro0450: BlockList[Registro0450]
    Registro0460: BlockList[Registro0460]
    Registro0500: BlockList[Registro0500]
    Registro0600: BlockList[Registro0600]


class Registro0002(Registro):
    CLAS_ESTAB_IND: str  # ///Informar a classificação do estabelecimento conforme tabela 4.5.5


class Registro0990(Registro):
    QTD_LIN_0: int  # /// Quantidade total de linhas do Bloco 0


class Bloco_0(BlocoSPED):
    Registro0000: Registro0000  # /// BLOCO 0 - Registro0000
    Registro0001: Registro0001  # /// BLOCO 0 - Registro0001
    Registro0002: Registro0002  # /// BLOCO 0 - Registro0002
    Registro0990: Registro0990  # /// BLOCO 0 - Registro0990
    Registro0005Count: int
    Registro0015Count: int
    Registro0150Count: int
    Registro0175Count: int
    Registro0200Count: int
    Registro0190Count: int
    Registro0205Count: int
    Registro0206Count: int
    Registro0210Count: int
    Registro0220Count: int
    Registro0221Count: int
    Registro0300Count: int
    Registro0305Count: int
    Registro0400Count: int
    Registro0450Count: int
    Registro0460Count: int
    Registro0500Count: int
    Registro0600Count: int


class RegistroG140(Registro):
    NUM_ITEM: str  # /// Numero Sequencial do Item no documento fiscal
    COD_ITEM: str  # /// Codigo Correspondente do bem no documento fiscal
    QTDE: Decimal  # /// Quantidade, deste item da nota fiscal, que foi aplicada neste bem, expressa na mesma unidade constante no documento fiscal de entrada
    UNID: str  # ///Unidade do item constante no documento fiscal de entrada
    VL_ICMS_OP_APLICADO: Decimal  # /// Valor do ICMS da Operação Própria na entrada do item, proporcional à quantidade aplicada no bem ou componente.
    VL_ICMS_ST_APLICADO: Decimal  # /// Valor do ICMS ST na entrada do item, proporcional à quantidade aplicada no bem ou componente.
    VL_ICMS_FRT_APLICADO: Decimal  # /// Valor do ICMS sobre Frete do Conhecimento de Transporte na entrada do item, proporcional à quantidade aplicada no bem ou componente.
    VL_ICMS_DIF_APLICADO: Decimal  # /// Valor do ICMS Diferencial de Alíquota, na entrada do item, proporcional à quantidade aplicada no bem ou componente.


class RegistroG130(Registro):
    IND_EMIT: IndEmit  # /// Código do ajuste da apuração e dedução, conforme a Tabela indicada no item 5.1.1.
    COD_PART: str  # /// Descrição complementar do ajuste da apuração.
    COD_MOD: str  # /// Valor do ajuste da apuração
    SERIE: str
    NUM_DOC: str
    CHV_NFE_CTE: str
    DT_DOC: date
    NUM_DA: str  # /// 09 Número do documento de arrecadação estadual, se houver
    RegistroG140: BlockList[RegistroG140]


class RegistroG126(Registro):
    DT_INI: date
    DT_FIN: date
    NUM_PARC: int
    VL_PARC_PASS: Decimal
    VL_TRIB_OC: Decimal
    VL_TOTAL: Decimal
    IND_PER_SAI: Decimal
    VL_PARC_APROP: Decimal


class RegistroG125(Registro):
    COD_IND_BEM: str  # /// Codigo individualizado do bem ou componente
    DT_MOV: date  # /// Data movimentacao ou saldo inicial
    TIPO_MOV: MovimentoBens  # /// Tipo de movimentacao do bem ou componente
    VL_IMOB_ICMS_OP: Decimal  # /// Valor ICMS Operacao Propria na entrada do bem ou componente
    VL_IMOB_ICMS_ST: Decimal  # /// Valor ICMS Operacao Subst.Trib. na entrada do bem ou componente
    VL_IMOB_ICMS_FRT: Decimal  # /// Valor ICMS Frete CTC na entrada do bem ou componente
    VL_IMOB_ICMS_DIF: Decimal  # /// Valor ICMS Diferencial de Aliquota cfe. Doc. arrecadacao na entrada do bem ou componente
    NUM_PARC: int  # /// Numero da Parcela do ICMS
    VL_PARC_PASS: Decimal  # /// Valor parcela icms passivel de apropriacao
    VL_PARC_APROP: Decimal  # /// Valor da parcela apropriada do ICMS
    RegistroG130: BlockList[RegistroG130]  # /// BLOCO G - Lista de RegistroG130 (FILHO do FILHO)
    RegistroG126: BlockList[RegistroG126]


class RegistroG110(Registro):
    DT_INI: date
    DT_FIN: date
    MODO_CIAP: str  # /// Modelo de CIAP adotado C ou D
    SALDO_IN_ICMS: Decimal  # /// Saldo inicial de ICMS do CIAP Modelo C
    SALDO_FN_ICMS: Decimal  # /// Saldo Final ICMS do CIAP Modelo C
    SOM_PARC: Decimal  # /// Somatorio das Parcelas ICMS Passivel de Apropriacao Modelo D
    VL_TRIB_EXP: Decimal  # /// Valor do somatorio das saidas tributadas e saidas para exportacao
    VL_TOTAL: Decimal  # /// Valor Total das Saidas
    IND_PER_SAI: Decimal  # /// Participacao percentual do valor do somatorio das saidas tributadas e para exportacao
    ICMS_APROP: Decimal  # /// Parcela de ICMS a ser apropriada no Registro de Apuracao do ICMS
    SOM_ICMS_OC: Decimal  # /// Valor de outros créditos a ser apropriado na Apuração do ICMS, correspondente ao somatório do campo 09 do registro G126
    RegistroG125: BlockList[RegistroG125]  # /// BLOCO G - Lista de RegistroG110 (FILHO fo FILHO)


class RegistroG001(BlocoInicial):
    RegistroG110: BlockList[RegistroG110]


class RegistroG990(Registro):
    QTD_LIN_G: int  # /// Quantidade total de linhas do Bloco H


class Bloco_G(BlocoSPED):
    Bloco_0: Bloco_0
    RegistroG001: RegistroG001  # /// BLOCO G - RegistroG001
    RegistroG990: RegistroG990  # /// BLOCO G - RegistroG990
    RegistroG110Count: int
    RegistroG125Count: int
    RegistroG126Count: int
    RegistroG130Count: int
    RegistroG140Count: int


class EventsBloco_D:
    pass


class RegistroD101(Registro):
    VL_FCP_UF_DEST: Decimal  # /// VALOR TOTAL FUNDO DE COMBATE A POBREZA
    VL_ICMS_UF_DEST: Decimal  # /// VALOR TOTAL DO ICMS DA UF DE DESTINO
    VL_ICMS_UF_REM: Decimal  # /// VALOR TOTAL DO ICMS DA UF DE ORIGEM


class RegistroD120(Registro):
    COD_MUN_ORIG: str  # // Código do município de origem do serviço, conforme a tabela IBGE
    COD_MUN_DEST: str  # // Código do município de destino, conforme a tabela IBGE
    VEIC_ID: str  # // Placa de identificação do veículo
    UF_ID: str  # // Sigla da UF da placa do veículo


class RegistroD110(Registro):
    NUN_ITEM: int
    COD_ITEM: str
    VL_SERV: Decimal
    VL_OUT: Decimal
    RegistroD120: BlockList[RegistroD120]


class RegistroD130(Registro):
    COD_PART_CONSG: str
    COD_PART_RED: str
    IND_FRT_RED: TipoFreteRedespacho
    COD_MUN_ORIG: str
    COD_MUN_DEST: str
    VEIC_ID: str
    VL_LIQ_FRT: Decimal
    VL_SEC_CAT: Decimal
    VL_DESP: Decimal
    VL_PEDG: Decimal
    VL_OUT: Decimal
    VL_FRT: Decimal
    UF_ID: str


class RegistroD140(Registro):
    COD_PART_CONSG: str
    COD_MUN_ORIG: str
    COD_MUN_DEST: str
    IND_VEIC: TipoVeiculo
    VEIC_ID: str
    IND_NAV: TipoNavegacao
    VIAGEM: str
    VL_FRT_LIQ: Decimal
    VL_DESP_PORT: Decimal
    VL_DESP_CAR_DESC: Decimal
    VL_OUT: Decimal
    VL_FRT_BRT: Decimal
    VL_FRT_MM: Decimal


class RegistroD150(Registro):
    COD_MUN_ORIG: str
    COD_MUN_DEST: str
    VEIC_ID: str
    VIAGEM: str
    IND_TFA: TipoTarifa
    VL_PESO_TX: Decimal
    VL_TX_TERR: Decimal
    VL_TX_RED: Decimal
    VL_OUT: Decimal
    VL_TX_ADV: Decimal


class RegistroD161(Registro):
    IND_CARGA: TipoTransporte
    CNPJ_COL: str
    IE_COL: str
    COD_MUN_COL: str
    CNPJ_ENTG: str
    IE_ENTG: str
    COD_MUN_ENTG: str


class RegistroD162(Registro):
    COD_MOD: str
    SER: str  # /// Série do documento
    NUM_DOC: str  # /// Numero
    DT_DOC: date  # /// Data de emissão
    VL_DOC: Decimal  # /// Valor total do documento fiscal
    VL_MERC: Decimal  # /// Valor das mercadorias constantes no documento fiscal
    QTD_VOL: int  # /// Quantidade de volumes transportados
    PESO_BRT: Decimal  # /// Peso bruto
    PESO_LIQ: Decimal  # /// Peso liquido


class RegistroD160(Registro):
    DESPACHO: str  # /// Identificação do número do despacho
    CNPJ_CPF_REM: str  # /// CNPJ ou CPF do remetente das mercadorias que constam na nota fiscal.
    IE_REM: str  # /// Inscrição Estadual do remetente das mercadorias que constam na nota fiscal.
    COD_MUN_ORI: str  # /// Código do Município de origem, conforme tabela IBGE
    CNPJ_CPF_DEST: str  # /// CNPJ ou CPF do destinatário das mercadorias que constam na nota fiscal.
    IE_DEST: str  # /// Inscrição Estadual do destinatário das mercadorias que constam na nota fiscal.
    COD_MUN_DEST: str  # /// Código do Município de destino, conforme tabela IBGE
    RegistroD161: BlockList[RegistroD161]
    RegistroD162: BlockList[RegistroD162]


class RegistroD170(Registro):
    COD_PART_CONSG: str
    COD_PART_RED: str
    COD_MUN_ORIG: str
    COD_MUN_DEST: str
    OTM: str
    IND_NAT_FRT: NaturezaFrete
    VL_LIQ_FRT: Decimal
    VL_GRIS: Decimal
    VL_PDG: Decimal
    VL_OUT: Decimal
    VL_FRT: Decimal
    VEIC_ID: str
    UF_ID: str


class RegistroD180(Registro):
    NUM_SEQ: str
    IND_EMIT: IndEmit
    CNPJ_EMIT: str
    UF_EMIT: str
    IE_EMIT: str
    COD_MUN_ORIG: str
    CNPJ_CPF_TOM: str
    UF_TOM: str
    IE_TOM: str
    COD_MUN_DEST: str
    COD_MOD: str
    SER: str
    SUB: str
    NUM_DOC: str
    DT_DOC: date
    VL_DOC: Decimal


class RegistroD190(Registro):
    CST_ICMS: str
    CFOP: str
    ALIQ_ICMS: Decimal
    VL_OPR: Decimal
    VL_BC_ICMS: Decimal
    VL_ICMS: Decimal
    VL_RED_BC: Decimal
    COD_OBS: str


class RegistroD197(Registro):
    COD_AJ: str
    DESCR_COMPL_AJ: str
    COD_ITEM: str
    VL_BC_ICMS: Decimal
    ALIQ_ICMS: Decimal
    VL_ICMS: Decimal
    VL_OUTROS: Decimal


class RegistroD195(Registro):
    COD_OBS: str
    TXT_COMPL: str
    RegistroD197: BlockList[RegistroD197]


class RegistroD100(Registro):
    IND_OPER: IndOper
    IND_EMIT: IndEmit
    COD_PART: str
    COD_MOD: str
    COD_SIT: CodSit
    SER: str
    SUB: str
    NUM_DOC: str
    CHV_CTE: str
    DT_DOC: date
    DT_A_P: date
    TP_CT_e: str
    CHV_CTE_REF: str
    VL_DOC: Decimal
    VL_DESC: Decimal
    IND_FRT: IndFrt
    VL_SERV: Decimal
    VL_BC_ICMS: Decimal
    VL_ICMS: Decimal
    VL_NT: Decimal
    COD_INF: str
    COD_CTA: str
    COD_MUN_ORIG: str
    COD_MUN_DEST: str
    RegistroD101: BlockList[RegistroD101]
    RegistroD110: BlockList[RegistroD110]
    RegistroD130: BlockList[RegistroD130]
    RegistroD140: BlockList[RegistroD140]
    RegistroD150: BlockList[RegistroD150]
    RegistroD160: BlockList[RegistroD160]
    RegistroD170: BlockList[RegistroD170]
    RegistroD180: BlockList[RegistroD180]
    RegistroD190: BlockList[RegistroD190]  # /// BLOCO D - Lista de RegistroD190 (FILHO)
    RegistroD195: BlockList[RegistroD195]


class RegistroD301(Registro):
    NUM_DOC_CANC: str


class RegistroD310(Registro):
    COD_MUN_ORIG: str
    VL_SERV: Decimal
    VL_BC_ICMS: Decimal
    VL_ICMS: Decimal


class RegistroD300(Registro):
    COD_MOD: str
    SER: str
    SUB: str
    NUM_DOC_INI: str
    NUM_DOC_FIN: str
    CST_ICMS: str
    CFOP: str
    ALIQ_ICMS: Decimal
    DT_DOC: date
    VL_OPR: Decimal
    VL_DESC: Decimal
    VL_SERV: Decimal
    VL_SEG: Decimal
    VL_OUT_DESP: Decimal
    VL_BC_ICMS: Decimal
    VL_ICMS: Decimal
    VL_RED_BC: Decimal
    COD_OBS: str
    COD_CTA: str
    RegistroD301: BlockList[RegistroD301]
    RegistroD310: BlockList[RegistroD310]


class RegistroD360(Registro):
    VL_PIS: Decimal
    VL_COFINS: Decimal


class RegistroD370(Registro):
    COD_MUN_ORIG: str
    VL_SERV: Decimal
    QTD_BILH: int
    VL_BC_ICMS: Decimal
    VL_ICMS: Decimal


class RegistroD365(Registro):
    COD_TOT_PAR: str
    VLR_ACUM_TOT: Decimal
    NR_TOT: str
    DESCR_NR_TOT: str
    RegistroD370: BlockList[RegistroD370]


class RegistroD390(Registro):
    CST_ICMS: str
    CFOP: str
    ALIQ_ICMS: Decimal
    VL_OPR: Decimal
    VL_BC_ISSQN: Decimal
    ALIQ_ISSQN: Decimal
    VL_ISSQN: Decimal
    VL_BC_ICMS: Decimal
    VL_ICMS: Decimal
    COD_OBS: str


class RegistroD355(Registro):
    DT_DOC: date
    CRO: int
    CRZ: int
    NUM_COO_FIN: int
    GT_FIN: Decimal
    VL_BRT: Decimal
    RegistroD360: BlockList[RegistroD360]
    RegistroD365: BlockList[RegistroD365]
    RegistroD390: BlockList[RegistroD390]


class RegistroD350(Registro):
    COD_MOD: str
    ECF_MOD: str
    ECF_FAB: str
    ECF_CX: str
    RegistroD355: BlockList[RegistroD355]


class RegistroD411(Registro):
    NUM_DOC_CANC: str


class RegistroD410(Registro):
    COD_MOD: str
    SER: str
    SUB: str
    NUM_DOC_INI: str
    NUM_DOC_FIN: str
    DT_DOC: date
    CST_ICMS: str
    CFOP: str
    ALIQ_ICMS: Decimal
    VL_OPR: Decimal
    VL_DESC: Decimal
    VL_SERV: Decimal
    VL_BC_ICMS: Decimal
    VL_ICMS: Decimal
    RegistroD411: BlockList[RegistroD411]


class RegistroD420(Registro):
    COD_MUN_ORIG: str
    VL_SERV: Decimal
    VL_BC_ICMS: Decimal
    VL_ICMS: Decimal


class RegistroD400(Registro):
    COD_PART: str
    COD_MOD: str
    COD_SIT: CodSit
    SER: str
    SUB: str
    NUM_DOC: str
    DT_DOC: date
    VL_DOC: Decimal
    VL_DESC: Decimal
    VL_SERV: Decimal
    VL_BC_ICMS: Decimal
    VL_ICMS: Decimal
    VL_PIS: Decimal
    VL_COFINS: Decimal
    COD_CTA: str
    RegistroD410: BlockList[RegistroD410]
    RegistroD420: BlockList[RegistroD420]


class RegistroD510(Registro):
    NUM_ITEM: str  # //Número sequencial do item no documento fiscal
    COD_ITEM: str  # //Código do item (campo 02 do Registro 0200)
    COD_CLASS: str  # //Código de classificação do item do serviço de comunicação ou de telecomunicação, conforme a Tabela 4.4.1
    QTD: Decimal  # //Quantidade do item
    UNID: str  # //Unidade do item (Campo 02 do registro 0190)
    VL_ITEM: Decimal  # //Valor do item
    VL_DESC: Decimal  # //Valor total do desconto
    CST_ICMS: str  # //Código da Situação Tributária, conforme a Tabela indicada no item 4.3.1
    CFOP: str  # //Código Fiscal de Operação e Prestação
    VL_BC_ICMS: Decimal  # //Valor da base de cálculo do ICMS
    ALIQ_ICMS: Decimal  # //Alíquota do ICMS
    VL_ICMS: Decimal  # //Valor do ICMS creditado/debitado
    VL_BC_ICMS_UF: Decimal  # //Valor da base de cálculo do ICMS de outras UFs
    VL_ICMS_UF: Decimal  # //Valor do ICMS de outras UFs
    IND_REC: IndReceita  # //Indicador do tipo de receita
    COD_PART: str  # //Código do participante
    VL_PIS: Decimal  # //Valor do PIS
    VL_COFINS: Decimal  # //Valor da COFINS
    COD_CTA: str  # //Código da conta analítica contábil debitada/creditada


class RegistroD530(Registro):
    IND_SERV: ServicoPrestado  # //Indicador do tipo de serviço prestado
    DT_INI_SERV: date  # //Data em que se iniciou a prestação do serviço
    DT_FIN_SERV: date  # //Data em que se encerrou a prestação do serviço
    PER_FISCAL: str  # //Período fiscal da prestação do serviço (MMAAAA)
    COD_AREA: str  # //Código de área do terminal faturado
    TERMINAL: str  # //Identificação do terminal faturado


class RegistroD590(Registro):
    CST_ICMS: str  # /// Código da Situação Tributária, conforme a Tabela indicada no item 4.3.1.
    CFOP: str  # /// Código Fiscal de Operação e Prestação do agrupamento de itens
    ALIQ_ICMS: Decimal  # /// Alíquota do ICMS
    VL_OPR: Decimal  # /// Valor da operação correspondente à combinação de CST_ICMS, CFOP, e alíquota do ICMS.
    VL_BC_ICMS: Decimal  # /// Parcela correspondente ao "Valor da base de cálculo do ICMS" referente à combinação de CST_ICMS, CFOP e alíquota do ICMS.
    VL_ICMS: Decimal  # /// Parcela correspondente ao "Valor do ICMS" referente à combinação de CST_ICMS, CFOP e alíquota do ICMS.
    VL_BC_ICMS_UF: Decimal  # /// Parcela correspondente ao "Valor da base de cálculo do ICMS" da substituição tributária referente à combinação de CST_ICMS, CFOP e alíquota do ICMS.
    VL_ICMS_UF: Decimal  # /// Parcela correspondente ao valor creditado/debitado do ICMS da substituição tributária, referente à combinação de CST_ICMS,  CFOP, e alíquota do ICMS.
    VL_RED_BC: Decimal  # /// Valor não tributado em função da redução da base de cálculo do ICMS, referente à combinação de CST_ICMS, CFOP e alíquota do ICMS.
    COD_OBS: str  # /// Código da observação do lançamento fiscal (campo 02 do Registro 0460)


class RegistroD500(Registro):
    IND_OPER: IndOper
    IND_EMIT: IndEmit
    COD_PART: str
    COD_MOD: str
    COD_SIT: CodSit
    SER: str
    SUB: str
    NUM_DOC: str
    DT_DOC: date
    DT_A_P: date
    VL_DOC: Decimal
    VL_DESC: Decimal
    VL_SERV: Decimal
    VL_SERV_NT: Decimal
    VL_TERC: Decimal
    VL_DA: Decimal
    VL_BC_ICMS: Decimal
    VL_ICMS: Decimal
    COD_INF: str
    VL_PIS: Decimal
    VL_COFINS: Decimal
    COD_CTA: str
    TP_ASSINANTE: TpAssinante
    RegistroD510: BlockList[RegistroD510]
    RegistroD530: BlockList[RegistroD530]
    RegistroD590: BlockList[RegistroD590]  # /// BLOCO D - Lista de RegistroD590 (FILHO) {Jean Barreiros 04Dez2009}


class RegistroD610(Registro):
    pass


class RegistroD690(Registro):
    pass


class RegistroD600(Registro):
    RegistroD610: BlockList[RegistroD610]
    RegistroD690: BlockList[RegistroD690]


class RegistroD697(Registro):
    UF: str  # /// Sigla da unidade da federação
    VL_BC_ICMS: Decimal  # /// Valor da base de cálculo do ICMS
    VL_ICMS: Decimal  # /// Valor do ICMS


class RegistroD696(Registro):
    CST_ICMS: str  # /// Código da Situação Tributária, conforme a Tabela indicada no item 4.3.1.
    CFOP: str  # /// Código Fiscal de Operação e Prestação do agrupamento de itens
    ALIQ_ICMS: Decimal  # /// Alíquota do ICMS
    VL_OPR: Decimal  # /// Valor da operação correspondente à combinação de CST_ICMS, CFOP, e alíquota do ICMS.
    VL_BC_ICMS: Decimal  # /// Parcela correspondente ao "Valor da base de cálculo do ICMS" referente à combinação de CST_ICMS, CFOP e alíquota do ICMS.
    VL_ICMS: Decimal  # /// Parcela correspondente ao "Valor do ICMS" referente à combinação de CST_ICMS, CFOP e alíquota do ICMS.
    VL_BC_ICMS_UF: Decimal  # /// Parcela correspondente ao "Valor da base de cálculo do ICMS" da substituição tributária referente à combinação de CST_ICMS, CFOP e alíquota do ICMS.
    VL_ICMS_UF: Decimal  # /// Parcela correspondente ao valor creditado/debitado do ICMS da substituição tributária, referente à combinação de CST_ICMS,  CFOP, e alíquota do ICMS.
    VL_RED_BC: Decimal  # /// Valor não tributado em função da redução da base de cálculo do ICMS, referente à combinação de CST_ICMS, CFOP e alíquota do ICMS.
    COD_OBS: str  # /// Código da observação do lançamento fiscal (campo 02 do Registro 0460)
    RegistroD697: BlockList[RegistroD697]


class RegistroD695(Registro):
    COD_MOD: str  # // Código do modelo do documento fiscal, conforme a Tabela 4.1.1
    SER: str  # // Série do documento fiscal
    NRO_ORD_INI: int  # // Número de ordem inicial
    NRO_ORD_FIN: int  # // Número de ordem final
    DT_DOC_INI: date  # // Data de emissão inicial dos documentos
    DT_DOC_FIN: date  # // Data de emissão final dos documentos
    NOM_MEST: str  # // Nome do arquivo Mestre de Documento Fiscal
    CHV_COD_DIG: str  # // Chave de codificação digital do arquivo Mestre de Documento Fiscal
    RegistroD696: BlockList[RegistroD696]


class RegistroD731(Registro):
    VL_FCP_OP: Decimal  # // Valor do Fundo de Combate à Pobreza (FCP) vinculado à operação própria, na combinação de CST_ICMS, CFOP e alíquota do ICMS


class RegistroD730(Registro):
    CST_ICMS: str  # // Código da Situação Tributária
    CFOP: str  # // Código Fiscal de Operação e Prestação
    ALIQ_ICMS: Decimal  # // Alíquota do ICMS
    VL_OPR: Decimal  # // Valor da prestação correspondente à combinação de CST_ICMS, CFOP, e alíquota do ICMS, incluídas as despesas acessórias e acréscimos
    VL_BC_ICMS: Decimal  # // Parcela correspondente ao "Valor da base de cálculo do ICMS" referente à combinação CST_ICMS, CFOP, e alíquota do ICMS
    VL_ICMS: Decimal  # // Parcela correspondente ao "Valor do ICMS" referente à combinação CST_ICMS, CFOP, e alíquota do ICMS, incluindo o FCP, quando aplicável, referente à combinação de CST_ICMS, CFOP e alíquota do ICMS
    VL_RED_BC: Decimal  # // Valor não tributado em função da redução da base de cálculo do ICMS, referente à combinação de CST_ICMS, CFOP e alíquota do ICMS
    COD_OBS: str  # // Código da observação
    RegistroD731: BlockList[RegistroD731]


class RegistroD737(Registro):
    COD_AJ: str  # // Código do ajustes/benefício/incentivo
    DESCR_COMPL_AJ: str  # // Descrição complementar do ajuste do documento fiscal
    COD_ITEM: str  # // Código do item
    VL_BC_ICMS: Decimal  # // Base de cálculo do ICMS
    ALIQ_ICMS: Decimal  # // Alíquota do ICMS
    VL_ICMS: Decimal  # // Valor do ICMS
    VL_OUTROS: Decimal  # // Outros valores


class RegistroD735(Registro):
    COD_OBS: str  # // Código da observação do lançamento fiscal
    TXT_COMPL: str  # // Descrição complementar do código de observação.
    RegistroD737: BlockList[RegistroD737]


class RegistroD700(Registro):
    IND_OPER: IndOper  # // Indicador do tipo de prestação
    IND_EMIT: IndEmit  # // Indicador do emitente do documento fiscal
    COD_PART: str  # // Código do participante
    COD_MOD: str  # // Código do modelo do documento fiscal
    COD_SIT: CodSit  # // Código da situação do documento fiscal
    DED: Decimal  # // Deduções
    SER: str  # //
    NUM_DOC: str  # // Número do documento fiscal
    DT_DOC: date  # // Data da emissão do documento fiscal
    DT_E_S: date  # // Data da entrada
    VL_DOC: Decimal  # // Valor do Documento Fiscal
    VL_DESC: Decimal  # // Valor do Desconto
    VL_SERV: Decimal  # // Valor dos serviços tributados pelo ICMS
    VL_SERV_NT: Decimal  # // Valores cobrados em nome do prestador sem destaque de ICMS
    VL_TERC: Decimal  # // Valores cobrados em nome de terceiros
    VL_DA: Decimal  # // Valor de despesas acessórias indicadas no documento fiscal
    VL_BC_ICMS: Decimal  # // Valor da Base de Cálculo (BC) do ICMS
    VL_ICMS: Decimal  # // Valor do ICMS
    COD_INF: str  # // Código da informação complementar do documento fiscal
    VL_PIS: Decimal  # // Valor do Pis/Pasep
    VL_COFINS: Decimal  # // Valor do Cofins
    CHV_DOCe: str  # // Chave da Nota Fiscal Fatura de Serviço de Comunicação Eletrônica
    FIN_DOCe: FinEmissaoFaturaEletronica  # // Finalidade da emissão do documento eletrônico
    TIP_FAT: TipoFaturamentoDocumentoEletronico  # // Tipo de faturamento do documento eletrônico
    COD_MOD_DOC_REF: str  # // Código do modelo do documento fiscal referenciado
    CHV_DOCe_REF: str  # // Chave da nota referenciada
    HASH_DOC_REF: str  # // Código de autenticação digital do registro
    SER_DOC_REF: str  # // Série do documento fiscal referenciado
    NUM_DOC_REF: str  # // Número do documento fiscal referenciado
    MES_DOC_REF: str  # // Mês e ano da emissão do documento fiscal referenciado
    COD_MUN_DEST: str  # // Código do município do destinatário conforme a tabela do IBGE
    RegistroD730: BlockList[RegistroD730]
    RegistroD735: BlockList[RegistroD735]


class RegistroD761(Registro):
    VL_FCP_OP: Decimal  # // Valor do Fundo de Combate à Pobreza (FCP) vinculado à operação própria, na combinação de CST_ICMS, CFOP e alíquota do ICMS


class RegistroD760(Registro):
    CST_ICMS: str
    CFOP: str
    ALIQ_ICMS: Decimal
    VL_OPR: Decimal
    VL_BC_ICMS: Decimal
    VL_ICMS: Decimal
    VL_RED_BC: Decimal
    COD_OBS: str
    RegistroD761: BlockList[RegistroD761]


class RegistroD750(Registro):
    COD_MOD: str  # // Código do modelo do documento fiscal
    DED: Decimal  # // Deduções
    SER: str  # // Série do documento fiscal
    DT_DOC: date  # // Data da emissão dos documentos
    QTD_CONS: Decimal  # // Quantidade de documentos consolidados neste registro
    IND_PREPAGO: IndicadorFormaPagto  # // Forma de pagamento
    VL_DOC: Decimal  # // Valor total dos documentos
    VL_SERV: Decimal  # // Valor total dos descontos
    VL_SERV_NT: Decimal  # // Valores cobrados em nome do prestador sem destaque de ICMS
    VL_TERC: Decimal  # // Valor total cobrado em nome de terceiros
    VL_DESC: Decimal  # // Valor total dos descontos
    VL_DA: Decimal  # // Valor total das despesas acessórias
    VL_BC_ICMS: Decimal  # // Valor total da base de cálculo do ICMS
    VL_ICMS: Decimal  # // Valor total do ICMS
    VL_PIS: Decimal  # // Valor total do PIS
    VL_COFINS: Decimal  # // Valor total do COFINS
    RegistroD760: BlockList[RegistroD760]


class RegistroD001(BlocoInicial):
    RegistroD100: BlockList[RegistroD100]
    RegistroD300: BlockList[RegistroD300]
    RegistroD350: BlockList[RegistroD350]
    RegistroD400: BlockList[RegistroD400]
    RegistroD500: BlockList[RegistroD500]
    RegistroD600: BlockList[RegistroD600]
    RegistroD695: BlockList[RegistroD695]
    RegistroD700: BlockList[RegistroD700]
    RegistroD750: BlockList[RegistroD750]


class RegistroD990(Registro):
    QTD_LIN_D: int  # /// Quantidade total de linhas do Bloco D


class RegistroE112(Registro):
    NUM_DA: str  # /// Número do documento de arrecadação estadual, se houver
    NUM_PROC: str  # /// Número do processo ao qual o ajuste está vinculado, se houver
    IND_PROC: OrigemProcesso  # /// Indicador da origem do processo: 0- Sefaz; 1- Justiça Federal; 2- Justiça Estadual; 9- Outros
    PROC: str  # /// Descrição resumida do processo que embasou o lançamento
    TXT_COMPL: str  # /// Código de referência à observação (campo 02 do Registro 0460)


class RegistroE113(Registro):
    COD_PART: str  # /// Código do participante (campo 02 do Registro 0150): Do emitente do documento ou do remetente das mercadorias, no caso de entradas; Do adquirente, no caso de saídas
    COD_MOD: str  # /// Código do modelo do documento fiscal, conforme a Tabela 4.1.1
    SER: str  # /// Série do documento fiscal
    SUB: str  # /// Subserie do documento fiscal
    NUM_DOC: str  # /// Número do documento fiscal
    DT_DOC: date  # /// Data da emissão do documento fiscal
    CHV_NFE: str  # /// Chave da Nota Fiscal Eletrônica - Versões abaixo de 004
    COD_ITEM: str  # /// Código do item (campo 02 do Registro 0200)
    VL_AJ_ITEM: Decimal  # /// Valor do ajuste para a operação/item


class RegistroE111(Registro):
    COD_AJ_APUR: str  # /// Código do ajuste da apuração e dedução, conforme a Tabela indicada no item 5.1.1.
    DESCR_COMPL_AJ: str  # /// Descrição complementar do ajuste da apuração.
    VL_AJ_APUR: Decimal  # /// Valor do ajuste da apuração
    RegistroE112: BlockList[RegistroE112]
    RegistroE113: BlockList[RegistroE113]


class RegistroE115(Registro):
    COD_INF_ADIC: str  # /// Código da informação adicional conforme tabela a ser definida pelas SEFAZ, conforme tabela definida no item 5.2.
    VL_INF_ADIC: Decimal  # /// Valor referente à informação adicional
    DESCR_COMPL_AJ: str  # /// Descrição complementar do ajuste


class RegistroE116(Registro):
    COD_OR: str  # /// Código da obrigação a recolher, conforme a Tabela 5.4
    VL_OR: Decimal  # /// Valor da obrigação a recolher
    DT_VCTO: date  # /// Data de vencimento da obrigação
    COD_REC: str  # /// Código de receita referente à obrigação, próprio da unidade da federação, conforme legislação estadual,
    NUM_PROC: str  # /// Número do processo ou auto de infração ao qual a obrigação está vinculada, se houver.
    IND_PROC: OrigemProcesso  # /// Indicador da origem do processo: 0- Sefaz; 1- Justiça Federal; 2- Justiça Estadual; 9- Outros
    PROC: str  # /// Descrição resumida do processo que embasou o lançamento
    TXT_COMPL: str  # /// Descrição complementar das obrigações a recolher.
    MES_REF: str  # /// VERSÃO 103 : Informe o mês de referência no formato mmaaaa


class RegistroE110(Registro):
    VL_TOT_DEBITOS: Decimal  # /// Valor total dos débitos por "Saídas e prestações com débito do imposto"
    VL_AJ_DEBITOS: Decimal  # /// Valor total dos ajustes a débito decorrentes do documento fiscal.
    VL_TOT_AJ_DEBITOS: Decimal  # /// Valor total de "Ajustes a débito"
    VL_ESTORNOS_CRED: Decimal  # /// Valor total de Ajustes Estornos de créditos
    VL_TOT_CREDITOS: Decimal  # /// Valor total dos créditos por "Entradas e aquisições com crédito do imposto"
    VL_AJ_CREDITOS: Decimal  # /// Valor total dos ajustes a crédito decorrentes do documento fiscal.
    VL_TOT_AJ_CREDITOS: Decimal  # /// Valor total de "Ajustes a crédito"
    VL_ESTORNOS_DEB: Decimal  # /// Valor total de Ajustes Estornos de Débitos
    VL_SLD_CREDOR_ANT: Decimal  # /// Valor total de "Saldo credor do período anterior"
    VL_SLD_APURADO: Decimal  # /// Valor total de "Saldo devedor (02+03+04+05-06-07-08-09-10) antes das deduções"
    VL_TOT_DED: Decimal  # /// Valor total de "Deduções"
    VL_ICMS_RECOLHER: Decimal  # /// Valor total de "ICMS a recolher (11-12)
    VL_SLD_CREDOR_TRANSPORTAR: Decimal  # /// Valor total de "Saldo credor a transportar para o período seguinte
    DEB_ESP: Decimal  # /// Valores recolhidos ou a recolher, extra-apuração.
    RegistroE111: BlockList[RegistroE111]
    RegistroE115: BlockList[RegistroE115]
    RegistroE116: BlockList[RegistroE116]


class RegistroE100(Registro):
    DT_INI: date
    DT_FIN: date
    RegistroE110: RegistroE110


class RegistroE230(Registro):
    NUM_DA: str  # /// Número do documento de arrecadação estadual, se houver
    NUM_PROC: str  # /// Número do processo ao qual o ajuste está vinculado, se houver
    IND_PROC: OrigemProcesso  # /// Indicador da origem do processo: 0- Sefaz; 1- Justiça Federal; 2- Justiça Estadual; 9- Outros
    PROC: str  # /// Descrição resumida do processo que embasou o lançamento
    TXT_COMPL: str  # /// Código de referência à observação (campo 02 do Registro 0460)


class RegistroE240(Registro):
    COD_PART: str  # /// Código do participante (campo 02 do Registro 0150): Do emitente do documento ou do remetente das mercadorias, no caso de entradas; Do adquirente, no caso de saídas
    COD_MOD: str  # /// Código do modelo do documento fiscal, conforme a Tabela 4.1.1
    SER: str  # /// Série do documento fiscal
    SUB: str  # /// Subserie do documento fiscal
    NUM_DOC: str  # /// Número do documento fiscal
    DT_DOC: date  # /// Data da emissão do documento fiscal
    CHV_NFE: str  # /// Chave da Nota Fiscal Eletrônica
    COD_ITEM: str  # /// Código do item (campo 02 do Registro 0200)
    VL_AJ_ITEM: Decimal  # /// Valor do ajuste para a operação/item


class RegistroE220(Registro):
    COD_AJ_APUR: str  # /// Código do ajuste da apuração e dedução, conforme a Tabela indicada no item 5.1.1
    DESCR_COMPL_AJ: str  # /// Descrição complementar do ajuste da apuração
    VL_AJ_APUR: Decimal  # /// Valor do ajuste da apuração
    RegistroE230: BlockList[RegistroE230]
    RegistroE240: BlockList[RegistroE240]


class RegistroE250(Registro):
    COD_OR: str  # /// Código da obrigação a recolher, conforme a Tabela 5.4
    VL_OR: Decimal  # /// Valor da obrigação ICMS ST a recolher
    DT_VCTO: date  # /// Data de vencimento da obrigação
    COD_REC: str  # /// Código de receita referente à obrigação, próprio da unidade da federação
    NUM_PROC: str  # /// Número do processo ou auto de infração ao qual a obrigação está vinculada, se houver
    IND_PROC: OrigemProcesso  # /// Indicador da origem do processo: 0- Sefaz; 1- Justiça Federal; 2- Justiça Estadual; 9- Outros
    PROC: str  # /// Descrição resumida do processo que embasou o lançamento
    TXT_COMPL: str  # /// Descrição complementar das obrigações a recolher
    MES_REF: str  # /// VERSÃO 103 : Informe o mês de referência no formato mmaaaa


class RegistroE210(Registro):
    IND_MOV_ST: MovimentoST  # /// Indicador de movimento: 0 - Sem operações com ST 1 - Com operações de ST
    VL_SLD_CRED_ANT_ST: Decimal  # /// Valor do "Saldo credor de período anterior - Substituição Tributária"
    VL_DEVOL_ST: Decimal  # /// Valor total do ICMS ST de devolução de mercadorias
    VL_RESSARC_ST: Decimal  # /// Valor total do ICMS ST de ressarcimentos
    VL_OUT_CRED_ST: Decimal  # /// Valor total de Ajustes "Outros créditos ST" e Estorno de débitos ST
    VL_AJ_CREDITOS_ST: Decimal  # /// Valor total dos ajustes a crédito de ICMS ST, provenientes de ajustes do documento fiscal.
    VL_RETENCAO_ST: Decimal  # /// Valor Total do ICMS retido por Substituição Tributária
    VL_OUT_DEB_ST: Decimal  # /// Valor Total dos ajustes "Outros débitos ST" " e Estorno de créditos ST
    VL_AJ_DEBITOS_ST: Decimal  # /// Valor total dos ajustes a débito de ICMS ST, provenientes de ajustes do documento fiscal.
    VL_SLD_DEV_ANT_ST: Decimal  # /// Valor total de "Saldo devedor antes das deduções" = (08+09+10)-(03+04+05+06+07)]
    VL_DEDUCOES_ST: Decimal  # /// Valor total dos ajustes "Deduções ST"
    VL_ICMS_RECOL_ST: Decimal  # /// Imposto a recolher ST (11-12)
    VL_SLD_CRED_ST_TRANSPORTAR: Decimal  # /// Saldo credor de ST a transportar para o período seguinte [(03+04+05+06+07)- (08+09+10)].
    DEB_ESP_ST: Decimal  # /// Valores recolhidos ou a recolher, extra-apuração.
    RegistroE220: BlockList[RegistroE220]
    RegistroE250: BlockList[RegistroE250]


class RegistroE200(Registro):
    UF: str  # /// Sigla da unidade da federação a que se refere a apuração do ICMS ST
    DT_INI: date  # /// Data inicial a que a apuração se refere
    DT_FIN: date  # /// Data final a que a apuração se refere
    RegistroE210: BlockList[RegistroE210]


class RegistroE312(Registro):
    NUM_DA: str  # /// Número do documento de arrecadação estadual, se houver
    NUM_PROC: str  # /// Número do processo ao qual o ajuste está vinculado, se houver
    IND_PROC: OrigemProcesso  # /// Indicador da origem do processo: 0- Sefaz; 1- Justiça Federal; 2- Justiça Estadual; 9- Outros
    PROC: str  # /// Descrição resumida do processo que embasou o lançamento
    TXT_COMPL: str  # /// Descrição Complementar


class RegistroE313(Registro):
    COD_PART: str  # /// Código do participante (campo 02 do Registro 0150): Do emitente do documento ou do remetente das mercadorias, no caso de entradas; Do adquirente, no caso de saídas
    COD_MOD: str  # /// Código do modelo do documento fiscal, conforme a Tabela 4.1.1
    SER: str  # /// Série do documento fiscal
    SUB: str  # /// Subserie do documento fiscal
    NUM_DOC: str  # /// Número do documento fiscal
    CHV_DOCe: str
    DT_DOC: date  # /// Data da emissão do documento fiscal
    COD_ITEM: str  # /// Código do item (campo 02 do Registro 0200)
    VL_AJ_ITEM: Decimal  # /// Valor do ajuste para a operação/item


class RegistroE311(Registro):
    COD_AJ_APUR: str  # /// Código do ajuste da apuração e dedução, conforme a Tabela indicada no item 5.1.1
    DESCR_COMPL_AJ: str  # /// Descrição complementar do ajuste da apuração
    VL_AJ_APUR: Decimal  # /// Valor do ajuste da apuração
    RegistroE312: BlockList[RegistroE312]
    RegistroE313: BlockList[RegistroE313]


class RegistroE316(Registro):
    COD_OR: str  # /// Código da obrigação a recolher, conforme a Tabela 5.4
    VL_OR: Decimal  # /// Valor da obrigação ICMS ST a recolher
    DT_VCTO: date  # /// Data de vencimento da obrigação
    COD_REC: str  # /// Código de receita referente à obrigação, próprio da unidade da federação
    NUM_PROC: str  # /// Número do processo ou auto de infração ao qual a obrigação está vinculada, se houver
    IND_PROC: OrigemProcesso  # /// Indicador da origem do processo: 0- Sefaz; 1- Justiça Federal; 2- Justiça Estadual; 9- Outros
    PROC: str  # /// Descrição resumida do processo que embasou o lançamento
    TXT_COMPL: str  # /// Descrição complementar das obrigações a recolher
    MES_REF: str  # /// Informe o mês de referência no formato mmaaaa


class RegistroE310(Registro):
    IND_MOV_DIFAL: MovimentoDIFAL
    VL_SLD_CRED_ANT_DIF: Decimal
    VL_TOT_DEBITOS_DIFAL: Decimal
    VL_OUT_DEB_DIFAL: Decimal
    VL_TOT_CREDITOS_DIFAL: Decimal
    VL_OUT_CRED_DIFAL: Decimal
    VL_SLD_DEV_ANT_DIFAL: Decimal
    VL_DEDUCOES_DIFAL: Decimal
    DEB_ESP_DIFAL: Decimal
    VL_RECOL_DIFAL: Decimal
    VL_SLD_CRED_TRANSPORTAR_DIFAL: Decimal
    VL_SLD_CRED_ANT_FCP: Decimal
    VL_TOT_DEB_FCP: Decimal
    VL_OUT_DEB_FCP: Decimal
    VL_TOT_CRED_FCP: Decimal
    VL_OUT_CRED_FCP: Decimal
    VL_SLD_DEV_ANT_FCP: Decimal
    VL_DEDUCOES_FCP: Decimal
    VL_RECOL_FCP: Decimal
    VL_SLD_CRED_TRANSPORTAR_FCP: Decimal
    DEB_ESP_FCP: Decimal
    VL_RECOL: Decimal
    VL_SLD_CRED_TRANSPORTAR: Decimal
    RegistroE311: BlockList[RegistroE311]
    RegistroE316: BlockList[RegistroE316]


class RegistroE300(Registro):
    UF: str  # /// Sigla da unidade da federação a que se refere a apuração
    DT_INI: date  # /// Data inicial a que a apuração se refere
    DT_FIN: date  # /// Data final a que a apuração se refere
    RegistroE310: BlockList[RegistroE310]


class RegistroE510(Registro):
    CFOP: str  # /// Código Fiscal de Operação e Prestação do agrupamento de itens
    CST_IPI: str  # /// Código da Situação Tributária referente ao IPI, conforme a Tabela indicada no item 4.3.2.
    VL_CONT_IPI: Decimal  # /// Parcela correspondente ao "Valor Contábil" referente ao CFOP e ao Código de Tributação do IPI
    VL_BC_IPI: Decimal  # /// Parcela correspondente ao "Valor da base de cálculo do IPI" referente ao CFOP e ao Código de Tributação do IPI, para operações tributadas
    VL_IPI: Decimal  # /// Parcela correspondente ao "Valor do IPI" referente ao CFOP e ao Código de Tributação do IPI, para operações tributadas


class RegistroE531(Registro):
    COD_PART: str  # /// Código do participante (campo 02 do Registro 0150): Do emitente do documento ou do remetente das mercadorias, no caso de entradas; Do adquirente, no caso de saídas
    COD_MOD: str  # /// Código do modelo do documento fiscal, conforme a Tabela 4.1.1
    SER: str  # /// Série do documento fiscal
    SUB: str  # /// Subserie do documento fiscal
    NUM_DOC: str  # /// Número do documento fiscal
    DT_DOC: date  # /// Data da emissão do documento fiscal
    CHV_NFE: str  # /// Chave da Nota Fiscal Eletrônica - Versões abaixo de 004
    COD_ITEM: str  # /// Código do item (campo 02 do Registro 0200)
    VL_AJ_ITEM: Decimal  # /// Valor do ajuste para a operação/item


class RegistroE530(Registro):
    IND_AJ: TipoAjuste  # /// Indicador do tipo de ajuste: 0- Ajuste a débito; 1- Ajuste a crédito
    VL_AJ: Decimal  # /// Valor do ajuste
    COD_AJ: str  # /// Código do ajuste da apuração, conforme a Tabela indicada no item 4.5.4.
    IND_DOC: OrigemDocto  # /// Indicador da origem do documento vinculado ao ajuste: 0 - Processo Judicial; 1 - Processo Administrativo; 2 - PER/DCOMP; 9 - Outros.
    NUM_DOC: str  # /// Número do documento / processo / declaração ao qual o ajuste está vinculado, se houver
    DESCR_AJ: str  # /// Descrição resumida do ajuste.
    RegistroE531: BlockList[RegistroE531]


class RegistroE520(Registro):
    VL_SD_ANT_IPI: Decimal  # /// Saldo credor do IPI transferido do período anterior
    VL_DEB_IPI: Decimal  # /// Valor total dos débitos por "Saídas com débito do imposto"
    VL_CRED_IPI: Decimal  # /// Valor total dos créditos por "Entradas e aquisições com crédito do imposto"
    VL_OD_IPI: Decimal  # /// Valor de "Outros débitos" do IPI (inclusive estornos de crédito)
    VL_OC_IPI: Decimal  # /// Valor de "Outros créditos" do IPI (inclusive estornos de débitos)
    VL_SC_IPI: Decimal  # /// Valor do saldo credor do IPI a transportar para o período seguinte
    VL_SD_IPI: Decimal  # /// Valor do saldo devedor do IPI a recolher
    RegistroE530: BlockList[RegistroE530]


class RegistroE500(Registro):
    IND_APUR: ApuracaoIPI  # /// Indicador de período de apuração do IPI: 0 - Mensal; 1 - Decendial
    DT_INI: date  # /// Data inicial a que a apuração se refere
    DT_FIN: date  # /// Data final a que a apuração se refere
    RegistroE510: BlockList[RegistroE510]
    RegistroE520: BlockList[RegistroE520]


class RegistroE001(BlocoInicial):
    RegistroE100: BlockList[RegistroE100]
    RegistroE200: BlockList[RegistroE200]
    RegistroE300: BlockList[RegistroE300]
    RegistroE500: BlockList[RegistroE500]


class RegistroE990(Registro):
    QTD_LIN_E: int  # /// Quantidade total de linhas do Bloco E


class Registro1010(Registro):
    IND_EXP: str  # // Reg. 1100 - Ocorreu averbação (conclusão) de exportação no período:
    IND_CCRF: str  # // Reg. 1200  Existem informações acerca de créditos de ICMS a serem controlados, definidos pela Sefaz:
    IND_COMB: str  # // Reg. 1300  É comercio varejista de combustíveis:
    IND_USINA: str  # // Reg. 1390  Usinas de açúcar e/álcool  O estabelecimento é produtor de açúcar e/ou álcool carburante:
    IND_VA: str  # // Reg. 1400  Existem informações a serem prestadas neste registro e o registro é obrigatório em sua Unidade da Federação:
    IND_EE: str  # // Reg. 1500 - A empresa é distribuidora de energia e ocorreu fornecimento de energia elétrica para consumidores de outra UF:
    IND_CART: str  # // Reg. 1600 ou 1601 - Realizou vendas com Cartão de Crédito ou de débito / instrumentos eletrônicos de pagamento
    IND_FORM: str  # // Reg. 1700 - É obrigatório em sua unidade da federação o controle de utilização de documentos  fiscais em papel:
    IND_AER: str  # // Reg. 1800  A empresa prestou serviços de transporte aéreo de cargas e de passageiros:
    IND_GIAF1: str  # // Reg. 1960  Possui informações GIAF1:
    IND_GIAF3: str  # // Reg. 1970  Possui informações GIAF3:
    IND_GIAF4: str  # // Reg. 1980  Possui informações GIAF4:
    IND_REST_RESSARC_COMPL_ICMS: str  # //Reg. 1250  Possui informações consolidadas de saldos de restituição, ressarcimento e complementação do ICMS?


class Registro1110(Registro):
    COD_PART: str
    COD_MOD: str
    SER: str
    NUM_DOC: str
    DT_DOC: date
    CHV_NFE: str
    NR_MEMO: str
    QTD: float
    UNID: str


class Registro1105(Registro):
    COD_MOD: str
    SERIE: str
    NUM_DOC: str
    CHV_NFE: str
    DT_DOC: date
    COD_ITEM: str
    Registro1110: BlockList[Registro1110]


class Registro1100(Registro):
    IND_DOC: TipoDocto
    NRO_DE: str
    DT_DE: date
    NAT_EXP: Exportacao
    NRO_RE: str
    DT_RE: date
    CHC_EMB: str
    DT_CHC: date
    DT_AVB: date
    TP_CHC: ConhecEmbarque
    PAIS: str
    Registro1105: BlockList[Registro1105]


class Registro1210(Registro):
    TIPO_UTIL: str
    NR_DOC: str
    VL_CRED_UTIL: Decimal
    CHV_DOCe: str


class Registro1200(Registro):
    COD_AJ_APUR: str
    SLD_CRED: Decimal
    CRED_APR: Decimal
    CRED_RECEB: Decimal
    CRED_UTIL: Decimal
    SLD_CRED_FIM: Decimal
    Registro1210: BlockList[Registro1210]


class Registro1255(Registro):
    COD_MOT_REST_COMPL: str  # /// Código do motivo da restituição ou complementação conforme Tabela 5.7.
    VL_CREDITO_ICMS_OP_MOT: Decimal  # /// Informar o valor total do ICMS operação própria que o informante tem direito ao crédito, na forma prevista na legislação, referente às hipóteses de restituição em que há previsão deste crédito, para o mesmo COD_MOT_REST_COMPL.
    VL_ICMS_ST_REST_MOT: Decimal  # /// Informar o valor total do ICMS ST que o informante tem direito ao crédito, na forma prevista na legislação, referente às hipóteses de restituição em que há previsão deste crédito, para o mesmo COD_MOT_REST_COMPL.
    VL_FCP_ST_REST_MOT: Decimal  # /// Informar o valor total do FCP_ST agregado ao valor do ICMS ST informado no campo VL_ICMS_ST_REST_MOT.
    VL_ICMS_ST_COMPL_MOT: Decimal  # /// Informar o valor total do débito referente ao complemento do imposto, nos casos previstos na legislação, para o mesmo COD_MOT_REST_COMPL.
    VL_FCP_ST_COMPL_MOT: Decimal  # /// Informar o valor total do FCP_ST agregado ao valor informado no campo VL_ICMS_ST_COMPL_MOT.


class Registro1250(Registro):
    VL_CREDITO_ICMS_OP: Decimal  # /// Informar o valor total do ICMS operação própria que o informante tem direito ao crédito, na forma prevista na legislação, referente às hipóteses de restituição em que há previsão deste crédito.
    VL_ICMS_ST_REST: Decimal  # /// Informar o valor total do ICMS ST que o informante tem direito ao crédito, na forma prevista na legislação, referente às hipóteses de restituição em que há previsão deste crédito.
    VL_FCP_ST_REST: Decimal  # /// Informar o valor total do FCP_ST agregado ao valor do ICMS ST informado no campo VL_ICMS_ST_REST.
    VL_ICMS_ST_COMPL: Decimal  # /// Informar o valor total do débito referente ao complemento do imposto, nos casos previstos na legislação.
    VL_FCP_ST_COMPL: Decimal  # /// Informar o valor total do FCP_ST agregado ao valor informado no campo VL_ICMS_ST_COMPL.
    Registro1255: BlockList[Registro1255]


class Registro1320(Registro):
    NUM_BICO: str  # /// Bico Ligado à Bomba
    NR_INTERV: str  # /// Número da intervenção
    MOT_INTERV: str  # /// Motivo da Intervenção
    NOM_INTERV: str  # /// Nome do Interventor
    CNPJ_INTERV: str  # /// CNPJ da empresa responsável pela intervenção
    CPF_INTERV: str  # /// CPF do técnico responsável pela intervenção
    VAL_FECHA: float  # /// Valor da leitura final do contador, no fechamento do bico
    VAL_ABERT: float  # /// Valor da leitura inicial do contador, na abertura do bico
    VOL_AFERI: float  # /// Aferições da Bomba, em litros
    VOL_VENDAS: float  # /// Vendas (08  09 - 10 ) do bico, em litros


class Registro1310(Registro):
    NUM_TANQUE: str  # /// Tanque onde foi armazenado o combustível
    ESTQ_ABERT: float  # /// Estoque no inicio do dia, em litros
    VOL_ENTR: float  # /// Volume Recebido no dia (em litros)
    VOL_DISP: float  # /// Volume Disponível (03 + 04), em litros
    VOL_SAIDAS: float  # /// Volume Total das Saídas, em litros
    ESTQ_ESCR: float  # /// Estoque Escritural(05  06), litros
    VAL_AJ_PERDA: float  # /// Valor da Perda, em litros
    VAL_AJ_GANHO: float  # /// Valor do ganho, em litros
    FECH_FISICO: float  # /// Volume aferido no tanque, em litros. Estoque de fechamento físico do tanque
    Registro1320: BlockList[Registro1320]  # /// BLOCO 1 - Lista de Registro1320 (FILHO)


class Registro1300(Registro):
    COD_ITEM: str
    DT_FECH: date
    ESTQ_ABERT: float
    VOL_ENTR: float
    VOL_DISP: float
    VOL_SAIDAS: float
    ESTQ_ESCR: float
    VAL_AJ_PERDA: float
    VAL_AJ_GANHO: float
    FECH_FISICO: float  # /// Volume aferido no tanque, em litros. Estoque de fechamento físico do tanque
    Registro1310: BlockList[Registro1310]  # /// BLOCO 1 - Lista de Registro1310 (FILHO)


class Registro1360(Registro):
    NUM_LACRE: str  # /// Número de Série da Bomba
    DT_APLICACAO: date  # /// Nome do Fabricante da Bomba


class Registro1370(Registro):
    NUM_BICO: str  # /// Número seqüencial do bico ligado a bomba N 003 - O
    COD_ITEM: str  # /// Código do Produto, constante do registro 0200 C 060 - O
    NUM_TANQUE: str  # /// Tanque que armazena o combustível.


class Registro1350(Registro):
    SERIE: str  # /// Número de Série da Bomba
    FABRICANTE: str  # /// Nome do Fabricante da Bomba
    MODELO: str  # /// Modelo da Bomba
    TIPO_MEDICAO: Medicao  # /// Identificador de medição: [ 0 - analógico -  1  digital ]
    Registro1360: BlockList[Registro1360]  # /// BLOCO 1 - Lista de Registro1360 (FILHO)
    Registro1370: BlockList[Registro1370]  # /// BLOCO 1 - Lista de Registro1360 (FILHO)


class Registro1391(Registro):
    DT_REGISTRO: date  # /// Data de produção (DDMMAAAA)
    QTD_MOID: Decimal  # /// Quantidade de cana esmagada (toneladas)
    ESTQ_INI: Decimal  # /// Estoque inicial (litros / Kg)
    QTD_PRODUZ: Decimal  # /// Quantidade produzida (litros / Kg)
    ENT_ANID_HID: Decimal  # /// Entrada de álcool anidro decorrente da transformação do álcool hidratado ou Entrada de álcool hidratado decorrente da transformação do álcool anidro (litros)
    OUTR_ENTR: Decimal  # /// Outras entradas (litros / Kg)
    PERDA: Decimal  # /// Evaporação (litros) ou Quebra de peso (Kg)
    CONS: Decimal  # /// Consumo (litros)
    SAI_ANI_HID: Decimal  # /// Saída para transformação (litros).
    SAIDAS: Decimal  # /// Saídas (litros / Kg)
    ESTQ_FIN: Decimal  # /// Estoque final (litros / Kg)
    ESTQ_INI_MEL: Decimal  # /// Estoque inicial de mel residual (Kg)
    PROD_DIA_MEL: Decimal  # /// Produção de mel residual (Kg) e entradas de mel (Kg)
    UTIL_MEL: Decimal  # /// Mel residual utilizado (Kg) e saídas de mel (Kg)
    PROD_ALC_MEL: Decimal  # /// Produção de álcool (litros) ou açúcar (Kg) proveniente do mel residual.
    OBS: str  # /// Observações
    COD_ITEM: str  # /// Informar o insumo conforme código do item (campo 02 do Registro 0200)
    TP_RESIDUO: int  # /// Tipo de resíduo produzido: 01 - Bagaço de cana
    QTD_RESIDUO: Decimal  # /// Quantidade de resíduo produzido (toneladas)
    QTD_RESIDUO_DDG: Decimal  # /// Quantidade de resíduo produzido de DDG (toneladas)
    QTD_RESIDUO_WDG: Decimal  # /// Quantidade de resíduo produzido de WDG (toneladas)
    QTD_RESIDUO_CANA: Decimal  # /// Quantidade de resíduo produzido de bagaço de cana (toneladas)


class Registro1390(Registro):
    COD_PROD: str  # /// Código do item (campo 02 do Registro 0200)
    Registro1391: BlockList[Registro1391]  # /// REGISTRO 1391: PRODUÇÃO DIÁRIA DA USINA


class Registro1400(Registro):
    COD_ITEM: str
    COD_ITEM_IPM: str
    MUN: str
    VALOR: Decimal


class Registro1510(Registro):
    NUM_ITEM: str
    COD_ITEM: str
    COD_CLASS: str
    QTD: float
    UNID: str
    VL_ITEM: Decimal
    VL_DESC: Decimal
    CST_ICMS: str
    CFOP: str
    VL_BC_ICMS: Decimal
    ALIQ_ICMS: Decimal
    VL_ICMS: Decimal
    VL_BC_ICMS_ST: Decimal
    ALIQ_ST: Decimal
    VL_ICMS_ST: Decimal
    IND_REC: IndReceita
    COD_PART: str
    VL_PIS: Decimal
    VL_COFINS: Decimal
    COD_CTA: str


class Registro1500(Registro):
    IND_OPER: str
    IND_EMIT: str
    COD_PART: str
    COD_MOD: str
    COD_SIT: CodSit
    SER: str
    SUB: str
    COD_CONS: ClasseConsumo
    NUM_DOC: str
    DT_DOC: date
    DT_E_S: date
    VL_DOC: Decimal
    VL_DESC: Decimal
    VL_FORN: Decimal
    VL_SERV_NT: Decimal
    VL_TERC: Decimal
    VL_DA: Decimal
    VL_BC_ICMS: Decimal
    VL_ICMS: Decimal
    VL_BC_ICMS_ST: Decimal
    VL_ICMS_ST: Decimal
    COD_INF: str
    VL_PIS: Decimal
    VL_COFINS: Decimal
    TP_LIGACAO: TpLigacao  # /// Código de tipo de Ligação [ 1 - Monofásico 2 - Bifásico 3 - Trifásico ]
    COD_GRUPO_TENSAO: GrupoTensao  # /// Código de grupo de tensão: Vide Manual Registro C500 Campo 27
    Registro1510: BlockList[Registro1510]


class Registro1600(Registro):
    COD_PART: str
    TOT_CREDITO: Decimal
    TOT_DEBITO: Decimal


class Registro1601(Registro):
    COD_PART_IP: str  # /// Código do participante (campo 02 do Registro 0150): identificação da instituição que efetuou o pagamento
    COD_PART_IT: str  # /// Código do participante (campo 02 do Registro 0150): identificação do intermediador da transação
    TOT_VS: Decimal  # /// Valor total bruto das vendas e/ou prestações de serviços no campo de incidência do ICMS, incluindo operações com imunidade do imposto.
    TOT_ISS: Decimal  # /// Valor total bruto das prestações de serviços no campo de incidência do ISS
    TOT_OUTROS: Decimal  # /// Valor total de operações deduzido dos valores dos campos TOT_VS e TOT_ISS.


class Registro1710(Registro):
    NUM_DOC_INI: str  # /// Numero Documento Fiscal Inicial
    NUM_DOC_FIN: str  # /// Numero Documento Fiscal Final


class Registro1700(Registro):
    COD_DISP: Dispositivo  # /// Codigo Dispositivo autorizado
    COD_MOD: str  # /// Codigo Modelo Documento Fiscal
    SER: str  # /// Serie Documento Fiscal
    SUB: str  # /// SubSerie Documento Fiscal
    NUM_DOC_INI: str  # /// Numero Documento Fiscal Inicial - deve ser String
    NUM_DOC_FIN: str  # /// Numero Documento Fiscal Final - deve ser String
    NUM_AUT: str  # /// Numero da Autorizacao - deve ser String
    Registro1710: BlockList[Registro1710]  # /// BLOCO 1- Lista de Registro1710 (FILHO fo FILHO)


class Registro1800(Registro):
    VL_CARGA: Decimal  # /// Valor Prestacoes Cargas Tributado
    VL_PASS: Decimal  # /// Valor Prestacoes Cargas Nao Tributado
    VL_FAT: Decimal  # /// Valor total do faturamento
    IND_RAT: Decimal  # /// Indice para rateio
    VL_ICMS_ANT: Decimal  # /// Valor Total Creditos ICMS
    VL_BC_ICMS: Decimal  # /// Valor Base Calculo ICMS
    VL_ICMS_APUR: Decimal  # /// Valor ICMS apurado no calculo
    VL_BC_ICMS_APUR: Decimal  # /// Valor base ICMS apurada
    VL_DIF: Decimal  # /// Valor diferenca a estorno de credito na apuracao


class Registro1922(Registro):
    NUM_DA: str
    NUM_PROC: str
    IND_PROC: str
    PROC: str
    TXT_COMPL: str


class Registro1923(Registro):
    COD_PART: str
    COD_MOD: str
    SER: str
    SUB: str
    NUM_DOC: str
    DT_DOC: date
    COD_ITEM: str
    VL_AJ_ITEM: Decimal
    CHV_DOCe: str


class Registro1921(Registro):
    COD_AJ_APUR: str
    DESCR_COMPL_AJ: str
    VL_AJ_APUR: Decimal
    Registro1922: BlockList[Registro1922]
    Registro1923: BlockList[Registro1923]


class Registro1925(Registro):
    COD_INF_ADIC: str
    VL_INF_ADIC: Decimal
    DESCR_COMPL_AJ: str


class Registro1926(Registro):
    COD_OR: str
    VL_OR: Decimal
    DT_VCTO: date
    COD_REC: str
    NUM_PROC: str
    IND_PROC: str
    PROC: str
    TXT_COMPL: str
    MES_REF: str


class Registro1920(Registro):
    VL_TOT_TRANSF_DEBITOS_OA: Decimal
    VL_TOT_AJ_DEBITOS_OA: Decimal
    VL_ESTORNOS_CRED_OA: Decimal
    VL_TOT_TRANSF_CREDITOS_OA: Decimal
    VL_TOT_AJ_CREDITOS_OA: Decimal
    VL_ESTORNOS_DEB_OA: Decimal
    VL_SLD_CREDOR_ANT_OA: Decimal
    VL_SLD_APURADO_OA: Decimal
    VL_TOT_DED: Decimal
    VL_ICMS_RECOLHER_OA: Decimal
    VL_SLD_CREDOR_TRANSP_OA: Decimal
    DEB_ESP_OA: Decimal
    Registro1921: BlockList[Registro1921]
    Registro1925: BlockList[Registro1925]
    Registro1926: BlockList[Registro1926]


class Registro1910(Registro):
    DT_INI: date
    DT_FIN: date
    Registro1920: BlockList[Registro1920]


class Registro1900(Registro):
    IND_APUR_ICMS: str
    DESCR_COMPL_OUT_APUR: str
    Registro1910: BlockList[Registro1910]


class Registro1960(Registro):
    IND_AP: str  # ///Indicador da sub-apuração por tipo de benefício(conforme tabela 4.7.1)
    G1_01: Decimal  # /// Percentual de crédito presumido
    G1_02: Decimal  # /// Saídas não incentivadas de PI
    G1_03: Decimal  # /// Saídas incentivadas de PI
    G1_04: Decimal  # /// Saídas incentivadas de PI para fora do Nordeste
    G1_05: Decimal  # /// Saldo devedor do ICMS antes das deduções do incentivo
    G1_06: Decimal  # /// Saldo devedor do ICMS relativo à faixa incentivada de PI
    G1_07: Decimal  # /// Crédito presumido nas saídas incentivadas de PI para fora do Nordeste
    G1_08: Decimal  # /// Saldo devedor relativo à faixa incentivada de PI após o crédito presumido nas saídas para fora do Nordeste
    G1_09: Decimal  # /// Crédito presumido
    G1_10: Decimal  # /// Dedução de incentivo da Indústria (crédito presumido)
    G1_11: Decimal  # /// Saldo devedor do ICMS após deduções


class Registro1975(Registro):
    ALIQ_IMP_BASE: Decimal  # /// Alíquota incidente sobre as importações-base( Valores Válidos: [3,50; 6,00; 8,00; 10,00] )
    G3_10: Decimal  # /// Saídas incentivadas de PI
    G3_11: Decimal  # /// Importações-base para o crédito presumido
    G3_12: Decimal  # /// Crédito presumido nas saídas internas


class Registro1970(Registro):
    IND_AP: str  # /// Indicador da sub-apuração por tipo de benefício (conforme tabela 4.7.1)
    G3_01: Decimal  # /// Importações com ICMS diferido
    G3_02: Decimal  # /// ICMS diferido nas importações
    G3_03: Decimal  # /// Saídas não incentivadas de PI
    G3_04: Decimal  # /// Percentual de incentivo nas saídas para fora do Estado
    G3_05: Decimal  # /// Saídas incentivadas de PI para fora do Estado
    G3_06: Decimal  # /// ICMS das saídas incentivadas de PI para fora do Estado
    G3_07: Decimal  # /// Crédito presumido nas saídas para fora do Estado.
    G3_T: Decimal  # /// Dedução de incentivo da Importação (crédito presumido)
    G3_08: Decimal  # /// Saldo devedor do ICMS antes das deduções do incentivo
    G3_09: Decimal  # /// Saldo devedor do ICMS após deduções do incentivo
    Registro1975: BlockList[Registro1975]  # /// BLOCO 1- Lista de Registro1975 (FILHO fo FILHO)


class Registro1980(Registro):
    IND_AP: str  # ///Indicador da sub-apuração por tipo de benefício(conforme tabela 4.7.1)
    G4_01: Decimal  # /// Entradas (percentual de incentivo)
    G4_02: Decimal  # /// Entradas não incentivadas de PI
    G4_03: Decimal  # /// Entradas incentivadas de PI
    G4_04: Decimal  # /// Saídas (percentual de incentivo)
    G4_05: Decimal  # /// Saídas não incentivadas de PI
    G4_06: Decimal  # /// Saídas incentivadas de PI
    G4_07: Decimal  # /// Saldo devedor do ICMS antes das deduções do incentivo (PI e itens não incentivados)
    G4_08: Decimal  # /// Crédito presumido nas entradas incentivadas de PI
    G4_09: Decimal  # /// Crédito presumido nas saídas incentivadas de PI
    G4_10: Decimal  # /// Dedução de incentivo da Central de Distribuição (entradas/saídas)
    G4_11: Decimal  # /// Saldo devedor do ICMS após deduções do incentivo
    G4_12: Decimal  # /// ndice de recolhimento da central de distribuição


class Registro1001(BlocoInicial):
    Registro1010: BlockList[Registro1010]
    Registro1100: BlockList[Registro1100]
    Registro1200: BlockList[Registro1200]
    Registro1250: BlockList[Registro1250]
    Registro1300: BlockList[Registro1300]
    Registro1350: BlockList[Registro1350]
    Registro1390: BlockList[Registro1390]
    Registro1391: BlockList[Registro1391]
    Registro1400: BlockList[Registro1400]
    Registro1500: BlockList[Registro1500]
    Registro1600: BlockList[Registro1600]
    Registro1601: BlockList[Registro1601]
    Registro1700: BlockList[Registro1700]
    Registro1800: BlockList[Registro1800]
    Registro1900: BlockList[Registro1900]
    Registro1960: BlockList[Registro1960]
    Registro1970: BlockList[Registro1970]
    Registro1980: BlockList[Registro1980]


class Registro1990(Registro):
    QTD_LIN_1: int  # /// Quantidade total de linhas do Bloco 1


class EventsBloco_0:
    pass


class RegistroK010(Registro):
    IND_TIPO_LEIAUTE: IndTipoLeiaute


class RegistroK200(Registro):
    DT_EST: date
    COD_ITEM: str
    QTD: float
    IND_EST: IndEstoque
    COD_PART: str


class RegistroK215(Registro):
    COD_ITEM_DES: str
    QTD_DES: float


class RegistroK210(Registro):
    DT_INI_OS: date
    DT_FIN_OS: date
    COD_DOC_OS: str
    COD_ITEM_ORI: str
    QTD_ORI: float
    RegistroK215: BlockList[RegistroK215]


class RegistroK220(Registro):
    DT_MOV: date
    COD_ITEM_ORI: str
    COD_ITEM_DEST: str
    QTD: float
    QTD_DEST: float


class RegistroK235(Registro):
    DT_SAIDA: date
    COD_ITEM: str
    QTD: float
    COD_INS_SUBST: str


class RegistroK230(Registro):
    DT_INI_OP: date
    DT_FIN_OP: date
    COD_DOC_OP: str
    COD_ITEM: str
    QTD_ENC: float
    RegistroK235: BlockList[RegistroK235]


class RegistroK255(Registro):
    DT_CONS: date
    COD_ITEM: str
    QTD: float
    COD_INS_SUBST: str


class RegistroK250(Registro):
    DT_PROD: date
    COD_ITEM: str
    QTD: float
    RegistroK255: BlockList[RegistroK255]


class RegistroK265(Registro):
    COD_ITEM: str
    QTD_CONS: float
    QTD_RET: float


class RegistroK260(Registro):
    COD_OP_OS: str
    COD_ITEM: str
    DT_SAIDA: date
    QTD_SAIDA: float
    DT_RET: date
    QTD_RET: float
    RegistroK265: BlockList[RegistroK265]


class RegistroK275(Registro):
    COD_ITEM: str
    QTD_COR_POS: float
    QTD_COR_NEG: float
    COD_INS_SUBST: str


class RegistroK270(Registro):
    DT_INI_AP: date
    DT_FIN_AP: date
    COD_OP_OS: str
    COD_ITEM: str
    QTD_COR_POS: float
    QTD_COR_NEG: float
    ORIGEM: str
    RegistroK275: BlockList[RegistroK275]


class RegistroK280(Registro):
    DT_EST: date
    COD_ITEM: str
    QTD_COR_POS: float
    QTD_COR_NEG: float
    IND_EST: IndEstoque
    COD_PART: str


class RegistroK291(Registro):
    COD_ITEM: str
    QTD: float


class RegistroK292(Registro):
    COD_ITEM: str
    QTD: float


class RegistroK290(Registro):
    DT_INI_OP: date
    DT_FIN_OP: date
    COD_DOC_OP: str
    RegistroK291: BlockList[RegistroK291]
    RegistroK292: BlockList[RegistroK292]


class RegistroK301(Registro):
    COD_ITEM: str
    QTD: float


class RegistroK302(Registro):
    COD_ITEM: str
    QTD: float


class RegistroK300(Registro):
    DT_PROD: date
    RegistroK301: BlockList[RegistroK301]
    RegistroK302: BlockList[RegistroK302]


class RegistroK100(Registro):
    DT_INI: date  # //Data final a que a apuração se refere
    DT_FIN: date  # //Data inicial a que a apuração se refere
    RegistroK200: BlockList[RegistroK200]
    RegistroK210: BlockList[RegistroK210]
    RegistroK220: BlockList[RegistroK220]
    RegistroK230: BlockList[RegistroK230]
    RegistroK250: BlockList[RegistroK250]
    RegistroK260: BlockList[RegistroK260]
    RegistroK270: BlockList[RegistroK270]
    RegistroK280: BlockList[RegistroK280]
    RegistroK290: BlockList[RegistroK290]
    RegistroK300: BlockList[RegistroK300]


class RegistroK001(BlocoInicial):
    RegistroK010: RegistroK010
    RegistroK100: BlockList[RegistroK100]


class RegistroK990(Registro):
    QTD_LIN_K: int  # /// Quantidade total de linhas do Bloco K


class Bloco_K(BlocoSPED):
    Bloco_0: Bloco_0
    RegistroK001: RegistroK001  # /// BLOCO K - RegistroK001
    RegistroK990: RegistroK990  # /// BLOCO K - RegistroK990
    RegistroK100Count: int
    RegistroK200Count: int
    RegistroK210Count: int
    RegistroK215Count: int
    RegistroK220Count: int
    RegistroK230Count: int
    RegistroK235Count: int
    RegistroK250Count: int
    RegistroK255Count: int
    RegistroK260Count: int
    RegistroK265Count: int
    RegistroK270Count: int
    RegistroK275Count: int
    RegistroK280Count: int
    RegistroK290Count: int
    RegistroK291Count: int
    RegistroK292Count: int
    RegistroK300Count: int
    RegistroK301Count: int
    RegistroK302Count: int


class ChecksBloco_C:
    pass


class EventsBloco_C:
    pass


class EventsBloco_B:
    pass


class EventsBloco_E:
    pass


class Bloco_1(BlocoSPED):
    Bloco_0: Bloco_0
    Registro1001: Registro1001  # /// BLOCO 1 - Registro1001
    Registro1990: Registro1990  # /// BLOCO 1 - Registro1990
    Registro1010Count: int
    Registro1100Count: int
    Registro1105Count: int
    Registro1110Count: int
    Registro1200Count: int
    Registro1210Count: int
    Registro1250Count: int
    Registro1255Count: int
    Registro1300Count: int
    Registro1310Count: int
    Registro1320Count: int
    Registro1350Count: int
    Registro1360Count: int
    Registro1370Count: int
    Registro1390Count: int
    Registro1391Count: int
    Registro1400Count: int
    Registro1500Count: int
    Registro1510Count: int
    Registro1600Count: int
    Registro1601Count: int
    Registro1700Count: int
    Registro1710Count: int
    Registro1800Count: int
    Registro1900Count: int
    Registro1910Count: int
    Registro1920Count: int
    Registro1921Count: int
    Registro1922Count: int
    Registro1923Count: int
    Registro1925Count: int
    Registro1926Count: int
    Registro1960Count: int
    Registro1970Count: int
    Registro1975Count: int
    Registro1980Count: int


class Registro9001(BlocoInicial):
    pass


class Registro9900(Registro):
    REG_BLC: str  # /// Registro que será totalizado no próximo campo.
    QTD_REG_BLC: int  # /// Total de registros do tipo informado no campo anterior.


class Registro9990(Registro):
    QTD_LIN_9: int  # /// Quantidade total de linhas do arquivo digital.


class Registro9999(Registro):
    QTD_LIN: int  # /// Quantidade total de linhas do arquivo digital.


class Bloco_9(BlocoSPED):
    Registro9001: Registro9001  # /// BLOCO 9 - Registro9001
    Registro9900: BlockList[Registro9900]  # /// BLOCO 9 - Lista de Registro9900
    Registro9990: Registro9990  # /// BLOCO 9 - Registro9990
    Registro9999: Registro9999  # /// BLOCO 9 - Registro9999


class Bloco_B(BlocoSPED):
    Bloco_0: Bloco_0
    RegistroB001: RegistroB001  # /// BLOCO B - RegistroB001
    RegistroB990: RegistroB990  # /// BLOCO B - RegistroB990
    RegistroB020Count: int
    RegistroB025Count: int
    RegistroB030Count: int
    RegistroB035Count: int
    RegistroB350Count: int
    RegistroB420Count: int
    RegistroB440Count: int
    RegistroB460Count: int
    RegistroB470Count: int
    RegistroB500Count: int
    RegistroB510Count: int


class Bloco_C(BlocoSPED):
    Bloco_0: Bloco_0
    RegistroC001: RegistroC001  # /// BLOCO C - RegistroC001
    RegistroC990: RegistroC990  # /// BLOCO C - RegistroC990
    RegistroC100Count: int
    RegistroC101Count: int
    RegistroC105Count: int
    RegistroC110Count: int
    RegistroC112Count: int
    RegistroC113Count: int
    RegistroC114Count: int
    RegistroC115Count: int
    RegistroC116Count: int
    RegistroC111Count: int
    RegistroC120Count: int
    RegistroC130Count: int
    RegistroC140Count: int
    RegistroC141Count: int
    RegistroC160Count: int
    RegistroC165Count: int
    RegistroC170Count: int
    RegistroC171Count: int
    RegistroC172Count: int
    RegistroC173Count: int
    RegistroC174Count: int
    RegistroC175Count: int
    RegistroC176Count: int
    RegistroC177Count: int
    RegistroC178Count: int
    RegistroC179Count: int
    RegistroC180Count: int
    RegistroC181Count: int
    RegistroC185Count: int
    RegistroC186Count: int
    RegistroC190Count: int
    RegistroC191Count: int
    RegistroC195Count: int
    RegistroC197Count: int
    RegistroC300Count: int
    RegistroC310Count: int
    RegistroC320Count: int
    RegistroC321Count: int
    RegistroC330Count: int
    RegistroC350Count: int
    RegistroC370Count: int
    RegistroC380Count: int
    RegistroC390Count: int
    RegistroC400Count: int
    RegistroC405Count: int
    RegistroC410Count: int
    RegistroC420Count: int
    RegistroC425Count: int
    RegistroC430Count: int
    RegistroC460Count: int
    RegistroC465Count: int
    RegistroC470Count: int
    RegistroC480Count: int
    RegistroC490Count: int
    RegistroC495Count: int
    RegistroC500Count: int
    RegistroC510Count: int
    RegistroC590Count: int
    RegistroC591Count: int
    RegistroC595Count: int
    RegistroC597Count: int
    RegistroC600Count: int
    RegistroC601Count: int
    RegistroC610Count: int
    RegistroC690Count: int
    RegistroC700Count: int
    RegistroC790Count: int
    RegistroC791Count: int
    RegistroC800Count: int
    RegistroC810Count: int
    RegistroC850Count: int
    RegistroC855Count: int
    RegistroC857Count: int
    RegistroC860Count: int
    RegistroC870Count: int
    RegistroC890Count: int
    RegistroC895Count: int
    RegistroC897Count: int


class Bloco_D(BlocoSPED):
    Bloco_0: Bloco_0
    RegistroD001: RegistroD001  # /// BLOCO D - RegistroD001
    RegistroD990: RegistroD990  # /// BLOCO D - RegistroD990
    RegistroD100Count: int
    RegistroD101Count: int
    RegistroD110Count: int
    RegistroD120Count: int
    RegistroD130Count: int
    RegistroD140Count: int
    RegistroD150Count: int
    RegistroD160Count: int
    RegistroD161Count: int
    RegistroD162Count: int
    RegistroD170Count: int
    RegistroD180Count: int
    RegistroD190Count: int
    RegistroD195Count: int
    RegistroD197Count: int
    RegistroD300Count: int
    RegistroD301Count: int
    RegistroD310Count: int
    RegistroD350Count: int
    RegistroD355Count: int
    RegistroD360Count: int
    RegistroD365Count: int
    RegistroD370Count: int
    RegistroD390Count: int
    RegistroD400Count: int
    RegistroD410Count: int
    RegistroD411Count: int
    RegistroD420Count: int
    RegistroD500Count: int
    RegistroD510Count: int
    RegistroD530Count: int
    RegistroD590Count: int
    RegistroD600Count: int
    RegistroD610Count: int
    RegistroD690Count: int
    RegistroD695Count: int
    RegistroD696Count: int
    RegistroD697Count: int
    RegistroD700Count: int
    RegistroD730Count: int
    RegistroD731Count: int
    RegistroD735Count: int
    RegistroD737Count: int
    RegistroD750Count: int
    RegistroD760Count: int
    RegistroD761Count: int


class Bloco_E(BlocoSPED):
    Bloco_0: Bloco_0
    RegistroE001: RegistroE001  # /// BLOCO E - RegistroE001
    RegistroE990: RegistroE990  # /// BLOCO E - RegistroE990
    RegistroE100Count: int
    RegistroE110Count: int
    RegistroE111Count: int
    RegistroE112Count: int
    RegistroE113Count: int
    RegistroE115Count: int
    RegistroE116Count: int
    RegistroE200Count: int
    RegistroE210Count: int
    RegistroE220Count: int
    RegistroE230Count: int
    RegistroE240Count: int
    RegistroE250Count: int
    RegistroE300Count: int
    RegistroE310Count: int
    RegistroE311Count: int
    RegistroE312Count: int
    RegistroE313Count: int
    RegistroE316Count: int
    RegistroE500Count: int
    RegistroE510Count: int
    RegistroE520Count: int
    RegistroE530Count: int
    RegistroE531Count: int


class RegistroH011(Registro):
    CNPJ: str  # /// CNPJ DA EMPRESA RESPONSÁVEL PELO INVENTARIO


class RegistroH020(Registro):
    CST_ICMS: str
    BC_ICMS: Decimal
    VL_ICMS: Decimal


class RegistroH030(Registro):
    VL_ICMS_OP: float  # /// Valor médio unitário do ICMS OP.
    VL_BC_ICMS_ST: float  # /// Valor médio unitário da base de cálculo do ICMS ST.
    VL_ICMS_ST: float  # /// Valor médio unitário do ICMS ST.
    VL_FCP: float  # /// Valor médio unitário do FCP.


class RegistroH010(Registro):
    COD_ITEM: str
    UNID: str
    QTD: float
    VL_UNIT: float
    VL_ITEM: Decimal
    IND_PROP: IndProp
    COD_PART: str
    TXT_COMPL: str
    COD_CTA: str
    VL_ITEM_IR: float  # /// Valor do item para efeitos do Imposto de Renda.
    RegistroH011: BlockList[RegistroH011]  # /// BLOCO H - Lista de RegistroH011 (FILHO)
    RegistroH020: BlockList[RegistroH020]  # /// BLOCO H - Lista de RegistroH020 (FILHO)
    RegistroH030: BlockList[RegistroH030]  # /// BLOCO H - Lista de RegistroH030 (FILHO)


class RegistroH005(Registro):
    DT_INV: date
    VL_INV: Decimal
    MOT_INV: MotInv  # /// 01  No final no período;
    RegistroH010: BlockList[RegistroH010]  # /// BLOCO H - Lista de RegistroH010 (FILHO)


class RegistroH001(BlocoInicial):
    RegistroH005: BlockList[RegistroH005]


class RegistroH990(Registro):
    QTD_LIN_H: int


class Bloco_H(BlocoSPED):
    Bloco_0: Bloco_0
    RegistroH001: RegistroH001  # /// BLOCO H - RegistroH001
    RegistroH990: RegistroH990  # /// BLOCO H - RegistroH990
    RegistroH005Count: int
    RegistroH010Count: int
    RegistroH011Count: int
    RegistroH020Count: int
    RegistroH030Count: int


class SPEDFiscal:
    Conteudo: BlockList[str]
    DT_INI: date
    DT_FIN: date
    Bloco_0: Bloco_0
    Bloco_1: Bloco_1
    Bloco_9: Bloco_9
    Bloco_B: Bloco_B
    Bloco_C: Bloco_C
    Bloco_D: Bloco_D
    Bloco_E: Bloco_E
    Bloco_G: Bloco_G
    Bloco_H: Bloco_H
    Bloco_K: Bloco_K  # /// Método do evento OnError
    Path: str  # /// Path do arquivo a ser gerado
    Arquivo: str
    LinhasBuffer: int
    Delimitador: str
    ReplaceDelimitador: bool
    TrimString: bool
    CurMascara: str
    ChecksBloco_C: ChecksBloco_C
    EventsBloco_0: EventsBloco_0
    EventsBloco_B: EventsBloco_B
    EventsBloco_C: EventsBloco_C
    EventsBloco_D: EventsBloco_D
    EventsBloco_E: EventsBloco_E
