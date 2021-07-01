import os
import datetime
from lxml import etree
from ..base import DocumentoFiscal
from .settings import Config
from .v400 import NFe, nfeProc
from .ws import StatusServico, Autorizacao, RetAutorizacao, Consulta, RecepcaoEvento, inutNFe
from brasil.dfe.leiaute.nfe.eventoCancNFe_v100 import evento as TEventoCanc
from brasil.utils.text import remover_acentos


class _NFe:
    NFe: NFe = None
    nfeProc: nfeProc = None

    def __init__(self, nfe=None, proc=None):
        if nfe:
            self.NFe = nfe
        elif proc:
            self.nfeProc = proc
            self.NFe = self.nfeProc.NFe

    @property
    def chave(self):
        return self.NFe.infNFe.Id[3:]


class NotasFiscais(list):
    def __init__(self, config: Config):
        super().__init__()
        self._config = config

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
                nfe._config = self._config
                nfe._read_xml(xml)
                item = _NFe(nfe=nfe)
                self.append(item)
                return item
            raise Exception('Impossível carregar os dados do xml')
        nfe = _NFe(nfe=NFe())
        nfe.NFe._config = self._config
        self.append(nfe)
        return nfe


class NotaFiscal(DocumentoFiscal):
    notas: NotasFiscais[_NFe]

    def __init__(self, xml=None, config: Config = None):
        self.config: Config = config
        self.notas = NotasFiscais(config)
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
            # nf.Signature = self.assinar(nf._xml(), nf.infNFe.Id, self.config.certificado)
            svc.xml.NFe.append(nf)
        svc.xml.idLote = str(lote)
        svc.xml.indSinc = '1' if sincrono else '0'
        svc.executar()
        return svc

    def cancelar(self, justificativa: str, lote, seq="1", cnpjcpf=None, dh=None, chave=None, orgao=None, protocolo=None, amb=2):
        if dh is None:
            dh = datetime.datetime.now()
        assert dh, 'O campo data/hora do evento é obrigatório'
        evento = TEventoCanc()
        evento.versao = '1.00'
        inf = evento.infEvento
        inf.detEvento.xJust = remover_acentos(justificativa).decode('utf-8')
        inf.dhEvento = dh
        inf.tpAmb = amb
        inf.nSeqEvento = seq
        cnpjcpf = ''.join(filter(str.isdigit, cnpjcpf))
        if len(cnpjcpf) == 11:
            inf.CPF = cnpjcpf
        else:
            inf.CNPJ = cnpjcpf
        inf.cOrgao = orgao or self.config.orgao
        inf.verEvento = '1.00'
        if chave:
            inf.chNFe = chave
            inf.tpAmb = amb
            inf.detEvento.nProt = protocolo
        elif len(self.notas):
            nota = self.nota
            inf.chNFe = nota.chave
            inf.tpAmb = nota.NFe.infNFe.ide.tpAmb
            inf.detEvento.nProt = nota.nfeProc.protNFe.infProt.nProt
        return self.enviar_evento(lote, evento)

    def enviar_evento(self, lote, evento: TEventoCanc):
        svc = RecepcaoEvento(self.config)
        id_evento = evento.infEvento.Id = 'ID' + evento.infEvento.tpEvento + evento.infEvento.chNFe + str(evento.infEvento.nSeqEvento).zfill(2)
        svc.xml.idLote = lote
        svc.xml.evento.append(evento)
        evento.Signature = self.config.certificado.assinar(etree.fromstring(evento._xml()), id_evento)
        # evento.Signature = '<Signature xmlns="http://www.w3.org/2000/09/xmldsig#"><SignedInfo><CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"></CanonicalizationMethod><SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"></SignatureMethod><Reference URI="#ID1101112921060003314160690055920000000708123800195401"><Transforms><Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"></Transform><Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"></Transform></Transforms><DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"></DigestMethod><DigestValue>hnfdfEXVzMEbJReFpOZFcskn4EE=</DigestValue></Reference></SignedInfo><SignatureValue>RVD6VYTf7D+c7xFFXpX1zSa33C4342FfJWMIQthdUMsN95Z9hw1Tf0Ic+5qfPtZd12femHrfKKLNoMlpDbuLX0RnmLxBU4RUQxqWUZOKq/4DxJJyfHteyay+I7DS/tvdmN6FMaOPT2DlFcRfb68P6zAFba0VVLpkXm9uJ+8RVZUIdLjljuGZNDJVgXku5tDYUYZ/5YJ6uRXvFAniSqd46sAcROUz7NsGkwCFSvOWJNLk3ewv1RNeD6Cxlg4HOKmn7MKNBVJzNrHgFYghhH4Wct2flRvV6RVgRblOaY0er9CpqFG+ujkGNnPY3XOQR/r3n8YYhp4+XODkkDYkC3AAfw==</SignatureValue><KeyInfo><X509Data><X509Certificate>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</X509Certificate></X509Data></KeyInfo></Signature>'
        svc.executar()
        return svc

    def consultar(self, chave=None):
        svc = Consulta(self.config)
        svc.xml.chNFe = chave or self.nota.NFe.chave
        svc.executar()
        return svc

    def consultar_recibo(self, recibo):
        svc = RetAutorizacao(self.config)
        svc.xml.nRec = recibo
        svc.executar()
        return svc

    def inutilizar_nfe(self, orgao=None, ano=None, cnpj=None, mod=None, serie=None, nf_ini=None, nf_fim=None, justificativa=None, amb=2):
        from brasil.dfe.leiaute.nfe.inutNFe_v400 import inutNFe
        inut = inutNFe()
        if not orgao:
            orgao = self.config.orgao
        inut.infInut.cUF = orgao
        inut.infInut.serie = serie
        inut.infInut.mod = mod
        inut.infInut.CNPJ = cnpj
        inut.infInut.ano = ano
        inut.infInut.nNFIni = nf_ini
        inut.infInut.nNFFin = nf_fim
        inut.infInut.xJust = justificativa

    def assinar(self):
        for nota in self.notas:
            nota.NFe.assinar()

    def status_servico(self, uf):
        st = StatusServico(self.config)
        st.xml.cUF = uf
        st.executar()
        return st

    def _imprimir_pdf(self, nfe: _NFe):
        if nfe.nfeProc:
            self.pdf_lib.nfePdf(nfe.nfeProc._xml().encode('utf-8'))
        else:
            self.pdf_lib.nfePdf(nfe.NFe._xml().encode('utf-8'))
        pdf = os.path.join(self.pdf_output_path, nfe.chave + '-nfe.pdf')
        if os.path.isfile(pdf):
            return pdf

    def _imprimir_evento_pdf(self, xml: str):
        pdf = xml.split('Id="', 1)[1][2:54] + '-procEventoNFe.pdf'
        self.pdf_lib.nfeEventoPdf(xml.encode('utf-8'))
        if os.path.isfile(os.path.join(self.pdf_output_path, pdf)):
            return pdf


class WebServices:
    pass
