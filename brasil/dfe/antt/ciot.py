from typing import Annotated, Literal, NotRequired, TypedDict, get_type_hints, get_origin, get_args
import datetime
from dataclasses import dataclass
from decimal import Decimal

import requests

PROD = '1'
HOMOLOG = '2'

AMBIENTE = {
    '1': 'https://appservices.antt.gov.br/pefServices',
    '2': 'https://appservices-hml.antt.gov.br/pefServices',
}


@dataclass(frozen=True)
class Rules:
    names: tuple[str, ...]

    def __init__(self, *names: str):
        object.__setattr__(self, 'names', names)


TipoOperacao = Literal[1, 2, 3]
TipoPagamento = Literal[1, 2, 3, 4, 5, 6]
IndPagamento = Literal[0, 1]
TipoTransportador = Literal['TAC', 'ETC', 'CTC']


class ConsultarSituacaoTransportadorRequest(TypedDict):
    CpfCnpjInteressado: Annotated[
        str, '#1 CPF ou CNPJ do Interessado. Se informado: 11 dígitos CPF ou 14 dígitos CNPJ.']
    CpfCnpjTransportador: Annotated[
        str, '#2 CPF ou CNPJ do Transportador. Se informado: 11 dígitos CPF ou 14 dígitos CNPJ.', Rules('B112')]
    RNTRCTransportador: Annotated[
        str, '#3 Número do RNTRC do Transportador. Caso informado com 8 dígitos, deve ser completado com zero à esquerda para 9 dígitos.', Rules(
            'B3', 'B60')]


class ConsultarSituacaoTransportadorResponse(TypedDict):
    CpfCnpjTransportador: Annotated[str, '#1 CPF ou CNPJ do Transportador. 11 dígitos CPF ou 14 dígitos CNPJ.']
    RNTRCTransportador: Annotated[
        str, '#2 RNTRC do transportador consultado, normalizado com 9 dígitos quando aplicável.']
    NomeRazaoSocialTransportador: Annotated[str, '#3 Nome ou Razão Social do Transportador.']
    RNTRCAtivo: Annotated[bool, '#4 Situação do RNTRC ativa: false = situação não ativa; true = situação ativa.']
    TipoTransportador: Annotated[TipoTransportador, '#6 Categoria do transportador: TAC, ETC ou CTC.']
    EquiparadoTAC: Annotated[bool, '#7 Indica se o transportador é equiparado ao TAC: false = não; true = sim.']
    Protocolo: Annotated[str, '#8 Protocolo retornado após consumo do serviço.']
    Codigo: Annotated[str, '#9 Código do erro ou sucesso no retorno da informação.']
    Mensagem: Annotated[str, '#10 Mensagem de erro ou sucesso no retorno da informação.']


class ConsultarFrotaTransportadorRequest(TypedDict):
    CpfCnpjInteressado: Annotated[str, '#1 CPF ou CNPJ do Interessado. 11 dígitos CPF ou 14 dígitos CNPJ.']
    CpfCnpjTransportador: Annotated[
        str, '#2 CPF ou CNPJ do Transportador. 11 dígitos CPF ou 14 dígitos CNPJ.', Rules('B112')]
    RNTRCTransportador: Annotated[
        str, '#3 RNTRC do transportador consultado, normalizado com 9 dígitos quando aplicável.', Rules('B3', 'B60')]
    Placas: Annotated[list[str], '#4 Placas dos veículos a serem pesquisados.', Rules('B1')]


class FrotaTransportadorItemResponse(TypedDict):
    PlacaVeiculo: Annotated[str, '#5.1 Placa do Veículo.']
    SituacaoVeiculoFrotaTransportador: Annotated[
        bool, '#5.2 Situação do Veículo: false = não pertence ao Transportador; true = pertence ao Transportador.']


class ConsultarFrotaTransportadorResponse(TypedDict):
    CpfCnpjTransportador: Annotated[str, '#1 CPF ou CNPJ do transportador. 11 dígitos CPF ou 14 dígitos CNPJ.']
    RNTRCTransportador: Annotated[
        str, '#2 Número do RNTRC do transportador consultado, normalizado com 9 dígitos quando aplicável.']
    NomeRazaoSocialTransportador: Annotated[str, '#3 Nome ou Razão Social do Transportador.']
    RNTRCAtivo: Annotated[bool, '#4 Situação do RNTRC ativa: false = situação não ativa; true = situação ativa.']
    Frota: Annotated[list[FrotaTransportadorItemResponse], '#5 Situações de todos os veículos pesquisados.']
    Protocolo: Annotated[str, '#6 Protocolo retornado após consumo do serviço.']
    Codigo: Annotated[str, '#7 Código do erro ou sucesso no retorno da informação.']
    Mensagem: Annotated[str, '#8 Mensagem de erro ou sucesso no retorno da informação.']


class VeiculoDOT(TypedDict):
    Placa: Annotated[str, '#13.1 Placa do veículo.', Rules('B5', 'B20', 'B117')]
    RNTRC: NotRequired[Annotated[str, '#13.2 RNTRC do veículo.', Rules('B15', 'B60')]]
    NumeroEixos: Annotated[
        str, '#13.3 Número de eixos. Para veículo automotor: 2 a 4 eixos. Implemento: 1 a 4.', Rules('B101')]


class OrigemDOT(TypedDict):
    CodigoMunicipioOrigem: NotRequired[Annotated[
        int, '#14.1.1 Código do município de origem conforme tabela oficial adotada pelo sistema, tabela IBGE.']]
    CepOrigem: NotRequired[Annotated[str, '#14.1.2 CEP de origem. Informar somente números.']]
    LatitudeOrigem: NotRequired[Annotated[
        Decimal, '#14.1.3 Latitude de origem. Deve ser informada em conjunto com LongitudeOrigem, quando aplicável.']]
    LongitudeOrigem: NotRequired[Annotated[
        Decimal, '#14.1.4 Longitude de origem. Deve ser informada em conjunto com LatitudeOrigem, quando aplicável.']]


class DestinoDOT(TypedDict):
    CodigoMunicipioDestino: NotRequired[
        Annotated[int, '#14.2.1 Código do município de destino conforme tabela oficial adotada pelo sistema.']]
    CepDestino: NotRequired[Annotated[str, '#14.2.2 CEP de destino. Informar somente números.']]
    LatitudeDestino: NotRequired[Annotated[
        Decimal, '#14.2.3 Latitude de destino. Deve ser informada em conjunto com LongitudeDestino, quando aplicável.']]
    LongitudeDestino: NotRequired[Annotated[
        Decimal, '#14.2.4 Longitude de destino. Deve ser informada em conjunto com LatitudeDestino, quando aplicável.']]


class OrigemDestinoDOT(TypedDict):
    Origem: Annotated[
        OrigemDOT, '#14.1 Objeto vinculado ao item de OrigemDestino. Obrigatório se TipoOperacao = 1 ou TipoOperacao = 2.']
    Destino: Annotated[
        DestinoDOT, '#14.2 Objeto vinculado ao item de OrigemDestino. Obrigatório se TipoOperacao = 1 ou TipoOperacao = 2.']
    DistanciaPercorrida: NotRequired[Annotated[
        int, '#14.3 Distância percorrida em km. Deve ser maior que zero. Obrigatório se TipoOperacao = 1 ou TipoOperacao = 2.', Rules(
            'B62', 'B82')]]


class DadosCargaDOT(TypedDict):
    CodigoNaturezaCarga: NotRequired[Annotated[
        int, '#15.1 Código da natureza da carga. Obrigatório se TipoOperacao = 1 ou TipoOperacao = 2.', Rules('B9',
                                                                                                              'B69')]]
    PesoCarga: NotRequired[Annotated[
        Decimal, '#15.2 Peso da carga. Deve ser maior que zero. Obrigatório se TipoOperacao = 1 ou TipoOperacao = 2.', Rules(
            'B18')]]
    CodigoTipoCarga: NotRequired[Annotated[
        int, '#15.3 Código do tipo de carga. 1=Granel sólido; 2=Granel líquido; 3=Frigorificada ou Aquecida; 4=Conteinerizada; 5=Carga Geral; 6=Neogranel; 7=Perigosa granel sólido; 8=Perigosa granel líquido; 9=Perigosa frigorificada ou aquecida; 10=Perigosa conteinerizada; 11=Perigosa carga geral; 12=Carga Granel Pressurizada. Obrigatório se TipoOperacao = 1 ou TipoOperacao = 2.']]
    ContratantesCargFrac: NotRequired[Annotated[
        list[str], '#15.4 CPF e CNPJ dos contratantes da carga fracionada. Obrigatório se TipoOperacao = 2.', Rules(
            'B64', 'B67', 'B119')]]


class InfPagamentoDOT(TypedDict):
    TipoPagamento: Annotated[
        TipoPagamento, '#16.1 Tipo de pagamento: 1=IP/cartão pré-pago emitido por IP ou IF; 2=Conta Corrente; 3=Conta Poupança; 4=Conta Pagamento; 5=Outros; 6=Pix.', Rules(
            'B100', 'B118')]
    CodigoInstituicaoFinanceira: NotRequired[Annotated[
        int, '#16.2 Código da instituição financeira. Obrigatório quando TipoPagamento = 1, 2, 3 ou 4. Campos bancários não devem ser informados quando TipoPagamento diferente de 1, 2, 3 ou 4.', Rules(
            'B92', 'B99')]]
    NumeroAgencia: NotRequired[Annotated[
        str, '#16.3 Número da agência. Obrigatório quando TipoPagamento = 2, 3 ou 4. Campos bancários não devem ser informados quando TipoPagamento diferente de 1, 2, 3 ou 4.', Rules(
            'B92', 'B99')]]
    NumeroConta: NotRequired[Annotated[
        str, '#16.4 Número da conta ou identificador do meio de pagamento utilizado. Obrigatório quando TipoPagamento = 1, 2, 3 ou 4. Campos bancários não devem ser informados quando TipoPagamento diferente de 1, 2, 3 ou 4.', Rules(
            'B92', 'B99')]]
    ChavePix: NotRequired[Annotated[
        str, '#16.5 Chave Pix. Obrigatório quando TipoPagamento = 6. Campos Pix não devem ser informados quando TipoPagamento diferente de 6.', Rules(
            'B92', 'B99')]]
    CpfCnpjCreditado: Annotated[str, '#16.6 CPF ou CNPJ do recebedor do pagamento.']
    CodigoPagamento: NotRequired[Annotated[
        int, '#16.7 Código identificador do pagamento realizado, usado para registrar ou rastrear a transação associada à operação de transporte.']]
    IdentificadorPix: NotRequired[Annotated[
        str, '#16.8 Identificador Pix. Obrigatório quando TipoPagamento = 6. Campos Pix não devem ser informados quando TipoPagamento diferente de 6.', Rules(
            'B92', 'B99')]]
    IndPagamento: Annotated[IndPagamento, '#16.9 Indicador de pagamento: 0 = à vista; 1 = a prazo.']
    NumeroParcela: NotRequired[Annotated[
        int, '#16.10.1 Número da parcela. Obrigatório quando IndPagamento = 1. Não deve ser informado quando IndPagamento = 0.', Rules(
            'B105', 'B106')]]
    DataVencimento: NotRequired[Annotated[
        str, '#16.10.2 Data de vencimento. Obrigatório quando IndPagamento = 1. Não deve ser informado quando IndPagamento = 0.', Rules(
            'B105', 'B106')]]
    ValorParcela: NotRequired[Annotated[
        Decimal, '#16.10.3 Valor da parcela. Obrigatório quando IndPagamento = 1. Não deve ser informado quando IndPagamento = 0.', Rules(
            'B105', 'B106')]]


class InfIndicadoresOperacionaisDOT(TypedDict):
    IndAltoDesempenho: NotRequired[Annotated[
        bool, '#17.1 Indicador de alto desempenho: true = operação de alto desempenho; false = padrão. Obrigatório se TipoOperacao = 1.']]
    IndRetornoVazio: NotRequired[Annotated[
        bool, '#17.2 Indicador de retorno vazio: true = operação com retorno vazio; false = sem previsão de retorno vazio. Obrigatório se TipoOperacao = 1.']]
    ComposicaoVeicular: NotRequired[Annotated[
        bool, '#17.3 Indicador de composição veicular: true = é composição veicular; false = não é composição veicular. Obrigatório se TipoOperacao = 1.']]


class DeclaracaoOperacaoTransporteRequest(TypedDict):
    IdOperacaoTransporte: Annotated[
        str, '#1 Código Identificador da Operação de Transporte.', Rules('B17', 'B24', 'B25', 'B31', 'B32', 'B33',
                                                                         'B115')]
    TipoOperacao: Annotated[
        TipoOperacao, '#2 Tipo da operação: 1 = Operação Carga Lotação; 2 = Operação Carga Fracionada; 3 = Operação TAC-Agregado.']
    CpfCnpjContratado: Annotated[str, '#3 CPF ou CNPJ do contratado.', Rules('B3', 'B27')]
    RNTRCContratado: Annotated[str, '#4 RNTRC do contratado.', Rules('B3', 'B14', 'B60')]
    CpfCnpjContratante: Annotated[str, '#5 CPF ou CNPJ do contratante.']
    RNTRCContratante: NotRequired[Annotated[
        str, '#6 RNTRC do contratante. Quando informado, deve validar se pertence ao CpfCnpjContratante.', Rules('B60',
                                                                                                                 'B71')]]
    CpfCnpjDestinatario: Annotated[
        str, '#7 CPF ou CNPJ do destinatário. Não deve ser informado para TipoOperacao = 3.', Rules('B62', 'B66')]
    ValorFrete: Annotated[Decimal, '#8 Valor do frete. Deve ser maior que zero.', Rules('B80', 'B120')]
    DataDeclaracao: Annotated[str, '#9 Data e hora da declaração.', Rules('B11', 'B19', 'B96')]
    IndContingencia: Annotated[
        bool, '#10 Indicador de contingência: true = contingência; false = fora da contingência.']
    JustificativaContingencia: NotRequired[Annotated[
        str, '#11 Justificativa de contingência. Obrigatória quando IndContingencia = true e não permitida quando IndContingencia = false.', Rules(
            'B103', 'B104')]]
    DataInicioViagem: Annotated[str, '#12 Data de início da viagem.', Rules('B6', 'B12', 'B21', 'B22', 'B30', 'B56')]
    DataFimViagem: Annotated[str, '#13 Data de fim da viagem.', Rules('B13', 'B21', 'B30')]
    Veiculos: Annotated[list[VeiculoDOT], '#13 Veículos da operação.', Rules('B15', 'B49', 'B73', 'B83', 'B84')]
    OrigemDestino: NotRequired[Annotated[list[
        OrigemDestinoDOT], '#14 Origem e destino. Quando dentro de um par OD for informado mais de um tipo, deve-se utilizar sempre o mais específico: LatLong -> CEP -> Cidade. Obrigatório se TipoOperacao = 1 ou TipoOperacao = 2.', Rules(
        'B62', 'B109', 'B110', 'B111')]]
    DadosCarga: NotRequired[Annotated[
        DadosCargaDOT, '#15 Informações da carga. Obrigatório se TipoOperacao = 1 ou TipoOperacao = 2.', Rules('B62')]]
    InfPagamento: Annotated[list[InfPagamentoDOT], '#16 Informações do pagamento do frete.']
    InfIndicadoresOperacionais: NotRequired[Annotated[
        InfIndicadoresOperacionaisDOT, '#17 Objeto que agrupa os indicadores operacionais. Obrigatório se TipoOperacao = 1.']]


class DeclaracaoOperacaoTransporteResponse(TypedDict):
    CodigoIdentificacaoOperacao: Annotated[str, '#1 CIOT - Código Identificador da Operação de Transporte.']
    CodigoVerificador: Annotated[
        str, '#2 Código verificador gerado pela ANTT validando os dados enviados - protocolo de autorização.']
    Protocolo: Annotated[str, '#3 Número do protocolo de erro ou de sucesso da operação de declaração.']
    Codigo: Annotated[str, '#4 Código do erro ou sucesso no retorno da informação.']
    Mensagem: Annotated[str, '#5 Mensagem de erro ou sucesso no retorno da informação.']
    AvisoTransportador: Annotated[
        str, '#6 Mensagem de aviso cadastrada pela ANTT para o contratado. Quando existir, sua apresentação ao transportador e impressão no documento correspondente é obrigatória.']


class CancelamentoOperacaoTransporteRequest(TypedDict):
    CodigoIdentificacaoOperacao: Annotated[
        str, '#1 CIOT - Código Identificador da Operação de Transporte com Código Verificador.', Rules('B34', 'B35',
                                                                                                       'B36', 'B37',
                                                                                                       'B38', 'B113')]
    MotivoCancelamento: Annotated[str, '#2 Motivo do cancelamento.', Rules('B34', 'B37', 'B39')]


class CancelamentoOperacaoTransporteResponse(TypedDict):
    CodigoIdentificacaoOperacao: Annotated[
        str, '#1 CIOT - Código Identificador da Operação de Transporte com Código Verificador.']
    DataCancelamento: Annotated[str, '#2 Data/Hora do cancelamento da Operação de Transporte.']
    Protocolo: Annotated[str, '#3 Protocolo de sucesso no cancelamento.']
    Codigo: Annotated[str, '#4 Código do erro ou sucesso no retorno da informação.']
    Mensagem: Annotated[str, '#5 Mensagem de erro ou sucesso no retorno da informação.']


class RetificacaoOrigemDestinoDOT(TypedDict):
    Origem: Annotated[OrigemDOT, '#4.1 Objeto vinculado ao item OrigemDestino. Obrigatório se TipoOperacao = 3.']
    Destino: Annotated[DestinoDOT, '#4.2 Objeto vinculado ao item OrigemDestino. Obrigatório se TipoOperacao = 3.']


class RetificacaoDadosCargaDOT(TypedDict):
    CodigoNaturezaCarga: NotRequired[Annotated[int, '#5.1 Código da natureza da carga.']]
    PesoCarga: NotRequired[Annotated[Decimal, '#5.2 Peso da carga. Deve ser maior que zero.']]
    CodigoTipoCarga: NotRequired[
        Annotated[int, '#5.3 Código do tipo de carga. Deve existir na tabela de domínio de tipo de carga.']]


class RetificacaoOperacaoTransporteRequest(TypedDict):
    CodigoIdentificacaoOperacao: Annotated[
        str, '#1 CIOT - Código Identificador da Operação de Transporte com Código Verificador.', Rules('B34', 'B37',
                                                                                                       'B38', 'B39',
                                                                                                       'B40', 'B113',
                                                                                                       'B121')]
    ValorFrete: NotRequired[Annotated[Decimal, '#2 Valor do frete. Deve ser maior que zero.', Rules('B80', 'B120')]]
    DataFimViagem: NotRequired[Annotated[
        str, '#3 Data de fim da viagem. Obrigatório se TipoOperacao = 3.', Rules('B13', 'B21', 'B30', 'B57', 'B64')]]
    OrigemDestino: NotRequired[Annotated[
        list[RetificacaoOrigemDestinoDOT], '#4 Origem e destino. Obrigatório se TipoOperacao = 3.', Rules('B62', 'B64',
                                                                                                          'B109',
                                                                                                          'B110',
                                                                                                          'B111')]]
    DadosCarga: NotRequired[Annotated[
        RetificacaoDadosCargaDOT, '#5 Dados da carga. Para carga fracionada, o usuário pode ou não retificar a informação.', Rules(
            'B62', 'B64')]]


class RetificacaoOperacaoTransporteResponse(TypedDict):
    CodigoIdentificacaoOperacao: Annotated[
        str, '#1 CIOT - Código Identificador da Operação de Transporte com Código Verificador.']
    DataRetificacao: Annotated[str, '#2 Data/Hora da Retificação da Operação de Transporte.']
    Protocolo: Annotated[str, '#3 Protocolo de erro ou sucesso na retificação.']
    Codigo: Annotated[str, '#4 Código do erro ou sucesso no retorno da informação.']
    Mensagem: Annotated[str, '#5 Mensagem de erro ou sucesso no retorno da informação.']


class EncerramentoOrigemDestinoDOT(TypedDict):
    Origem: Annotated[OrigemDOT, '#2.1 Objeto vinculado ao item OrigemDestino. Obrigatório se TipoOperacao = 3.']
    Destino: Annotated[DestinoDOT, '#2.2 Objeto vinculado ao item OrigemDestino. Obrigatório se TipoOperacao = 3.']
    DistanciaPercorrida: NotRequired[
        Annotated[int, '#2.3 Distância percorrida em km. Deve ser maior que zero. Obrigatório se TipoOperacao = 3.']]
    QtdViagens: NotRequired[Annotated[int, '#2.4 Quantidade de viagens. Obrigatório se TipoOperacao = 3.']]


class EncerramentoDadosCargaDOT(TypedDict):
    PesoTotalCarga: NotRequired[Annotated[
        Decimal, '#3 Peso total da carga. Deve ser maior que zero. Obrigatório se TipoOperacao = 1.', Rules('B18',
                                                                                                            'B57',
                                                                                                            'B62',
                                                                                                            'B65')]]


class EncerramentoOperacaoTransporteRequest(TypedDict):
    CodigoIdentificacaoOperacao: Annotated[
        str, '#1 Código Identificador da Operação de Transporte com Código Verificador.', Rules('B34', 'B37', 'B38',
                                                                                                'B46', 'B113', 'B116')]
    OrigemDestino: NotRequired[Annotated[list[
        EncerramentoOrigemDestinoDOT], '#2 Origem e destino. Estrutura do tipo array. Obrigatório se TipoOperacao = 3.', Rules(
        'B57', 'B58', 'B64', 'B109', 'B110', 'B111')]]
    DadosCarga: NotRequired[Annotated[EncerramentoDadosCargaDOT, '#3 Dados da carga para encerramento.']]


class EncerramentoOperacaoTransporteResponse(TypedDict):
    CodigoIdentificacaoOperacao: Annotated[
        str, '#1 CIOT - Código Identificador da Operação de Transporte com Código Verificador.']
    DataEncerramento: Annotated[str, '#2 Data/Hora do encerramento da Operação de Transporte.']
    Protocolo: Annotated[str, '#3 Protocolo de erro ou de sucesso no encerramento.']
    Codigo: Annotated[str, '#4 Código do erro ou sucesso no retorno da informação.']
    Mensagem: Annotated[str, '#5 Mensagem de erro ou sucesso no retorno da informação.']


class ConsultarExcecaoRequest(TypedDict):
    CpfCnpjTransportador: Annotated[
        str, '#1 CPF ou CNPJ do transportador: 11 dígitos CPF ou 14 dígitos CNPJ.', Rules('B112', 'B122')]


class ConsultarExcecaoRetorno(TypedDict):
    CpfCnpjTransportador: Annotated[str, '#1.1 CPF ou CNPJ: 11 dígitos CPF ou 14 dígitos CNPJ.']
    Flag: Annotated[
        bool, '#1.2 Indica se o CPF/CNPJ do transportador está na lista: false = não está na lista; true = está na lista.']


class ConsultarExcecaoResponse(TypedDict):
    Retorno: Annotated[ConsultarExcecaoRetorno, '#1 Retorno da consulta de exceção.']
    Codigo: Annotated[str, '#2 Código do erro ou sucesso no retorno da informação.']
    Mensagem: Annotated[str, '#3 Mensagem de erro ou sucesso no retorno da informação.']


class ConsultarCIOTGeradoRequest(TypedDict):
    CodigoIdentificacaoOperacao: Annotated[
        str, '#1 CIOT - Código Identificador da Operação de Transporte.', Rules('B34', 'B113')]
    AnoDeclaracao: NotRequired[Annotated[int, '#2 Ano de declaração.']]


class ConsultarCIOTGeradoResponse(TypedDict):
    CodigoIdentificacaoOperacao: Annotated[
        str, '#1 CIOT - Código Identificador da Operação de Transporte com Código Verificador.']
    Codigo: Annotated[list[str], '#2 Código do erro ou sucesso no retorno da informação.']
    Mensagem: Annotated[list[str], '#3 Código e mensagem de erro ou sucesso no retorno da informação.']


def _prepare_dict(payload: dict):
    for k, v in [*payload.items()]:
        if isinstance(v, dict) and v:
            _prepare_dict(v)
        elif isinstance(v, list) and v:
            for item in v:
                if isinstance(item, dict):
                    _prepare_dict(item)
        elif v is None or (isinstance(v, (list, dict)) and not v):
            payload.pop(k)


def _dot_validate(dot: DeclaracaoOperacaoTransporteRequest):
    # 7
    if dot['TipoOperacao'] == 3 and dot['CpfCnpjContratante']:
        raise ValueError('Destinatário não deve ser informado para TipoOperacao = 3')
    if dot['ValorFrete'] <= 0:
        raise ValueError('Valor do frete deve ser maior que zero')
    if dot['IndContingencia'] and not dot['JustificativaContingencia']:
        raise ValueError('Justificativa de contingência deve ser informada')
    # 16.1
    if dot['InfPagamento']:
        for pag in dot['InfPagamento']:
            if pag['TipoPagamento'] in (1, 2, 3, 4) and not pag['CodigoInstituicaoFinanceira']:
                raise ValueError('Código de instituição financeira não informado')
            if pag['TipoPagamento'] == 6 and not pag.get('IdentificadorPix'):
                raise ValueError('Identificador Pix não informado')
            # remover campos
            if pag['TipoPagamento'] != 6 and pag.get('IdentificadorPix'):
                pag.pop('IdentificadorPix')
            if pag['IndPagamento'] == 1:
                if not pag.get('NumeroParcela'):
                    raise ValueError('Número de parcela não informado')



validate_rules = {
    DeclaracaoOperacaoTransporteRequest: _dot_validate,
}


class PEFANTTClient:
    def __init__(self, tp_amb: Literal['1', '2']):
        self.tp_amb = tp_amb

    @classmethod
    def prepare(cls, payload: DeclaracaoOperacaoTransporteRequest, request_type: type[TypedDict]) -> None:
        # remover elementos vazios
        th = get_type_hints(request_type)
        if isinstance(payload, dict):
            _prepare_dict(payload)
        if sub := set(payload.keys()) - set(th.keys()):
            raise ValueError(f'Os campos {", ".join(sub)} não são válidos')
        for k, v in th.items():
            val = payload.get(k)
            if val is None and k in request_type.__required_keys__:
                raise ValueError(f'Campo {k} é obrigatório')
            origin = get_origin(v)
            args = get_args(v)
            if origin and args:
                if origin is list and args:
                    arg = args[0] if args else None
                    if arg:
                        arg = get_type_hints(arg)
                        if isinstance(arg, dict):
                            if isinstance(val, list):
                                for vi in val:
                                    cls.prepare(vi, args[0])
                            elif isinstance(val, dict):
                                cls.prepare(val, args[0])
                            continue
                    if str(val) not in map(str, args):
                        raise ValueError(f'{val} não é um valor válido para {k}')
            elif v is Decimal:
                payload[k] = 0 if val is None else round(float(val), 2)
            elif v is int:
                payload[k] = val and int(val)
            elif v is str:
                if isinstance(val, (datetime.date, datetime.datetime)):
                    payload[k] = datetime.datetime.strftime(val, '%Y-%m-%d')
                else:
                    payload[k] = str(val)
            elif v is bool:
                payload[k] = bool(val)
        if validator := validate_rules.get(request_type):
            validator(payload)
        return True

    def _post(self, endpoint: str, payload: dict) -> dict:
        url = f'{AMBIENTE[self.tp_amb]}/{endpoint}'
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    def consultar_situacao_transportador(
            self,
            payload: ConsultarSituacaoTransportadorRequest,
    ) -> ConsultarSituacaoTransportadorResponse:
        ...

    def consultar_frota_transportador(
            self,
            payload: ConsultarFrotaTransportadorRequest,
    ) -> ConsultarFrotaTransportadorResponse:
        pass

    def declaracao_operacao_transporte(
            self,
            payload: DeclaracaoOperacaoTransporteRequest
    ) -> DeclaracaoOperacaoTransporteResponse:
        self.prepare(payload, DeclaracaoOperacaoTransporteRequest)
        return self._post('DeclaracaoOperacaoTransporte', payload)

    def cancelamento_operacao_transporte(
            self,
            payload: CancelamentoOperacaoTransporteRequest,
    ) -> CancelamentoOperacaoTransporteResponse:
        ...

    def retificacao_operacao_transporte(
            self,
            payload: RetificacaoOperacaoTransporteRequest,
    ) -> RetificacaoOperacaoTransporteResponse:
        ...

    def encerramento_operacao_transporte(
            self,
            payload: EncerramentoOperacaoTransporteRequest,
    ) -> EncerramentoOperacaoTransporteResponse:
        ...

    def consultar_excecao(
            self,
            payload: ConsultarExcecaoRequest,
    ) -> ConsultarExcecaoResponse:
        ...

    def consultar_ciot_gerado(
            self,
            payload: ConsultarCIOTGeradoRequest,
    ) -> ConsultarCIOTGeradoResponse:
        ...
