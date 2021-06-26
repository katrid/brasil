from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *



class TNSU(str):
    """Tipo número sequencial único do AN"""
    _restriction = Restriction(base=r"xs:string", pattern=r"[0-9]{1,15}", enumeration=[])
    pass



class TVeConsNFeDest(str):
    """Tipo Versão da consultaNFeDest"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1.01'])
    pass



class TConsNFeDest(Element):
    """Tipo Pedido de Consulta de Nota Fiscal Eletrônica"""
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    xServ: str = Element(str, documentation=['Serviço Solicitado'])
    CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do destinatário da NF-e'])
    indNFe: str = Element(str, documentation=['Indicador de NF-e consultada:\n0 – Todas as NF-e;\n1 – Somente as NF-e ainda não confirmadas.\n2 – Somente as NF-e ainda não confirmadas (inclusive Ciência).\n'])
    indEmi: str = Element(str, documentation=['Indicador do Emissor da NF-e:\n0 – Todos os Emitentes;\n1 – Somente as NF-e emitidas por emissores que não tenham a mesma raiz do CNPJ (para excluir as notas fiscais de transferência entre filiais).'])
    ultNSU: str = Element(str, documentation=['Último NSU recebido. Caso seja informado com zero, a consulta deve ser realizada no universo das notas fiscais tenham sido recepcionadas nos últimos 30 dias.'])
    versao: str = Attribute(TVeConsNFeDest)



class TRetConsNFeDest(Element):
    """Tipo Retorno do pedido de Consulta de Nota Fiscal Eletrônica"""
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que processou a NF-e'])
    cStat: TStat = Element(TStat, documentation=['Código do status da mensagem enviada.'])
    xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do serviço solicitado.'])
    dhResp: dateTime = Element(dateTime, documentation=['Data e hora da resposta à solicitação, no formato AAAA-MM-DDTHH:MM:SS'])
    indCont: str = Element(str, documentation=['Indicador de continuidade. Indica que o ambiente consultado POSSUI ainda documentos não pesquisados. 0 = NÃO possui documentos. 1 = Possui documentos.'])
    ultNSU: str = Element(str, documentation=['último NSU pesquisado, deve ser informado pelo WS, sempre que realizar alguma pesquisa para que o solicitante possa atualizar o último NSU pesquisado.'])

    class ret(ComplexType):
        """Resumo de NF-e ou CC-e"""
        _max_occurs = 50
        _choice = [['resNFe', 'resCanc', 'resCCe']]

        def add(self, resNFe=None, resCanc=None, resCCe=None) -> TRetConsNFeDest.ret:
            return super().add(resNFe=resNFe, resCanc=resCanc, resCCe=resCCe)


        class resNFe(ComplexType):
            """Informações resumo da NF-e localizadas"""
            _choice = [['CNPJ', 'CPF']]
            chNFe: TChNFe = Element(TChNFe, documentation=['Chaves de acesso da NF-e consultada'])
            CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do Remetente da NF-e'])
            CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CPF do Remetente da NF-e'])
            xNome: str = Element(str, documentation=['Razão Social ou Nome do Remetente'])
            IE: TIe = Element(TIe, filter=str.isdigit, documentation=['IE do Remetente. Valores válidos: vazio (não contribuinte do ICMS), ISENTO (contribuinte  do ICMS ISENTO de Inscrição no Cadastro de Contribuintes) ou IE (Contribuinte do ICMS)'])
            dEmi: TData = Element(TData, documentation=['Data de Emissão da NF-e'])
            tpNF: str = Element(str, documentation=['Tipo do Documento Fiscal (0 - entrada; 1 - saída)'])
            vNF: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), documentation=['Valor Total da NF-e'])
            digVal: str = Element(str, documentation=['Digest Value da NF-e na base de dados da SEFAZ '])
            dhRecbto: dateTime = Element(dateTime, documentation=['Data e hora de processamento de autorização, no formato AAAA-MM-DDTHH:MM:SS.'])
            cSitNFe: str = Element(str, documentation=['Situação da NF-e\n1-Uso autorizado no momento da consulta;\n2-Uso denegado;\n3-NF-e cancelada;'])
            cSitConf: str = Element(str, documentation=['Situação Confirmação do Destinatário:\n0 – sem manifestacao;\n1 – confirmada;\n2 – desconhecida;\n3 – recusada\n4 - ciência. '])
            NSU: str = Attribute(TNSU)
        resNFe: resNFe = Element(resNFe, documentation=['Informações resumo da NF-e localizadas'])

        class resCanc(ComplexType):
            """Informações resumo da NF-e canceladas localizadas"""
            _choice = [['CNPJ', 'CPF']]
            chNFe: TChNFe = Element(TChNFe, documentation=['Chaves de acesso da NF-e consultada'])
            CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do Remetente da NF-e'])
            CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CPF do Remetente da NF-e'])
            xNome: str = Element(str, documentation=['Razão Social ou Nome do Remetente'])
            IE: TIe = Element(TIe, filter=str.isdigit, documentation=['IE do Remetente. Valores válidos: vazio (não contribuinte do ICMS), ISENTO (contribuinte  do ICMS ISENTO de Inscrição no Cadastro de Contribuintes) ou IE (Contribuinte do ICMS)'])
            dEmi: TData = Element(TData, documentation=['Data de Emissão da NF-e'])
            tpNF: str = Element(str, documentation=['Tipo do Documento Fiscal (0 - entrada; 1 - saída)'])
            vNF: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), documentation=['Valor Total da NF-e'])
            digVal: str = Element(str, documentation=['Digest Value da NF-e na base de dados da SEFAZ '])
            dhRecbto: dateTime = Element(dateTime, documentation=['Data e hora de processamento de autorização, no formato AAAA-MM-DDTHH:MM:SS.'])
            cSitNFe: str = Element(str, documentation=['Situação da NF-e\n3-NF-e cancelada;'])
            cSitConf: str = Element(str, documentation=['Situação Confirmação do Destinatário:\n0 – sem manifestacao;\n1 – confirmada;\n2 – desconhecida;\n3 – recusada\n4 - ciência.'])
            NSU: str = Attribute(TNSU)
        resCanc: resCanc = Element(resCanc, documentation=['Informações resumo da NF-e canceladas localizadas'])

        class resCCe(ComplexType):
            """Informações da carta de correção da NF-e localizadas"""
            chNFe: TChNFe = Element(TChNFe, documentation=['Chave de Acesso da NF-e vinculada ao evento'])
            dhEvento: str = Element(str, documentation=['Data e Hora do Evento, formato UTC (AAAA-MM-DDThh:mm:ssTZD, onde TZD = +hh:mm ou -hh:mm)'])
            tpEvento: str = Element(str, documentation=['Tipo do Evento'])
            nSeqEvento: str = Element(str, documentation=['Seqüencial do evento para o mesmo tipo de evento.  Para maioria dos eventos será 1, nos casos em que possa existir mais de um evento, como é o caso da carta de correção, o autor do evento deve numerar de forma seqüencial.'])
            descEvento: str = Element(str, documentation=['Descrição do Evento - “Carta de Correção”'])
            xCorrecao: str = Element(str, documentation=['Correção a ser considerada'])
            tpNF: str = Element(str, documentation=['Tipo do Documento Fiscal (0 - entrada; 1 - saída)'])
            dhRecbto: dateTime = Element(dateTime, documentation=['Data e hora de processamento de autorização, no formato AAAA-MM-DDTHH:MM:SS.'])
            NSU: str = Attribute(TNSU)
        resCCe: resCCe = Element(resCCe, documentation=['Informações da carta de correção da NF-e localizadas'])
    ret: List[ret] = Element(ret, max_occurs=50, documentation=['Resumo de NF-e ou CC-e'])
    versao: str = Attribute(TVeConsNFeDest)


