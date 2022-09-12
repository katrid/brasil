import datetime
from lxml import etree
from ..base import DocumentoFiscal
from .v300 import CTe, TCancCTe, cteProc, Element
from .settings import Config
from .ws import Recepcao, Consulta, RetornoRecepcao, RecepcaoEvento, eventoCTe
from brasil.utils.text import remover_acentos


class _CTe:
    CTe: CTe = None
    cteProc: cteProc = None

    def __init__(self, cte=None, proc=None):
        if cte:
            self.CTe = cte
        elif proc:
            self.cteProc = proc
            self.CTe = self.cteProc.CTe

    @property
    def chave(self):
        return self.CTe.infCte.Id[3:]


class Conhecimentos(list):
    def __init__(self, config):
        super().__init__()
        self._config = config

    def add(self, xml: str = None):
        if xml:
            xml = etree.fromstring(xml)
            if xml.tag == '{http://www.portalfiscal.inf.br/cte}cteProc':
                proc = cteProc()
                proc._read_xml(xml)
                item = _CTe(proc=proc)
                self.append(item)
                return item
            elif xml.tag == '{http://www.portalfiscal.inf.br/cte}CTe':
                cte = CTe()
                cte._config = self._config
                cte._read_xml(xml)
                item = _CTe(cte=cte)
                self.append(item)
                return item
            raise Exception('Impossível carregar os dados do xml')
        cte = _CTe(cte=CTe())
        cte.CTe._config = self._config
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

    def consultar(self, recibo: str) -> RetornoRecepcao:
        svc = RetornoRecepcao(self.config)
        svc.recibo = recibo
        svc.executar()
        return svc

    def cancelar(self, justificativa: str, lote, seq="1", cnpjcpf=None, dh=None, chave=None, orgao=None, protocolo=None, amb=2) -> RecepcaoEvento:
        if dh is None:
            dh = datetime.datetime.now()
        evento = eventoCTe()
        inf = evento.infEvento
        inf.tpEvento = '110111'
        inf.detEvento.evCancCTe.xJust = remover_acentos(justificativa).decode('utf-8')
        inf.dhEvento = dh
        inf.tpAmb = amb
        inf.nSeqEvento = seq
        cnpjcpf = ''.join(filter(str.isdigit, cnpjcpf))
        if len(cnpjcpf) == 11:
            inf.CPF = cnpjcpf
        else:
            inf.CNPJ = cnpjcpf
        inf.cOrgao = orgao or self.config.orgao
        if chave:
            inf.chNFe = chave
            inf.tpAmb = amb
            inf.detEvento.evCancCTe.nProt = protocolo
        elif len(self.conhecimentos):
            nota = self.conhecimento
            inf.chCTe = nota.chave
            inf.tpAmb = self.config.amb
            inf.detEvento.evCancCTe.nProt = nota.cteProc.protCTe.infProt.nProt
        return self.enviar_evento(lote, evento)

    def enviar_evento(self, lote, evento):
        svc = RecepcaoEvento(self.config)
        id_evento = evento.infEvento.Id = 'ID' + evento.infEvento.tpEvento + evento.infEvento.chCTe + str(evento.infEvento.nSeqEvento).zfill(2)
        evento.idLote = lote
        svc.xml = evento
        xml = evento._xml()
        evento.Signature = self.config.certificado.assinar(xml, id_evento)
        # evento.Signature = '<Signature xmlns="http://www.w3.org/2000/09/xmldsig#"><SignedInfo><CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"></CanonicalizationMethod><SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"></SignatureMethod><Reference URI="#ID1101112921060003314160690055920000000708123800195401"><Transforms><Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"></Transform><Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"></Transform></Transforms><DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"></DigestMethod><DigestValue>hnfdfEXVzMEbJReFpOZFcskn4EE=</DigestValue></Reference></SignedInfo><SignatureValue>RVD6VYTf7D+c7xFFXpX1zSa33C4342FfJWMIQthdUMsN95Z9hw1Tf0Ic+5qfPtZd12femHrfKKLNoMlpDbuLX0RnmLxBU4RUQxqWUZOKq/4DxJJyfHteyay+I7DS/tvdmN6FMaOPT2DlFcRfb68P6zAFba0VVLpkXm9uJ+8RVZUIdLjljuGZNDJVgXku5tDYUYZ/5YJ6uRXvFAniSqd46sAcROUz7NsGkwCFSvOWJNLk3ewv1RNeD6Cxlg4HOKmn7MKNBVJzNrHgFYghhH4Wct2flRvV6RVgRblOaY0er9CpqFG+ujkGNnPY3XOQR/r3n8YYhp4+XODkkDYkC3AAfw==</SignatureValue><KeyInfo><X509Data><X509Certificate>MIIG6DCCBNCgAwIBAgIIOSMgBxNBRyAwDQYJKoZIhvcNAQELBQAwWTELMAkGA1UEBhMCQlIxEzARBgNVBAoTCklDUC1CcmFzaWwxFTATBgNVBAsTDEFDIFNPTFVUSSB2NTEeMBwGA1UEAxMVQUMgU09MVVRJIE11bHRpcGxhIHY1MB4XDTIwMDcxMzE0MTEwMFoXDTIxMDcxMzE0MTEwMFowgaIxCzAJBgNVBAYTAkJSMRMwEQYDVQQKEwpJQ1AtQnJhc2lsMR4wHAYDVQQLExVBQyBTT0xVVEkgTXVsdGlwbGEgdjUxFzAVBgNVBAsTDjI2MTgyMjcxMDAwMTA3MRowGAYDVQQLExFDZXJ0aWZpY2FkbyBQRiBBMTEpMCcGA1UEAxMgSk9SR0UgVEFEQVNISSBLT1lBTUE6MzMxNDE2MDY5MDAwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCjb+YQt7Bbh9mwOkc9N6JzQtWtKS3lMPCH7HUbzlbNvJAOSaQNnikdj31FBBM4zHYHoHRbA2LGgR3EmEDjCmkwH1LLDr7Ui7F5Nfmyv1w9Atp7+LLDOlcukOng5VL9Ci1aUQZSkC4PvFTNxDIoqgTkKmY/N6uJe1Qad/tRx3+tac+6oED44RxRnrOg5HB3nkMqKLo3P4mt6Uj2+uEAg70f1JLY5ClG+t8w6H/wIfVP6pgRKoo+1b9ruAn1AfSyOpu5S/Nr7pBfqW4sizS9rFyF+MD4Bt0vR57+rluE+2yFF+jGhk80Odhtvo5v9KdSsc6Kq9IZIwJxkzaZjjQUTgKHAgMBAAGjggJoMIICZDAJBgNVHRMEAjAAMB8GA1UdIwQYMBaAFMVS7SWACd+cgsifR8bdtF8x3bmxMFQGCCsGAQUFBwEBBEgwRjBEBggrBgEFBQcwAoY4aHR0cDovL2NjZC5hY3NvbHV0aS5jb20uYnIvbGNyL2FjLXNvbHV0aS1tdWx0aXBsYS12NS5wN2IwgZcGA1UdEQSBjzCBjIEXZmF6ZW5kYWtveWFtYUBnbWFpbC5jb22gOAYFYEwBAwGgLxMtMjAwNjE5NTQzMzE0MTYwNjkwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwoBcGBWBMAQMGoA4TDDMzMTQxNjA2OTAwMaAeBgVgTAEDBaAVExMwMDAwMDAwMDAwMDAwMDAwMDAwMF0GA1UdIARWMFQwUgYGYEwBAgEmMEgwRgYIKwYBBQUHAgEWOmh0dHA6Ly9jY2QuYWNzb2x1dGkuY29tLmJyL2RvY3MvZHBjLWFjLXNvbHV0aS1tdWx0aXBsYS5wZGYwKQYDVR0lBCIwIAYIKwYBBQUHAwIGCCsGAQUFBwMEBgorBgEEAYI3FAICMIGMBgNVHR8EgYQwgYEwPqA8oDqGOGh0dHA6Ly9jY2QuYWNzb2x1dGkuY29tLmJyL2xjci9hYy1zb2x1dGktbXVsdGlwbGEtdjUuY3JsMD+gPaA7hjlodHRwOi8vY2NkMi5hY3NvbHV0aS5jb20uYnIvbGNyL2FjLXNvbHV0aS1tdWx0aXBsYS12NS5jcmwwHQYDVR0OBBYEFIdxpsKswGbQa7LAF0qCX7DKMlfuMA4GA1UdDwEB/wQEAwIF4DANBgkqhkiG9w0BAQsFAAOCAgEAiN5vKryN3DhOAkcnrPMvOR1LuizeSELwfDjnMWkMJNFNNO0lWpF4kN8Shd39hj2bP4Zpu+H8BYiCi3LP2Ju3wFh8Xn9yYXDKViyofwd+N2F59vmAlV8VKnM2sMQaz5AcGV6x/3nALxaDJXrzNks5ONL8vYQpmkngJ1sH6LYmpnG1rhXcmLNLMw69IonfyaZmQfgWpzETa6iFt+9K7e6WK1Xy0e8U/N8LpUuqJaM3EIyPRyw2ECLC3D8kKBZM13NAKbDJ4Are12Z8lW7x6pteM28nciw+UUOS5+bV5z5EtAhhsPyhpHeei1LqkT0GV2diqArYVaDAFbwUa4PVojyqjl2Ptbsj1lHtCK1F96RKnPYwAZNQLFbSCkfDyllBb6Uckngq2i1TnTejq+OLHPFn+CQa72Z5rwIuNYH052mA/tWeMSHVDaXNTRID7Hb/+mqipm2pSw+dmUkXFQuOpxluNyHHIrAf+jYSaam/oLGbipQTpDMQIPCGOZYSFlkfaOAjFbfF29h2a6eJlP5uNOcNEkZumpxPXa0hQ4RD8fOX8siQ8RYyftJntgCttrDO361e0tvRBFUklfoRhszIJ5sh6NyL90KhQYEN1zgi4I60APLB8T9vankG8XXBy6ulNpwnCxoNewz8DxeChEcDj+UDfUZmvFYCTNSKxOcz6MGcivU=</X509Certificate></X509Data></KeyInfo></Signature>'
        svc.executar()
        return svc
