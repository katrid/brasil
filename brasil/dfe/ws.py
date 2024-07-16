import os
import base64
import gzip
import datetime
import requests
from lxml import etree

from .utils.xml_utils import tag
from .services import BaseConfig
from .ws import *


class Header:
    soapVersion: str = 'soap12'
    element: str = None
    xmlns: str = None
    cUF: str = None
    versaoDados: str = None

    def __str__(self):
        v = str(self.soapVersion) + ':' if self.soapVersion else ''
        kwargs = {}
        if self.xmlns:
            kwargs['xmlns'] = self.xmlns
        return tag(
            v + 'Header',
            tag(
                self.element,
                tag('cUF', self.cUF),
                tag('versaoDados', self.versaoDados),
                **kwargs
            ),
        )


class Body:
    soapVersion: str = 'soap12'
    xmlns: str = None
    element: str = None
    xml: str = None

    def __str__(self):
        v = str(self.soapVersion) + ':' if self.soapVersion else ''
        kwargs = {}
        if self.xmlns:
            kwargs['xmlns'] = self.xmlns
        return tag(
            v + 'Body',
            tag(
                self.element,
                self.xml,
                **kwargs
            ),
            )



class BaseService:
    header: Header
    body: Body
    webservice: str
    service: str
    method: str
    contentType = 'application/soap+xml; charset=utf-8;'
    xml = None
    Xml = None
    namespace = 'http://www.portalfiscal.inf.br'
    campoRetorno: str = None
    wsdl = 'http://www.portalfiscal.inf.br/wsdl'
    xmlattrs = 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope"'
    _xmlresp: etree.Element
    response: requests.Response
    ok = None
    uf: str = None

    def __init__(self, config: BaseConfig):
        self.config = config
        if self.uf is None:
            self.uf = config.uf
        self.tpAmb = config.amb
        if self.header:
            self.header = self.header()
            self.header.xmlns = self.xmlns
        if self.body:
            self.body = self.body()
            self.body.xmlns = self.xmlns
        self.clear()

    def clear(self):
        self.xml = self.Xml()

    @property
    def url(self):
        return self.config.services.get(self.webservice, self.uf, self.tpAmb, self.versao)

    def envelope(self):
        self.preparar()
        s = ''
        self.body.xml = self.xml.to_string()
        if self.config.salvar_arquivos:
            self.config.salvar_arquivo(self.body.xml, self.filename('env'))
        s += str(self.body)
        t = self.body.soapVersion + ':Envelope'
        return f'<?xml version="1.0" encoding="UTF-8"?><{t} {self.xmlattrs}>{s}</{t}>'.encode('utf-8')

    def executar(self):
        envelope = self.envelope()
        self.enviar(envelope)
        self.finalizar()
        self.ok = self.response.status_code == 200
        return self.ok

    def preparar(self):
        from brasil.consts import CODIGO_UF
        if self.header:
            self.header.cUF = CODIGO_UF[self.uf]

    def finalizar(self):
        if self.response.status_code == 200:
            self.config.log.debug('HTTP Sucesso', self.response.status_code)
            self._xmlresp = etree.fromstring(self.response.content)
            ret = self.Retorno()
            xml = self.find(ret._name)
            ret._read_xml(xml)
            self.retorno = ret
        else:
            self.config.log.error('HTTP Error', self.response.status_code)

    def enviar(self, data):
        # salvar arquivo antes de prosseguir
        self.config.log.debug('Enviando envelope...', self.tpAmb, self.uf)
        if self.config.salvar_soap:
            filename = self.filename('env')
            self.config.salvar_arquivo(data, filename)
        res = self._enviar(data)
        self.config.log.debug('Envelope enviado...', self.tpAmb, self.uf)
        # salvar o arquivo de retorno
        if self.config.salvar_soap:
            filename = self.filename('res')
            self.config.salvar_arquivo(res.content, filename)
        self.response = res

    def _enviar(self, data):
        return requests.post(
            self.url, data, verify=False,
            cert=(self.config.certificado.cert_file, self.config.certificado.key_file),
            headers=self.headers,
        )

    @property
    def xmlns(self):
        return self.wsdl

    @property
    def soapwsdl(self):
        return '%s/%s' % (self.wsdl, self.method)

    @property
    def headers(self):
        return {
            'Content-Type': self.contentType,
        }

    def filename(self, suffix=None):
        if suffix:
            suffix += '-'
        else:
            suffix = ''
        return '%s-%s%s.xml' % (datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'), suffix, self.method.lower())

    def find(self, tag, xml=None):
        if xml is None:
            xml = self._xmlresp
        return xml.find('.//{%s}%s' % (self.namespace, tag))

