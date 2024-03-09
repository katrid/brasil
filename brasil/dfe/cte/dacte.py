"""
Módulo para perparação de CTe em formato JSON compatível com reptile.
Especificação do DACTE para NFe 4.00 de acordo com Anexo II MOC
(ref: https://dfe-portal.svrs.rs.gov.br/Cte/Documentos#)
"""
import datetime
from typing import List
from dateutil.parser import isoparse
from brasil.dfe.retrato import DocumentoAuxiliar
from brasil.utils.xml import CTe, Documento, NodeProxy
from brasil.dfe.utils.dfe_utils import *


class DACTE(DocumentoAuxiliar):
    """
    Converter XML em estrutura JSON compatível com reptile engine de acordo com a
    especificação oficial do DACTE
    :param str xml: String contendo XML do CTe a ser convertido
    """
    prepared_xml: dict = None
    infcte: dict = None

    def __init__(self, xml: str) -> None:
        self._xml = CTe.fromstring(xml)
        self.id = self._xml._docs[0].find('{http://www.portalfiscal.inf.br/cte}infCte').get('Id')
        self.xml = {}
        self.load_docs(self._xml)

    def load_docs(self, xml: CTe):
        for doc in xml._docs:
            self.xml = {**self.xml, **NodeProxy.to_dict(doc._node[0])}
        if 'protCTe' in self.xml:
            self.xml = { 'cteProc': self.xml }

    def prepare(self):
        self.load_template('DACTERetrato.json')
        # armazena tag com dados formatáveis do Cte
        if 'cteProc' in self.xml:
            self.infcte = self.xml['cteProc']['CTe']['infCte']
            # remove marca d'agua se documento estiver emitido
            if 'watermark' in self.template['report']:
                del self.template['report']['watermark']
        else:
            self.infcte = self.xml['CTe']['infCte']

        self.prepare_xml()
        # prepara datasources
        self.template['report']['datasources'] = self.get_datasources()
        return self.template, self.id + '.pdf'

    def prepare_xml(self) -> None:
        """
        Formata campos específicos para exibição no PDF.
        """
        self.infcte['modal_name'] = CTE_TP_MODAL.get(self.infcte['ide']['modal'])
        self.infcte['tpServ'] = CTE_TP_SERV.get(self.infcte['ide']['tpServ'])
        self.infcte['globalizado'] = 'Sim' if 'indGlobalizado' in self.infcte['ide'] else 'Não'
        if 'cteProc' in self.xml:
            self.infcte['chave'] = self.xml['cteProc']['protCTe']['infProt']['chCTe']
            self.infcte['prot'] = self.xml['cteProc']['protCTe']['infProt']['nProt']
            self.infcte["qrcode"] = (
                self.xml["cteProc"]["CTe"]["infCTeSupl"]["qrCodCTe"]
                .replace("<![CDATA[", "")
                .replace("]]", "")
            )
        else:
            self.infcte['chave'] = self.id[3:]
            self.infcte["qrcode"] = (
                self.xml["CTe"]["infCTeSupl"]["qrCodCTe"]
                .replace("<![CDATA[", "")
                .replace("]]", "")
            )
        self.infcte['ide']['dhEmi'] = datetime.fromisoformat(self.infcte['ide']['dhEmi'])
        self.infcte['tpEmis'] = CTE_TP_EMIS.get(self.infcte['ide']['tpEmis'])
        self.infcte['tpCTe'] = TP_CTE.get(self.infcte['ide']['tpCTe'])
        self.infcte = format_all_numbers(self.infcte)

    def get_tomador(self, infcte: dict) -> dict:
        """
        Retorna o tomador correto de acordo com os contexto do CTe.
        """
        toma = infcte['emit']
        toma['enderToma'] = infcte['emit']['enderEmit']
        return toma

    def get_datasources(self) -> List[dict]:
        """
        Prepara dados do xml estruturados em dicionários compatíveis com reptile para
        renderização do PDF.
        """
        res =  [
            {
                'name': 'dados',
                'data': [self.infcte]
            },
            {
                'name': 'atoresds',
                'data': [{
                    'emit': self.infcte['emit'],
                    'exped': self.infcte['exped'],
                    'rem': self.infcte['rem'],
                    'dest': self.infcte['dest'],
                    'receb': self.infcte['receb'],
                    'toma': self.get_tomador(self.infcte)
                }]
            },
            {
                'name': 'impostods',
                'data': [self.get_imposto()]
            },
            {
                'name': 'prestds',
                'data': [self.get_componentes()]
            },
            {
                'name': 'obsds',
                'data': [self.infcte['compl']]
            }
        ]

        if self.infcte['ide']['tpCTe'] == '0':
            res.append(
                {
                    'name': 'modalrodods', # TODO expandir para demais tipos de modais
                    'data': [self.infcte['infCTeNorm']['infModal']['rodo']]
                }
            )
            res.append(
                {
                    'name': 'cargads',
                    'data': [self.get_carga()]
                },
            )
            res.append(
                {
                    'name': 'docsds',
                    'data': self.get_docs()
                },
            )
        elif self.infcte['ide']['tpCTe'] == '1':
            res.append(
                {
                    'name': 'compds',
                    'data': [self.infcte['infCteComp']]
                }
            )
        return res

    def get_carga(self) -> dict:
        # TODO calcular demais casos para tipos diferentes de carga (PAG 22  do Anexo II)
        carga = self.infcte['infCTeNorm']['infCarga']
        if carga['infQ']['cUnid'] == '00':
            carga['cubagem'] = carga['infQ']['qCarga']
        return carga

    def get_componentes(self):
        # TODO preparar forma de renderizar quaisquer quantidade de componentes
        # não encontrei no manual se ha algum numero maximo de componentes possiveis
        # para composicao do valor da prestacao
        # para permanecer no layout padrao do Acbr e sugerido no manual
        # (tres "caixas" na horizontal exibindo os componentes)
        # e como atualmente o reptile nao renderiza masterdata na horizontal,
        # padronizarei apenas tres componentes por enquanto
        return self.infcte['vPrest']

    def get_imposto(self):
        icms = list(self.infcte['imp']['ICMS'].items())[0][1]
        icms['desc'] = CST_ICMS.get(icms['CST'])
        return icms

    def get_docs(self):
        res = []
        for k, v in self.infcte['infCTeNorm']['infDoc'].items():
            if k.startswith('infNFe'):
                v['numero'] = v['chave'][25:34]
                v['tipo'] = 'NF-e'
                res.append(v)
        return res
