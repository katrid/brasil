from typing import List, Required, Annotated
import enum
from datetime import date
from decimal import Decimal

from brasil.sped.registro import BlockList, Registro, BlocoSPED

class CodVer(enum.StrEnum):
   Versao100 = "001"  # Código 001 - Versão 100 ADE Cofis nº 31/2010 de 01/01/2011
   Versao101 = "002"  # Código 002 - Versão 101 ADE Cofis nº 34/2010 de 01/01/2011
   Versao200 = "002"  # Código 002 - Versão 200 ADE Cofis nº 20/2012
   Versao201 = "003"  # Código 003 - Versão 201 ADE Cofis nº 20/2012 de 14/03/2012
   Versao202 = "004"  # Código 004
   Versao310 = "005"  # Código 005 - ADE Cofis nº 82/2018 - Apuração em 01/01/2019
   Versao320 = "006"  # Código 006 - ADE Cofis ??? - Apuração em 01/01/2020


class IndMov(enum.StrEnum):
   ComDados = "0"  # 0- Bloco com dados informados;
   SemDados = "1"  # 1- Bloco sem dados informados.


class TipoEscrit(enum.StrEnum):
   EscrOriginal = "0"  # 0 - Original
   EscrRetificadora = "1"  # 1 - Retificadora


class IndSitEsp(enum.StrEnum):
   SitAbertura = "0"  # 0 - Abertura
   SitCisao = "1"  # 1 - Cisão
   SitFusao = "2"  # 2 - Fusão
   SitIncorporacao = "3"  # 3 - Incorporação
   SitEncerramento = "4"  # 4 - Encerramento
   Nenhum = "5"  # 5 - Vazio


class IndNatPJ(enum.StrEnum):
   NatPJSocEmpresariaGeral = "0"  # 0 - Sociedade empresária geral
   NatPJSocCooperativa = "1"  # 1 - Sociedade Cooperativa
   NatPJEntExclusivaFolhaSal = "2"  # 2 - Entidade sujeita ao PIS/Pasep exclusivamente com base  na folha de salários
   NatPJSocEmpresariaGeralSCP = "3"  # 3 - Geral participante de SCP
   NatPJSocCooperativaSCP = "4"  # 4 - Sociedade Cooperativa Participante SCP
   NatPJSocContaParticante = "5"  # 5 - Sociedade em Conta de Particpante
   NatPJNenhum = ""


class IndAtiv(enum.StrEnum):
   AtivIndustrial = "0"  # 0 - Industrial ou equiparado a industrial
   AtivPrestadorServico = "1"  # 1 - Prestador de serviços
   AtivComercio = "2"  # 2 - Atividade de comércios
   AtivoFincanceira = "3"  # 3 - Atividade Financeira
   AtivoImobiliaria = "4"  # 4 - Atividade Imobiliária
   AtivoOutros = "9"  # 9 - Outros


class CodIndIncTributaria(enum.StrEnum):
   EscrOpIncNaoCumulativo = "1"  # 1 - Escrituração de operações com incidencia exclusivamente no regime não cumulativo
   EscrOpIncCumulativo = "2"  # 2 - Escrituração de operações com incidencia exclusivamente no regime cumulativo
   EscrOpIncAmbos = "3"  # 3 - Escrituração de operações com incidencia nos regimes cumulativo e não cumulativo


class IndAproCred(enum.StrEnum):
   MetodoApropriacaoDireta = "0"  # 0 - Método de apropriação direta
   MetodoDeRateioProporcional = "1"  # 1 - Método de rateio proporcional(Receita Bruta);


class CodIndTipoCon(enum.StrEnum):
   IndTipoConExclAliqBasica = "1"  # 1 - Apuração da Contribuição Exclusivamente a Alíquota Básica
   IndTipoAliqEspecificas = "2"  # 2 - Apuração da Contribuição a Alíquotas Específicas (Diferenciadas e/ou por Unidade de Medida de Produto)


class CodIndCritEscrit(enum.StrEnum):
   RegimeCaixa = "1"  # 1  Regime de Caixa  Escrituração consolidada (Registro F500);
   RegimeCompetEscritConsolidada = "2"  # 2  Regime de Competência - Escrituração consolidada (Registro F550);
   RegimeCompetEscritDetalhada = "9"  # 9  Regime de Competência - Escrituração detalhada, com base nos registros dos Blocos A, C, D e F.


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


class IndicadorTpOperacao(enum.StrEnum):
   Contratado = "0"  # 0 - Serviço Contratado pelo Estabelecimento
   Prestado = "1"  # 1 - Serviço Prestado pelo Estabelecimento


class IndicadorEmitenteDF(enum.StrEnum):
   Proprio = "0"  # 0 - Emissão própria
   Terceiro = "1"  # 1 - Emissão de Terceiros


class TipoPagamento(enum.StrEnum):
   Vista = "0"  # 0 - À Vista
   Prazo = "1"  # 1 - A Prazo
   SemPagamento = "9"  # 9 - Sem pagamento (2 - Outros, para registros após 01/07/2012)
   Nenhum = ""  # Preencher vazio


class BaseCalculoCredito(enum.StrEnum):
   Vazio = ""  # ''   // vazio.
   AqBensRevenda = "01"  # '01' // Aquisição de bens para revenda
   AqBensUtiComoInsumo = "02"  # '02' // Aquisição de bens utilizados como insumo
   AqServUtiComoInsumo = "03"  # '03' // Aquisição de serviços utilizados como insumo
   EnergiaEletricaTermica = "04"  # '04' // Energia elétrica e térmica, inclusive sob a forma de vapor
   AluguelPredios = "05"  # '05' // Aluguéis de prédios
   AluguelMaqEquipamentos = "06"  # '06' // Aluguéis de máquinas e equipamentos
   ArmazenagemMercadoria = "07"  # '07' // Armazenagem de mercadoria e frete na operação de venda
   ConArrendamentoMercantil = "08"  # '08' // Contraprestações de arrendamento mercantil
   MaqCredDepreciacao = "09"  # '09' // Máquinas, equipamentos e outros bens incorporados ao ativo imobilizado (crédito sobre encargos de depreciação).
   MaqCredAquisicao = "10"  # '10' // Máquinas, equipamentos e outros bens incorporados ao ativo imobilizado (crédito com base no valor de aquisição).
   AmortizacaoDepreciacaoImoveis = "11"  # '11' // Amortização e Depreciação de edificações e benfeitorias em imóveis
   DevolucaoSujeita = "12"  # '12' // Devolução de Vendas Sujeitas à Incidência Não-Cumulativa
   OutrasOpeComDirCredito = "13"  # '13' // Outras Operações com Direito a Crédito
   AtTransporteSubcontratacao = "14"  # '14' // Atividade de Transporte de Cargas  Subcontratação
   AtImobCustoIncorrido = "15"  # '15' // Atividade Imobiliária  Custo Incorrido de Unidade Imobiliária
   AtImobCustoOrcado = "16"  # '16' // Atividade Imobiliária  Custo Orçado de unidade não concluída
   AtPresServ = "17"  # '17' // Atividade de Prestação de Serviços de Limpeza, Conservação e Manutenção  vale-transporte, vale-refeição ou vale-alimentação, fardamento ou uniforme.
   EstoqueAberturaBens = "18"  # '18' // Estoque de abertura de bens


class OrigemCredito(enum.StrEnum):
   MercadoInterno = "0"  # 0  Operação no Mercado Interno
   Importacao = "1"  # 1  Operação de Importação
   Vazio = ""  # Vazio.


class IdentBemImob(enum.StrEnum):
   EdificacoesBenfeitorias = "01"  # '01' // Edificações e Benfeitorias
   Instalacoes = "03"  # '03' // Instalações
   Maquinas = "04"  # '04' // Máquinas
   Equipamentos = "05"  # '05' // Equipamentos
   Veiculos = "06"  # '06' // Veículos
   Outros = "99"  # '99' // Outros bens incorporados ao Ativo Imobilizado


class IndUtilBemImob(enum.StrEnum):
   ProducaoBensDestinadosVenda = "1"  # '1' // Produção de Bens Destinados a Venda
   PrestacaoServicos = "2"  # '2' // Prestação de Serviços
   LocacaoTerceiros = "3"  # '3' // Locação a Terceiros
   Outros = "9"  # '9' // Outros


class IndNrParc(enum.StrEnum):
   Integral = "1"  # '1' // Integral (Mês de Aquisição)
   IndNrParc12Meses = "2"  # '2' // 12 Meses
   IndNrParc24Meses = "3"  # '3' // 24 Meses
   IndNrParc48Meses = "4"  # '4' // 48 Meses
   IndNrParc6Meses = "5"  # '5' // 6 Meses (Embalagens de bebidas frias)
   Outra = "9"  # '9' // Outra periodicidade definida em Lei


class TipoOperacao(enum.StrEnum):
   EntradaAquisicao = "0"  # 0 - Entrada
   SaidaPrestacao = "1"  # 1 - Saída


class Emitente(enum.StrEnum):
   EmissaoPropria = "0"  # 0 - Emissão própria
   Terceiros = "1"  # 1 - Terceiro


class TipoFrete(enum.StrEnum):
   PorContaEmitente = "0"  # 0 - Por conta do emitente
   PorContaDestinatario = "1"  # 1 - Por conta do destinatário
   PorContaTerceiros = "2"  # 2 - Por conta de terceiros
   ProprioPorContaEmitente = "3"  # 3 - Próprio Por conta do emitente
   ProprioPorContaDestinatario = "4"  # 4 - Próprio Por conta do destinatário
   SemCobrancaFrete = "9"  # 9 - Sem cobrança de frete
   Nenhum = ""


class OrigemProcesso(enum.StrEnum):
   JusticaFederal = "1"  # 1 - Justiça Federal'
   SecexRFB = "3"  # 3  Secretaria da Receita Federal do Brasil
   Outros = "9"  # 9 - Outros
   Nenhum = ""  # Preencher vazio


class DoctoImporta(enum.StrEnum):
   Importacao = "0"  # 0  Declaração de Importação
   SimplificadaImport = "1"  # 1  Declaração Simplificada de Importação


class IndMovFisica(enum.StrEnum):
   Sim = "0"  # 0 - Sim
   Nao = "1"  # 1 - Não


class ApuracaoIPI(enum.StrEnum):
   Mensal = "0"  # 0 - Mensal
   Decendial = "1"  # 1 - Decendial
   Vazio = "None"  # / Indicador de tipo de referência da base de cálculo do ICMS (ST) do produto farmacêutico


class SituacaoDF(enum.StrEnum):
   Regular = "00"  # 00  Documento regular
   ExtRegular = "01"  # 01 - Escrituração extemporânea de documento regular
   Cancelado = "02"  # 02  Documento cancelado
   ExtCancelado = "03"  # 03 Escrituração extemporânea de documento cancelado
   Denegado = "04"  # 04 NF-e ou CT-e  denegado
   Inutilizado = "05"  # 05 NF-e ou CT-e - Numeração inutilizada
   Complementar = "06"  # 06 Documento Fiscal Complementar
   ExtComplementar = "07"  # 07 Escrituração extemporânea de documento complementar
   Especial = "08"  # 08 Documento Fiscal emitido com base em Regime Especial ou Norma Específica


class CodSitF(enum.StrEnum):
   Regular = "00"  # 00  Documento regular
   Cancelado = "02"  # 02  Documento cancelado
   Outros = "99"  # 99  Outros


class NaturezaFrtContratado(enum.StrEnum):
   VendaOnusEstVendedor = "0"  # 0 - Operações de vendas, com ônus suportado pelo estabelecimento vendedor
   VendaOnusAdquirente = "1"  # 1 - Operações de vendas, com ônus suportado pelo adquirente
   CompraGeraCred = "2"  # 2 - Operações de compras (bens para revenda, matériasprima e outros produtos, geradores de crédito)
   CompraNaoGeraCred = "3"  # 3 - Operações de compras (bens para revenda, matériasprima e outros produtos, não geradores de crédito)
   TransfAcabadosPJ = "4"  # 4 - Transferência de produtos acabados entre estabelecimentos da pessoa jurídica
   TransfNaoAcabadosPJ = "5"  # 5 - Transferência de produtos em elaboração entre estabelecimentos da pessoa jurídica
   Outras = "9"  # 9 - Outras.


class NaturezaConta(enum.StrEnum):
   Ativo = "01"  # 01 - Contas de ativo
   Passivo = "02"  # 02 - Contas de passivo
   Liquido = "03"  # 03 - Patrimônio líquido
   Resultado = "04"  # 04 - Contas de resultado
   Compensacao = "05"  # 05 - Contas de compensação
   Outras = "09"  # 09 - Outras


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


class SituacaoTribPIS(enum.StrEnum):
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


class SituacaoTribCOFINS(enum.StrEnum):
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


class CstPisCofins(enum.StrEnum):
   OperTribuComAliqBasica = "01"  # 01 Operação Tributável com Alíquota Básica
   OperTribuAliqZero = "06"  # 06 Operação Tributável a Alíquota Zero
   OperIsentaContribuicao = "07"  # 07 Operação Isenta da Contribuição
   OperSemIncidenciaContribuicao = "08"  # 08 Operação sem Incidência da Contribuição
   OperComSuspensaoContribuicao = "09"  # 09 Operação com Suspensão da Contribuição
   OutrasOperacoesSaida = "49"  # 49 Outras Operações de Saída
   OutrasDespesas = "99"  # 99 Outras Operações
   Nenhum = ""


class LocalExecServico(enum.StrEnum):
   ExecutPais = "0"  # 0  Executado no País;
   ExecutExterior = "1"  # 1  Executado no Exterior, cujo resultado se verifique no País.


class IndCodIncidencia(enum.StrEnum):
   IndiTabNaoTem = "None"
   IndTabI = "01"  # 01 - Tabela I
   IndTabII = "02"  # 02 - Tabela II
   IndTabIII = "03"  # 03 - Tabela III
   IndTabIV = "04"  # 04 - Tabela IV
   IndTabV = "05"  # 05 - Tabela V
   IndTabVI = "06"  # 06 - Tabela VI
   IndTabVII = "07"  # 07 - Tabela VII
   IndTabVIII = "08"  # 08 - Tabela VIII
   IndTabIX = "09"  # 09 - Tabela IX
   IndTabX = "10"  # 10 - Tabela X
   IndTabXI = "11"  # 11 - Tabela XI
   IndiTabXII = "12"  # 12 - Tabela XII


class IndCTA(enum.StrEnum):
   CTASintetica = "S"  # S Sintética
   CTAnalitica = "A"  # A Analitica


class IndEscrituracao(enum.StrEnum):
   IndEscriConsolidado = "1"  # 1  Apuração com base nos registros de consolidação das operações por NF-e (C180 e C190) e por ECF (C490);
   IndEscriIndividualizado = "2"  # 2  Apuração com base no registro individualizado de NF-e (C100 e C170) e de ECF (C400)


class IndAJ(enum.StrEnum):
   AjReducao = "0"  # '0' // Ajuste de redução;
   AjAcressimo = "1"  # '1' // Ajuste de acréscimo.


class CodAj(enum.StrEnum):
   AjAcaoJudicial = "01"  # '01' // Ajuste Oriundo de Ação Judicial
   AjProAdministrativo = "02"  # '02' // Ajuste Oriundo de Processo Administrativo
   AjLegTributaria = "03"  # '03' // Ajuste Oriundo da Legislação Tributária
   AjEspRTI = "04"  # '04' // Ajuste Oriundo Especificamente do RTT
   AjOutrasSituacaoes = "05"  # '05' // Ajuste Oriundo de Outras Situações
   AjEstorno = "06"  # '06' // Estorno
   AjCPRBAdocaoRegCaixa = "07"  # '07' // Ajuste da CPRB: Adoção do Regime de Caixa
   AjCPRBDiferValRecPer = "08"  # '08' // Ajuste da CPRB: Diferimento de Valores a Recolher no Período
   AjCPRBAdicValDifPerAnt = "09"  # '09' // Ajuste da CPRB: Adição de Valores Diferidos em Período(s) Anterior(es)


class IndNatRec(enum.StrEnum):
   NaoCumulativa = "0"
   Cumulativa = "1"
   Nenhum = "9"


class NatCredDesc(enum.StrEnum):
   AliqBasica = "01"  # '01' // Crédito a Alíquota Básica;
   AliqDiferenciada = "02"  # '02' // Crédito a Alíquota Diferenciada;
   AliqUnidProduto = "03"  # '03' // Crédito a Alíquota por Unidade de Produto;
   PresAgroindustria = "04"  # '04' // Crédito Presumido da Agroindústria.


class CodCred(enum.StrEnum):
   RTMIAliqBasica = "101"  # '101' // Crédito vinculado à receita tributada no mercado interno - Alíquota Básica
   RTMIAliqDiferenciada = "102"  # '102' // Crédito vinculado à receita tributada no mercado interno - Alíquotas Diferenciadas
   RTMIAliqUnidProduto = "103"  # '103' // Crédito vinculado à receita tributada no mercado interno - Alíquota por Unidade de Produto
   RTMIEstAbertura = "104"  # '104' // Crédito vinculado à receita tributada no mercado interno - Estoque de Abertura
   RTMIAquiEmbalagem = "105"  # '105' // Crédito vinculado à receita tributada no mercado interno - Aquisição Embalagens para revenda
   RTMIPreAgroindustria = "106"  # '106' // Crédito vinculado à receita tributada no mercado interno - Presumido da Agroindústria
   RTMIImportacao = "108"  # '108' // Crédito vinculado à receita tributada no mercado interno - Importação
   RTMIAtivImobiliaria = "109"  # '109' // Crédito vinculado à receita tributada no mercado interno - Atividade Imobiliária
   RTMIOutros = "199"  # '199' // Crédito vinculado à receita tributada no mercado interno - Outros
   RNTMIAliqBasica = "201"  # '201' // Crédito vinculado à receita não tributada no mercado interno - Alíquota Básica
   RNTMIAliqDiferenciada = "202"  # '202' // Crédito vinculado à receita não tributada no mercado interno - Alíquotas Diferenciadas
   RNTMIAliqUnidProduto = "203"  # '203' // Crédito vinculado à receita não tributada no mercado interno - Alíquota por Unidade de Produto
   RNTMIEstAbertura = "204"  # '204' // Crédito vinculado à receita não tributada no mercado interno - Estoque de Abertura
   RNTMIAquiEmbalagem = "205"  # '205' // Crédito vinculado à receita não tributada no mercado interno - Aquisição Embalagens para revenda
   RNTMIPreAgroindustria = "206"  # '206' // Crédito vinculado à receita não tributada no mercado interno - Presumido da Agroindústria
   RNTMIImportacao = "208"  # '208' // Crédito vinculado à receita não tributada no mercado interno - Importação
   RNTMIOutros = "299"  # '299' // Crédito vinculado à receita não tributada no mercado interno - Outros
   REAliqBasica = "301"  # '301' // Crédito vinculado à receita de exportação - Alíquota Básica
   REAliqDiferenciada = "302"  # '302' // Crédito vinculado à receita de exportação - Alíquotas Diferenciadas
   REAliqUnidProduto = "303"  # '303' // Crédito vinculado à receita de exportação - Alíquota por Unidade de Produto
   REEstAbertura = "304"  # '304' // Crédito vinculado à receita de exportação - Estoque de Abertura
   REAquiEmbalagem = "305"  # '305' // Crédito vinculado à receita de exportação - Aquisição Embalagens para revenda
   REPreAgroindustria = "306"  # '306' // Crédito vinculado à receita de exportação - Presumido da Agroindústria
   REPreAgroindustriaPCR = "307"  # '307' // Crédito vinculado à receita de exportação - Presumido da Agroindústria  Passível de Compensação e/ou Ressarcimento
   REImportacao = "308"  # '308' // Crédito vinculado à receita de exportação - Importação
   REOutros = "399"  # '399' // Crédito vinculado à receita de exportação - Outros


class IndTipCoop(enum.StrEnum):
   ProdAgropecuaria = "01"  # '01' // Cooperativa de Produção Agropecuária;
   Consumo = "02"  # '02' // Cooperativa de Consumo;
   Credito = "03"  # '03' // Cooperativa de Crédito;
   EletRural = "04"  # '04' // Cooperativa de Eletrificação Rural;
   TransCargas = "05"  # '05' // Cooperativa de Transporte Rodoviário de Cargas;
   Medicos = "06"  # '06' // Cooperativa de Médicos;
   Outras = "99"  # '99' // Outras.


class IndCredOri(enum.StrEnum):
   OperProprias = "0"
   EvenFusaoCisao = "1"


class IndRec(enum.StrEnum):
   PropServPrestados = "0"
   PropCobDebitos = "1"
   PropServPrePagAnterior = "2"
   PropServPrePagAtual = "3"
   PropServOutrosComunicacao = "4"
   CFaturamento = "5"
   ServAFaturar = "6"
   NaoAcumulativa = "7"
   Terceiros = "8"
   Outras = "9"


class IndDescCred(enum.StrEnum):
   Total = "0"
   Parcial = "1"


class CodCont(enum.StrEnum):
   NaoAcumAliqBasica = "01"  # 01 // Contribuição não-cumulativa apurada a alíquota básica
   NaoAcumAliqDiferenciada = "02"  # 02 // Contribuição não-cumulativa apurada a alíquotas diferenciadas
   NaoAcumAliqUnidProduto = "03"  # 03 // Contribuição não-cumulativa apurada a alíquota por unidade de medida de produto
   NaoAcumAliqBasicaAtivImobiliaria = "04"  # 04 // Contribuição não-cumulativa apurada a alíquota básica - Atividade Imobiliária
   ApuradaPorST = "31"  # 31 // Contribuição apurada por substituição tributária
   ApuradaPorSTManaus = "32"  # 32 // Contribuição apurada por substituição tributária - Vendas à Zona Franca de Manaus
   AcumAliqBasica = "51"  # 51 // Contribuição cumulativa apurada a alíquota básica
   AcumAliqDiferenciada = "52"  # 52 // Contribuição cumulativa apurada a alíquotas diferenciadas
   AcumAliqUnidProduto = "53"  # 53 // Contribuição cumulativa apurada a alíquota por unidade de medida de produto
   AcumAliqBasicaAtivImobiliaria = "54"  # 54 // Contribuição cumulativa apurada a alíquota básica - Atividade Imobiliária
   ApuradaAtivImobiliaria = "70"  # 70 // Contribuição apurada da Atividade Imobiliária - RET
   ApuradaSCPNaoCumulativa = "71"  # 71 // Contribuição apurada de SCP - Incidência Não Cumulativa
   ApuradaSCPCumulativa = "72"  # 72 // Contribuição apurada de SCP - Incidência Cumulativa
   PISPasepSalarios = "99"  # 99 // Contribuição para o PIS/Pasep - Folha de Salários


class IndNatRetFonte(enum.StrEnum):
   RetOrgAutarquiasFundFederais = "01"  # 01 - Retenção por Órgãos, Autarquias e Fundações Federais
   RetEntAdmPublicaFederal = "02"  # 02 - Retenção por outras Entidades da Administração Pública Federal
   RetPesJuridicasDireitoPri = "03"  # 03 - Retenção por Pessoas Jurídicas de Direito Privado
   RecolhimentoSociedadeCoop = "04"  # 04 - Recolhimento por Sociedade Cooperativa
   RetFabricanteMaqVeiculos = "05"  # 05 - Retenção por Fabricante de Máquinas e Veículos
   OutrasRetencoes = "99"  # 99 - Outras Retenções


class IndOrigemDiversas(enum.StrEnum):
   CredPreMed = "01"  # 01  Créditos Presumidos - Medicamentos
   CredAdmRegCumulativoBeb = "02"  # 02  Créditos Admitidos no Regime Cumulativo  Bebidas Frias
   ContribSTZFM = "03"  # 03  Contribuição Paga pelo Substituto Tributário - ZFM
   STNaoOCFatoGeradorPres = "04"  # 04  Substituição Tributária  Não Ocorrência do Fato Gerador Presumido
   OutrasDeducoes = "99"  # 99 - Outras Deduções


class IndNatDeducao(enum.StrEnum):
   NaoAcumulativa = "0"  # 0  Dedução de Natureza Não Cumulativa
   Acumulativa = "1"  # 1  Dedução de Natureza Cumulativa


class IndTpOperacaoReceita(enum.StrEnum):
   RepCustosDespesasEncargos = "0"  # 0  Operação Representativa de Aquisição, Custos, Despesa ou Encargos, Sujeita à Incidência de Crédito de PIS/Pasep ou Cofins (CST 50 a 66).
   RepReceitaAuferida = "1"  # 1  Operação Representativa de Receita Auferida Sujeita ao Pagamento da Contribuição para o PIS/Pasep e da Cofins (CST 01, 02, 03 ou 05).
   RepReceitaNaoAuferida = "2"  # 2 - Operação Representativa de Receita Auferida Não Sujeita ao Pagamento da Contribuição para o PIS/Pasep e da Cofins (CST 04, 06, 07, 08, 09, 49 ou 99).


class Ind_Rec(enum.StrEnum):
   Cliente = "01"  # 01- Clientes
   Administradora = "02"  # 02- Administradora de cartão de débito/crédito
   TituloDeCredito = "03"  # 03- Título de crédito - Duplicata, nota promissória, cheque, etc.
   DocumentoFiscal = "04"  # 04- Documento fiscal
   ItemVendido = "05"  # 05- Item vendido (produtos e serviços)
   Outros = "99"  # 99- Outros (Detalhar no campo 10  Informação Complementar)


class TabCodAjBaseCalcContrib(enum.StrEnum):
   VendasCanceladas = "01"  # 01 - Vendas canceladas de receitas tributadas em períodos anteriores
   DevolucoesVendas = "02"  # 02 - Devoluções de vendas tributadas em períodos anteriores
   ICMSaRecolher = "21"  # 21 - ICMS a recolher sobre Operações próprias
   OutrVlrsDecJudicial = "41"  # 41 - Outros valores a excluir, vinculados a decisão judicial
   OutrVlrsSemDecJudicial = "42"  # 42 - Outros valores a excluir, não vinculados a decisão judicial


class IndicadorApropAjuste(enum.StrEnum):
   RefPisCofins = "01"  # 01  Referente ao PIS/Pasep e a Cofins
   UnicaPISPasep = "02"  # 02  Referente unicamente ao PIS/Pasep
   RefUnicaCofins = "03"  # 03  Referente unicamente à Cofins


class BlocoInicial:
   IND_MOV: IndMov  # /// Indicador de movimento: 0- Bloco com dados informados, 1- Bloco sem dados informados.


class RegistroA110(Registro):
   COD_INF: str
   TXT_COMPL: str


class RegistroA111(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroA120(Registro):
   VL_TOT_SERV: Decimal | str
   VL_BC_PIS: Decimal | str
   VL_PIS_IMP: Decimal | str
   DT_PAG_PIS: date
   VL_BC_COFINS: Decimal | str
   VL_COFINS_IMP: Decimal | str
   DT_PAG_COFINS: date
   LOC_EXE_SERV: LocalExecServico


class RegistroA170(Registro):
   NUM_ITEM: int
   COD_ITEM: str
   DESCR_COMPL: str
   VL_ITEM: Decimal | str
   VL_DESC: Decimal | str
   NAT_BC_CRED: BaseCalculoCredito
   IND_ORIG_CRED: OrigemCredito
   CST_PIS: SituacaoTribPIS
   VL_BC_PIS: Decimal | str
   ALIQ_PIS: Decimal | str
   VL_PIS: Decimal | str
   CST_COFINS: SituacaoTribCOFINS
   VL_BC_COFINS: Decimal | str
   ALIQ_COFINS: Decimal | str
   VL_COFINS: Decimal | str
   COD_CTA: str
   COD_CCUS: str


class RegistroA100(Registro):
   IND_OPER: IndicadorTpOperacao
   IND_EMIT: IndicadorEmitenteDF
   COD_PART: str
   COD_SIT: SituacaoDF
   SER: str
   SUB: str
   NUM_DOC: str
   CHV_NFSE: str
   DT_DOC: date
   DT_EXE_SERV: date
   VL_DOC: Decimal | str
   IND_PGTO: TipoPagamento
   VL_DESC: Decimal | str
   VL_BC_PIS: Decimal | str
   VL_PIS: Decimal | str
   VL_BC_COFINS: Decimal | str
   VL_COFINS: Decimal | str
   VL_PIS_RET: Decimal | str
   VL_COFINS_RET: Decimal | str
   VL_ISS: Decimal | str
   RegistroA110: BlockList[RegistroA110]
   RegistroA111: BlockList[RegistroA111]
   RegistroA120: BlockList[RegistroA120]
   RegistroA170: BlockList[RegistroA170]


class RegistroA010(Registro):
   RegistroA100: BlockList[RegistroA100]
   CNPJ: str


class RegistroA001(BlocoInicial):
   RegistroA010: BlockList[RegistroA010]


class RegistroA990(Registro):
   QTD_LIN_A: int


class Registro0000(Registro):
   COD_VER: CodVer
   TIPO_ESCRIT: TipoEscrit
   IND_SIT_ESP: IndSitEsp
   NUM_REC_ANTERIOR: str  # //Número do Recibo da Escrituração anterior a ser retificada, utilizado quando TIPO_ESCRIT for igual a 1
   DT_INI: date  # //Data inicial das informações contidas no arquivo
   DT_FIN: date  # //Data final das informações contidas no arquivo
   NOME: str  # //Nome empresarial da pessoa jurídica
   CNPJ: str  # //Número de inscrição do estabelecimento matriz da pessoa jurídica no CNPJ
   UF: str  # //Sigla da Unidade da Federação da pessoa jurídica
   COD_MUN: int  # //Código do município do domicílio fiscal da pessoa jurídica, conforme a tabela IBGE
   SUFRAMA: str  # //Inscrição da pessoa jurídica na Suframa
   IND_NAT_PJ: IndNatPJ
   IND_ATIV: IndAtiv


class Registro0035(Registro):
   COD_SCP: str  # //Identificação da SCP
   DESC_SCP: str  # //Descrição da SCP
   INF_COMP: str  # //Informação Complementar


class Registro0100(Registro):
   NOME: str  # //Nome do contabilista
   CPF: str  # //Número de inscrição do contabilista no CPF
   CRC: str  # //Número de inscrição do contabilista no Conselho Regional de Contabilidade
   CNPJ: str  # //Número de inscrição do escritório de contabilidade no CNPJ, se houver
   CEP: str  # //Código de Endereçamento Postal.
   ENDERECO: str  # //Logradouro e endereço do imóvel
   NUM: str  # //Número do imóvel
   COMPL: str  # //Dados complementares do endereço
   BAIRRO: str  # //Bairro em que o imóvel está situado
   FONE: str  # //Número do telefone
   FAX: str  # //Número do fax
   EMAIL: str  # //Endereço do correio eletrônico
   COD_MUN: int  # //Código do município, conforme tabela IBGE


class Registro0111(Registro):
   REC_BRU_NCUM_TRIB_MI: Decimal  # //Receita Bruta Não-Cumulativa - Tributada no Mercado Interno
   REC_BRU_NCUM_NT_MI: Decimal  # //Receita Bruta Não-Cumulativa  Não Tributada no Mercado Interno (Vendas com suspensão, alíquota zero, isenção e sem incidência das contribuições)
   REC_BRU_NCUM_EXP: Decimal  # //Receita Bruta Não-Cumulativa  Exportação
   REC_BRU_CUM: Decimal  # //Receita Bruta Cumulativa
   REC_BRU_TOTAL: Decimal  # //Receita Bruta Total


class Registro0110(Registro):
   COD_INC_TRIB: CodIndIncTributaria  # //Código indicador da incidência tributária no período: 1  Escrituração de operações com incidência exclusivamente no regime não-cumulativo; 2  Escrituração de operações com incidência exclusivamente no regime cumulativo; 3  Escrituração de operações com incidência nos regimes não-cumulativo e cumulativo.
   IND_APRO_CRED: IndAproCred  # //Código indicador de método de apropriação de créditos comuns, no caso de incidência no regime nãocumulativo (COD_INC_TRIB = 1 ou 3): 1  Método de Apropriação Direta; 2  Método de Rateio Proporcional (Receita Bruta)
   COD_TIPO_CONT: CodIndTipoCon  # //Código indicador do Tipo de Contribuição Apurada no Período: 1  Apuração da Contribuição Exclusivamente a Alíquota Básica; 2  Apuração da Contribuição a Alíquotas Específicas (Diferenciadas e/ou por Unidade de Medida de Produto)
   IND_REG_CUM: CodIndCritEscrit
   Registro0111: Registro0111


class Registro0120(Registro):
   MES_DISPENSA: str  # //Mês de referência do ano-calendário da escrituração, dispensada da entrega. Formato MMAAAA
   INF_COMP: str  # //Informação complementar do registro.


class Registro0145(Registro):
   COD_INC_TRIB: str  # //Código indicador da incidência tributária no período:
   VL_REC_TOT: Decimal  # //Valor da Receita Bruta Total da Pessoa Jurídica no Período
   VL_REC_ATIV: Decimal  # //Valor da Receita Bruta da(s) Atividade(s) Sujeita(s) à Contribuição Previdenciária sobre a Receita Bruta
   VL_REC_DEMAIS_ATIV: Decimal  # //Valor da Receita Bruta da(s) Atividade(s) Sujeita(s) à Contribuição Previdenciária sobre a Remuneração
   INFO_COMPL: str  # //Informação complementar


class Registro0150(Registro):
   COD_PART: str  # // Código de identificação do participante no arquivo
   NOME: str  # // Nome pessoal ou empresarial do participante
   COD_PAIS: str  # // Código do país do participante, conforme a tabela indicada no item 3.2.1
   CNPJ: str  # // CNPJ do participante
   CPF: str  # // CPF do participante
   IE: str  # // Inscrição Estadual do participante
   COD_MUN: int  # // Código do município, conforme a tabela IBGE
   SUFRAMA: str  # // Número de inscrição do participante na Suframa
   ENDERECO: str  # // Logradouro e endereço do imóvel
   NUM: str  # // Número do imóvel
   COMPL: str  # // Dados complementares do endereço
   BAIRRO: str  # // Bairro em que o imóvel está situado


class Registro0190(Registro):
   UNID: str  # //Código da unidade de medida
   DESCR: str  # //Descrição da unidade de medida


class Registro0205(Registro):
   DESCR_ANT_ITEM: str  # //Descrição anterior do item
   DT_INI: date  # //Data inicial de utilização da descrição do item
   DT_FIM: date  # //Data final de utilização da descrição do item
   COD_ANT_ITEM: str  # //Código anterior do item com relação à última informação apresentada


class Registro0206(Registro):
   COD_COMB: str  # //Código do combustível, conforme tabela publicada pela ANP


class Registro0208(Registro):
   COD_TAB: IndCodIncidencia  # //Código indicador da Tabela de Incidência, conforme Anexo III do Decreto nº 6.707/08: 01  Tabela I; 02  Tabela II; 03  Tabela III; 04  Tabela IV; 05  Tabela V; 06  Tabela VI; 07  Tabela VII; 08 Tabela VIII; 09  Tabela IX; 10  Tabela X; 11  Tabela XI; 12  Tabela XII;
   COD_GRU: str  # //Código do grupo, conforme Anexo III do Decreto nº 6.707/08
   MARCA_COM: str  # //Marca Comercial


class Registro0200(Registro):
   COD_ITEM: str  # //Código do item
   DESCR_ITEM: str  # // Descrição do item
   COD_BARRA: str  # //Representação alfanumérico do código de barra do produto, se houver
   COD_ANT_ITEM: str  # //Código anterior do item com relação à última informação apresentada
   UNID_INV: str  # //Unidade de medida utilizada na quantificação de estoques
   TIPO_ITEM: TipoItem  # //Tipo do item  Atividades Industriais, Comerciais e Serviços: 00  Mercadoria para Revenda; 01  Matéria-Prima; 02  Embalagem; 03  Produto em Processo; 04  Produto Acabado; 05  Subproduto; 06  Produto Intermediário; 07  Material de Uso e Consumo; 08  Ativo Imobilizado; 09  Serviços; 10  Outros insumos; 99  Outras
   COD_NCM: str  # //Código da Nomenclatura Comum do Mercosul
   EX_IPI: str  # //Código EX, conforme a TIPI
   COD_GEN: str  # //Código do gênero do item, conforme a Tabela 4.2.1.
   COD_LST: str  # //Código do serviço conforme lista do Anexo I da Lei Complementar Federal nº 116/03
   ALIQ_ICMS: Decimal | str  # //Alíquota de ICMS aplicável ao item nas operações internas
   Registro0205: BlockList[Registro0205]
   Registro0206: Registro0206
   Registro0208: Registro0208


class Registro0400(Registro):
   COD_NAT: str  # //Código da natureza da operação/prestação
   DESCR_NAT: str  # //Descrição da natureza da operação/prestação


class Registro0450(Registro):
   COD_INF: str  # //Código da informação complementar do documento fiscal.
   TXT: str  # //Texto livre da informação complementar existente no documento fiscal, inclusive espécie de normas legais, poder normativo, número, capitulação, data e demais referências pertinentes com indicação referentes ao tributo


class Registro0140(Registro):
   COD_EST: str  # // Código de identificação do estabelecimento
   NOME: str  # // Nome empresarial do estabelecimento
   CNPJ: str  # // Número de inscrição do estabelecimento no CNPJ
   UF: str  # // Sigla da unidade da federação do estabelecimento
   IE: str  # // Inscrição Estadual do estabelecimento, se contribuinte de ICMS
   COD_MUN: int  # // Código do município do domicílio fiscal do estabelecimento,conforme a tabela IBGE
   IM: str  # // Inscrição Municipal do estabelecimento, se contribuinte do ISS
   SUFRAMA: str  # // Inscrição do estabelecimento na Suframa
   Registro0145: Registro0145
   Registro0150: BlockList[Registro0150]
   Registro0190: BlockList[Registro0190]
   Registro0200: BlockList[Registro0200]
   Registro0400: BlockList[Registro0400]
   Registro0450: BlockList[Registro0450]


class Registro0500(Registro):
   DT_ALT: date  # //Data da inclusão/alteração
   COD_NAT_CC: NaturezaConta  # //Código da natureza da conta/grupo de contas: 01 - Contas de ativo; 02 - Contas de passivo; 03 - Patrimônio líquido; 04 - Contas de resultado; 05 - Contas de compensação; 09 - Outras
   IND_CTA: IndCTA  # //Indicador do tipo de conta: S - Sintética (grupo de contas); A - Analítica (conta)
   NIVEL: str  # //Nível da conta analítica/grupo de contas
   COD_CTA: str  # //Código da conta analítica/grupo de contas
   NOME_CTA: str  # //Nome da conta analítica/grupo de contas
   COD_CTA_REF: str  # //Código da conta correlacionada no Plano de Contas Referenciado, publicado pela RFB
   CNPJ_EST: str  # //CNPJ do estabelecimento, no caso da conta informada no campo COD_CTA ser específica de um estabelecimento


class Registro0600(Registro):
   DT_ALT: date  # //Data da inclusão/alteração
   COD_CCUS: str  # //Código do centro de custos
   CCUS: str  # //Nome do centro de custos.


class Registro0900(Registro):
   REC_TOTAL_BLOCO_A: float  # /// Receita total referente aos registros escriturados no Bloco A
   REC_NRB_BLOCO_A: Decimal | str  # /// Parcela da receita total escriturada no Bloco A (Campo 02), não classificada como receita bruta
   REC_TOTAL_BLOCO_C: float  # /// Receita total referente aos registros escriturados no Bloco C
   REC_NRB_BLOCO_C: Decimal | str  # /// Parcela da receita total escriturada no Bloco C (Campo 04), não classificada como receita bruta
   REC_TOTAL_BLOCO_D: float  # /// Receita total referente aos registros escriturados no Bloco D
   REC_NRB_BLOCO_D: Decimal | str  # /// Parcela da receita total escriturada no Bloco D (Campo 06), não classificada como receita bruta
   REC_TOTAL_BLOCO_F: float  # /// Receita total referente aos registros escriturados no Bloco F
   REC_NRB_BLOCO_F: Decimal | str  # /// Parcela da receita total escriturada no Bloco F (Campo 08), não classificada como receita bruta
   REC_TOTAL_BLOCO_I: float  # /// Receita total referente aos registros escriturados no Bloco I
   REC_NRB_BLOCO_I: Decimal | str  # /// Parcela da receita total escriturada no Bloco I (Campo 10) não classificada como receita bruta
   REC_TOTAL_BLOCO_1: float  # /// Receita total referente aos registros escriturados no Bloco 1 (RET)
   REC_NRB_BLOCO_1: Decimal | str  # /// Parcela da receita total escriturada no Bloco 1 (Campo 12), não classificada como receita bruta
   REC_TOTAL_PERIODO: float  # /// Receita bruta total (Soma dos Campos 02, 04, 06, 08, 10 e 12)
   REC_TOTAL_NRB_PERIODO: Decimal | str  # /// Parcela da receita total escriturada (Campo 14), não classificada como receita bruta (Soma dos Campos 03, 05, 07, 09, 11 e 13)  public


class Registro0001(BlocoInicial):
   Registro0035: BlockList[Registro0035]
   Registro0100: BlockList[Registro0100]
   Registro0110: Registro0110
   Registro0120: BlockList[Registro0120]  # //Implementado por Fábio Gabriel - 29/11/2012
   Registro0140: BlockList[Registro0140]
   Registro0500: BlockList[Registro0500]
   Registro0600: BlockList[Registro0600]
   Registro0900: Registro0900


class Registro0990(Registro):
   QTD_LIN_0: int  # //Quantidade total de linhas do Bloco 0


class Bloco_0(BlocoSPED):
   Registro0000: Registro0000  # /// BLOCO 0 - Registro0000
   Registro0001: Registro0001  # /// BLOCO 0 - Registro0001
   Registro0990: Registro0990  # /// BLOCO 0 - Registro0990
   Registro0035Count: int
   Registro0100Count: int
   Registro0110Count: int
   Registro0111Count: int
   Registro0120Count: int  # //Adicionado por Fábio Gabriel - 29/11/2012
   Registro0140Count: int
   Registro0145Count: int
   Registro0150Count: int
   Registro0190Count: int
   Registro0200Count: int
   Registro0205Count: int
   Registro0206Count: int
   Registro0208Count: int
   Registro0400Count: int
   Registro0450Count: int
   Registro0500Count: int
   Registro0600Count: int
   Registro0900Count: int  # //Adicionado por Fábio Gabriel - 29/11/2012


class Bloco_A(BlocoSPED):
   Bloco_0: Bloco_0
   RegistroA001: RegistroA001  # /// BLOCO 0 - Registro0001
   RegistroA990: RegistroA990  # /// BLOCO 0 - Registro0990
   RegistroA010Count: int
   RegistroA100Count: int
   RegistroA110Count: int
   RegistroA111Count: int
   RegistroA120Count: int
   RegistroA170Count: int


class EventsBloco_C:
   pass


class Registro1001(BlocoInicial):
   Registro1010: BlockList[Registro1010]  # // NIVEL 2
   Registro1020: BlockList[Registro1020]  # // NIVEL 2
   Registro1050: BlockList[Registro1050]  # // NIVEL 2
   Registro1100: BlockList[Registro1100]  # // NIVEL 2
   Registro1200: BlockList[Registro1200]  # // NIVEL 2
   Registro1300: BlockList[Registro1300]  # // NIVEL 2
   Registro1500: BlockList[Registro1500]  # // NIVEL 2
   Registro1600: BlockList[Registro1600]  # // NIVEL 2
   Registro1700: BlockList[Registro1700]  # // NIVEL 2
   Registro1800: BlockList[Registro1800]  # // NIVEL 2
   Registro1900: BlockList[Registro1900]  # // NIVEL 2


class Registro1990(Registro):
   QTD_LIN_1: int


class Bloco_1(BlocoSPED):
   Bloco_0: Bloco_0
   Registro1001: Registro1001  # /// BLOCO 1 - Registro1001
   Registro1990: Registro1990  # /// BLOCO 1 - Registro1990
   Registro1010Count: int
   Registro1011Count: int
   Registro1020Count: int
   Registro1050Count: int
   Registro1100Count: int
   Registro1101Count: int
   Registro1102Count: int
   Registro1200Count: int
   Registro1210Count: int
   Registro1220Count: int
   Registro1300Count: int
   Registro1500Count: int
   Registro1501Count: int
   Registro1502Count: int
   Registro1600Count: int
   Registro1610Count: int
   Registro1620Count: int
   Registro1700Count: int
   Registro1800Count: int
   Registro1809Count: int
   Registro1900Count: int


class Registro9001(BlocoInicial):
   Registro9900: BlockList[Registro9900]


class Registro9900(Registro):
   REG_BLC: str
   QTD_REG_BLC: int


class Registro9990(Registro):
   QTD_LIN_9: int


class Registro9999(Registro):
   QTD_LIN: int


class Bloco_9(BlocoSPED):
   Registro9001: Registro9001  # /// BLOCO 9 - Registro9001
   Registro9900: BlockList[Registro9900]  # /// BLOCO 9 - Lista de Registro9900
   Registro9990: Registro9990  # /// BLOCO 9 - Registro9990
   Registro9999: Registro9999  # /// BLOCO 9 - Registro9999


class RegistroC001(BlocoInicial):
   RegistroC010: BlockList[RegistroC010]


class RegistroC990(Registro):
   QTD_LIN_C: int


class Bloco_C(BlocoSPED):
   Bloco_0: Bloco_0
   RegistroC001: RegistroC001  # /// BLOCO 0 - Registro0001
   RegistroC990: RegistroC990  # /// BLOCO 0 - Registro0990
   RegistroC010Count: int
   RegistroC100Count: int
   RegistroC110Count: int
   RegistroC111Count: int
   RegistroC120Count: int
   RegistroC170Count: int
   RegistroC175Count: int
   RegistroC180Count: int
   RegistroC181Count: int
   RegistroC185Count: int
   RegistroC188Count: int
   RegistroC190Count: int
   RegistroC191Count: int
   RegistroC195Count: int
   RegistroC198Count: int
   RegistroC199Count: int
   RegistroC380Count: int
   RegistroC381Count: int
   RegistroC385Count: int
   RegistroC395Count: int
   RegistroC396Count: int
   RegistroC400Count: int
   RegistroC405Count: int
   RegistroC481Count: int
   RegistroC485Count: int
   RegistroC489Count: int
   RegistroC490Count: int
   RegistroC491Count: int
   RegistroC495Count: int
   RegistroC499Count: int
   RegistroC500Count: int
   RegistroC501Count: int
   RegistroC505Count: int
   RegistroC509Count: int
   RegistroC600Count: int
   RegistroC601Count: int
   RegistroC605Count: int
   RegistroC609Count: int
   RegistroC800Count: int
   RegistroC810Count: int
   RegistroC820Count: int
   RegistroC830Count: int
   RegistroC860Count: int
   RegistroC870Count: int
   RegistroC880Count: int
   RegistroC890Count: int


class RegistroD001(BlocoInicial):
   RegistroD010: BlockList[RegistroD010]


class RegistroD990(Registro):
   QTD_LIN_D: int


class Bloco_D(BlocoSPED):
   Bloco_0: Bloco_0
   RegistroD001: RegistroD001  # /// BLOCO D - RegistroD001
   RegistroD990: RegistroD990  # /// BLOCO D - RegistroD990
   RegistroD010Count: int
   RegistroD100Count: int
   RegistroD101Count: int
   RegistroD105Count: int
   RegistroD111Count: int
   RegistroD200Count: int
   RegistroD201Count: int
   RegistroD205Count: int
   RegistroD209Count: int
   RegistroD300Count: int
   RegistroD309Count: int
   RegistroD350Count: int
   RegistroD359Count: int
   RegistroD500Count: int
   RegistroD501Count: int
   RegistroD505Count: int
   RegistroD509Count: int
   RegistroD600Count: int
   RegistroD601Count: int
   RegistroD605Count: int
   RegistroD609Count: int


class RegistroF001(BlocoInicial):
   RegistroF010: BlockList[RegistroF010]


class RegistroF990(Registro):
   QTD_LIN_F: int


class Bloco_F(BlocoSPED):
   Bloco_0: Bloco_0
   RegistroF001: RegistroF001  # /// BLOCO F - RegistroF001
   RegistroF990: RegistroF990  # /// BLOCO F - RegistroF990
   RegistroF010Count: int
   RegistroF100Count: int
   RegistroF111Count: int
   RegistroF120Count: int
   RegistroF129Count: int
   RegistroF130Count: int
   RegistroF139Count: int
   RegistroF150Count: int
   RegistroF200Count: int
   RegistroF205Count: int
   RegistroF210Count: int
   RegistroF211Count: int
   RegistroF500Count: int
   RegistroF509Count: int
   RegistroF510Count: int
   RegistroF519Count: int
   RegistroF525Count: int
   RegistroF550Count: int
   RegistroF559Count: int
   RegistroF560Count: int
   RegistroF569Count: int
   RegistroF600Count: int
   RegistroF700Count: int
   RegistroF800Count: int


class RegistroI001(BlocoInicial):
   RegistroI010: BlockList[RegistroI010]


class RegistroI990(Registro):
   QTD_LIN_I: int


class Bloco_I(BlocoSPED):
   Bloco_0: Bloco_0
   RegistroI001: RegistroI001  # /// BLOCO I - RegistroI001
   RegistroI990: RegistroI990  # /// BLOCO I - RegistroI990
   RegistroI010Count: int
   RegistroI100Count: int
   RegistroI199Count: int
   RegistroI200Count: int
   RegistroI299Count: int
   RegistroI300Count: int
   RegistroI399Count: int


class RegistroM105(Registro):
   NAT_BC_CRED: BaseCalculoCredito
   CST_PIS: SituacaoTribPIS
   VL_BC_PIS_TOT: Decimal | str
   VL_BC_PIS_CUM: Decimal | str
   VL_BC_PIS_NC: Decimal | str
   VL_BC_PIS: Decimal | str
   QUANT_BC_PIS_TOT: Decimal | str
   QUANT_BC_PIS: Decimal | str
   DESC_CRED: str


class RegistroM115(Registro):
   DET_VALOR_AJ: Decimal
   CST_PIS: SituacaoTribPIS
   DET_BC_CRED: Decimal
   DET_ALIQ: Decimal
   DT_OPER_AJ: date
   DESC_AJ: str
   COD_CTA: str
   INFO_COMPL: str


class RegistroM110(Registro):
   IND_AJ: IndAJ
   VL_AJ: Decimal
   COD_AJ: CodAj
   NUM_DOC: str
   DESCR_AJ: str
   DT_REF: date
   RegistroM115: BlockList[RegistroM115]


class RegistroM100(Registro):
   COD_CRED: str
   IND_CRED_ORI: IndCredOri
   VL_BC_PIS: Decimal | str
   ALIQ_PIS: Decimal | str
   QUANT_BC_PIS: Decimal | str
   ALIQ_PIS_QUANT: Decimal | str
   VL_CRED: Decimal
   VL_AJUS_ACRES: Decimal
   VL_AJUS_REDUC: Decimal
   VL_CRED_DIF: Decimal
   VL_CRED_DISP: Decimal
   IND_DESC_CRED: IndDescCred
   VL_CRED_DESC: Decimal | str
   SLD_CRED: Decimal
   RegistroM105: BlockList[RegistroM105]  # // NIVEL 3
   RegistroM110: BlockList[RegistroM110]  # // NIVEL 3


class RegistroM205(Registro):
   NUM_CAMPO: str
   COD_REC: str
   VL_DEBITO: Decimal


class RegistroM211(Registro):
   IND_TIP_COOP: IndTipCoop
   VL_BC_CONT_ANT_EXC_COOP: Decimal
   VL_EXC_COOP_GER: Decimal
   VL_EXC_ESP_COOP: Decimal
   VL_BC_CONT: Decimal


class RegistroM215(Registro):
   IND_AJ_BC: IndAJ
   VL_AJ_BC: Decimal
   COD_AJ_BC: TabCodAjBaseCalcContrib
   NUM_DOC: str
   DESCR_AJ_BC: str
   DT_REF: date
   COD_CTA: str
   CNPJ: str
   INFO_COMPL: str


class RegistroM225(Registro):
   DET_VALOR_AJ: Decimal
   CST_PIS: SituacaoTribPIS
   DET_BC_CRED: Decimal
   DET_ALIQ: Decimal
   DT_OPER_AJ: date
   DESC_AJ: str
   COD_CTA: str
   INFO_COMPL: str


class RegistroM220(Registro):
   IND_AJ: IndAJ
   VL_AJ: Decimal
   COD_AJ: CodAj
   NUM_DOC: str
   DESCR_AJ: str
   DT_REF: date
   RegistroM225: BlockList[RegistroM225]


class RegistroM230(Registro):
   CNPJ: str
   VL_VEND: Decimal
   VL_NAO_RECEB: Decimal
   VL_CONT_DIF: Decimal
   VL_CRED_DIF: Decimal
   COD_CRED: str


class RegistroM210(Registro):
   COD_CONT: CodCont
   VL_REC_BRT: Decimal
   VL_BC_CONT: Decimal
   VL_AJUS_ACRES_BC_PIS: Decimal
   VL_AJUS_REDUC_BC_PIS: Decimal
   VL_BC_CONT_AJUS: Decimal
   ALIQ_PIS: Decimal | str
   QUANT_BC_PIS: Decimal | str
   ALIQ_PIS_QUANT: Decimal | str
   VL_CONT_APUR: Decimal
   VL_AJUS_ACRES: Decimal
   VL_AJUS_REDUC: Decimal
   VL_CONT_DIFER: Decimal | str
   VL_CONT_DIFER_ANT: Decimal | str
   VL_CONT_PER: Decimal
   RegistroM211: RegistroM211  # // NIVEL 4
   RegistroM215: BlockList[RegistroM215]  # // NIVEL 4
   RegistroM220: BlockList[RegistroM220]  # // NIVEL 4
   RegistroM230: BlockList[RegistroM230]  # // NIVEL 4


class RegistroM200(Registro):
   VL_TOT_CONT_NC_PER: Decimal
   VL_TOT_CRED_DESC: Decimal
   VL_TOT_CRED_DESC_ANT: Decimal
   VL_TOT_CONT_NC_DEV: Decimal
   VL_RET_NC: Decimal
   VL_OUT_DED_NC: Decimal
   VL_CONT_NC_REC: Decimal
   VL_TOT_CONT_CUM_PER: Decimal
   VL_RET_CUM: Decimal
   VL_OUT_DED_CUM: Decimal
   VL_CONT_CUM_REC: Decimal
   VL_TOT_CONT_REC: Decimal
   RegistroM205: BlockList[RegistroM205]  # // NIVEL 3
   RegistroM210: BlockList[RegistroM210]  # // NIVEL 3


class RegistroM300(Registro):
   COD_CONT: CodCont
   VL_CONT_APUR_DIFER: Decimal
   NAT_CRED_DESC: NatCredDesc
   VL_CRED_DESC_DIFER: Decimal
   VL_CONT_DIFER_ANT: Decimal
   PER_APUR: str
   DT_RECEB: date


class RegistroM350(Registro):
   VL_TOT_FOL: Decimal
   VL_EXC_BC: Decimal
   VL_TOT_BC: Decimal
   ALIQ_PIS_FOL: Decimal
   VL_TOT_CONT_FOL: Decimal


class RegistroM410(Registro):
   NAT_REC: str
   VL_REC: Decimal
   COD_CTA: str
   DESC_COMPL: str


class RegistroM400(Registro):
   CST_PIS: SituacaoTribPIS
   VL_TOT_REC: Decimal
   COD_CTA: str
   DESC_COMPL: str
   RegistroM410: BlockList[RegistroM410]  # // NIVEL 3


class RegistroM505(Registro):
   NAT_BC_CRED: BaseCalculoCredito
   CST_COFINS: SituacaoTribCOFINS
   VL_BC_COFINS_TOT: Decimal | str
   VL_BC_COFINS_CUM: Decimal | str
   VL_BC_COFINS_NC: Decimal | str
   VL_BC_COFINS: Decimal | str
   QUANT_BC_COFINS_TOT: Decimal | str
   QUANT_BC_COFINS: Decimal | str
   DESC_CRED: str


class RegistroM515(Registro):
   DET_VALOR_AJ: Decimal
   CST_COFINS: SituacaoTribCOFINS
   DET_BC_CRED: Decimal
   DET_ALIQ: Decimal
   DT_OPER_AJ: date
   DESC_AJ: str
   COD_CTA: str
   INFO_COMPL: str


class RegistroM510(Registro):
   IND_AJ: IndAJ
   VL_AJ: Decimal
   COD_AJ: CodAj
   NUM_DOC: str
   DESCR_AJ: str
   DT_REF: date
   RegistroM515: BlockList[RegistroM515]


class RegistroM500(Registro):
   COD_CRED: str
   IND_CRED_ORI: IndCredOri
   VL_BC_COFINS: Decimal | str
   ALIQ_COFINS: Decimal | str
   QUANT_BC_COFINS: Decimal | str
   ALIQ_COFINS_QUANT: Decimal | str
   VL_CRED: Decimal
   VL_AJUS_ACRES: Decimal
   VL_AJUS_REDUC: Decimal
   VL_CRED_DIFER: Decimal
   VL_CRED_DISP: Decimal
   IND_DESC_CRED: IndDescCred
   VL_CRED_DESC: Decimal | str
   SLD_CRED: Decimal
   RegistroM505: BlockList[RegistroM505]  # // NIVEL 3
   RegistroM510: BlockList[RegistroM510]  # // NIVEL 3


class RegistroM605(Registro):
   NUM_CAMPO: str
   COD_REC: str
   VL_DEBITO: Decimal


class RegistroM611(Registro):
   IND_TIP_COOP: IndTipCoop
   VL_BC_CONT_ANT_EXC_COOP: Decimal
   VL_EXC_COOP_GER: Decimal
   VL_EXC_ESP_COOP: Decimal
   VL_BC_CONT: Decimal


class RegistroM615(Registro):
   IND_AJ_BC: IndAJ
   VL_AJ_BC: Decimal
   COD_AJ_BC: TabCodAjBaseCalcContrib
   NUM_DOC: str
   DESCR_AJ_BC: str
   DT_REF: date
   COD_CTA: str
   CNPJ: str
   INFO_COMPL: str


class RegistroM625(Registro):
   DET_VALOR_AJ: Decimal
   CST_COFINS: SituacaoTribCOFINS
   DET_BC_CRED: Decimal
   DET_ALIQ: Decimal
   DT_OPER_AJ: date
   DESC_AJ: str
   COD_CTA: str
   INFO_COMPL: str


class RegistroM620(Registro):
   IND_AJ: IndAJ
   VL_AJ: Decimal
   COD_AJ: CodAj
   NUM_DOC: str
   DESCR_AJ: str
   DT_REF: date
   RegistroM625: BlockList[RegistroM625]


class RegistroM630(Registro):
   CNPJ: str
   VL_VEND: Decimal
   VL_NAO_RECEB: Decimal
   VL_CONT_DIF: Decimal
   VL_CRED_DIF: Decimal
   COD_CRED: str


class RegistroM610(Registro):
   COD_CONT: CodCont
   VL_REC_BRT: Decimal
   VL_BC_CONT: Decimal
   VL_AJUS_ACRES_BC_COFINS: Decimal
   VL_AJUS_REDUC_BC_COFINS: Decimal
   VL_BC_CONT_AJUS: Decimal
   ALIQ_COFINS: Decimal | str
   QUANT_BC_COFINS: Decimal | str
   ALIQ_COFINS_QUANT: Decimal | str
   VL_CONT_APUR: Decimal
   VL_AJUS_ACRES: Decimal
   VL_AJUS_REDUC: Decimal
   VL_CONT_DIFER: Decimal | str
   VL_CONT_DIFER_ANT: Decimal | str
   VL_CONT_PER: Decimal
   RegistroM611: RegistroM611  # // NIVEL 4
   RegistroM615: BlockList[RegistroM615]  # // NIVEL 4
   RegistroM620: BlockList[RegistroM620]  # // NIVEL 4
   RegistroM630: BlockList[RegistroM630]  # // NIVEL 4


class RegistroM600(Registro):
   VL_TOT_CONT_NC_PER: Decimal
   VL_TOT_CRED_DESC: Decimal
   VL_TOT_CRED_DESC_ANT: Decimal
   VL_TOT_CONT_NC_DEV: Decimal
   VL_RET_NC: Decimal
   VL_OUT_DED_NC: Decimal
   VL_CONT_NC_REC: Decimal
   VL_TOT_CONT_CUM_PER: Decimal
   VL_RET_CUM: Decimal
   VL_OUT_DED_CUM: Decimal
   VL_CONT_CUM_REC: Decimal
   VL_TOT_CONT_REC: Decimal
   RegistroM605: BlockList[RegistroM605]
   RegistroM610: BlockList[RegistroM610]  # // NIVEL 3


class RegistroM700(Registro):
   COD_CONT: CodCont
   VL_CONT_APUR_DIFER: Decimal
   NAT_CRED_DESC: NatCredDesc
   VL_CRED_DESC_DIFER: Decimal
   VL_CONT_DIFER_ANT: Decimal
   PER_APUR: str
   DT_RECEB: date


class RegistroM810(Registro):
   NAT_REC: str
   VL_REC: Decimal
   COD_CTA: str
   DESC_COMPL: str


class RegistroM800(Registro):
   CST_COFINS: SituacaoTribCOFINS
   VL_TOT_REC: Decimal
   COD_CTA: str
   DESC_COMPL: str
   RegistroM810: BlockList[RegistroM810]  # // NIVEL 3


class RegistroM001(BlocoInicial):
   RegistroM100: BlockList[RegistroM100]  # // NIVEL 2
   RegistroM200: RegistroM200  # // NIVEL 2
   RegistroM300: BlockList[RegistroM300]  # // NIVEL 2
   RegistroM350: RegistroM350  # // NIVEL 2
   RegistroM400: BlockList[RegistroM400]  # // NIVEL 2
   RegistroM500: BlockList[RegistroM500]  # // NIVEL 2
   RegistroM600: RegistroM600  # // NIVEL 2
   RegistroM700: BlockList[RegistroM700]  # // NIVEL 2
   RegistroM800: BlockList[RegistroM800]  # // NIVEL 2


class RegistroM990(Registro):
   QTD_LIN_M: int


class Bloco_M(BlocoSPED):
   Bloco_0: Bloco_0
   RegistroM001: RegistroM001  # /// BLOCO M - RegistroM001
   RegistroM990: RegistroM990  # /// BLOCO M - RegistroM990
   RegistroM100Count: int
   RegistroM105Count: int
   RegistroM110Count: int
   RegistroM115Count: int
   RegistroM200Count: int
   RegistroM205Count: int
   RegistroM210Count: int
   RegistroM211Count: int
   RegistroM215Count: int
   RegistroM220Count: int
   RegistroM225Count: int
   RegistroM230Count: int
   RegistroM300Count: int
   RegistroM350Count: int
   RegistroM400Count: int
   RegistroM410Count: int
   RegistroM500Count: int
   RegistroM505Count: int
   RegistroM510Count: int
   RegistroM515Count: int
   RegistroM600Count: int
   RegistroM605Count: int
   RegistroM610Count: int
   RegistroM611Count: int
   RegistroM615Count: int
   RegistroM620Count: int
   RegistroM625Count: int
   RegistroM630Count: int
   RegistroM700Count: int
   RegistroM800Count: int
   RegistroM810Count: int


class RegistroP001(BlocoInicial):
   RegistroP010: BlockList[RegistroP010]
   RegistroP200: BlockList[RegistroP200]


class RegistroP990(Registro):
   QTD_LIN_P: int


class Bloco_P(BlocoSPED):
   Bloco_0: Bloco_0
   RegistroP001: RegistroP001
   RegistroP990: RegistroP990
   RegistroP010Count: int
   RegistroP100Count: int
   RegistroP110Count: int
   RegistroP199Count: int
   RegistroP200Count: int
   RegistroP210Count: int


class SPEDPisCofins:
   Conteudo: BlockList[str]
   DT_INI: date
   DT_FIN: date
   Bloco_0: Bloco_0
   Bloco_1: Bloco_1
   Bloco_9: Bloco_9
   Bloco_A: Bloco_A
   Bloco_C: Bloco_C
   Bloco_D: Bloco_D
   Bloco_F: Bloco_F
   Bloco_I: Bloco_I
   Bloco_M: Bloco_M
   Bloco_P: Bloco_P  # /// Método do evento OnError
   Path: str  # /// Path do arquivo a ser gerado
   Arquivo: str
   LinhasBuffer: int
   Delimitador: str
   ReplaceDelimitador: bool
   TrimString: bool
   CurMascara: str
   EventsBloco_C: EventsBloco_C


class RegistroD101(Registro):
   IND_NAT_FRT: NaturezaFrtContratado
   VL_ITEM: Decimal
   CST_PIS: SituacaoTribPIS
   NAT_BC_CRED: BaseCalculoCredito
   VL_BC_PIS: Decimal
   ALIQ_PIS: Decimal
   VL_PIS: Decimal
   COD_CTA: str


class RegistroD105(Registro):
   IND_NAT_FRT: NaturezaFrtContratado
   VL_ITEM: Decimal
   CST_COFINS: SituacaoTribCOFINS
   NAT_BC_CRED: BaseCalculoCredito
   VL_BC_COFINS: Decimal
   ALIQ_COFINS: Decimal
   VL_COFINS: Decimal
   COD_CTA: str


class RegistroD111(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroD100(Registro):
   IND_OPER: str
   IND_EMIT: IndicadorEmitenteDF
   COD_PART: str
   COD_MOD: str
   COD_SIT: SituacaoDF
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
   IND_FRT: TipoFrete
   VL_SERV: Decimal
   VL_BC_ICMS: Decimal
   VL_ICMS: Decimal
   VL_NT: Decimal
   COD_INF: str
   COD_CTA: str
   RegistroD101: BlockList[RegistroD101]
   RegistroD105: BlockList[RegistroD105]
   RegistroD111: BlockList[RegistroD111]


class RegistroD201(Registro):
   CST_PIS: SituacaoTribPIS
   VL_ITEM: Decimal
   VL_BC_PIS: Decimal
   ALIQ_PIS: Decimal
   VL_PIS: Decimal
   COD_CTA: str


class RegistroD205(Registro):
   CST_COFINS: SituacaoTribCOFINS
   VL_ITEM: Decimal
   VL_BC_COFINS: Decimal
   ALIQ_COFINS: Decimal
   VL_COFINS: Decimal
   COD_CTA: str


class RegistroD209(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroD200(Registro):
   COD_MOD: str
   COD_SIT: SituacaoDF
   SER: str
   SUB: str
   NUM_DOC_INI: int
   NUM_DOC_FIN: int
   CFOP: int
   DT_REF: date
   VL_DOC: Decimal
   VL_DESC: Decimal
   RegistroD201: BlockList[RegistroD201]
   RegistroD205: BlockList[RegistroD205]
   RegistroD209: BlockList[RegistroD209]


class RegistroD309(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroD300(Registro):
   COD_MOD: str
   SER: str
   SUB: int
   NUM_DOC_INI: int
   NUM_DOC_FIN: int
   CFOP: int
   DT_REF: date
   VL_DOC: Decimal
   VL_DESC: Decimal
   CST_PIS: SituacaoTribPIS
   VL_BC_PIS: Decimal
   ALIQ_PIS: Decimal
   VL_PIS: Decimal
   CST_COFINS: SituacaoTribCOFINS
   VL_BC_COFINS: Decimal
   ALIQ_COFINS: Decimal
   VL_COFINS: Decimal
   COD_CTA: str
   RegistroD309: BlockList[RegistroD309]


class RegistroD359(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroD350(Registro):
   COD_MOD: str
   ECF_MOD: str
   ECF_FAB: str
   DT_DOC: date
   CRO: int
   CRZ: int
   NUM_COO_FIN: int
   GT_FIN: Decimal
   VL_BRT: Decimal
   CST_PIS: SituacaoTribPIS
   VL_BC_PIS: Decimal | str
   ALIQ_PIS: Decimal | str
   QUANT_BC_PIS: Decimal | str
   ALIQ_PIS_QUANT: Decimal | str
   VL_PIS: Decimal | str
   CST_COFINS: SituacaoTribCOFINS
   VL_BC_COFINS: Decimal | str
   ALIQ_COFINS: Decimal | str
   QUANT_BC_COFINS: Decimal | str
   ALIQ_COFINS_QUANT: Decimal | str
   VL_COFINS: Decimal | str
   COD_CTA: str
   RegistroD359: BlockList[RegistroD359]


class RegistroD501(Registro):
   CST_PIS: SituacaoTribPIS
   VL_ITEM: Decimal
   NAT_BC_CRED: BaseCalculoCredito
   VL_BC_PIS: Decimal
   ALIQ_PIS: Decimal
   VL_PIS: Decimal
   COD_CTA: str


class RegistroD505(Registro):
   CST_COFINS: SituacaoTribCOFINS
   VL_ITEM: Decimal
   NAT_BC_CRED: BaseCalculoCredito
   VL_BC_COFINS: Decimal
   ALIQ_COFINS: Decimal
   VL_COFINS: Decimal
   COD_CTA: str


class RegistroD509(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroD500(Registro):
   IND_OPER: IndicadorTpOperacao
   IND_EMIT: IndicadorEmitenteDF
   COD_PART: str
   COD_MOD: str
   COD_SIT: SituacaoDF
   SER: str
   SUB: int
   NUM_DOC: int
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
   CHV_DOC_E: str
   RegistroD501: BlockList[RegistroD501]
   RegistroD505: BlockList[RegistroD505]
   RegistroD509: BlockList[RegistroD509]


class RegistroD601(Registro):
   COD_CLASS: int
   VL_ITEM: Decimal | str
   VL_DESC: Decimal | str
   CST_PIS: SituacaoTribPIS
   VL_BC_PIS: Decimal | str
   ALIQ_PIS: Decimal | str
   VL_PIS: Decimal | str
   COD_CTA: str


class RegistroD605(Registro):
   COD_CLASS: int
   VL_ITEM: Decimal | str
   VL_DESC: Decimal | str
   CST_COFINS: SituacaoTribCOFINS
   VL_BC_COFINS: Decimal | str
   ALIQ_COFINS: Decimal | str
   VL_COFINS: Decimal | str
   COD_CTA: str


class RegistroD609(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroD600(Registro):
   COD_MOD: str
   COD_MUN: int
   SER: str
   SUB: int
   IND_REC: IndRec
   QTD_CONS: int
   DT_DOC_INI: date
   DT_DOC_FIN: date
   VL_DOC: Decimal
   VL_DESC: Decimal
   VL_SERV: Decimal
   VL_SERV_NT: Decimal
   VL_TERC: Decimal
   VL_DA: Decimal
   VL_BC_ICMS: Decimal
   VL_ICMS: Decimal
   VL_PIS: Decimal
   VL_COFINS: Decimal
   RegistroD601: BlockList[RegistroD601]
   RegistroD605: BlockList[RegistroD605]
   RegistroD609: BlockList[RegistroD609]


class RegistroD010(Registro):
   CNPJ: str
   RegistroD100: BlockList[RegistroD100]
   RegistroD200: BlockList[RegistroD200]
   RegistroD300: BlockList[RegistroD300]
   RegistroD350: BlockList[RegistroD350]
   RegistroD500: BlockList[RegistroD500]
   RegistroD600: BlockList[RegistroD600]


class Registro1011(Registro):
   REG_REF: str  # /// Registro da escrituração que terá o detalhamento das contribuições sociais com exigibilidade suspensa (Blocos A, C, D, F e I, 1800)
   CHAVE_DOC: str  # /// Chave do documento eletrônico
   COD_PART: str  # /// Código do participante (Campo 02 do Registro 0150)
   COD_ITEM: str  # /// Código do item (campo 02 do Registro 0200)
   DT_OPER: date  # /// Data da Operação (ddmmaaaa)
   VL_OPER: Decimal  # /// Valor da Operação/Item
   CST_PIS: int  # /// Código da Situação Tributária conforme escrituração, referente ao PIS/PASEP, conforme a Tabela indicada no item 4.3.3.
   VL_BC_PIS: Decimal | str  # /// Base de cálculo do PIS/PASEP, conforme escrituração
   ALIQ_PIS: Decimal | str  # /// Alíquota do PIS/PASEP, conforme escrituração
   VL_PIS: Decimal | str  # /// Valor do PIS/PASEP, conforme escrituração
   CST_COFINS: int  # /// Código da Situação Tributária conforme escrituração, referente a COFINS, conforme a Tabela indicada no item 4.3.4.
   VL_BC_COFINS: Decimal | str  # /// Base de cálculo da COFINS, conforme escrituração
   ALIQ_COFINS: Decimal | str  # /// Alíquota da COFINS, conforme escrituração
   VL_COFINS: Decimal | str  # /// Valor da COFINS, conforme escrituração
   CST_PIS_SUSP: int  # /// Código da Situação Tributária conforme decisão judicial, referente ao PIS/PASEP, conforme a Tabela indicada no item 4.3.3.
   VL_BC_PIS_SUSP: Decimal | str  # /// Base de cálculo do PIS/PASEP, conforme decisão judicial
   ALIQ_PIS_SUSP: Decimal | str  # /// Alíquota do PIS/PASEP, conforme decisão judicial
   VL_PIS_SUSP: Decimal | str  # /// Valor do PIS/PASEP, conforme decisão judicial
   CST_COFINS_SUSP: int  # /// Código da Situação Tributária conforme decisão judicial, referente a COFINS, conforme a Tabela indicada no item 4.3.4.
   VL_BC_COFINS_SUSP: Decimal | str  # /// Base de cálculo da COFINS, conforme decisão judicial
   ALIQ_COFINS_SUSP: Decimal | str  # /// Alíquota da COFINS, conforme decisão judicial
   VL_COFINS_SUSP: Decimal | str  # /// Valor da COFINS, conforme decisão judicial
   COD_CTA: str  # /// Código da conta analítica contábil debitada/creditada
   COD_CCUS: str  # /// Código do Centro de Custos
   DESC_DOC_OPER: str  # /// Descrição do Documento/Operação


class Registro1010(Registro):
   NUM_PROC: str
   ID_SEC_JUD: str
   ID_VARA: str
   IND_NAT_ACAO: int
   DESC_DEC_JUD: str
   DT_SENT_JUD: date
   Registro1011: BlockList[Registro1011]


class Registro1020(Registro):
   NUM_PROC: str
   IND_NAT_ACAO: int
   DT_DEC_ADM: date


class Registro1050(Registro):
   DT_REF: date
   IND_AJ_BC: TabCodAjBaseCalcContrib
   CNPJ: str
   VL_AJ_TOT: Decimal
   VL_AJ_CST01: Decimal
   VL_AJ_CST02: Decimal
   VL_AJ_CST03: Decimal
   VL_AJ_CST04: Decimal
   VL_AJ_CST05: Decimal
   VL_AJ_CST06: Decimal
   VL_AJ_CST07: Decimal
   VL_AJ_CST08: Decimal
   VL_AJ_CST09: Decimal
   VL_AJ_CST49: Decimal
   VL_AJ_CST99: Decimal
   IND_APROP: IndicadorApropAjuste
   NUM_REC: str
   INFO_COMPL: str


class Registro1102(Registro):
   VL_CRED_PIS_TRIB_MI: Decimal | str
   VL_CRED_PIS_NT_MI: Decimal | str
   VL_CRED_PIS_EXP: Decimal | str


class Registro1101(Registro):
   COD_PART: str
   COD_ITEM: str
   COD_MOD: str
   SER: str
   SUB_SER: str
   NUM_DOC: int
   DT_OPER: date
   CHV_NFE: str
   VL_OPER: Decimal
   CFOP: int
   NAT_BC_CRED: str
   IND_ORIG_CRED: int
   CST_PIS: int
   VL_BC_PIS: Decimal
   ALIQ_PIS: Decimal
   VL_PIS: Decimal
   COD_CTA: str
   COD_CCUS: str
   DESC_COMPL: str
   PER_ESCRIT: int
   CNPJ: str
   Registro1102: Registro1102  # // NIVEL 4


class Registro1100(Registro):
   PER_APU_CRED: int
   ORIG_CRED: int
   CNPJ_SUC: str
   COD_CRED: int
   VL_CRED_APU: Decimal
   VL_CRED_EXT_APU: Decimal
   VL_TOT_CRED_APU: Decimal
   VL_CRED_DESC_PA_ANT: Decimal
   VL_CRED_PER_PA_ANT: Decimal
   VL_CRED_DCOMP_PA_ANT: Decimal
   SD_CRED_DISP_EFD: Decimal
   VL_CRED_DESC_EFD: Decimal
   VL_CRED_PER_EFD: Decimal
   VL_CRED_DCOMP_EFD: Decimal
   VL_CRED_TRANS: Decimal
   VL_CRED_OUT: Decimal
   SLD_CRED_FIM: Decimal
   Registro1101: BlockList[Registro1101]  # // NIVEL 3


class Registro1210(Registro):
   CNPJ: str
   CST_PIS: SituacaoTribPIS
   COD_PART: str
   DT_OPER: date
   VL_OPER: Decimal
   VL_BC_PIS: Decimal
   ALIQ_PIS: Decimal
   VL_PIS: Decimal
   COD_CTA: str
   DESC_COMPL: str


class Registro1220(Registro):
   PER_APU_CRED: int
   ORIG_CRED: int
   COD_CRED: int
   VL_CRED: Decimal


class Registro1200(Registro):
   PER_APUR_ANT: int
   NAT_CONT_REC: str
   VL_CONT_APUR: Decimal
   VL_CRED_PIS_DESC: Decimal
   VL_CONT_DEV: Decimal
   VL_OUT_DED: Decimal
   VL_CONT_EXT: Decimal
   VL_MUL: Decimal
   VL_JUR: Decimal
   DT_RECOL: date
   Registro1210: BlockList[Registro1210]  # // NIVEL 3
   Registro1220: BlockList[Registro1220]  # // NIVEL 3


class Registro1300(Registro):
   IND_NAT_RET: int
   PR_REC_RET: int
   VL_RET_APU: Decimal
   VL_RET_DED: Decimal
   VL_RET_PER: Decimal
   VL_RET_DCOMP: Decimal
   SLD_RET: Decimal


class Registro1502(Registro):
   VL_CRED_COFINS_TRIB_MI: Decimal | str
   VL_CRED_COFINS_NT_MI: Decimal | str
   VL_CRED_COFINS_EXP: Decimal | str


class Registro1501(Registro):
   COD_PART: str
   COD_ITEM: str
   COD_MOD: str
   SER: str
   SUB_SER: str
   NUM_DOC: int
   DT_OPER: date
   CHV_NFE: str
   VL_OPER: Decimal
   CFOP: int
   NAT_BC_CRED: str
   IND_ORIG_CRED: int
   CST_COFINS: int
   VL_BC_COFINS: Decimal
   ALIQ_COFINS: Decimal
   VL_COFINS: Decimal
   COD_CTA: str
   COD_CCUS: str
   DESC_COMPL: str
   PER_ESCRIT: int
   CNPJ: str
   Registro1502: Registro1502  # // NIVEL 4


class Registro1500(Registro):
   PER_APU_CRED: int
   ORIG_CRED: int
   CNPJ_SUC: str
   COD_CRED: int
   VL_CRED_APU: Decimal
   VL_CRED_EXT_APU: Decimal
   VL_TOT_CRED_APU: Decimal
   VL_CRED_DESC_PA_ANT: Decimal
   VL_CRED_PER_PA_ANT: Decimal
   VL_CRED_DCOMP_PA_ANT: Decimal
   SD_CRED_DISP_EFD: Decimal
   VL_CRED_DESC_EFD: Decimal
   VL_CRED_PER_EFD: Decimal
   VL_CRED_DCOMP_EFD: Decimal
   VL_CRED_TRANS: Decimal
   VL_CRED_OUT: Decimal
   SLD_CRED_FIM: Decimal
   Registro1501: BlockList[Registro1501]  # // NIVEL 3


class Registro1610(Registro):
   CNPJ: str
   CST_COFINS: SituacaoTribCOFINS
   COD_PART: str
   DT_OPER: date
   VL_OPER: Decimal
   VL_BC_COFINS: Decimal
   ALIQ_COFINS: Decimal
   VL_COFINS: Decimal
   COD_CTA: str
   DESC_COMPL: str


class Registro1620(Registro):
   PER_APU_CRED: int
   ORIG_CRED: int
   COD_CRED: int
   VL_CRED: Decimal


class Registro1600(Registro):
   PER_APUR_ANT: int
   NAT_CONT_REC: str
   VL_CONT_APUR: Decimal
   VL_CRED_COFINS_DESC: Decimal
   VL_CONT_DEV: Decimal
   VL_OUT_DED: Decimal
   VL_CONT_EXT: Decimal
   VL_MUL: Decimal
   VL_JUR: Decimal
   DT_RECOL: date
   Registro1610: BlockList[Registro1610]  # // NIVEL 3
   Registro1620: BlockList[Registro1620]  # // NIVEL 3


class Registro1700(Registro):
   IND_NAT_RET: int
   PR_REC_RET: int
   VL_RET_APU: Decimal
   VL_RET_DED: Decimal
   VL_RET_PER: Decimal
   VL_RET_DCOMP: Decimal
   SLD_RET: Decimal


class Registro1809(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class Registro1800(Registro):
   INC_IMOB: str
   REC_RECEB_RET: Decimal
   REC_FIN_RET: Decimal
   BC_RET: Decimal
   ALIQ_RET: Decimal
   VL_REC_UNI: Decimal
   DT_REC_UNI: date
   COD_REC: str
   Registro1809: BlockList[Registro1809]  # // NIVEL 3


class Registro1900(Registro):
   CNPJ: str
   COD_MOD: str
   SER: str
   SUB_SER: str
   COD_SIT: CodSitF
   VL_TOT_REC: Decimal
   QUANT_DOC: int
   CST_PIS: SituacaoTribPIS
   CST_COFINS: SituacaoTribCOFINS
   CFOP: int
   INF_COMPL: str
   COD_CTA: str


class RegistroP110(Registro):
   REG: str
   NUM_CAMPO: str
   COD_DET: str
   DET_VALOR: Decimal
   INF_COMPL: str


class RegistroP199(Registro):
   REG: str
   NUM_PROC: str
   IND_PROC: str


class RegistroP100(Registro):
   REG: str
   DT_INI: date
   DT_FIM: date
   VL_REC_TOT_EST: Decimal
   COD_ATIV_ECON: str
   VL_REC_ATIV_ESTAB: Decimal
   VL_EXC: Decimal
   VL_BC_CONT: Decimal
   ALIQ_CONT: Decimal
   VL_CONT_APU: Decimal
   COD_CTA: str
   INFO_COMPL: str
   RegistroP110: BlockList[RegistroP110]
   RegistroP199: BlockList[RegistroP199]


class RegistroP010(Registro):
   REG: str
   CNPJ: str
   RegistroP100: BlockList[RegistroP100]


class RegistroP210(Registro):
   REG: str
   IND_AJ: str
   VL_AJ: Decimal
   COD_AJ: str
   NUM_DOC: str
   DESCR_AJ: str
   DT_REF: date


class RegistroP200(Registro):
   REG: str
   PER_REF: str
   VL_TOT_CONT_APU: Decimal
   VL_TOT_AJ_REDUC: Decimal
   VL_TOT_AJ_ACRES: Decimal
   VL_TOT_CONT_DEV: Decimal
   COD_REC: str
   RegistroP210: BlockList[RegistroP210]


class RegistroF111(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroF100(Registro):
   IND_OPER: IndTpOperacaoReceita
   COD_PART: str  # //Código do participante (Campo 02 do Registro 0150)
   COD_ITEM: str  # //Código do item (campo 02 do Registro 0200)
   DT_OPER: date
   VL_OPER: Decimal  # //Valor da Operação/Item
   CST_PIS: SituacaoTribPIS  # //Código da Situação Tributária referente ao PIS/PASEP, conforme a Tabela indicada no item 4.3.3.
   VL_BC_PIS: Decimal  # //Valor da Base de cálculo do PIS/PASEP
   ALIQ_PIS: Decimal  # //Alíquota do PIS/PASEP (em percentual)
   VL_PIS: Decimal  # //Valor do PIS/PASEP
   CST_COFINS: SituacaoTribCOFINS  # //Código da Situação Tributária referente a COFINS, conforme a Tabela indicada no item 4.3.4.
   VL_BC_COFINS: Decimal  # //Valor da Base de cálculo da COFINS
   ALIQ_COFINS: Decimal  # //Alíquota da COFINS (em percentual)
   VL_COFINS: Decimal  # //Valor da COFINS
   NAT_BC_CRED: BaseCalculoCredito  # //Código da Base de Cálculo dos Créditos, conforme a tabela indicada no item 4.3.7, caso seja informado código representativo de crédito nos Campos 07 (CST_PIS) e 11 (CST_COFINS).
   IND_ORIG_CRED: OrigemCredito  # //Indicador da origem do crédito: 0 - Operação no Mercado Interno 1 - Operação de Importação
   COD_CTA: str  # //Código da conta analítica contábil debitada/creditada
   COD_CCUS: str  # //Código do Centro de Custos
   DESC_DOC_OPER: str  # //Descrição  do Documento/Operação
   RegistroF111: BlockList[RegistroF111]


class RegistroF129(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroF120(Registro):
   NAT_BC_CRED: BaseCalculoCredito
   IDENT_BEM_IMOB: IdentBemImob  # //Identificação dos Bens/Grupo de Bens Incorporados ao Ativo Imobilizado:
   IND_ORIG_CRED: OrigemCredito  # //Indicador da origem do bem incorporado ao ativo imobilizado, gerador de crédito: 0 - Aquisição no Mercado Interno 1 - Aquisição no Mercado Externo (Importação)
   IND_UTIL_BEM_IMOB: IndUtilBemImob  # //Indicador da Utilização dos Bens Incorporados ao Ativo Imobilizado:
   VL_OPER_DEP: Decimal  # //Valor do Encargo de Depreciação/Amortização Incorrido no Período
   PARC_OPER_NAO_BC_CRED: Decimal  # //Parcela do Valor do Encargo de Depreciação/Amortização a excluir da base de cálculo de Crédito
   CST_PIS: SituacaoTribPIS  # //Código da Situação Tributária referente ao PIS/PASEP, conforme a Tabela indicada no item 4.3.3.
   VL_BC_PIS: Decimal  # //Base de cálculo do Crédito de PIS/PASEP no período
   ALIQ_PIS: Decimal  # //Alíquota do PIS/PASEP (em percentual)
   VL_PIS: Decimal  # //Valor do Crédito de PIS/PASEP
   CST_COFINS: SituacaoTribCOFINS  # //Código da Situação Tributária referente a COFINS, conforme a Tabela indicada no item 4.3.4.
   VL_BC_COFINS: Decimal  # //Base de Cálculo do Crédito da COFINS no período (06 - 07)
   ALIQ_COFINS: Decimal  # //Alíquota da COFINS (em percentual)
   VL_COFINS: Decimal  # //Valor do crédito da COFINS
   COD_CTA: str  # //Código da conta analítica contábil debitada/creditada
   COD_CCUS: str  # //Código do Centro de Custos
   DESC_BEM_IMOB: str  # //Descrição complementar do bem ou grupo de bens, com crédito apurado com base nos encargos de depreciação ou amortização.
   RegistroF129: BlockList[RegistroF129]


class RegistroF139(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroF130(Registro):
   NAT_BC_CRED: BaseCalculoCredito
   IDENT_BEM_IMOB: IdentBemImob  # //Identificação dos Bens/Grupo de Bens Incorporados ao Ativo Imobilizado:
   IND_ORIG_CRED: OrigemCredito  # //Indicador da origem do bem incorporado ao ativo imobilizado, gerador de crédito: 0 - Aquisição no Mercado Interno 1 - Aquisição no Mercado Externo (Importação)
   IND_UTIL_BEM_IMOB: IndUtilBemImob  # //Indicador da Utilização dos Bens Incorporados ao Ativo Imobilizado:
   MES_OPER_AQUIS: str  # //Mês/Ano de Aquisição dos Bens Incorporados ao Ativo Imobilizado, com apuração de crédito com base no valor de aquisição.
   VL_OPER_AQUIS: Decimal  # //Valor de Aquisição dos Bens Incorporados ao Ativo Imobilizado - Crédito com base no valor de aquisição.
   PARC_OPER_NAO_BC_CRED: Decimal  # //Parcela do Valor de Aquisição a excluir da base de cálculo de Crédito
   VL_BC_CRED: Decimal  # //Valor da Base de Cálculo do Crédito sobre Bens Incorporados ao Ativo Imobilizado (07 - 08)
   IND_NR_PARC: IndNrParc  # //Indicador do Numero de Parcelas a serem apropriadas (Crédito sobre Valor de Aquisição):
   CST_PIS: SituacaoTribPIS  # //Código da Situação Tributária referente ao PIS/PASEP, conforme a Tabela indicada no item 4.3.3.
   VL_BC_PIS: Decimal  # //Base de cálculo Mensal do Crédito de PIS/PASEP, conforme indicador informado no campo 10.
   ALIQ_PIS: Decimal  # //Alíquota do PIS/PASEP
   VL_PIS: Decimal  # //Valor do Crédito de PIS/PASEP
   CST_COFINS: SituacaoTribCOFINS  # //Código da Situação Tributária referente a COFINS, conforme a Tabela indicada no item 4.3.4.
   VL_BC_COFINS: Decimal  # //Base de Cálculo Mensal do Crédito da COFINS, conforme indicador informado no campo 10.
   ALIQ_COFINS: Decimal  # //Alíquota da COFINS
   VL_COFINS: Decimal  # //Valor do crédito da COFINS
   COD_CTA: str  # //Código da conta analítica contábil debitada/creditada
   COD_CCUS: str  # //Código do Centro de Custos
   DESC_BEM_IMOB: str  # //Descrição complementar do bem ou grupo de bens, com crédito apurado com base no valor de aquisição.
   RegistroF139: BlockList[RegistroF139]


class RegistroF150(Registro):
   NAT_BC_CRED: BaseCalculoCredito  # //Texto fixo contendo "18" Código da Base de Cálculo do Crédito sobre Estoque de Abertura, conforme a Tabela indicada no item 4.3.7.
   VL_TOT_EST: Decimal  # //Valor Total do Estoque de Abertura
   EST_IMP: Decimal  # //Parcela do estoque de abertura referente a bens, produtos e mercadorias importados, ou adquiridas no mercado interno sem direito ao crédito
   VL_BC_EST: Decimal  # //Valor da Base de Cálculo do Crédito sobre o Estoque de Abertura (03 - 04)
   VL_BC_MEN_EST: Decimal  # //Valor da Base de Cálculo Mensal do Crédito sobre o Estoque de Abertura (1/12 avos do campo 05)
   CST_PIS: SituacaoTribPIS  # //Código da Situação Tributária referente ao PIS/PASEP, conforme a Tabela indicada no item 4.3.3.
   ALIQ_PIS: Decimal  # //Alíquota do PIS/PASEP
   VL_CRED_PIS: Decimal  # //Valor Mensal do Crédito Presumido Apurado para o Período -  PIS/PASEP  (06 x 08)
   CST_COFINS: SituacaoTribCOFINS  # //Descrição do estoque
   ALIQ_COFINS: Decimal  # //Código da Situação Tributária referente a COFINS, conforme a Tabela indicada no item 4.3.4.
   VL_CRED_COFINS: Decimal  # //Alíquota da COFINS
   DESC_EST: str  # //Código da conta analítica contábil debitada/creditada
   COD_CTA: str  # //Valor Mensal do Crédito Presumido Apurado para o Período -  COFINS (06 x 11)


class RegistroF205(Registro):
   VL_CUS_INC_ACUM_ANT: Decimal
   VL_CUS_INC_PER_ESC: Decimal
   VL_CUS_INC_ACUM: Decimal
   VL_EXC_BC_CUS_INC_ACUM: Decimal
   VL_BC_CUS_INC: Decimal
   CST_PIS: SituacaoTribPIS
   ALIQ_PIS: Decimal
   VL_CRED_PIS_ACUM: Decimal
   VL_CRED_PIS_DESC_ANT: Decimal
   VL_CRED_PIS_DESC: Decimal
   VL_CRED_PIS_DESC_FUT: Decimal
   CST_COFINS: SituacaoTribCOFINS
   ALIQ_COFINS: Decimal
   VL_CRED_COFINS_ACUM: Decimal
   VL_CRED_COFINS_DESC_ANT: Decimal
   VL_CRED_COFINS_DESC: Decimal
   VL_CRED_COFINS_DESC_FUT: Decimal


class RegistroF210(Registro):
   VL_CUS_ORC: Decimal
   VL_EXC: Decimal
   VL_CUS_ORC_AJU: Decimal
   VL_BC_CRED: Decimal
   CST_PIS: SituacaoTribPIS
   ALIQ_PIS: Decimal
   VL_CRED_PIS_UTIL: Decimal
   CST_COFINS: SituacaoTribCOFINS
   ALIQ_COFINS: Decimal
   VL_CRED_COFINS_UTIL: Decimal


class RegistroF211(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroF200(Registro):
   IND_OPER: str
   UNID_IMOB: str
   IDENT_EMP: str
   DESC_UNID_IMOB: str
   NUM_CONT: str
   CPF_CNPJ_ADQU: str
   DT_OPER: date
   VL_TOT_VEND: Decimal
   VL_REC_ACUM: Decimal
   VL_TOT_REC: Decimal
   CST_PIS: SituacaoTribPIS
   VL_BC_PIS: Decimal
   ALIQ_PIS: Decimal
   VL_PIS: Decimal
   CST_COFINS: SituacaoTribCOFINS
   VL_BC_COFINS: Decimal
   ALIQ_COFINS: Decimal
   VL_COFINS: Decimal
   PERC_REC_RECEB: Decimal
   IND_NAT_EMP: str
   INF_COMP: str
   RegistroF205: RegistroF205
   RegistroF210: BlockList[RegistroF210]
   RegistroF211: BlockList[RegistroF211]


class RegistroF509(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroF500(Registro):
   VL_REC_CAIXA: Decimal
   CST_PIS: SituacaoTribPIS
   VL_DESC_PIS: Decimal
   VL_BC_PIS: Decimal
   ALIQ_PIS: Decimal
   VL_PIS: Decimal
   CST_COFINS: SituacaoTribCOFINS
   VL_DESC_COFINS: Decimal
   VL_BC_COFINS: Decimal
   ALIQ_COFINS: Decimal
   VL_COFINS: Decimal
   COD_MOD: str
   CFOP: int
   COD_CTA: str
   INFO_COMPL: str
   RegistroF509: BlockList[RegistroF509]


class RegistroF519(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroF510(Registro):
   VL_REC_CAIXA: Decimal
   CST_PIS: SituacaoTribPIS
   VL_DESC_PIS: Decimal
   QUANT_BC_PIS: Decimal
   ALIQ_PIS_QUANT: Decimal
   VL_PIS: Decimal
   CST_COFINS: SituacaoTribCOFINS
   VL_DESC_COFINS: Decimal
   QUANT_BC_COFINS: Decimal
   ALIQ_COFINS_QUANT: Decimal
   VL_COFINS: Decimal
   COD_MOD: str
   CFOP: int
   COD_CTA: str
   INFO_COMPL: str
   RegistroF519: BlockList[RegistroF519]


class RegistroF525(Registro):
   VL_REC: Decimal
   IND_REC: Ind_Rec
   CNPJ_CPF: str
   NUM_DOC: str
   COD_ITEM: str
   VL_REC_DET: Decimal
   CST_PIS: SituacaoTribPIS
   CST_COFINS: SituacaoTribCOFINS
   INFO_COMPL: str
   COD_CTA: str


class RegistroF559(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroF550(Registro):
   VL_REC_COMP: Decimal
   CST_PIS: SituacaoTribPIS
   VL_DESC_PIS: Decimal
   VL_BC_PIS: Decimal
   ALIQ_PIS: Decimal
   VL_PIS: Decimal
   CST_COFINS: SituacaoTribCOFINS
   VL_DESC_COFINS: Decimal
   VL_BC_COFINS: Decimal
   ALIQ_COFINS: Decimal
   VL_COFINS: Decimal
   COD_MOD: str
   CFOP: int
   COD_CTA: str
   INFO_COMPL: str
   RegistroF559: BlockList[RegistroF559]


class RegistroF569(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroF560(Registro):
   VL_REC_COMP: Decimal
   CST_PIS: SituacaoTribPIS
   VL_DESC_PIS: Decimal
   QUANT_BC_PIS: Decimal
   ALIQ_PIS_QUANT: Decimal
   VL_PIS: Decimal
   CST_COFINS: SituacaoTribCOFINS
   VL_DESC_COFINS: Decimal
   QUANT_BC_COFINS: Decimal
   ALIQ_COFINS_QUANT: Decimal
   VL_COFINS: Decimal
   COD_MOD: str
   CFOP: int
   COD_CTA: str
   INFO_COMPL: str
   RegistroF569: BlockList[RegistroF569]


class RegistroF600(Registro):
   IND_NAT_RET: IndNatRetFonte
   DT_RET: date
   VL_BC_RET: Decimal
   VL_RET: Decimal
   COD_REC: str
   IND_NAT_REC: IndNatRec
   CNPJ: str
   VL_RET_PIS: Decimal
   VL_RET_COFINS: Decimal
   IND_DEC: str


class RegistroF700(Registro):
   IND_ORI_DED: IndOrigemDiversas
   IND_NAT_DED: IndNatDeducao
   VL_DED_PIS: Decimal
   VL_DED_COFINS: Decimal
   VL_BC_OPER: Decimal
   CNPJ: str
   INF_COMP: str


class RegistroF800(Registro):
   IND_NAT_EVEN: str
   DT_EVEN: date
   CNPJ_SUCED: str
   PA_CONT_CRED: str
   COD_CRED: CodCred
   VL_CRED_PIS: Decimal
   VL_CRED_COFINS: Decimal
   PER_CRED_CIS: Decimal


class RegistroF010(Registro):
   CNPJ: str
   RegistroF100: BlockList[RegistroF100]
   RegistroF120: BlockList[RegistroF120]
   RegistroF130: BlockList[RegistroF130]
   RegistroF150: BlockList[RegistroF150]
   RegistroF200: BlockList[RegistroF200]
   RegistroF500: BlockList[RegistroF500]
   RegistroF510: BlockList[RegistroF510]
   RegistroF525: BlockList[RegistroF525]
   RegistroF550: BlockList[RegistroF550]
   RegistroF560: BlockList[RegistroF560]
   RegistroF600: BlockList[RegistroF600]
   RegistroF700: BlockList[RegistroF700]
   RegistroF800: BlockList[RegistroF800]


class RegistroC110(Registro):
   COD_INF: str
   TXT_COMPL: str


class RegistroC111(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroC120(Registro):
   COD_DOC_IMP: DoctoImporta
   NUM_DOC__IMP: str
   PIS_IMP: Decimal
   COFINS_IMP: Decimal
   NUM_ACDRAW: str


class RegistroC170(Registro):
   NUM_ITEM: str
   COD_ITEM: str
   DESCR_COMPL: str
   QTD: Decimal | str
   UNID: str
   VL_ITEM: Decimal
   VL_DESC: Decimal
   IND_MOV: IndMovFisica
   CST_ICMS: CstIcms
   CFOP: str
   COD_NAT: str
   VL_BC_ICMS: Decimal
   ALIQ_ICMS: Decimal
   VL_ICMS: Decimal
   VL_BC_ICMS_ST: Decimal
   ALIQ_ST: Decimal
   VL_ICMS_ST: Decimal
   IND_APUR: ApuracaoIPI
   CST_IPI: CstIpi
   COD_ENQ: str
   VL_BC_IPI: Decimal
   ALIQ_IPI: Decimal
   VL_IPI: Decimal
   CST_PIS: SituacaoTribPIS
   VL_BC_PIS: Decimal | str
   ALIQ_PIS_PERC: Decimal | str
   QUANT_BC_PIS: Decimal | str
   ALIQ_PIS_R: Decimal | str
   VL_PIS: Decimal | str
   CST_COFINS: SituacaoTribCOFINS
   VL_BC_COFINS: Decimal | str
   ALIQ_COFINS_PERC: Decimal | str
   QUANT_BC_COFINS: Decimal | str
   ALIQ_COFINS_R: Decimal | str
   VL_COFINS: Decimal | str
   COD_CTA: str


class RegistroC175(Registro):
   CFOP: str
   VL_OPR: Decimal | str
   VL_DESC: Decimal | str
   CST_PIS: SituacaoTribPIS
   VL_BC_PIS: Decimal | str
   ALIQ_PIS: Decimal | str
   QUANT_BC_PIS: Decimal | str
   ALIQ_PIS_QUANT: Decimal | str
   VL_PIS: Decimal | str
   CST_COFINS: SituacaoTribCOFINS
   VL_BC_COFINS: Decimal | str
   ALIQ_COFINS: Decimal | str
   QUANT_BC_COFINS: Decimal | str
   ALIQ_COFINS_QUANT: Decimal | str
   VL_COFINS: Decimal | str
   COD_CTA: str
   INFO_COMPL: str


class RegistroC100(Registro):
   IND_OPER: TipoOperacao
   IND_EMIT: Emitente
   COD_PART: str
   COD_MOD: str
   COD_SIT: SituacaoDF
   SER: str
   NUM_DOC: str
   CHV_NFE: str
   DT_DOC: date
   DT_E_S: date
   VL_DOC: Decimal
   IND_PGTO: TipoPagamento
   VL_DESC: Decimal
   VL_ABAT_NT: Decimal
   VL_MERC: Decimal
   IND_FRT: TipoFrete
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
   RegistroC110: BlockList[RegistroC110]  # /// BLOCO C - Lista de RegistroC110 (FILHO)
   RegistroC111: BlockList[RegistroC111]  # /// BLOCO C - Lista de RegistroC111 (FILHO)
   RegistroC120: BlockList[RegistroC120]  # /// BLOCO C - Lista de RegistroC120 (FILHO)
   RegistroC170: BlockList[RegistroC170]  # /// BLOCO C - Lista de RegistroC170 (FILHO)
   RegistroC175: BlockList[RegistroC175]  # /// BLOCO C - Lista de RegistroC175 (FILHO)


class RegistroC181(Registro):
   CST_PIS: SituacaoTribPIS
   CFOP: str
   VL_ITEM: Decimal
   VL_DESC: Decimal | str
   VL_BC_PIS: Decimal | str
   ALIQ_PIS: Decimal | str
   QUANT_BC_PIS: Decimal | str
   ALIQ_PIS_QUANT: Decimal | str
   VL_PIS: Decimal | str
   COD_CTA: str


class RegistroC185(Registro):
   CST_COFINS: SituacaoTribCOFINS
   CFOP: str
   VL_ITEM: Decimal
   VL_DESC: Decimal | str
   VL_BC_COFINS: Decimal | str
   ALIQ_COFINS: Decimal | str
   QUANT_BC_COFINS: Decimal | str
   ALIQ_COFINS_QUANT: Decimal | str
   VL_COFINS: Decimal | str
   COD_CTA: str


class RegistroC188(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroC180(Registro):
   COD_MOD: str
   DT_DOC_INI: date
   DT_DOC_FIN: date
   COD_ITEM: str
   COD_NCM: str
   EX_IPI: str
   VL_TOT_ITEM: Decimal
   RegistroC181: BlockList[RegistroC181]
   RegistroC185: BlockList[RegistroC185]
   RegistroC188: BlockList[RegistroC188]


class RegistroC191(Registro):
   CNPJ_CPF_PART: str
   CST_PIS: SituacaoTribPIS
   CFOP: int
   VL_ITEM: Decimal
   VL_DESC: Decimal | str
   VL_BC_PIS: Decimal | str
   ALIQ_PIS: Decimal | str
   QUANT_BC_PIS: Decimal | str
   ALIQ_PIS_QUANT: Decimal | str
   VL_PIS: Decimal | str
   COD_CTA: str


class RegistroC195(Registro):
   CNPJ_CPF_PART: str
   CST_COFINS: SituacaoTribCOFINS
   CFOP: int
   VL_ITEM: Decimal
   VL_DESC: Decimal | str
   VL_BC_COFINS: Decimal | str
   ALIQ_COFINS: Decimal | str
   QUANT_BC_COFINS: Decimal | str
   ALIQ_COFINS_QUANT: Decimal | str
   VL_COFINS: Decimal
   COD_CTA: str


class RegistroC198(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroC199(Registro):
   COD_DOC_IMP: DoctoImporta
   NUM_DOC__IMP: str
   VL_PIS_IMP: Decimal
   VL_COFINS_IMP: Decimal
   NUM_ACDRAW: str


class RegistroC190(Registro):
   COD_MOD: str
   DT_REF_INI: date
   DT_REF_FIN: date
   COD_ITEM: str
   COD_NCM: str
   EX_IPI: str
   VL_TOT_ITEM: Decimal
   RegistroC191: BlockList[RegistroC191]  # /// BLOCO C - Lista de RegistroC190 (FILHO)
   RegistroC195: BlockList[RegistroC195]  # /// BLOCO C - Lista de RegistroC195 (FILHO)
   RegistroC198: BlockList[RegistroC198]  # /// BLOCO C - Lista de RegistroC195 (FILHO)
   RegistroC199: BlockList[RegistroC199]  # /// BLOCO C - Lista de RegistroC195 (FILHO)


class RegistroC381(Registro):
   CST_PIS: SituacaoTribPIS
   COD_ITEM: str
   VL_ITEM: Decimal
   VL_BC_PIS: Decimal | str
   ALIQ_PIS: Decimal | str
   QUANT_BC_PIS: Decimal | str
   ALIQ_PIS_QUANT: Decimal | str
   VL_PIS: Decimal | str
   COD_CTA: str


class RegistroC385(Registro):
   CST_COFINS: SituacaoTribCOFINS
   COD_ITEM: str
   VL_ITEM: Decimal
   VL_BC_COFINS: Decimal | str
   ALIQ_COFINS: Decimal | str
   QUANT_BC_COFINS: Decimal | str
   ALIQ_COFINS_QUANT: Decimal | str
   VL_COFINS: Decimal | str
   COD_CTA: str


class RegistroC380(Registro):
   COD_MOD: str
   DT_DOC_INI: date
   DT_DOC_FIN: date
   NUM_DOC_INI: int
   NUM_DOC_FIN: int
   VL_DOC: Decimal
   VL_DOC_CANC: Decimal
   RegistroC381: BlockList[RegistroC381]
   RegistroC385: BlockList[RegistroC385]


class RegistroC396(Registro):
   COD_ITEM: str
   VL_ITEM: Decimal
   VL_DESC: Decimal
   NAT_BC_CRED: BaseCalculoCredito
   CST_PIS: SituacaoTribPIS
   VL_BC_PIS: Decimal
   ALIQ_PIS: Decimal
   VL_PIS: Decimal
   CST_COFINS: SituacaoTribCOFINS
   VL_BC_COFINS: Decimal
   ALIQ_COFINS: Decimal
   VL_COFINS: Decimal
   COD_CTA: str


class RegistroC395(Registro):
   COD_MOD: str
   COD_PART: str
   SER: str
   SUB_SER: str
   NUM_DOC: str
   DT_DOC: date
   VL_DOC: Decimal
   RegistroC396: BlockList[RegistroC396]


class RegistroC481(Registro):
   CST_PIS: SituacaoTribPIS
   VL_ITEM: Decimal
   VL_BC_PIS: Decimal | str
   ALIQ_PIS: Decimal | str
   QUANT_BC_PIS: Decimal | str
   ALIQ_PIS_QUANT: Decimal | str
   VL_PIS: Decimal | str
   COD_ITEM: str
   COD_CTA: str


class RegistroC485(Registro):
   CST_COFINS: SituacaoTribCOFINS
   VL_ITEM: Decimal
   VL_BC_COFINS: Decimal | str
   ALIQ_COFINS: Decimal | str
   QUANT_BC_COFINS: Decimal | str
   ALIQ_COFINS_QUANT: Decimal | str
   VL_COFINS: Decimal | str
   COD_ITEM: str
   COD_CTA: str


class RegistroC405(Registro):
   DT_DOC: date
   CRO: int
   CRZ: int
   NUM_COO_FIN: int
   GT_FIN: Decimal
   VL_BRT: Decimal
   RegistroC481: BlockList[RegistroC481]
   RegistroC485: BlockList[RegistroC485]


class RegistroC489(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroC400(Registro):
   COD_MOD: str
   ECF_MOD: str
   ECF_FAB: str
   ECF_CX: int
   RegistroC405: BlockList[RegistroC405]
   RegistroC489: BlockList[RegistroC489]


class RegistroC491(Registro):
   COD_ITEM: str
   CST_PIS: SituacaoTribPIS
   CFOP: int
   VL_ITEM: Decimal
   VL_BC_PIS: Decimal | str
   ALIQ_PIS: Decimal | str
   QUANT_BC_PIS: Decimal | str
   ALIQ_PIS_QUANT: Decimal | str
   VL_PIS: Decimal | str
   COD_CTA: str


class RegistroC495(Registro):
   COD_ITEM: str
   CST_COFINS: SituacaoTribCOFINS
   CFOP: int
   VL_ITEM: Decimal
   VL_BC_COFINS: Decimal | str
   ALIQ_COFINS: Decimal | str
   QUANT_BC_COFINS: Decimal | str
   ALIQ_COFINS_QUANT: Decimal | str
   VL_COFINS: Decimal | str
   COD_CTA: str


class RegistroC499(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroC490(Registro):
   DT_DOC_INI: date
   DT_DOC_FIN: date
   COD_MOD: str
   RegistroC491: BlockList[RegistroC491]
   RegistroC495: BlockList[RegistroC495]
   RegistroC499: BlockList[RegistroC499]


class RegistroC501(Registro):
   CST_PIS: SituacaoTribPIS
   VL_ITEM: Decimal
   NAT_BC_CRED: BaseCalculoCredito
   VL_BC_PIS: Decimal
   ALIQ_PIS: Decimal
   VL_PIS: Decimal
   COD_CTA: str


class RegistroC505(Registro):
   CST_COFINS: SituacaoTribCOFINS
   VL_ITEM: Decimal
   NAT_BC_CRED: BaseCalculoCredito
   VL_BC_COFINS: Decimal
   ALIQ_COFINS: Decimal
   VL_COFINS: Decimal
   COD_CTA: str


class RegistroC509(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroC500(Registro):
   COD_PART: str
   COD_MOD: str
   COD_SIT: SituacaoDF
   SER: str
   SUB: int
   NUM_DOC: int
   DT_DOC: date
   DT_ENT: date
   VL_DOC: Decimal
   VL_ICMS: Decimal
   COD_INF: str
   VL_PIS: Decimal
   VL_COFINS: Decimal
   CHV_DOCe: str  # //15	CHV_DOCe Chave do Documento Fiscal Eletrônico
   RegistroC501: BlockList[RegistroC501]
   RegistroC505: BlockList[RegistroC505]
   RegistroC509: BlockList[RegistroC509]


class RegistroC601(Registro):
   CST_PIS: SituacaoTribPIS
   VL_ITEM: Decimal
   VL_BC_PIS: Decimal
   ALIQ_PIS: Decimal
   VL_PIS: Decimal
   COD_CTA: str


class RegistroC605(Registro):
   CST_COFINS: SituacaoTribCOFINS
   VL_ITEM: Decimal
   VL_BC_COFINS: Decimal
   ALIQ_COFINS: Decimal
   VL_COFINS: Decimal
   COD_CTA: str


class RegistroC609(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroC600(Registro):
   COD_MOD: str
   COD_MUN: int
   SER: str
   SUB: int
   COD_CONS: int
   QTD_CONS: int
   QTD_CANC: int
   DT_DOC: date
   VL_DOC: Decimal
   VL_DESC: Decimal
   CONS: int
   VL_FORN: Decimal
   VL_SERV_NT: Decimal
   VL_TERC: Decimal
   VL_DA: Decimal
   VL_BC_ICMS: Decimal
   VL_ICMS: Decimal
   VL_BC_ICMS_ST: Decimal
   VL_ICMS_ST: Decimal
   VL_PIS: Decimal
   VL_COFINS: Decimal
   RegistroC601: BlockList[RegistroC601]
   RegistroC605: BlockList[RegistroC605]
   RegistroC609: BlockList[RegistroC609]


class RegistroC810(Registro):
   CFOP: str
   VL_ITEM: Decimal
   COD_ITEM: str
   CST_PIS: SituacaoTribPIS
   VL_BC_PIS: Decimal | str
   ALIQ_PIS: Decimal | str
   VL_PIS: Decimal | str
   CST_COFINS: SituacaoTribCOFINS
   VL_BC_COFINS: Decimal | str
   ALIQ_COFINS: Decimal | str
   VL_COFINS: Decimal | str
   COD_CTA: str


class RegistroC820(Registro):
   CFOP: str
   VL_ITEM: Decimal
   COD_ITEM: str
   CST_PIS: SituacaoTribPIS
   QUANT_BC_PIS: Decimal | str
   ALIQ_PIS_QUANT: Decimal | str
   VL_PIS: Decimal | str
   CST_COFINS: SituacaoTribCOFINS
   QUANT_BC_COFINS: Decimal | str
   ALIQ_COFINS_QUANT: Decimal | str
   VL_COFINS: Decimal | str
   COD_CTA: str


class RegistroC830(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroC800(Registro):
   COD_MOD: str
   COD_SIT: SituacaoDF
   NUM_CFE: int
   DT_DOC: date
   VL_CFE: Decimal | str
   VL_PIS: Decimal | str
   VL_COFINS: Decimal | str
   CNPJ_CPF: str
   NR_SAT: str
   CHV_CFE: str
   VL_DESC: Decimal | str
   VL_MERC: Decimal | str
   VL_OUT_DA: Decimal | str
   VL_ICMS: Decimal | str
   VL_PIS_ST: Decimal | str
   VL_COFINS_ST: Decimal | str
   RegistroC810: BlockList[RegistroC810]
   RegistroC820: BlockList[RegistroC820]
   RegistroC830: BlockList[RegistroC830]


class RegistroC870(Registro):
   COD_ITEM: str
   CFOP: str
   VL_ITEM: Decimal | str
   VL_DESC: Decimal | str
   CST_PIS: SituacaoTribPIS
   VL_BC_PIS: Decimal | str
   ALIQ_PIS: Decimal | str
   VL_PIS: Decimal | str
   CST_COFINS: SituacaoTribCOFINS
   VL_BC_COFINS: Decimal | str
   ALIQ_COFINS: Decimal | str
   VL_COFINS: Decimal | str
   COD_CTA: str


class RegistroC880(Registro):
   COD_ITEM: str
   CFOP: str
   VL_ITEM: Decimal | str
   CST_PIS: SituacaoTribPIS
   QUANT_BC_PIS: Decimal | str
   ALIQ_PIS_QUANT: Decimal | str
   VL_PIS: Decimal | str
   CST_COFINS: SituacaoTribCOFINS
   QUANT_BC_COFINS: Decimal | str
   ALIQ_COFINS_QUANT: Decimal | str
   VL_COFINS: Decimal | str
   COD_CTA: str


class RegistroC890(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroC860(Registro):
   COD_MOD: str
   NR_SAT: int
   DT_DOC: date
   DOC_INI: int
   DOC_FIM: int
   RegistroC870: BlockList[RegistroC870]
   RegistroC880: BlockList[RegistroC880]
   RegistroC890: BlockList[RegistroC890]


class RegistroC010(Registro):
   CNPJ: str
   IND_ESCRI: IndEscrituracao
   RegistroC100: BlockList[RegistroC100]
   RegistroC180: BlockList[RegistroC180]
   RegistroC190: BlockList[RegistroC190]
   RegistroC380: BlockList[RegistroC380]
   RegistroC395: BlockList[RegistroC395]
   RegistroC400: BlockList[RegistroC400]
   RegistroC490: BlockList[RegistroC490]
   RegistroC500: BlockList[RegistroC500]
   RegistroC600: BlockList[RegistroC600]
   RegistroC800: BlockList[RegistroC800]
   RegistroC860: BlockList[RegistroC860]


class RegistroI199(Registro):
   NUM_PROC: str
   IND_PROC: OrigemProcesso


class RegistroI299(Registro):
   NUM_PROC: str  # //02 Identificação do processo ou ato concessório C 020 -
   IND_PROC: OrigemProcesso  # //03 Indicador da origem do processo: C 001* -


class RegistroI399(Registro):
   NUM_PROC: str  # //02 Identificação do processo ou ato concessório C 020 -
   IND_PROC: OrigemProcesso  # //03 Indicador da origem do processo: 1 - Justiça Federal; 3  Secretaria da Receita Federal do Brasil 9  Outros. C 001* -


class RegistroI300(Registro):
   COD_COMP: str  # //02 Código das Tabelas 7.1.3 (Receitas  Visão Analítica/Referenciada) e/ou 7.1.4 (Deduções e exclusões  Visão Analítica/Referenciada), objeto de complemento neste registro C 060 -
   DET_VALOR: float  # //03 Valor da receita, dedução ou exclusão, objeto de complemento/detalhamento neste registro, conforme código informado no campo 02 (especificados nas tabelas analíticas 7.1.3 e 7.1.4) ou no campo 04 (código da conta contábil) N - 02
   COD_CTA: str  # //04 Código da conta contábil referente ao valor informado no campo 03 C 060 -
   INFO_COMPL: str  # //05 Informação Complementar dos dados informados no registro C - -
   RegistroI399: BlockList[RegistroI399]


class RegistroI200(Registro):
   NUM_CAMPO: str  # //02 Informar o número do campo do registro I100 (Campos 02, 04 ou 05), objeto de informação neste registro.C 002* -
   COD_DET: str  # //03 Código do tipo de detalhamento, conforme Tabelas 7.1.1 e/ou 7.1.2 C 005* -
   DET_VALOR: float  # //04 Valor detalhado referente ao campo 03 (COD_DET) deste registro N - 02
   COD_CTA: str  # //05 Código da conta contábil referente ao valor informado no campo 04 (DET_VALOR) C 060 -
   INFO_COMPL: str  # //06 Informação Complementar dos dados informados no registro C - -
   RegistroI299: BlockList[RegistroI299]
   RegistroI300: BlockList[RegistroI300]


class RegistroI100(Registro):
   VL_REC: float  # //02 Valor Total do Faturamento/Receita Bruta no Período N - 02
   CST_PIS_COFINS: CstPisCofins  # //03 Código de Situação Tributária referente à Receita informada no Campo 02 (Tabelas 4.3.3 e 4.3.4) N 002* -
   VL_TOT_DED_GER: float  # //04 Valor Total das Deduções e Exclusões de Caráter Geral N - 02
   VL_TOT_DED_ESP: float  # //05 Valor Total das Deduções e Exclusões de Caráter Específico N - 02
   VL_BC_PIS: float  # //07 Alíquota do PIS/PASEP (em percentual) N 008 02
   ALIQ_PIS: float  # //08 Valor do PIS/PASEP N - 02
   VL_PIS: float  # //09 Valor da base de cálculo da Cofins N - 02
   VL_BC_COFINS: float  # //10 Alíquota da COFINS (em percentual) N 008 02
   ALIQ_COFINS: float  # //06 Valor da base de cálculo do PIS/PASEP N - 02
   VL_COFINS: float  # //11 Valor da COFINS N - 02
   INFO_COMPL: str  # //12 Informação Complementar dos dados informados no registro C - -
   RegistroI199: BlockList[RegistroI199]
   RegistroI200: BlockList[RegistroI200]


class RegistroI010(Registro):
   CNPJ: str  # //02 Número de inscrição da pessoa jurídica no CNPJ. N 014*
   IND_ATIV: int  # //03 Indicador de operações realizadas no período N 002*
   INFO_COMPL: str  # //04 Informação Complementar C
   RegistroI100: BlockList[RegistroI100]

