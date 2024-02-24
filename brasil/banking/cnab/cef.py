from typing import Annotated, List
from .base import Record
from .cnab240 import Arquivo240


class Cnab240:
    class Remessa(Arquivo240):
        class HeaderArquivo(Record):
            banco: Annotated[int, 3, "Banco"] = 104
            lote: Annotated[int, 4, "Lote"] = 0
            registro: Annotated[int, 1, "Registro"] = 0
            cnab: Annotated[str, 9, "CNAB"]
            tipo_inscricao: Annotated[int, 1, "Tipo Inscrição"]
            cnpj_beneficiario: Annotated[int, 14, "CNPJ Beneficiario"]
            zeros: Annotated[int, 20, "Zeros"]
            agencia: Annotated[int, 5, "Agencia"]
            dv_agencia: Annotated[str, 1, "DV Agencia"]
            codigo_beneficiario: Annotated[int, 7, "Código Beneficiário"]
            zeros2: Annotated[int, 6, "Zeros2"]
            caixa: Annotated[int, 1, "Caixa"]
            nome_empresa: Annotated[str, 30, "Nome Empresa"]
            banco_beneficiario: Annotated[str, 30, "Banco Beneficiário"]
            cnab2: Annotated[str, 10, "CNAB2"]
            codigo_arquivo: Annotated[int, 1, "Código Arquivo"] = 1
            data_geracao: Annotated[int, 8, "Data Geração"]
            hora_geracao: Annotated[int, 6, "Hora Geração"]
            nsa: Annotated[int, 6, "NSA"]
            versao_layout: Annotated[int, 3, "Versão Layout"]
            gravacao_arquivo: Annotated[int, 5, "Gravação Arquivo"]
            brancos: Annotated[str, 20, "Brancos"]
            reservado_empresa: Annotated[str, 20, "Reservado Empresa"]
            brancos2: Annotated[str, 4, "Brancos2"]
            cnab3: Annotated[str, 25, "CNAB3"]

        class HeaderLote(Record):
            banco: Annotated[int, 3, "Banco"] = 104
            servico: Annotated[int, 4, "Serviço"]
            registro: Annotated[int, 1, "Registro"] = 1
            tipo_operacao: Annotated[str, 1, "Tipo Operação"]
            tipo_servico: Annotated[int, 2, "Tipo de Serviço"]
            zeros: Annotated[int, 2, "Zeros"]
            n_versao_layout_lote: Annotated[int, 3, "Nº da Versão do Layout do Lote"]
            cnab: Annotated[str, 1, "CNAB"]
            tipo_inscricao: Annotated[int, 1, "Tipo Inscrição"]
            cnpj_beneficiario: Annotated[int, 15, "CNPJ Beneficiário"]
            codigo_beneficiario: Annotated[int, 7, "Código Beneficiário"]
            zeros2: Annotated[int, 13, "Zeros2"]
            agencia: Annotated[int, 5, "Agência"]
            dv_agencia: Annotated[str, 1, "DV Agência"]
            codigo_beneficiario2: Annotated[int, 6, "Código Beneficiário2"]
            codigo_modelo_personalizado: Annotated[int, 7, "Código Modelo Personalizado"]
            zeros3: Annotated[int, 1, "Zeros3"]
            nome_empresa: Annotated[str, 30, "Nome da Empresa"]
            informacoes: Annotated[str, 40, "Informações"]
            mensagem_2: Annotated[str, 40, "Mensagem 2"]
            controle_cobranca: Annotated[int, 8, "Controle da Cobrança"]
            data_gravacao: Annotated[int, 8, "Data Gravação"]
            data_credito: Annotated[int, 8, "Data Crédito"] = 0
            cnab2: Annotated[str, 33, "CNAB2"]

        class SegmentoP(Record):
            banco: Annotated[int, 3, "Banco"] = 104
            servico: Annotated[int, 4, "Serviço"]
            registro: Annotated[int, 1, "Registro"] = 3
            sequencial_lote: Annotated[int, 5, "Sequencial Lote"]
            segmento: Annotated[str, 1, "Segmento"] = "P"
            filler: Annotated[str, 1, "Filler"]
            codigo_movimento_remessa: Annotated[int, 2, "Código de Movimento Remessa"]
            codigo_identificacao_beneficiario: Annotated[int, 5, "Código de Identificação do Beneficiário"]
            digito_verificador_agencia: Annotated[str, 1, "Dígito Verificador da Agência"]
            codigo_beneficiario: Annotated[int, 7, "Código do Beneficiário"]
            uso_exclusivo_caixa: Annotated[int, 7, "Uso Exclusivo CAIXA"]
            uso_exclusivo_caixa2: Annotated[int, 2, "Uso Exclusivo CAIXA2"]
            nosso_numero: Annotated[int, 1, "Nosso Número"]
            modalidade_carteira_sigcb: Annotated[int, 2, "Modalidade da Carteira (SIGCB)"]
            identificacao_titulo_no_banco: Annotated[int, 15, "Identificação do Título no Banco"]
            caracteristicas_cobranca: Annotated[int, 1, "Características da Cobrança"]
            forma_cadastramento_titulo_no_banco: Annotated[int, 1, "Forma de Cadastramento do Título no Banco"] = 1
            tipo_documento: Annotated[str, 1, "Tipo de Documento"] = 2
            identificacao_emissao_boleto: Annotated[int, 1, "Identificação da Emissão do Boleto"]
            identificacao_entrega_boleto: Annotated[str, 1, "Identificação da Entrega do Boleto"]
            n_documento_seu_n: Annotated[str, 11, "Nº do Documento (Seu Nº)"]
            uso_exclusivo_caixa3: Annotated[str, 4, "Uso Exclusivo CAIXA3"]
            vencimento: Annotated[int, 8, "Vencimento"]
            valor_titulo: Annotated[float, 15, "Valor do Título"]
            ag_cobradora: Annotated[int, 5, "Ag. Cobradora"]
            dv: Annotated[str, 1, "DV"]
            especie_titulo: Annotated[int, 2, "Espécie de Título"]
            aceite: Annotated[str, 1, "Aceite"]
            data_emissao_titulo: Annotated[int, 8, "Data Emissão do Título"]
            juros: Annotated[int, 1, "Juros"]
            data_juros_mora: Annotated[int, 8, "Data do Juros de Mora"]
            juros_mora_por_diataxa: Annotated[float, 15, "Juros de Mora por Dia/Taxa"]
            desconto_1: Annotated[int, 1, "Desconto 1"]
            data_desconto_1: Annotated[int, 8, "Data do Desconto 1"]
            valorpercentual_ser_concedido: Annotated[float, 15, "Valor/Percentual a ser Concedido"]
            valor_iof: Annotated[float, 15, "Valor IOF"]
            valor_abatimento: Annotated[float, 15, "Valor Abatimento"]
            uso_empresa_beneficiario: Annotated[str, 25, "Uso Empresa Beneficiário"]
            codigo_p_protesto: Annotated[int, 1, "Código p/ Protesto"]
            prazo_p_protesto: Annotated[int, 2, "Prazo p/ Protesto"]
            codigo_p_baixadevolucao: Annotated[int, 1, "Código p/ Baixa/Devolução"]
            prazo_p_baixadevolucao: Annotated[int, 3, "Prazo p/ Baixa/Devolução"]
            codigo_moeda: Annotated[int, 2, "Código da Moeda"] = 9
            uso_exclusivo_caixa4: Annotated[int, 10, "Uso Exclusivo CAIXA4"]
            uso_livre_bancoempresa: Annotated[str, 1, "Uso livre banco/empresa"]

        class SegmentoQ(Record):
            banco: Annotated[int, 3, "Banco"] = 104
            lote: Annotated[int, 4, "Lote"]
            tipo_registro: Annotated[int, 1, "Tipo de Registro"] = 3
            servico: Annotated[int, 5, "Serviço"]
            segmento: Annotated[str, 1, "Segmento"] = "Q"
            filler: Annotated[str, 1, "Filler"]
            codigo_movimento_remessa: Annotated[int, 2, "Código de Movimento Remessa"]
            dados_pagador: Annotated[int, 1, "Dados do Pagador"]
            cnpj_pagador: Annotated[float, 15, "CNPJ Pagador"]
            nome_pagador: Annotated[str, 40, "Nome do Pagador"]
            endereco_pagador: Annotated[str, 40, "Endereço do Pagador"]
            bairro_pagador: Annotated[str, 15, "Bairro do Pagador"]
            cep_pagador: Annotated[int, 8, "CEP do Pagador"]
            cidade_pagador: Annotated[str, 15, "Cidade do Pagador"]
            unidade_federacao_pagador: Annotated[str, 2, "Unidade da Federação do Pagador"]
            dados_sacador_avalista: Annotated[int, 1, "Dados do Sacador/ Avalista"]
            numero_inscricao_sacadoravalista: Annotated[float, 15, "Número de Inscrição do Sacador/Avalista"]
            nome_sacadoravalista: Annotated[str, 40, "Nome do Sacador/Avalista"]
            banco_correspondente: Annotated[int, 3, "Banco Correspondente"]
            nosso_num_bco_correspondente: Annotated[str, 20, "Nosso Núm. Bco. Correspondente"]
            cnab: Annotated[str, 8, "CNAB"]

        class SegmentoR(Record):
            banco: Annotated[int, 3, "Banco"] = 104
            lote: Annotated[int, 4, "Lote"]
            tipo_registro: Annotated[int, 1, "Tipo de Registro"] = 3
            sequencial: Annotated[int, 5, "Sequencial"]
            cod_segmento_registro_detalhe: Annotated[str, 1, "Cód. Segmento do Registro Detalhe"] = "R"
            filler: Annotated[str, 1, "Filler"]
            codigo_movimento_remessa: Annotated[int, 2, "Código de Movimento Remessa"]
            codigo_desconto_2: Annotated[int, 1, "Código do Desconto 2"]
            data_desconto_2: Annotated[int, 8, "Data do Desconto 2"]
            valorpercentual_ser_concedido: Annotated[int, 15, "Valor/Percentual a ser Concedido"]
            codigo_desconto_3: Annotated[int, 1, "Código do Desconto 3"]
            data_desconto_3: Annotated[int, 8, "Data do Desconto 3"]
            valorpercentual_ser_concedido2: Annotated[int, 15, "Valor/Percentual a Ser Concedido2"]
            codigo_multa: Annotated[str, 1, "Código da Multa"]
            data_multa: Annotated[int, 8, "Data da Multa"]
            valorpercentual_ser_aplicado: Annotated[int, 15, "Valor/Percentual a Ser Aplicado"]
            informacao_ao_pagador: Annotated[str, 10, "Informação ao Pagador"]
            mensagem_3: Annotated[str, 40, "Mensagem 3"]
            mensagem_4: Annotated[str, 40, "Mensagem 4"]
            filler2: Annotated[str, 50, "Filler2"]
            filler3: Annotated[str, 11, "Filler3"]

        class TrailerLote(Record):
            banco: Annotated[int, 3, "Banco"] = 104
            lote_servico: Annotated[int, 4, "Lote Serviço"]
            tipo_registro: Annotated[int, 1, "Tipo Registro"] = 5
            cnab: Annotated[int, 9, "CNAB"]
            qtde_registros: Annotated[str, 6, "Qtde de Registros"]
            totalizacao_cobranca_simples: Annotated[int, 6, "Totalização da Cobrança Simples"]
            valor_total_titulos_simples: Annotated[int, 17, "Valor Total Títulos Simples"]
            qtde_titulos: Annotated[int, 6, "Qtde Títulos"] = 0
            valor_titulo_carteira_caucionada: Annotated[int, 17, "Valor Título Carteira Caucionada"] = 0
            qtde_titulos_cobranca_descontada: Annotated[int, 6, "Qtde Títulos Cobrança Descontada"]
            qtde_titulos_carteiras_descontadas: Annotated[int, 17, "Qtde Títulos Carteiras Descontadas"] = 0
            cnab2: Annotated[int, 31, "CNAB2"]
            cnab3: Annotated[str, 117, "CNAB3"]

        class TrailerArquivo(Record):
            banco: Annotated[int, 3, "Banco"] = 104
            lote: Annotated[int, 4, "Lote"] = 9999
            tipo_registro: Annotated[int, 1, "Tipo de Registro"] = 9
            cnab: Annotated[str, 9, "CNAB"]
            qtde_lotes: Annotated[int, 6, "Qtde Lotes"]
            qtde_registros_arquivo: Annotated[int, 6, "Qtde de Registros do Arquivo"]
            cnab2: Annotated[str, 6, "CNAB2"]
            cnab3: Annotated[str, 205, "CNAB3"]

        header_arquivo: HeaderArquivo
        header_lote: HeaderLote
        segmento_p: List[SegmentoP]
        segmento_q: List[SegmentoQ]
        segmento_r: List[SegmentoR]
        trailer_lote: TrailerLote
        trailer_arquivo: TrailerArquivo

    class Retorno(Arquivo240):
        class HeaderArquivo(Record):
            banco: Annotated[int, 3, "Banco"] = 104
            lote: Annotated[int, 4, "Lote"] = 0
            tipo_registro: Annotated[int, 1, "Tipo de Registro"] = 0
            cnab: Annotated[str, 9, "CNAB"]
            empresa_beneficiaria: Annotated[int, 1, "Empresa Beneficiária"]
            cnpj: Annotated[int, 14, "CNPJ"]
            uso_exclusivo_caixa: Annotated[int, 20, "Uso Exclusivo CAIXA"]
            agencia_mantenedora_conta: Annotated[int, 5, "Agência Mantenedora da Conta"]
            digito_verificador_agencia: Annotated[str, 1, "Dígito Verificador da Agência"]
            codigo_beneficiario: Annotated[int, 7, "Código do Beneficiário"]
            uso_exclusivo_caixa2: Annotated[int, 6, "Uso Exclusivo CAIXA2"]
            uso_exclusivo_caixa3: Annotated[int, 1, "Uso Exclusivo CAIXA3"]
            nome_empresa: Annotated[str, 30, "Nome da Empresa"]
            banco_beneficiario: Annotated[str, 30, "Banco Beneficiário"]
            cnab2: Annotated[str, 10, "CNAB2"]
            arquivo: Annotated[int, 1, "Arquivo"]
            data_geracao: Annotated[int, 8, "Data Geração"]
            hora_geracao: Annotated[int, 6, "Hora Geração"]
            nsa: Annotated[int, 6, "NSA"]
            versao_layout: Annotated[int, 3, "Versão Layout"]
            densidade_gravacao_arquivo: Annotated[int, 5, "Densidade de Gravação do Arquivo"]
            uso_exclusivo_caixa4: Annotated[str, 20, "Uso Exclusivo CAIXA4"]
            reservado_empresa: Annotated[str, 20, "Reservado Empresa"]
            versao_aplicativo: Annotated[str, 4, "Versão do Aplicativo"]
            cnab3: Annotated[str, 10, "CNAB3"]
            cnab4: Annotated[str, 3, "CNAB4"]
            cnab5: Annotated[str, 12, "CNAB5"]

        class HeaderLote(Record):
            banco: Annotated[int, 3, "Banco"] = 104
            lote: Annotated[int, 4, "Lote"]
            tipo_registro: Annotated[int, 1, "Tipo de Registro"] = 1
            servico: Annotated[str, 1, "Serviço"] = "T"
            tipo_servico: Annotated[int, 2, "Tipo de Serviço"] = 1
            filler: Annotated[int, 2, "Filler"]
            versao_layout: Annotated[int, 3, "Versão Layout"]
            cnab: Annotated[str, 1, "CNAB"]
            empresa: Annotated[int, 1, "Empresa"]
            cnpj: Annotated[int, 15, "CNPJ"]
            codigo_beneficiario: Annotated[int, 7, "Código do Beneficiário"]
            uso_exclusivo_caixa: Annotated[int, 13, "Uso Exclusivo CAIXA"]
            agencia_mantenedora_conta: Annotated[int, 5, "Agência Mantenedora da Conta"]
            digito_verificador_agencia: Annotated[str, 1, "Dígito Verificador da Agência"]
            uso_exclusivo_caixa2: Annotated[int, 7, "Uso Exclusivo CAIXA2"]
            codigo_modelo_personalizado: Annotated[int, 6, "Código do Modelo Personalizado"]
            uso_exclusivo_caixa3: Annotated[int, 1, "Uso Exclusivo CAIXA3"]
            nome_empresa: Annotated[str, 30, "Nome da Empresa"]
            informacoes: Annotated[str, 40, "Informações"]
            mensagem_2: Annotated[str, 40, "Mensagem 2"]
            controle_cobranca: Annotated[int, 8, "Controle da Cobrança"]
            data_gravacao_retorno: Annotated[int, 8, "Data de Gravação Retorno"]
            data_credito: Annotated[int, 8, "Data do Crédito"]
            cnab2: Annotated[str, 2, "CNAB2"]
            cnab3: Annotated[str, 26, "CNAB3"]
            cnab4: Annotated[str, 2, "CNAB4"]
            cnab5: Annotated[str, 3, "CNAB5"]

        class SegmentoT(Record):
            banco: Annotated[int, 3, "Banco"] = 104
            lote: Annotated[int, 4, "Lote"]
            tipo_registro: Annotated[int, 1, "Tipo de Registro"] = 3
            servico: Annotated[int, 5, "Serviço"]
            segmento: Annotated[str, 1, "Segmento"] = "T"
            filler: Annotated[str, 1, "Filler"]
            codigo_movimento_retorno: Annotated[int, 2, "Código de Movimento Retorno"]
            codigo_agencia: Annotated[int, 5, "Código da Agência"]
            dv_agencia: Annotated[int, 1, "DV da Agência"]
            codigo_beneficiario: Annotated[int, 7, "Código do Beneficiário"]
            uso_exclusivo_caixa: Annotated[int, 2, "Uso Exclusivo CAIXA"]
            numero_banco: Annotated[int, 3, "Número do Banco"]
            uso_exclusivo_caixa2: Annotated[int, 1, "Uso Exclusivo CAIXA2"]
            uso_exclusivo_caixa3: Annotated[str, 2, "Uso Exclusivo CAIXA3"]
            nosso_numero: Annotated[str, 1, "Nosso Número"]
            modalidade_carteira: Annotated[str, 2, "Modalidade da Carteira"]
            identificacao_titulo_no_banco: Annotated[str, 15, "Identificação do Título no Banco"]
            uso_exclusivo_caixa4: Annotated[str, 1, "Uso Exclusivo CAIXA4"]
            carteira: Annotated[int, 1, "Carteira"]
            numero_documento: Annotated[str, 11, "Número Documento"]
            uso_exclusivo_caixa5: Annotated[str, 4, "Uso Exclusivo CAIXA5"]
            vencimento: Annotated[int, 8, "Vencimento"]
            valor_titulo: Annotated[float, 15, "Valor do Título"]
            banco_cobradorrecebedor: Annotated[int, 3, "Banco Cobrador/Recebedor"]
            agencia_cobradorarecebedora: Annotated[int, 5, "Agência Cobradora/Recebedora"]
            dv_agencia_cobrreceb: Annotated[int, 1, "DV Agência Cobr/Receb"]
            uso_empresa: Annotated[str, 25, "Uso da Empresa"]
            codigo_moeda: Annotated[int, 2, "Código da Moeda"]
            pagador: Annotated[int, 1, "Pagador"]
            numero_inscricao_pagador: Annotated[int, 15, "Número de Inscrição do Pagador"]
            nome_pagador: Annotated[str, 40, "Nome do Pagador"]
            cnab: Annotated[str, 10, "CNAB"]
            valor_tarcustas: Annotated[int, 15, "Valor da Tar./Custas"]
            motivo_ocorrencia: Annotated[str, 10, "Motivo da Ocorrência"]
            cnab2: Annotated[str, 17, "CNAB2"]

        class SegmentoU(Record):
            banco: Annotated[int, 3, "Banco"] = 104
            lote_servico: Annotated[int, 4, "Lote de Serviço"]
            tipo_registro: Annotated[int, 1, "Tipo de Registro"] = 3
            servico: Annotated[int, 5, "Serviço"]
            segmento: Annotated[str, 1, "Segmento"] = "U"
            filler: Annotated[str, 1, "Filler"]
            cod_mov_retorno: Annotated[int, 2, "Cód. Mov. Retorno"]
            dados_titulo: Annotated[int, 15, "Dados do Título"]
            valor_desconto_concedido_para_titulo: Annotated[float, 15, "Valor do Desconto Concedido para o título"]
            valor_abat_concedidocancel_titulo: Annotated[float, 15, "Valor do Abat. Concedido/Cancel. Do título"]
            valor_iof_recolhido_para_titulo: Annotated[float, 15, "Valor do IOF Recolhido para o título"]
            valor_pago_pelo_pagador: Annotated[float, 15, "Valor Pago pelo Pagador"]
            valor_liquido_ser_creditado: Annotated[float, 15, "Valor Líquido a ser Creditado"]
            outras_despesas: Annotated[float, 15, "Outras Despesas"]
            outros_creditos: Annotated[float, 15, "Outros Créditos"]
            data_ocorrencia: Annotated[int, 8, "Data da Ocorrência"]
            data_credito: Annotated[int, 8, "Data do Crédito"]
            uso_exclusivo_caixa: Annotated[int, 4, "Uso Exclusivo CAIXA"]
            data_debito_tarifa: Annotated[int, 8, "Data do Débito da Tarifa"]
            codigo_pagador: Annotated[int, 15, "Código do Pagador"]
            uso_exclusivo_caixa2: Annotated[int, 30, "Uso Exclusivo CAIXA2"]
            cod_bco_corr: Annotated[int, 3, "Cód. Bco. Corr."]
            nosso_n_banco_correspondente: Annotated[int, 20, "Nosso Nº Banco Correspondente"]
            uso_exclusivo_febrabancnab: Annotated[str, 7, "Uso Exclusivo FEBRABAN/CNAB"]

        class TrailerLote(Record):
            banco: Annotated[int, 3, "Banco"] = 104
            lote: Annotated[int, 4, "Lote"]
            registro: Annotated[int, 1, "Registro"] = 5
            cnab: Annotated[str, 9, "CNAB"]
            qtde_registros: Annotated[int, 6, "Qtde de Registros"]
            totalizacao_cobranca_simples: Annotated[int, 6, "Totalização da Cobrança Simples"]
            valor_titulos_carteiras_cobranca_simples: Annotated[int, 17, "Valor Títulos Carteiras de Cobrança Simples"]
            qtde_cobranca_caucionada: Annotated[int, 6, "Qtde Cobrança Caucionada"]
            valor_carteiras_caucionadas: Annotated[int, 17, "Valor Carteiras Caucionadas"]
            qtde_cobranca_descontada: Annotated[int, 6, "Qtde da Cobrança Descontada"]
            qtde_titulos_carteiras_descontadas: Annotated[int, 17, "Qtde Títulos Carteiras Descontadas"]
            cnab2: Annotated[str, 31, "CNAB2"]
            cnab3: Annotated[str, 117, "CNAB3"]

        class TrailerArquivo(Record):
            banco: Annotated[int, 3, "Banco"] = 104
            lote: Annotated[int, 4, "Lote"] = 9999
            tipo_registro: Annotated[int, 1, "Tipo de Registro"] = 9
            cnab: Annotated[str, 9, "CNAB"]
            totais: Annotated[int, 6, "Totais"]
            qtde_registros_arquivo: Annotated[int, 6, "Qtde Registros do Arquivo"]
            cnab2: Annotated[str, 6, "CNAB2"]
            cnab3: Annotated[str, 205, "CNAB3"]

        header_arquivo: HeaderArquivo
        header_lote: HeaderLote
        segmento_t: List[SegmentoT]
        segmento_u: List[SegmentoU]
        trailer_lote: TrailerLote
        trailer_arquivo: TrailerArquivo

