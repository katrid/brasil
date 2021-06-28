from lxml import etree
from ..base import DocumentoFiscal
from .settings import Config
from .v400 import NFe, nfeProc
from .ws import StatusServico, Autorizacao, RetAutorizacao, Consulta


class _NFe:
    NFe: NFe
    nfeProc: nfeProc

    def __init__(self, nfe=None, proc=None):
        if nfe:
            self.NFe = nfe
        elif proc:
            self.nfeProc = proc
            self.NFe = self.nfeProc.NFe


class NotasFiscais(list):
    def add(self, xml=None):
        if xml:
            if isinstance(xml, str):
                xml = xml.replace(' xmlns="http://www.portalfiscal.inf.br/nfe"', '')
                xml = etree.fromstring(xml)
            if xml.tag == 'nfeProc':
                proc = nfeProc()
                proc._read_xml(xml)
                item = _NFe(proc=proc)
                self.append(item)
                return item
            elif xml.tag == 'NFe':
                nfe = NFe()
                nfe._read_xml(xml)
                item = _NFe(nfe=nfe)
                self.append(item)
                return item
            raise Exception('Impossível carregar os dados do xml')
        nfe = _NFe(nfe=NFe())
        self.append(nfe)
        return nfe


class NotaFiscal(DocumentoFiscal):
    notas: NotasFiscais[_NFe]

    def __init__(self, xml=None, config: Config = None):
        self.config: Config = config
        self.notas = NotasFiscais()
        if xml:
            self.notas.add(xml)

    def to_xml(self, doc: NFe=None):
        return doc._xml()

    @property
    def nota(self):
        return self.notas[0]

    def enviar(self, lote: str, sincrono=False):
        svc = Autorizacao(self.config)
        amb = self.config.amb
        for nota in self.notas:
            nf = nota.NFe
            if amb == 2:
                nf.infNFe.dest.xNome = 'NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL'
            nf.Signature = self.assinar(nf._xml(), nf.infNFe.Id, self.config.certificado)
            svc.xml.NFe.append(nf)
        svc.xml.idLote = str(lote)
        svc.xml.indSinc = '1' if sincrono else '0'
        svc.executar()
        return svc

    def consultar(self, chave):
        svc = Consulta(self.config)
        svc.xml.chNFe = chave
        svc.executar()
        return svc

    def consultar_recibo(self, recibo):
        svc = RetAutorizacao(self.config)
        svc.xml.nRec = recibo
        svc.executar()
        return svc

    @classmethod
    def assinar(cls, root, ref, certificado):
        if isinstance(root, str):
            root = etree.fromstring(root)
        for child in root:
            if child.tag.endswith('infNFe'):
                return certificado.assinar(child, ref)

    def status_servico(self, uf):
        st = StatusServico(self.config)
        st.xml.cUF = uf
        st.executar()
        return st


class WebServices:
    pass
