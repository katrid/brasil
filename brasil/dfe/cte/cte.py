from lxml import etree
from ..base import DocumentoFiscal
from .v300 import CTe
from .settings import Config
from .ws import Recepcao


class Conhecimentos(list):
    def __init__(self, config):
        super().__init__()
        self._config = config

    def add(self, xml=None):
        cte = CTe()
        cte._config = self._config
        if xml:
            cte._read_xml(xml)
        self.append(cte)
        return cte


class Conhecimento(DocumentoFiscal):
    conhecimentos: Conhecimentos

    def __init__(self, xml=None, config: Config = None):
        self.config: Config = config
        self.conhecimentos = Conhecimentos(config)
        if xml:
            self.conhecimentos.add(xml)

    def to_xml(self, doc: CTe=None):
        return doc._xml()

    def enviar(self, lote: int):
        svc = Recepcao(self.config)
        for ct in self.conhecimentos:
            svc.xml.CTe.append(ct)
        svc.xml.idLote = lote
        svc.executar()
        return svc

    @property
    def conhecimento(self):
        return self.conhecimentos[0]

    def assinar(self, root, ref):
        if isinstance(root, str):
            root = etree.fromstring(root)
        for child in root:
            if child.tag.endswith('infCte'):
                return self.config.certificado.assinar(child, ref)

    def from_xml(self, xml: str):
        doc = etree.fromstring(xml)
        doc.tag.endswith('cteProc')


class WebServices:
    pass
