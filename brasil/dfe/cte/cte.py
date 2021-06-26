from lxml import etree
from ..base import DocumentoFiscal
from .v300 import CTe


class Conhecimentos(list):
    def add(self, xml=None):
        cte = CTe()
        self.append(cte)
        return cte


class Conhecimento(DocumentoFiscal):
    conhecimentos: Conhecimentos

    def __init__(self, xml=None):
        self.conhecimentos = Conhecimentos()
        if xml:
            self.conhecimentos.add(xml)

    def to_xml(self, doc: CTe=None):
        return doc._xml()

    def enviar(self, lote: str, sincrono=False):
        pass

    @classmethod
    def assinar(cls, root, ref, certificado):
        if isinstance(root, str):
            root = etree.fromstring(root)
        for child in root:
            if child.tag.endswith('infCte'):
                return certificado.assinar(child, ref)


class WebServices:
    pass
