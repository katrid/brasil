"""
Módulo para centralizar funções de preparação e renderização
dos documentos fiscais em PDF de acordo com os manuais respectivos
"""
import os
import json
from typing import List
from brasil.utils.xml import Documento
from reptile.bands import Report

class DocumentoAuxiliar:
    """Classe base para documento auxiliar dos dfes
    """
    _xml: Documento = None
    xml: dict = None
    template: dict = None
    id: str = None

    def export(self, output_path: str) -> str:
        """
        Prepara a instância do documento para formato compatível com reptile e renderiza em
        PDF conforme especificado no template de retrato.
        :param str output_path: Caminho em que o arquivo PDF será salvo após renderizado.
        """
        from reptile.exports.pdf import PDF
        template, filename = self.prepare()
        rep = Report(template)
        doc = rep.prepare()
        PDF(doc).export(os.path.join(output_path, filename))
        return os.path.basename(filename)

    def load_docs(self, xml: Documento):
        """Carrega os documentos de acordo com o conteúdo do xml

        :param xml: XML estruturado no padrão específico
        :type xml: Documento
        :raises NotImplementedError: Sobrescrever em subclasse
        """
        raise NotImplementedError()

    def load_template(self, template_name: str):
        with open(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)), "dfe", "templates", template_name
            ),
            "r",
        ) as f:
            self.template = json.load(f)

    def prepare(self):
        """Prepara dados do xml

        :param template_name: Nome do arquivo de template do retrato
        :raises NotImplementedError: Sobrescrever en subclasse
        """
        raise NotImplementedError()

    def prepare_xml(self):
        """Formata dados de acordo com o manual para exibição no PDF
        """
        raise NotImplementedError()

    def get_datasources(self) -> List[dict]:
        """
        Prepara dados do xml estruturados em dicionários compatíveis com
        reptile para renderização do PDF.
        """
        raise NotImplementedError()
