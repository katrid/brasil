"""
Módulo para perparação de DAMDFE em formato JSON compatível com reptile.
"""
from typing import List
from brasil.dfe.retrato import DocumentoAuxiliar
from brasil.utils.xml import MDFe, NodeProxy
from brasil.dfe.utils.dfe_utils import *


class DAMDFE(DocumentoAuxiliar):
    """
    Converter XML em estrutura JSON compatível com reptile engine de acordo com o template definido
    :param str xml: String contendo XML da CCe e a ser convertida
    """
    prepared_xml: dict = None
    infmdfe: dict = None

    def __init__(self, xml: str | bytes) -> None:
        if isinstance(xml, str):
            xml = xml.encode()
        self._xml = MDFe.fromstring(xml)
        self.id = (
            self._xml._docs[0]
            .find("{http://www.portalfiscal.inf.br/mdfe}infMDFe")
            .get("Id")
        )
        self.xml = self.load_docs(self._xml)

    def load_docs(self, xml):
        res = {}
        for doc in xml._docs:
            res = {**res, **NodeProxy.to_dict(doc._node[0])}
        return res

    def prepare(self):
        self.load_template("DAMDFERetrato.json")
        self.prepare_xml()
        # prepara datasources
        self.template["report"]["datasources"] = self.get_datasources()
        return self.template, self.id + ".pdf"

    def prepare_xml(self) -> None:
        """
        Formata campos específicos para exibição no PDF.
        """
        if 'protMDFe' in self.xml:
            chave = self.xml['protMDFe']['infProt']['chMDFe']
            prot = self.xml['protMDFe']['infProt']['nProt']
            self.xml['autorizacao'] = prot + ' ' + format_iso_datetime(
                self.xml['protMDFe']['infProt']['dhRecbto']
            )
        else:
            chave = self.id.replace('MDFe', '')
            self.xml['autorizacao'] = 'MDFe sem Autorização de Uso da SEFAZ '
        self.xml['barcode'] = chave
        self.xml['chave'] = ' '.join([chave[i:i + 4] for i in range(0, len(chave), 4)])
        emit = self.xml['MDFe']['infMDFe']['emit']
        emit['documento'] = format_doc(emit)
        self.xml['dhEmi'] = format_iso_datetime(
            self.xml['MDFe']['infMDFe']['ide']['dhEmi']
        )

        self.xml = format_all_numbers(self.xml)

    def get_datasources(self) -> List[dict]:
        """
        Prepara dados do xml estruturados em dicionários compatíveis com
        reptile para renderização do PDF.
        """
        # parse veiculos e motoristas para datasource
        veiculos = []
        motoristas = []
        modal = self.xml['MDFe']['infMDFe']['infModal']
        rodo = modal['rodo']
        for k in rodo:
            if k.startswith('veic'):
                veiculos.append({'veiculo': rodo[k]})

        for k in rodo['veicTracao']:
            if k.startswith('condutor'):
                rodo['veicTracao'][k]['CPF'] = format_doc(rodo['veicTracao'][k])
                motoristas.append(rodo['veicTracao'][k])

        if len(veiculos) > len(motoristas):
            for idx, v in enumerate(veiculos):
                if idx < len(motoristas):
                    v['motorista'] = motoristas[idx]
                else:
                    v['motorista'] = ''
        else:
            for idx, v in enumerate(motoristas):
                if idx < len(veiculos):
                    veiculos[idx]['motorista'] = v
                else:
                    veiculos.append({'motorista': v, 'veiculo': ''})
        # pega pedagios, se houver, e alimenta o datasource
        pedagios = []
        if 'valePed' in rodo['infANTT']:
            for k in rodo['infANTT']['valePed']:
                if k.startswith('disp'):
                    pedagios.append(rodo['infANTT']['valePed'][k])
        # aliementa datasource dos documentos
        docs = []
        descarga = self.xml['MDFe']['infMDFe']['infDoc']['infMunDescarga']
        for k in descarga:
            if k.startswith('infNFe'):
                docs.append({
                    'tipo': 'NFe',
                    'chave': descarga[k]['chNFe']
                })
            elif k.startswith('infCTe'):
                docs.append({
                    'tipo': 'CTe',
                    'chave': descarga[k]['chCTe']
                })
        res = [
            {"name": "dados", "data": [self.xml]},
            {"name": "veiculos", "data": veiculos},
            {"name": "pedagios", "data": pedagios},
            {"name": "documentos", "data": docs},
        ]
        return res
