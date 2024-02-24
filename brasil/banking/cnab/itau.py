from typing import Annotated
from datetime import date, datetime, time
from .base import Record


class Cnab400:
    class RemessaHeader(Record):
        """
        Tipo 0 - Header de Remessa
        """
        cod_registro: Annotated[int, 1, 'Código do Registro'] = 0
        cod_remessa: Annotated[int, 1, 'Código da Remessa'] = 1
        literal_remessa: Annotated[str, 7, 'Literal da Remessa'] = 'REMESSA'
        cod_servico: Annotated[int, 2, 'Código do Serviço'] = 1
        literal_servico: Annotated[str, 15, 'Literal de Serviço'] = 'COBRANCA'
        agencia: Annotated[int, 4, 'Código da Agência']
        zeros: Annotated[int, 2, 'Zeros'] = 0
        conta: Annotated[int, 5, 'Conta']
        dac: Annotated[int, 1, 'DV Conta']
        brancos: Annotated[str, 8, 'Brancos']
        nome_empresa: Annotated[str, 30, 'Nome da Empresa']
        cod_banco: Annotated[int, 3, 'Código do Banco'] = 341
        nome_banco: Annotated[str, 15, 'Nome da Banco'] = 'BANCO ITAU SA'
        data_geracao: Annotated[date, 6, 'Data de Geração']
        brancos_2: Annotated[str, 294, 'Brancos']
        num_sequencial: Annotated[int, 6, 'Núm Sequencial'] = 1

    class RemessaDetalhe(Record):
        """
        Tipo 1 - Detalhe de Remessa
        """
        cod_registro: Annotated[int, 1, 'Código do Registro'] = 1
        nat_beneficiario: Annotated[int, 2, 'Tipo Inscrição'] = 2
        cnpj_beneficiario: Annotated[str, 14, 'Núm Inscrição']
        agencia: Annotated[int, 4, 'Agência Mantenedora']
        zeros: Annotated[int, 2, 'Zeros'] = 0
        conta: Annotated[int, 5, 'Conta']
        dac: Annotated[int, 1, 'DV Conta']
        brancos: Annotated[str, 4, 'Brancos']
        instrucao: Annotated[int, 4, 'Instrução/Alegação']
        uso_empresa: Annotated[str, 25, 'Uso Empresa']
        nosso_numero: Annotated[int, 8, 'Nosso Número']
        qtde_moeda: Annotated[float, 13, 'Quantidade de Moeda Variável']
        num_carteira: Annotated[int, 3, 'Núm Carteira']
        uso_banco: Annotated[str, 21, 'Uso Banco']
        carteira: Annotated[str, 1, 'Código da Carteira']
        cod_ocorrencia: Annotated[int, 2, 'Código da Ocorrência']
        num_documento: Annotated[str, 10, 'Núm Documento de Cobrança']
        vencimento: Annotated[date, 6, 'Data de Vencimento']
        valor_titulo: Annotated[int, 13, 'Valor do Título']
        cod_banco: Annotated[int, 3, 'Código Banco'] = 341
        agencia_cobradora: Annotated[int, 5, 'Agencia Cobradora']
        especie_titulo: Annotated[int, 2, 'Espécie Título']
        aceite: Annotated[str, 1, 'Aceite (A/N)']  # A Aceite / N Não Aceite
        data_emissao: Annotated[date, 6, 'Data emissão']
        instrucao_1: Annotated[str, 2, 'Instrução 1']
        instrucao_2: Annotated[str, 2, 'Instrução 2']
        juros_mora: Annotated[float, 13, 'Juros mora por dia']
        data_desconto: Annotated[date, 6, 'Data limite para concessão de desconto']
        valor_desconto: Annotated[int, 13, 'Valor desconto']
        valor_iof: Annotated[float, 13, 'Valor do IOF']
        abatimento: Annotated[float, 13, 'Valor do Abatimento']
        nat_pagador: Annotated[int, 2, 'Nat do Pagador (01 CPF; 02 CNPJ']  # (01; 02)
        cnpj_pagador: Annotated[int, 14, 'Núm Inscrição do Pagador']
        nome: Annotated[str, 30, 'Nome do Pagador']
        brancos: Annotated[str, 10, 'Brancos']
        endereco: Annotated[str, 40, 'Endereço']
        bairro: Annotated[str, 12, 'Bairro']
        cep: Annotated[int, 8, 'CEP']
        cidade: Annotated[str, 15, 'Cidade']
        uf: Annotated[str, 2, 'UF']
        sacador: Annotated[str, 30, 'Nome Sacador/Avalista']
        brancos_2: Annotated[str, 4, 'Brancos']
        data_mora: Annotated[date, 6, 'Data Mora']
        prazo: Annotated[int, 2, 'Prazo em dias']
        brancos_3: Annotated[str, 1, 'Brancos']
        num_sequencial: Annotated[int, 6, 'Núm Sequencial']

    class RemessaTrailer(Record):
        """
        Tipo 9 - Trailer de Remessa
        """
        cod_registro: Annotated[int, 1, 'Cod Registro'] = 9
        brancos: Annotated[str, 393, 'Brancos']
        num_sequencial: Annotated[int, 6, 'Num Sequencial']


class Cnab240:
    class HeaderArquivo(Record):
        """
        Header de arquivo
        """
        cod_banco: Annotated[int, 3, 'Código Banco'] = 341
        cod_lote: Annotated[int, 4, 'Lote Serviço'] = 0
        tipo_registro: Annotated[int, 1, 'Tipo Registro'] = 0
        brancos: Annotated[str, 9, 'Brancos']
        nat_juridica: Annotated[int, 1, '1 CPF/2 CNPJ']
        cnpj: Annotated[str, 14, 'Núm CPF/CNPJ']
        brancos2: Annotated[str, 1, 'Brancos']
        zeros: Annotated[int, 7, 'Zeros'] = 0
        conta: Annotated[int, 5, 'Conta']
        dac: Annotated[int, 1, 'DV Conta']
        nome_empresa: Annotated[str, 30, 'Nome Empresa']
        nome_banco: Annotated[str, 30, 'Nome Banco'] = 'BANCO ITAU SA'
        brancos3: Annotated[str, 1, 'Brancos']
        cod_arquivo: Annotated[int, 1, 'Remessa/Retorno'] = '1'
        data_geracao: Annotated[date, 8, 'Data Geração']
        hora_geracao: Annotated[time, 6, 'Hora Geração']
        seq_arq_retorno: Annotated[int, 6, 'Num Sequencial Arquivo de Retorno']
        layout_arquivo: Annotated[int, 3, 'Layout do Arquivo'] = 40
        zeros2: Annotated[int, 5, 'Zeros']
        brancos4: Annotated[str, 54, 'Brancos']
        zeros: Annotated[int, 3, 'Zeros']
        brancos5: Annotated[str, 12, 'Brancos']

    class HeaderLote(Record):
        """
        Header de lote
        """
        cod_banco: Annotated[int, 3, 'Código Banco'] = 341
        cod_lote: Annotated[int, 4, 'Lote Serviço']
        tipo_registro: Annotated[int, 1, 'Tipo Registro'] = 1
        operacao: Annotated[str, 1, 'Operação'] = 'R'
        cod_servico: Annotated[int, 2, 'Código Serviço'] = 1
        zeros: Annotated[int, 2, 'Zeros']
        layout_lote: Annotated[int, 3, 'Layout do Lote'] = 30
        brancos: Annotated[str, 1, 'Brancos']
        nat_juridica: Annotated[int, 1, '1 CPF/2 CNPJ']
        cnpj: Annotated[str, 14, 'CPF/CNPJ']
        brancos2: Annotated[str, 1, 'Brancos']
        zeros2: Annotated[int, 7, 'Zeros']
        conta: Annotated[int, 5, 'Conta']
        brancos2: Annotated[str, 1, 'Brancos']
        dac: Annotated[int, 1, 'DV Conta']
        nome_empresa: Annotated[str, 30, 'Nome Empresa']
        brancos3: Annotated[str, 80, 'Brancos']
        seq_arq_retorno: Annotated[int, 8, 'Num Sequencial Arquivo de Retorno']
        data_gravacao: Annotated[date, 8, 'Data Gravação']
        data_credito: Annotated[date, 8, 'Data Credito']
        brancos4: Annotated[str, 33, 'Brancos']

    class Detalhe(Record):
        cod_banco: Annotated[int, 3, 'Código Banco'] = 341
        cod_lote: Annotated[int, 4, 'Lote Serviço']
        tipo_registro: Annotated[int, 1, 'Tipo Registro'] = 3
        num_registro: Annotated[int, 5, 'Num Sequencial Registro no Lote']
        segmento: Annotated[str, 1, 'Segmento'] = 'P'
        brancos: Annotated[str, 1, 'Brancos']
        cod_ocorrencia: Annotated[int, 2, 'Cod Ocorrencia']
        zeros: Annotated[int, 7, 'Zeros'] = 0
        conta: Annotated[int, 5, 'Conta']
        brancos: Annotated[str, 1, 'Brancos']
        dac: Annotated[int, 1, 'DV Conta']
        num_carteira: Annotated[int, 3, 'Num Carteira']
        nosso_numero: Annotated[int, 8, 'Nosso Número']
        dac_nosso_numero: Annotated[int, 1, 'DV Nosso Número']
        brancos2: Annotated[str, 8, 'Brancos']
        zeros2: Annotated[int, 5, 'Zeros']
        num_documento: Annotated[str, 10, 'Num Documento']
        brancos: Annotated[str, 5, 'Brancos']
        vencimento: Annotated[date, 8, 'Data Vencimento']
        valor_titulo: Annotated[float, 13, 'Valor Título']
        agencia: Annotated[int, 5, 'Agência Cobradora']
        dac_agencia: Annotated[int, 1, 'DV Agência']
        especie: Annotated[int, 2, 'Espécie do Título']
        aceite: Annotated[str, 1, 'A/N']
        data_emissao: Annotated[date, 8, 'Data Emissão']
        zeros2: Annotated[int, 1, 'Zeros']
        data_juros: Annotated[date, 8, 'Data Juros Mora']
        juros_dia: Annotated[float, 13, 'Juros por Dia de Atraso']
        zeros3: Annotated[int, 1, 'Zeros']
        dasta_1_desc: Annotated[date, 8, 'Data 1 Desconto']
        valor_1_desc: Annotated[float, 13, 'Valor 1 Desconto']
        valor_iof: Annotated[float, 13, 'Valor IOF']
        valor_abatimento: Annotated[float, 13, 'Valor Abatimento']
        uso_empresa: Annotated[str, 25, 'Uso Empresa']
        cod_protesto: Annotated[int, 1, 'Cód Protesto']
        cod_baixa: Annotated[int, 1, 'Cód Baixa']
        prazo_baixa: Annotated[int, 2, 'Num dias para baixa']
        zeros: Annotated[int, 13, 'Zeros']
        brancos: Annotated[str, 1, 'Brancos']

    class SegmentoQ(Record):
        cod_banco: Annotated[int, 3, 'Código Banco'] = 341
        cod_lote: Annotated[int, 4, 'Lote Serviço']
        tipo_registro: Annotated[int, 1, 'Tipo Registro'] = 3
        num_registro: Annotated[int, 5, 'Num Sequencial Registro no Lote']
        segmento: Annotated[str, 1, 'Segmento'] = 'Q'
        brancos: Annotated[str, 1, 'Brancos']
        cod_ocorrencia: Annotated[int, 2, 'Cod Ocorrencia']
        nat_juridica: Annotated[int, 1, '1 CPF/2 CNPJ']
        cnpj: Annotated[str, 15, 'Núm CPF/CNPJ']
        nome: Annotated[str, 63, 'Nome Pagador']
        brancos: Annotated[str, 10, 'Brancos']
        endereco: Annotated[str, 40, 'Endereço']
        bairro: Annotated[str, 15, 'Bairro']
        cep: Annotated[int, 8, 'CEP']
        cidade: Annotated[str, 15, 'Cidade']
        uf: Annotated[str, 2, 'UF']
        nat_sacador: Annotated[int, 1, '1 CPF/2 CNPJ']
        brancos: Annotated[str, 10, 'Brancos']
        zeros: Annotated[int, 3, 'Zeros']
        brancos: Annotated[str, 28, 'Brancos']

