from lxml import etree
from ..base import DocumentoFiscal
from .v400 import NFe


class NotasFiscais(list):
    def add(self, xml=None):
        cte = NFe()
        self.append(cte)
        return cte


class NotaFiscal(DocumentoFiscal):
    notas: NotasFiscais

    def __init__(self, xml=None):
        self.notas = NotasFiscais()
        if xml:
            self.notas.add(xml)

    def to_xml(self, doc: NFe=None):
        return doc._xml()

    def enviar(self, lote: str, sincrono=False):
        pass

    @classmethod
    def assinar(cls, root, ref, certificado):
        if isinstance(root, str):
            root = etree.fromstring(root)
        for child in root:
            if child.tag.endswith('infNfe'):
                return certificado.assinar(child, ref)


class WebServices:
    pass
