"""
Módulo para perparação de Carta de Correção em formato JSON compatível com reptile.
"""
from typing import List
from brasil.dfe.retrato import DocumentoAuxiliar
from brasil.utils.xml import NotasFiscais, NodeProxy
from brasil.dfe.utils.dfe_utils import *


class CCe(DocumentoAuxiliar):
    """
    Converter XML em estrutura JSON compatível com reptile engine de acordo com o template definido
    :param str xml: String contendo XML da CCe e a ser convertida
    """
    nfe_xml: dict = None
    prepared_xml: dict = None

    def __init__(self, xml: str | bytes, nfe_xml: str | bytes) -> None:
        if isinstance(xml, str):
            xml = xml.encode()
        self._xml = NotasFiscais.fromstring(xml)
        self.nfe_xml = NotasFiscais.fromstring(nfe_xml)
        self.id = (
            self._xml._docs[0]
            .find("{http://www.portalfiscal.inf.br/nfe}evento")
            .find("{http://www.portalfiscal.inf.br/nfe}infEvento")
            .get("Id")
        )
        self.xml = self.load_docs(self._xml)
        self.nfe_xml = self.load_docs(self.nfe_xml)

    def load_docs(self, xml):
        res = {}
        for doc in xml._docs:
            res = {**res, **NodeProxy.to_dict(doc._node[0])}
        return res

    def prepare(self):
        self.load_template("CCeRetrato.json")
        self.prepare_xml()
        # prepara datasources
        self.template["report"]["datasources"] = self.get_datasources()
        return self.template, self.id + ".pdf"

    def prepare_xml(self) -> None:
        """
        Formata campos específicos para exibição no PDF.
        """
        emit = self.nfe_xml['NFe']['infNFe']['emit']
        emit['documento'] = format_doc(emit)
        dest = self.nfe_xml['NFe']['infNFe']['dest']
        dest['documento'] = format_doc(dest)
        
        numero = self.nfe_xml['NFe']['infNFe']['ide']['nNF']
        self.nfe_xml['NFe']['infNFe']['ide']['nNF'] = format_dfe_numero(numero)
        amb = self.xml['procEventoNFe']['evento']['infEvento']['tpAmb']
        if amb == 1:
            self.xml['procEventoNFe']['evento']['infEvento']['tpAmb'] = 'PRODUÇÃO'
        else:
            self.xml['procEventoNFe']['evento']['infEvento']['tpAmb'] = 'HOMOLOGAÇÃO'
        
        chave = self.xml['procEventoNFe']['evento']['infEvento']['chNFe']
        self.xml['procEventoNFe']['barcode'] = chave
        self.xml['procEventoNFe']['evento']['infEvento']['chNFe'] = ' '.join([chave[i:i + 4] for i in range(0, len(chave), 4)])

        dhEmi = self.nfe_xml['NFe']['infNFe']['ide']['dhEmi']
        self.nfe_xml['NFe']['infNFe']['ide']['dhEmi'] = format_iso_datetime(dhEmi)
        dhEvento = self.xml['procEventoNFe']['evento']['infEvento']['dhEvento']
        self.xml['procEventoNFe']['evento']['infEvento']['dhEvento'] = format_iso_datetime(dhEvento)
        dhReg = self.xml['procEventoNFe']['retEvento']['infEvento']['dhRegEvento']
        self.xml['procEventoNFe']['retEvento']['infEvento']['dhRegEvento'] = format_iso_datetime(dhReg)

        self.xml = format_all_numbers(self.xml)

    def get_datasources(self) -> List[dict]:
        """
        Prepara dados do xml estruturados em dicionários compatíveis com
        reptile para renderização do PDF.
        """
        res = [
            {"name": "dados", "data": [self.xml["procEventoNFe"]]},
            {"name": "nfe", "data": [self.nfe_xml["NFe"]["infNFe"]]},
        ]
        return res
