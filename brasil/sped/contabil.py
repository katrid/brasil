from typing import List, Required, Annotated
import enum
from datetime import date
from decimal import Decimal

from brasil.sped.registro import BlockList, Registro, BlocoSPED

class BlocoInicial:
   IND_DAD: int  # /// Indicador de movimento: 0- Bloco com dados informados, 1- Bloco sem dados informados.


class Registro0000(Registro):
   DT_INI: date
   DT_FIN: date
   NOME: str  # /// Nome empresarial do empresário ou sociedade empresária.
   CNPJ: str  # /// Número de inscrição do empresário ou sociedade empresária no CNPJ.
   UF: str  # /// Sigla da unidade da federação do empresário ou sociedade empresária.
   IE: str  # /// Inscrição Estadual do empresário ou sociedade empresária.
   COD_MUN: str  # /// Código do município do domicílio fiscal do empresário ou sociedade empresária, conforme tabela do IBGE - Instituto Brasileiro de Geografia e Estatística.
   IM: str  # /// Inscrição Municipal do empresário ou sociedade empresária.
   IND_SIT_ESP: str  # /// Indicador de situação especial (conforme tabela publicada pelo Sped).
   IND_SIT_INI_PER: str  # /// Indicador de situação no início do período (conforme tabela publicada pelo Sped).
   IND_NIRE: str  # /// Indicador de existência de NIRE
   IND_FIN_ESC: str  # /// Indicador de finalidade da escrituração
   COD_HASH_SUB: str  # /// Hash da escrituração substituída.
   NIRE_SUBST: str  # /// NIRE da escrituração substituída.
   IND_EMP_GRD_PRT: str  # /// Indicador de empresa de grande porte:
   TIP_ECD: str  # /// Indicador do tipo de ECD: 0  ECD de empresa não participante de SCP como sócio ostensivo. 1  ECD de empresa participante de SCP como sócio ostensivo. 2  ECD da SCP.
   COD_SCP: str  # /// Identificação da SCP.
   IDENT_MF: str  # /// Identificação de Moeda Funcional
   IND_ESC_CONS: str  # /// Escriturações Contábeis Consolidadas: Deve ser preenchido pela empresa controladora obrigada, nos termos da lei, a informações demonstrações contábeis consolidadas
   IND_CENTRALIZADA: str  # /// Indicador da modalidade de escrituração centralizada ou descentralizada: 0  Escrituração Centralizada 1  Escrituração Descentralizada
   IND_MUDANC_PC: str  # /// Indicador de mudança de plano de contas: 0  Não houve mudança no plano de contas. 1  Houve mudança no plano de contas.
   COD_PLAN_REF: str  # /// Código do Plano de Contas Referencial que será utilizado para o mapeamento de todas as contas analíticas Observação: Caso a pessoa jurídica não realize o mapeamento para os planos referenciais na ECD, este campo deve ficar em branco.


class Registro0001(BlocoInicial):
   pass


class Registro0007(Registro):
   COD_ENT_REF: str  # /// Código da instituição responsável pela administração do cadastro (conforme tabela publicada pelo Sped).
   COD_INSCR: str  # /// Código cadastral do empresário ou sociedade empresária na instituição identificada no campo 02.


class Registro0020(Registro):
   IND_DEC: int  # /// Indicador de descentralização: 0 - escrituração da matriz; 1 - escrituração da filial.
   CNPJ: str  # /// Número de inscrição do empresário ou sociedade empresária no CNPJ da matriz ou da filial.
   UF: str  # /// Sigla da unidade da federação da matriz ou da filial.
   IE: str  # /// Inscrição estadual da matriz ou da filial.
   COD_MUN: str  # /// Código do município do domicílio da matriz ou da filial.
   IM: str  # /// Número de Inscrição Municipal da matriz ou da filial.
   NIRE: str  # /// Número de Identificação do Registro de Empresas da matriz ou da filial na Junta Comercial.


class Registro0035(Registro):
   COD_SCP: str  # /// Identificação da SCP (CNPJ  art. 52 da Instrução Normativa RFB no 1.470, de 30 de maio de 2014)
   NOME_SCP: str  # /// Nome da SCP


class Registro0180(Registro):
   COD_REL: str  # /// Código do relacionamento conforme tabela publicada pelo Sped.
   DT_INI_REL: date  # /// Data do início do relacionamento.
   DT_FIN_REL: date  # /// Data do término do relacionamento.


class Registro0150(Registro):
   COD_PART: str  # /// Código de identificação do participante:
   NOME: str  # /// Nome pessoal ou empresarial:
   COD_PAIS: str  # /// Código do país do participante:
   CNPJ: str  # /// CNPJ do participante:
   CPF: str  # /// CPF do participante na unidade da federação do destinatário:
   NIT: str  # /// Número de Identificação do Trabalhador, Pis, Pasep, SUS.
   UF: str  # /// Sigla da unidade da federação do participante.
   IE: str  # /// Inscrição Estadual do participante:
   IE_ST: str  # /// Inscrição Estadual do participante na unidade da federação do destinatário, na condição de contribuinte substituto
   COD_MUN: int  # /// Código do município:
   IM: str  # /// Inscrição Municipal do participante.
   SUFRAMA: str  # /// Número de inscrição na Suframa:
   Registro0180: BlockList[Registro0180]  # /// BLOCO 0 - Lista de Registro0180 (FILHO)


class Registro0990(Registro):
   QTD_LIN_0: int  # /// Quantidade total de linhas do Bloco 0


class RegistroJ001(BlocoInicial):
   pass


class RegistroJ900(Registro):
   NUM_ORD: str  # /// Número de ordem do instrumento de escrituração.
   NAT_LIVRO: str  # /// Natureza do livro; finalidade a que se destinou o instrumento.
   NOME: str  # /// Nome empresarial.
   QTD_LIN: int  # /// Quantidade total de linhas do arquivo digital.
   DT_INI_ESCR: date  # /// Data de inicio da escrituração.
   DT_FIN_ESCR: date  # /// Data de término da escrituração.


class RegistroJ990(Registro):
   QTD_LIN_J: int


class Bloco_0(BlocoSPED):
   Registro0000: Registro0000  # /// BLOCO 0 - Registro0000
   Registro0001: Registro0001  # /// BLOCO 0 - Registro0001
   Registro0007: BlockList[Registro0007]  # /// BLOCO 0 - Lista de Registro0007
   Registro0020: BlockList[Registro0020]  # /// BLOCO 0 - Lista de Registro0020
   Registro0035: BlockList[Registro0035]  # /// BLOCO 0 - Lista de Registro0035
   Registro0150: BlockList[Registro0150]  # /// BLOCO 0 - Lista de Registro0150
   Registro0990: Registro0990  # /// BLOCO 0 - FRegistro0990
   Registro0180Count: int  # //    procedure SetRegistro0035(const Value: TRegistro0035List);      /// BLOCO 0 - FRegistro0990


class RegistroJ100(Registro):
   COD_AGL: str  # /// Código de aglutinação das contas, atribuído pelo empresário ou sociedade empresária.
   IND_COD_AGL: str  # /// Indicador do tipo de código de aglutinação das linhas (leiaute 7: T - Totalizador; D - Detalhe)
   NIVEL_AGL: str  # /// Nível do Código de aglutinação (mesmo conceito do plano de contas - Registro I050).
   COD_AGL_SUP: str  # /// Código de aglutinação sintético/grupo de código de aglutinação de nível superior
   IND_GRP_BAL: str  # /// Indicador de grupo do balanço: 1 ou A - Ativo; 2 ou P - Passivo e Patrimônio Líquido;
   DESCR_COD_AGL: str  # /// Descrição do Código de aglutinação.
   VL_CTA: Decimal  # /// Valor total do Código de aglutinação no Balanço Patrimonial no exercício informado, ou de período definido em norma específica.
   IND_DC_BAL: str  # /// Indicador da situação do saldo informado no campo anterior: D - Devedor; C - Credor.
   VL_CTA_INI: Decimal  # /// Valor inicial do código de aglutinação no Balanço Patrimonial no exercício informado, ou de período definido em norma específica.
   IND_DC_BAL_INI: str  # /// Indicador da situação do saldo inicial informado no campo anterior: D - Devedor; C  Credor.
   IND_DC_CTA_INI: str  # /// Indicador da situação do saldo inicial informado no campo anterior: D - Devedor; C  Credor.
   VL_CTA_FIN: Decimal  # /// Valor final do código de aglutinação no Balanço patrimonial no ecercíxio informado, ou de período definido de forma específica.
   IND_DC_CTA_FIN: str  # /// Indicador da situação do saldo final informado no campo anterior: D - Devedor; C - Credor;
   NOTAS_EXP_REF: str  # /// Notas explicativas relativas às demonstrações contábeis.


class RegistroJ150(Registro):
   NU_ORDEM: str  # /// Número de ordem da linha na visualização da demonstração
   COD_AGL: str  # /// Código de aglutinação das contas, atribuído pelo empresário ou sociedade empresária.
   IND_COD_AGL: str  # /// Indicador do tipo de código de aglutinação das linhas (leiaute 7: T - Totalizador; D - Detalhe)
   NIVEL_AGL: str  # /// Nível do Código de aglutinação (mesmo conceito do plano de contas - Registro I050).
   COD_AGL_SUP: str  # /// Código de aglutinação sintético/grupo de código de aglutinação de nível superior
   DESCR_COD_AGL: str  # /// Descrição do Código de aglutinação.
   VL_CTA_INI: Decimal  # /// Valor do saldo final da linha no período imediatamente anterior
   IND_DC_CTA_INI: str  # /// Indicador da situação do valor final da linha no período imediatamente anterior
   VL_CTA_FIN: Decimal  # /// Valor final da linha antes do encerramento do exercício
   IND_DC_CTA_FIN: str  # /// Indicador da situação do valor final da linha antes do encerramento
   VL_CTA: Decimal  # /// Valor total do Código de aglutinação na Demonstração do Resultado do Exercício no período informado.
   IND_VL: str  # /// Indicador da situação do valor informado no campo anterior: D - Despesa ou valor que represente parcela redutora do lucro;R - Receita ou valor que represente incremento do lucro;P - Subtotal ou total positivo;N - Subtotal ou total negativo.
   VL_CTA_ULT_DRE: Decimal  # /// Valor inicial total constante na Demonstração do Resultado do Exercício do último período informado.
   IND_VL_ULT_DRE: str  # /// Indicador da situação do valor informado no campo anterior: D - Despesa ou valor que represente parcela redutora do lucro;R - Receita ou valor que represente incremento do lucro;P - Subtotal ou total positivo;N - Subtotal ou total negativo.
   IND_DC_CTA: str  # /// Indicador da situação do valor total do código de aglutinação: D - Devedor; C - Credor;
   IND_GRP_DRE: str  # /// Indicador de grupo da DRE: D ou R
   NOTAS_EXP_REF: str  # /// Notas explicativas relativas às demonstrações contábeis.


class RegistroJ200(Registro):
   COD_HIST_FAT: str  # /// Código do histórico do fato contábil.
   DESC_FAT: str  # /// Descrição do fato contábil.


class RegistroJ215(Registro):
   COD_HIST_FAT: str  # /// Código do histórico do fato contábil.
   VL_FAT_CONT: Decimal  # /// Valor do fato contábil.
   IND_DC_FAT: str  # /// Indicador de situação do saldo informado no campo anterior
   DESC_FAT: str  # /// Descrição do fato contábil


class RegistroJ210(Registro):
   IND_TIP: str  # /// Indicador do tipo de demonstração: 0  DLPA, 1  DMPL
   COD_AGL: str  # /// Código de aglutinação das contas, atribuído pelo empresário ou sociedade empresária.
   DESCR_COD_AGL: str  # /// Descrição do Código de aglutinação.
   VL_CTA: Decimal  # /// Saldo final do código de aglutinação na demonstração do período informado.
   IND_DC_CTA: str  # /// Indicador da situação do saldo FINAL informado no campo anterior: D - Devedor; C - Credor.
   VL_CTA_INI: Decimal  # /// Saldo inicial do código de aglutinação na demonstração do período informado
   IND_DC_CTA_INI: str  # /// Indicador da situação do saldo inicial informado no campo anterior: D  Devedor C  Credor
   VL_CTA_FIN: Decimal  # /// Saldo final do código de aglutinação na demonstração do período informado
   IND_DC_CTA_FIN: str  # /// INdicador da situação do saldo final informado: D - Devedor; C - Credor
   NOTAS_EXP_REF: str  # /// Notas explicativas relativas às demonstrações contábeis.
   RegistroJ215: BlockList[RegistroJ215]  # /// BLOCO J - Lista de RegistroJ215 (FILHO)


class RegistroJ800(Registro):
   TIPO_DOC: str  # // Tipo de documento
   DESC_RTF: str  # // Descrição do arquivo
   HASH_RTF: str  # // Hash do arquivo
   ARQ_RTF: str  # // Seqüência de bytes que representem um único arquivo no formato RTF (Rich Text Format).


class RegistroJ801(Registro):
   TIPO_DOC: str  # // Tipo de documento
   DESC_RTF: str  # // Descrição do arquivo
   COD_MOT_SUBS: str  # /// Código do motivo da substituição
   HASH_RTF: str  # // Hash do arquivo
   ARQ_RTF: str  # // Seqüência de bytes que representem um único arquivo no formato RTF (Rich Text Format).


class RegistroJ005(Registro):
   DT_INI: date  # /// Data inicial das demonstrações contábeis.
   DT_FIN: date  # /// Data final das demonstrações contábeis.
   ID_DEM: int  # /// Identificação das demonstrações: 1 - demonstrações contábeis do empresário ou sociedade empresária a que se refere a escrituração; 2 - demonstrações consolidadas ou de outros empresários ou sociedades empresárias.
   CAB_DEM: str  # /// Cabeçalho das demonstrações.
   RegistroJ100: BlockList[RegistroJ100]  # /// BLOCO J - Lista de RegistroJ100 (FILHO)
   RegistroJ150: BlockList[RegistroJ150]  # /// BLOCO J - Lista de RegistroJ150 (FILHO)
   RegistroJ200: BlockList[RegistroJ200]  # /// BLOCO J - Lista de RegistroJ200 (FILHO)
   RegistroJ210: BlockList[RegistroJ210]
   RegistroJ800: BlockList[RegistroJ800]
   RegistroJ801: BlockList[RegistroJ801]


class RegistroJ930(Registro):
   IDENT_NOM: str  # /// Nome do signatário.
   IDENT_CPF: str  # /// CPF.
   IDENT_QUALIF: str  # /// Qualificação do assinante, conforme tabela do Departamento Nacional de Registro do Comércio - DNRC.
   COD_ASSIN: str  # /// Código de qualificação do assinante, conforme tabela do Departamento Nacional de Registro do Comércio - DNRC.
   IND_CRC: str  # /// Número de inscrição do contabilista no Conselho Regional de Contabilidade.
   EMAIL: str  # /// Email do signatário
   FONE: str  # /// Telefone do signatário.
   UF_CRC: str  # /// Indicação da unidade da federação que expediu o CRC.
   NUM_SEQ_CRC: str  # /// Número sequencial no seguinte formato: UF/ano/número
   DT_CRC: date  # /// Data de validade do CRC do contador
   IND_RESP_LEGAL: str  # /// Identificação do signatário que será validado como responsável legal da empresa junto as bases da RFB


class RegistroJ932(Registro):
   IDENT_NOM_T: str
   IDENT_CPF_CNPJ_T: str
   IDENT_QUALIF_T: str
   COD_ASSIN_T: str
   IND_CRC_T: str
   EMAIL_T: str
   FONE_T: str
   UF_CRC_T: str
   NUM_SEQ_CRC_T: str
   DT_CRC_T: date


class RegistroJ935(Registro):
   NOME_AUDITOR: str  # // Nome do auditor independente.
   NI_CPF_CNPJ: str
   COD_CVM_AUDITOR: str


class Bloco_J(BlocoSPED):
   RegistroJ001: RegistroJ001
   RegistroJ005: BlockList[RegistroJ005]
   RegistroJ800: BlockList[RegistroJ800]
   RegistroJ801: BlockList[RegistroJ801]
   RegistroJ900: RegistroJ900
   RegistroJ930: BlockList[RegistroJ930]
   RegistroJ932: BlockList[RegistroJ932]  # /// BLOCO J - Lista de RegistroJ932
   RegistroJ935: BlockList[RegistroJ935]
   RegistroJ990: RegistroJ990
   RegistroJ100Count: int
   RegistroJ150Count: int
   RegistroJ200Count: int
   RegistroJ210Count: int
   RegistroJ215Count: int
   RegistroJ800Count: int
   RegistroJ801Count: int


class RegistroC001(BlocoInicial):
   pass


class RegistroC040(Registro):
   HASH_ECD_REC: str
   DT_INI_ECD_REC: date
   DT_FIN_ECD_REC: date
   CNPJ_ECD_REC: str
   IND_ESC: str
   COD_VER_LC: str
   NUM_ORD: str
   NAT_LIVR: str
   IND_SIT_ESP_ECD_REC: int
   IND_NIRE_ECD_REC: int
   IND_FIN_ESC_ECD_REC: int
   TIP_ECD_REC: int
   COD_SCP_ECD_REC: str
   IDENT_MF_ECD_REC: str
   IND_ESC_CONS_ECD_REC: str
   IND_CENTRALIZADA_ECD_REC: int
   IND_MUDANCA_PC_ECD_REC: int
   IND_PLANO_REF_ECD_REC: int
   RegistroC050: BlockList[RegistroC050]
   RegistroC150: BlockList[RegistroC150]
   RegistroC600: BlockList[RegistroC600]


class RegistroC990(Registro):
   QTD_LIN_C: int  # /// Quantidade total de linhas do Bloco K


class Bloco_C(BlocoSPED):
   RegistroC001: RegistroC001
   RegistroC040: RegistroC040
   RegistroC990: RegistroC990
   RegistroC050Count: int
   RegistroC051Count: int
   RegistroC052Count: int
   RegistroC150Count: int
   RegistroC155Count: int
   RegistroC600Count: int
   RegistroC650Count: int


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
   Bloco_0: Bloco_0
   Registro9001: Registro9001  # /// BLOCO 9 - Registro9001
   Registro9900: BlockList[Registro9900]  # /// BLOCO 9 - Lista de Registro9900
   Registro9990: Registro9990  # /// BLOCO 9 - FRegistro9990
   Registro9999: Registro9999  # /// BLOCO 9 - Registro9999


class RegistroK001(BlocoInicial):
   pass


class RegistroK115(Registro):
   EMP_COD_PART: str  # /// Código da empresa envolvida na operação
   COND_PART: str  # /// Condição da empresa relacionada à operação: 1  Sucessora; 2  Adquirente; 3  Alienante.
   PER_EVT: Decimal  # /// Percentual da empresa participante envolvida na operação


class RegistroK110(Registro):
   EVENTO: str  # /// Evento societário ocorrido no período: 1  Aquisição 2  Alienação 3  Fusão 4  Cisão Parcial 5  Cisão Total 6  Incorporação 7  Extinção 8  Constituição
   DT_EVENTO: date  # /// Data do evento societário
   RegistroK115: BlockList[RegistroK115]  # /// BLOCO K - Lista de RegistroK115(FILHO)


class RegistroK100(Registro):
   COD_PAIS: str  # /// Código do país da empresa, conforme tabela do Banco Central do Brasil.
   EMP_COD: str  # /// Código de identificação da empresa participante.
   CNPJ: str  # /// CNPJ(somente os 8 primeiros dígitos).
   NOME: str  # /// Nome empresarial.
   PER_PART: Decimal  # /// Percentual de participação total do conglomerado na empresa no final do período consolidado: Informar a participação acionária.
   EVENTO: str  # /// Evento societário ocorrido no período: S - Sim N  Não
   PER_CONS: Decimal  # /// Percentual de consolidação da empresa no final do período consolidado: Informar o percentual do resultado da empresa que foi para a consolidação.
   DATA_INI_EMP: date  # /// Data inicial do período da escrituração contábil da empresa que foi consolidada.
   DATA_FIN_EMP: date  # /// Data final do período da escrituração contábil da empresa que foi consolidada
   RegistroK110: BlockList[RegistroK110]  # /// BLOCO K - Lista de RegistroK110 (FILHO)


class RegistroK210(Registro):
   COD_EMP: str  # /// Código de identificação da empresa participante
   COD_CTA_EMP: str  # /// Código da conta da empresa participante


class RegistroK200(Registro):
   COD_NAT: str  # /// Código da natureza da conta/grupo de contas, conforme tabela publicada pelo Sped.
   IND_CTA: str  # /// Indicador do tipo de conta: S - Sintética (grupo de contas); A - Analítica (conta).
   NIVEL: str  # /// Nível da conta
   COD_CTA: str  # /// Código da conta
   COD_CTA_SU: str  # /// Código da conta superior
   CTA: str  # /// Nome da conta
   RegistroK210: BlockList[RegistroK210]  # /// BLOCO K - Lista de RegistroK210 (FILHO)


class RegistroK315(Registro):
   EMP_COD_CONTRA: str  # /// Código da empresa da contrapartida
   COD_CONTRA: str  # /// Código da conta consolidada da contrapartida
   VALOR: Decimal  # /// Parcela da contrapartida do valor eliminado total
   IND_VALOR: str  # /// Indicador da situação do valor eliminado


class RegistroK310(Registro):
   EMP_COD_PARTE: str  # /// Código da empresa detentora do valor aglutinado que foi eliminado
   VALOR: Decimal  # /// Parcela do valor eliminado total
   IND_VALOR: str  # /// Indicador da situação do valor eliminado: D  Devedor C  Credor
   RegistroK315: BlockList[RegistroK315]  # /// BLOCO K - Lista de RegistroK315 (FILHO)


class RegistroK300(Registro):
   COD_CTA: str  # /// Código da conta consolidada
   VAL_AG: Decimal  # /// Valor absoluto aglutinado
   IND_VAL_AG: str  # /// Indicador da situação do valor aglutinado: D  Devedor C  Credor
   VAL_EL: Decimal  # /// Valor absoluto das eliminações
   IND_VAL_EL: str  # /// Indicador da situação do valor eliminado: D  Devedor C  Credor
   VAL_CS: Decimal  # /// Valor absoluto consolidado: VAL_CS = VAL_AG  VAL_EL
   IND_VAL_CS: str  # /// Indicador da situação do valor consolidado: D  Devedor C  Credor
   RegistroK310: BlockList[RegistroK310]  # /// BLOCO K - Lista de RegistroK310 (FILHO)


class RegistroK030(Registro):
   DT_INI: date  # /// Data de inicio da escrituração.
   DT_FIN: date  # /// Data de término da escrituração.
   RegistroK100: BlockList[RegistroK100]  # /// BLOCO K - Lista de RegistroK100 (FILHO)
   RegistroK200: BlockList[RegistroK200]  # /// BLOCO K - Lista de RegistroK200 (FILHO)
   RegistroK300: BlockList[RegistroK300]  # /// BLOCO K - Lista de RegistroK300 (FILHO)


class RegistroK990(Registro):
   QTD_LIN_K: int


class Bloco_K(BlocoSPED):
   Bloco_0: Bloco_0
   RegistroK001: RegistroK001
   RegistroK030: RegistroK030
   RegistroK990: RegistroK990
   RegistroK100Count: int
   RegistroK110Count: int
   RegistroK115Count: int
   RegistroK200Count: int
   RegistroK210Count: int
   RegistroK300Count: int
   RegistroK310Count: int
   RegistroK315Count: int


class RegistroC051(Registro):
   COD_CCUS: str
   COD_CTA_REF: str


class RegistroC052(Registro):
   COD_CCUS: str
   COD_AGL: str


class RegistroC050(Registro):
   DT_ALT: date
   COD_NAT: str
   IND_CTA: str
   NIVEL: str
   COD_CTA: str
   COD_CTA_SUP: str
   CTA: str
   RegistroC051: BlockList[RegistroC051]
   RegistroC052: BlockList[RegistroC052]


class RegistroC155(Registro):
   COD_CTA_REC: str
   COD_CCUS_REC: str
   VL_SLD_INI_REC: float
   IND_DC_INI_REC: str
   VL_DEB_REC: float
   VL_CRED_REC: float
   VL_SLD_FIN_REC: float
   IND_DC_FIN_REC: str


class RegistroC150(Registro):
   DT_INI: date
   DT_FIN: date
   RegistroC155: BlockList[RegistroC155]


class RegistroC650(Registro):
   COD_AGL: str
   NIVEL_AGL: str
   DESCR_COD_AGL: str
   VL_CTA_FIN: float
   IND_DC_CTA_FIN: str


class RegistroC600(Registro):
   DT_INI: date
   DT_FIN: date
   ID_DEM: int
   CAB_DEM: str
   RegistroC650: BlockList[RegistroC650]


class RegistroI001(BlocoInicial):
   pass


class RegistroI010(Registro):
   IND_ESC: str  # /// Indicador da forma de escrituração contábil:G - Livro Diário (Completo sem escrituração auxiliar);R - Livro Diário com Escrituração Resumida (com escrituração auxiliar);A - Livro Diário Auxiliar ao Diário com Escrituração Resumida;B - Livro Balancetes Diários e Balanços;Z - Razão Auxiliar (Livro Contábil Auxiliar conforme leiaute definido nos registros I500 a I555).
   COD_VER_LC: str  # /// Código da Versão do Leiaute Contábil (Ver manual).


class RegistroI030(Registro):
   NUM_ORD: str  # /// Número de ordem do instrumento de escrituração.
   NAT_LIVR: str  # /// Natureza do livro; finalidade a que se destina o instrumento.
   QTD_LIN: int  # /// Quantidade total de linhas do arquivo digital.
   NOME: str  # /// Nome empresarial.
   NIRE: str  # /// Número de Identificação do Registro de Empresas da Junta Comercial.
   CNPJ: str  # /// Número de inscrição no CNPJ .
   DT_ARQ: date  # /// Data do arquivamento dos atos constitutivos.
   DT_ARQ_CONV: date  # /// Data de arquivamento do ato de conversão de sociedade simples em sociedade empresária.
   DESC_MUN: str  # /// Município.
   DT_EX_SOCIAL: date  # /// Data de encerramento do exercício social
   NOME_AUDITOR: str  # /// Nome do auditor independente
   COD_CVM_AUDITOR: str  # /// Registro do auditor independente na CVM


class RegistroI990(Registro):
   QTD_LIN_I: int


class RegistroI015(Registro):
   COD_CTA_RES: str  # /// Código da(s) conta(s) analítica(s) do Livro Diário com Escrituração Resumida (R) que recebe os lançamentos globais.


class RegistroI012(Registro):
   NUM_ORD: str  # /// Número de ordem do instrumento associado.
   NAT_LIVR: str  # /// Natureza do livro associado; finalidade a que se destina o instrumento.
   TIPO: str  # /// Tipo de escrituração do livro associado: 0  digital (incluídos no Sped) 1  outros.
   COD_HASH_AUX: str  # /// Código Hash do arquivo correspondente ao livro auxiliar utilizado na assinatura digital.
   RegistroI015: BlockList[RegistroI015]  # /// BLOCO I - Lista de RegistroI051 (FILHO)


class RegistroI020(Registro):
   REG_COD: str  # /// Código do registro que recepciona o campo adicional.
   NUM_AD: str  # /// Número seqüencial do campo adicional.
   CAMPO: str  # /// Nome do campo adicional.
   DESCRICAO: str  # /// Descrição do campo adicional.
   TIPO_DADO: str  # /// Indicação do tipo de dado (N: numérico; C: caractere).


class RegistroI051(Registro):
   COD_PLAN_REF: str  # /// Código da instituição responsável pela manutenção do plano de contas referencial.
   COD_CCUS: str  # /// Código do centro de custo.
   COD_CTA_REF: str  # /// Código da conta de acordo com o plano de contas referencial, conforme tabela publicada pelos órgãos indicados no campo 02- COD_ENT_REF.


class RegistroI052(Registro):
   COD_CCUS: str  # /// Código do centro de custo.
   COD_AGL: str  # /// Código de aglutinação utilizado no Balanço Patrimonial e na Demonstração de Resultado do Exercício no Bloco J (somente para as contas analíticas).


class RegistroI053(Registro):
   COD_IDT: str  # /// Natureza da subconta correlata (conforme tabela de natureza da subconta publicada no Sped )
   COD_CNT_CORR: str  # /// Código de identificação do grupo de conta-subconta(a)
   NAT_SUB_CNT: str  # /// Código da subconta correlata (deve estar no plano de contas e só pode estar relacionada a um único grupo)


class RegistroI050(Registro):
   DT_ALT: date  # /// Data da inclusão/alteração.
   COD_NAT: str  # /// Código da natureza da conta/grupo de contas, conforme tabela publicada pelo Sped.
   IND_CTA: str  # /// Indicador do tipo de conta: S - Sintética (grupo de contas);A - Analítica (conta).
   NIVEL: str  # /// Nível da conta analítica/grupo de contas.
   COD_CTA: str  # /// Código da conta analítica/grupo de contas.
   COD_CTA_SUP: str  # /// Código da conta sintética /grupo de contas de nível imediatamente superior.
   CTA: str  # /// Nome da conta analítica/grupo de contas.
   RegistroI051: BlockList[RegistroI051]  # /// BLOCO I - Lista de RegistroI051 (FILHO)
   RegistroI052: BlockList[RegistroI052]  # /// BLOCO I - Lista de RegistroI052 (FILHO)
   RegistroI053: BlockList[RegistroI053]  # /// BLOCO I - Lista de RegistroI053 (FILHO)    ///


class RegistroI075(Registro):
   COD_HIST: str  # /// Código do histórico padronizado.
   DESCR_HIST: str  # /// Descrição do histórico padronizado.


class RegistroI100(Registro):
   DT_ALT: date  # /// Data da inclusão/alteração.
   COD_CCUS: str  # /// Código do centro de custos.
   CCUS: str  # /// Nome do centro de custos.


class RegistroI151(Registro):
   ASSIM_DIG: str  # /// Transcrição da assinatura digital utilizada no arquivo contendo o conjunto de fichas de lançamento


class RegistroI157(Registro):
   COD_CTA: str  # /// Código da conta analítica do plano de contas anterior.
   COD_CCUS: str  # /// Código do centro de custos.
   VL_SLD_INI: Decimal  # /// Valor do saldo inicial do período.
   IND_DC_INI: str  # /// Indicador da situação do saldo inicial:D - Devedor;C - Credor.
   VL_SLD_INI_MF: Decimal
   IND_DC_INI_MF: str


class RegistroI155(Registro):
   COD_CTA: str  # /// Código da conta analítica.
   COD_CCUS: str  # /// Código do centro de custos.
   VL_SLD_INI: Decimal  # /// Valor do saldo inicial do período.
   IND_DC_INI: str  # /// Indicador da situação do saldo inicial:D - Devedor;C - Credor.
   VL_DEB: Decimal  # /// Valor total dos débitos no período.
   VL_CRED: Decimal  # /// Valor total dos créditos no período.
   VL_SLD_FIN: Decimal  # /// Valor do saldo final do período.
   IND_DC_FIN: str  # /// Indicador da situação do saldo final: D - Devedor; C - Credor.
   VL_SLD_INI_MF: Decimal  # /// Valor do saldo inicial do período.
   IND_DC_INI_MF: str  # /// Indicador da situação do saldo inicial:D - Devedor;C - Credor.
   VL_DEB_MF: Decimal  # /// Valor total dos débitos no período.
   VL_CRED_MF: Decimal  # /// Valor total dos créditos no período.
   VL_SLD_FIN_MF: Decimal  # /// Valor do saldo final do período.
   IND_DC_FIN_MF: str  # /// Indicador da situação do saldo final: D - Devedor; C - Credor.
   RegistroI157: BlockList[RegistroI157]  # /// BLOCO I - Lista de RegistroI157 (FILHO)


class RegistroI150(Registro):
   DT_INI: date  # /// Data de início do período.
   DT_FIN: date  # /// Data de fim do período.
   RegistroI151: BlockList[RegistroI151]  # /// BLOCO I - Lista de RegistroI151 (FILHO)
   RegistroI155: BlockList[RegistroI155]  # /// BLOCO I - Lista de RegistroI155 (FILHO)


class RegistroI250(Registro):
   COD_CTA: str
   COD_CCUS: str
   VL_DC: Decimal
   IND_DC: str
   NUM_ARQ: str
   COD_HIST_PAD: str
   HIST: str
   COD_PART: str
   VL_DC_MF: Decimal
   IND_DC_MF: str


class RegistroI200(Registro):
   NUM_LCTO: str  # // Número de identificação do lançamento
   DT_LCTO: date  # // Data do lançamento
   VL_LCTO: Decimal  # // Valor do Lançamento
   IND_LCTO: str  # // Indicador do tipo do lançamento
   DT_LCTO_EXT: date  # // Data do lançamento extemporaneo
   VL_LCTO_MF: Decimal
   RegistroI250: BlockList[RegistroI250]  # /// BLOCO I - Lista de RegistroI250 (FILHO)


class RegistroI310(Registro):
   COD_CTA: str  # /// Código da conta analítica debitada/creditada.
   COD_CCUS: str  # /// Código do centro de custos.
   VAL_DEBD: Decimal  # /// Total dos débitos do dia.
   VAL_CRED: Decimal  # /// Total dos créditos do dia.
   VAL_DEBD_MF: Decimal
   VAL_CRED_MF: Decimal


class RegistroI300(Registro):
   DT_BCTE: date  # /// Data do Balancete.
   RegistroI310: BlockList[RegistroI310]  # /// BLOCO I - Lista de RegistroI310 (FILHO)


class RegistroI355(Registro):
   COD_CTA: str  # /// Código da conta analítica de resultado.
   COD_CCUS: str  # /// Código do centro de custos.
   VL_CTA: Decimal  # /// Valor do saldo final antes do lançamento de encerramento.
   IND_DC: str  # /// Indicador da situação do saldo final: D - Devedor; C - Credor.
   VL_CTA_MF: Decimal
   IND_DC_MF: str


class RegistroI350(Registro):
   DT_RES: date  # /// Data da apuração do resultado.
   RegistroI355: BlockList[RegistroI355]  # /// BLOCO I - Lista de RegistroI355 (FILHO)


class RegistroI500(Registro):
   TAM_FONTE: int  # /// Tamanho da fonte.


class RegistroI510(Registro):
   NM_CAMPO: str  # ///Nome do campo, sem espaços em branco ou caractere especial.
   DESC_CAMPO: str  # ///Descrição do campo que será utilizado na visualização do Livro Auxiliar.
   TIPO_CAMPO: str  # ///Tipo do campo: "N" - numérico; "C" - caractere.
   TAM_CAMPO: int  # ///Tamanho do campo.
   DEC_CAMPO: int  # ///Quantidade de casas decimais para campos tipo "N".
   COL_CAMPO: int  # ///Largura da coluna no relatório (em quantidade de caracteres).


class RegistroI555(Registro):
   RZ_CONT_TOT: str


class RegistroI550(Registro):
   RZ_CONT: str  # // Conteúdo dos campos mencionados no Registro I510.
   RegistroI555: BlockList[RegistroI555]  # /// BLOCO I - Lista de RegistroI555 (FILHO)


class Bloco_I(BlocoSPED):
   RegistroI001: RegistroI001  # /// BLOCO I - RegistroI001
   RegistroI010: RegistroI010  # /// BLOCO I - RegistroI010
   RegistroI012: BlockList[RegistroI012]
   RegistroI020: BlockList[RegistroI020]
   RegistroI030: RegistroI030
   RegistroI050: BlockList[RegistroI050]
   RegistroI075: BlockList[RegistroI075]
   RegistroI100: BlockList[RegistroI100]
   RegistroI150: BlockList[RegistroI150]
   RegistroI200: BlockList[RegistroI200]
   RegistroI300: BlockList[RegistroI300]
   RegistroI350: BlockList[RegistroI350]
   RegistroI500: BlockList[RegistroI500]
   RegistroI510: BlockList[RegistroI510]
   RegistroI550: BlockList[RegistroI550]
   RegistroI990: RegistroI990  # /// BLOCO I - FRegistroI990


class SPEDContabil:
   DT_INI: date
   DT_FIN: date
   Bloco_0: Bloco_0
   Bloco_C: Bloco_C
   Bloco_9: Bloco_9
   Bloco_I: Bloco_I
   Bloco_J: Bloco_J
   Bloco_K: Bloco_K

   def __str__(self):
      res = []
      if self.Bloco_0:
         if self.Bloco_0.Registro0000:
            self.Bloco_0.Registro0000.DT_INI = self.DT_INI
            self.Bloco_0.Registro0000.DT_FIN = self.DT_FIN
         res.append(str(self.Bloco_0))
      if self.Bloco_C:
         res.append(str(self.Bloco_C))
      if self.Bloco_9:
         res.append(str(self.Bloco_9))
      if self.Bloco_I:
         res.append(str(self.Bloco_I))
      if self.Bloco_J:
         res.append(str(self.Bloco_J))
      if self.Bloco_K:
         res.append(str(self.Bloco_K))
      return '\r\n'.join(res)
