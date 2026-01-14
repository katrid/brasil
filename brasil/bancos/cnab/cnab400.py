from typing import Annotated
from datetime import date
from .base import Record


class RemessaHeader(Record):
    """
    Tipo 0 - Header de Remessa
    """
    cod_registro: Annotated[int, 1, 'Código do Registro'] = 0  # 1
    cod_remessa: Annotated[int, 1, 'Código da Remessa'] = 1  # 2
    literal_remessa: Annotated[str, 7, 'Literal da Remessa'] = 'REMESSA'  # 3
    cod_servico: Annotated[int, 2, 'Código do Serviço'] = 1  # 4
    literal_servico: Annotated[str, 15, 'Literal de Serviço'] = 'COBRANCA'  # 5
    agencia: Annotated[int, 4, 'Código da Agência']  # 6
    cod_beneficiario: Annotated[int, 7, 'Código Beneficiário']  # 7
    uso_exclusivo: Annotated[str, 9, 'Uso Exclusivo']  # 8
    nome_empresa: Annotated[str, 30, 'Nome da Empresa']  # 9
    cod_banco: Annotated[int, 3, 'Código do Banco']  # 10
    nome_banco: Annotated[str, 15, 'Nome da Banco']  # 11
    data_geracao: Annotated[date, 6, 'Data de Geração']  # 12
    versao_layout: Annotated[int, 3, 'Versão do Layout']  # 12v
    uso_exclusivo2: Annotated[str, 286, 'Uso Exclusivo']  # 13
    num_sequencial_a: Annotated[int, 5, 'Núm Sequencial A']  # 14
    num_sequencial_b: Annotated[int, 6, 'Núm Sequencial B'] = 1  # 15


class RemessaDetalhe(Record):
    """
    Tipo 1 - Detalhe de Remessa
    """
    cod_registro: Annotated[int, 1, 'Código do Registro'] = 1  # 01.1
    nat_beneficiario: Annotated[int, 2, 'Tipo Inscrição'] = 2  # 02.1 (01; 02)
    cnpj_beneficiario: Annotated[int, 14, 'Núm Inscrição']  # 03.1
    uso_exclusivo: Annotated[int, 3, 'Uso Exclusivo']  # 04.1
    cod_beneficiario: Annotated[int, 7, 'Código Beneficiário']  # 05.1
    id_emissao: Annotated[int, 1, 'ID Emissão']  # 06.1
    id_postagem: Annotated[int, 1, 'ID Postagem']  # 07.1
    taxa_permanencia: Annotated[int, 2, 'Taxa Permanência']  # 09.1
    id_titulo: Annotated[str, 25, 'Identificação do título na empresa']  # 10.1
    nosso_numero: Annotated[int, 17, 'Nosso Número']  # 11.1
    brancos: Annotated[str, 2, 'Brancos']  # 12.1
    uso_livre: Annotated[int, 1, 'Uso livre branco']  # 12A.1
    cod_juros: Annotated[int, 1, 'Código Juros']  # 13.1
    data_juros: Annotated[date, 6, 'Data Juros']  # 13A.1
    cod_desconto: Annotated[int, 1, 'Código Desconto']  # 13B.1
    brancos_2: Annotated[str, 22, 'Brancos']  # 13C.1
    carteira: Annotated[int, 2, 'Carteira']  # 14.1
    cod_ocorrencia: Annotated[int, 2, 'Código Ocorrência']  # 15.1
    uso_empresa: Annotated[str, 10, 'Uso Empresa Beneficiário']  # 16.1
    vencimento: Annotated[date, 6, 'Vencimento']  # 17.1
    valor_titulo: Annotated[int, 13, 'Valor do Título']  # 18.1
    cod_banco: Annotated[int, 3, 'Código Banco']  # 19.1
    agencia_cobradora: Annotated[int, 5, 'Agencia Cobradora']  # 20.1
    especie_titulo: Annotated[int, 2, 'Espécie Título']  # 21.1
    aceite: Annotated[int, 1, 'Aceite']  # 22.1
    data_emissao: Annotated[date, 6, 'Data emissão']  # 23.1
    instrucao_1: Annotated[int, 2, 'Instrução 1']  # 24.1
    instrucao_2: Annotated[int, 2, 'Instrução 2']  # 25.1
    juros_mora: Annotated[int, 13, 'Juros Mora']  # 26.1
    data_desconto: Annotated[date, 6, 'Data desconto']  # 27.1
    valor_desconto: Annotated[int, 13, 'Valor desconto']  # 28.1
    valor_iof: Annotated[int, 13, 'Valor do IOF']  # 29.1
    abatimento: Annotated[int, 13, 'Valor do Abatimento']  # 30.1
    nat_pagador: Annotated[int, 2, 'Tipo Inscrição do Pagador']  # 31.1 (01; 02)
    cnpj_pagador: Annotated[int, 14, 'Núm Inscrição do Pagador']  # 32.1
    nome: Annotated[str, 40, 'Nome do Pagador']  # 33.1
    endereco: Annotated[str, 40, 'Endereço']  # 34.1
    bairro: Annotated[str, 12, 'Bairro']  # 35.1
    cep: Annotated[int, 8, 'CEP']  # 36.1
    cidade: Annotated[str, 15, 'Cidade']  # 37.1
    uf: Annotated[str, 2, 'UF']  # 38.1
    data_multa: Annotated[date, 6, 'Data da Multa']  # 39.1
    valor_multa: Annotated[int, 10, 'Valor da Multa']  # 40.1
    sacador: Annotated[str, 22, 'Sacador/Avalista']  # 41.1
    instrucao_3: Annotated[int, 2, 'Instrução 3']  # 42.1
    prazo: Annotated[int, 2, 'Prazo']  # 43.1
    cod_moeda: Annotated[int, 1, 'Cód Moeda']  # 44.1
    num_sequencial: Annotated[int, 6, 'Núm Sequencial']  # 45.1


class RemessaTrailer(Record):
    """
    Tipo 9 - Trailer de Remessa
    """
    cod_registro: Annotated[int, 1, 'Cod Registro'] = 9  # 01.9
    uso_exclusivo: Annotated[str, 393, 'Uso Exclusivo']  # 02.9
    num_sequencial: Annotated[int, 6, 'Num Sequencial']  # 03.9
