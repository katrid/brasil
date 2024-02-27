from typing import Annotated
from datetime import date, datetime, time
from .base import Record, Arquivo


class Cnab400:
    class Remessa(Arquivo):
        class Header(Record):
            """
            Tipo 0 - Header de Remessa
            """
            tipo_registro: Annotated[int, 1, "TIPO DE REGISTRO"] = 0
            operacao: Annotated[int, 1, "OPERAÇÃO"] = 1
            literal_remessa: Annotated[str, 7, "LITERAL DE REMESSA"] = "REMESSA"
            codigo_servico: Annotated[int, 2, "CÓDIGO DO SERVIÇO"] = 1
            literal_servico: Annotated[str, 15, "LITERAL DE SERVIÇO"] = "COBRANCA"
            agencia: Annotated[int, 4, "AGÊNCIA"]
            zeros: Annotated[int, 2, "ZEROS"] = 0
            conta: Annotated[int, 5, "CONTA"]
            dac: Annotated[int, 1, "DAC"]
            brancos: Annotated[str, 8, "BRANCOS"]
            nome_empresa: Annotated[str, 30, "NOME DA EMPRESA"]
            codigo_banco: Annotated[int, 3, "CÓDIGO DO BANCO"] = 341
            nome_banco: Annotated[str, 15, "NOME DO BANCO"] = "BANCO ITAU SA"
            data_geracao: Annotated[int, 6, "DATA DE GERAÇÃO"]
            brancos2: Annotated[str, 294, "BRANCOS2"]
            numero_sequencial: Annotated[int, 6, "NÚMERO SEQÜENCIAL"] = 1

        class Detalhe(Record):
            """
            Tipo 1 - Detalhe de Remessa
            """
            tipo_registro: Annotated[int, 1, "TIPO DE REGISTRO"] = 1
            codigo_inscricao: Annotated[int, 2, "CÓDIGO DE INSCRIÇÃO"]
            numero_inscricao: Annotated[int, 14, "NÚMERO DE INSCRIÇÃO"]
            agencia: Annotated[int, 4, "AGÊNCIA"]
            zeros: Annotated[int, 2, "ZEROS"] = 0
            conta: Annotated[int, 5, "CONTA"]
            dac: Annotated[int, 1, "DAC"]
            brancos: Annotated[str, 4, "BRANCOS"]
            instrucaoalegacao: Annotated[int, 4, "INSTRUÇÃO/ALEGAÇÃO"]
            uso_empresa: Annotated[str, 25, "USO DA EMPRESA"]
            nosso_numero: Annotated[int, 8, "NOSSO NÚMERO"]
            qtde_moeda: Annotated[float, 13, "QTDE DE MOEDA"]
            n_carteira: Annotated[int, 3, "Nº DA CARTEIRA"]
            uso_banco: Annotated[str, 21, "USO DO BANCO"]
            carteira: Annotated[str, 1, "CARTEIRA"]
            cod_ocorrencia: Annotated[int, 2, "CÓD. DE OCORRÊNCIA"]
            n_documento: Annotated[str, 10, "Nº DO DOCUMENTO"]
            vencimento: Annotated[int, 6, "VENCIMENTO"]
            valor_titulo: Annotated[float, 13, "VALOR DO TÍTULO"]
            codigo_banco: Annotated[int, 3, "CÓDIGO DO BANCO"] = 341
            agencia_cobradora: Annotated[int, 5, "AGÊNCIA COBRADORA"]
            especie: Annotated[str, 2, "ESPÉCIE"]
            aceite: Annotated[str, 1, "ACEITE"]
            data_emissao: Annotated[int, 6, "DATA DE EMISSÃO"]
            instrucao_1: Annotated[str, 2, "INSTRUÇÃO 1"]
            instrucao_2: Annotated[str, 2, "INSTRUÇÃO 2"]
            juros_1_dia: Annotated[float, 13, "JUROS DE 1 DIA"]
            desconto_ate: Annotated[date, 6, "DESCONTO ATÉ"]
            valor_desconto: Annotated[float, 13, "VALOR DO DESCONTO"]
            valor_iof: Annotated[float, 13, "VALOR DO I.O.F."]
            abatimento: Annotated[float, 13, "ABATIMENTO"]
            codigo_inscricao: Annotated[int, 2, "CÓDIGO DE INSCRIÇÃO"]
            numero_inscricao: Annotated[int, 14, "NÚMERO DE INSCRIÇÃO"]
            nome: Annotated[str, 30, "NOME"]
            brancos2: Annotated[str, 10, "BRANCOS2"]
            logradouro: Annotated[str, 40, "LOGRADOURO"]
            bairro: Annotated[str, 12, "BAIRRO"]
            cep: Annotated[int, 8, "CEP"]
            cidade: Annotated[str, 15, "CIDADE"]
            estado: Annotated[str, 2, "ESTADO"]
            sacadoravalista: Annotated[str, 30, "SACADOR/AVALISTA"]
            brancos3: Annotated[str, 4, "BRANCOS3"]
            data_mora: Annotated[int, 6, "DATA DE MORA"]
            prazo: Annotated[int, 2, "PRAZO"]
            brancos4: Annotated[str, 1, "BRANCOS4"]
            numero_sequencial: Annotated[int, 6, "NÚMERO SEQÜENCIAL"]

        class Trailer(Record):
            """
            Tipo 9 - Trailer de Remessa
            """
            cod_registro: Annotated[int, 1, 'Cod Registro'] = 9
            brancos: Annotated[str, 393, 'Brancos']
            num_sequencial: Annotated[int, 6, 'Num Sequencial']

