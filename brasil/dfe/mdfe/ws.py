import datetime

from lxml import etree

import brasil.dfe.ws
from brasil.dfe.utils.xml_utils import tag
from brasil.consts import CODIGO_UF
from .v300 import (
    consStatServMDFe, retConsStatServMDFe, consSitMDFe, retConsSitMDFe, enviMDFe, retEnviMDFe, eventoMDFe, retEventoMDFe,
    distMDFe, retDistMDFe, consReciMDFe, retConsReciMDFe, retMDFe, MDFe
)


class Header(brasil.dfe.ws.Header):
    soapVersion = 'soap12'
    versaoDados = '3.00'
    element = 'mdfeCabecMsg'


class Body(brasil.dfe.ws.Body):
    soapVersion = 'soap12'
    element = 'mdfeDadosMsg'


class WebService(brasil.dfe.ws.BaseService):
    versao = '3.00'
    namespace = 'http://www.portalfiscal.inf.br/mdfe'
    header = Header
    body = Body


class Distribuicao(WebService):
    class DistribuicaoBody(Body):
        soapVersion = 'soap12'
        element = 'mdfeDadosMsg'

        def __str__(self):
            v = str(self.soapVersion) + ':' if self.soapVersion else ''
            kwargs = {}
            if self.xmlns:
                kwargs['xmlns'] = self.xmlns
            return tag(
                v + 'Body',
                tag(
                    'mdfeDistDFeInteresse',
                    tag(
                        self.element,
                        self.xml,
                    ),
                    **kwargs
                ),
            )

    body = DistribuicaoBody
    header = None
    versao = '3.00'
    webservice = 'MDFeDistribuicaoDFe'
    namespace = 'http://www.portalfiscal.inf.br/mdfe'
    wsdl = 'http://www.portalfiscal.inf.br/mdfe/wsdl/MDFeDistribuicaoDFe'
    method = 'mdfeDistDFeInteresse'
    Xml = distMDFe
    xml: distMDFe
    Retorno = retDistMDFe
    retorno: retDistMDFe = None


class Consulta(WebService):
    versao = '3.00'
    webservice = 'MDFeConsulta'
    namespace = 'http://www.portalfiscal.inf.br/mdfe'
    wsdl = 'http://www.portalfiscal.inf.br/mdfe/wsdl/MDFeConsulta'
    method = 'MDFeConsulta'
    Xml = consSitMDFe
    xml: consSitMDFe
    Retorno = retConsSitMDFe
    retorno: retConsSitMDFe = None
    header = None

    def preparar(self):
        super().preparar()
        self.xml.versao = self.versao
        self.xml.tpAmb = self.config.amb
        self.xml.xServ = 'CONSULTAR'

    @property
    def chave(self):
        return self.xml.chMDFe

    @chave.setter
    def chave(self, value):
        self.xml.chMDFe = value


class RetornoRecepcao(WebService):
    webservice = 'MDFeRetRecepcao'
    wsdl = 'http://www.portalfiscal.inf.br/mdfe/wsdl/MDFeRetRecepcao'
    method = 'mdfeRetRecepcao'
    Xml = consReciMDFe
    xml: consReciMDFe
    Retorno = retConsReciMDFe
    retorno: retConsReciMDFe = None

    def preparar(self):
        super().preparar()
        self.xml.versao = self.versao
        self.xml.tpAmb = self.config.amb

    @property
    def recibo(self):
        return self.xml.nRec

    @recibo.setter
    def recibo(self, value):
        self.xml.nRec = value


class Recepcao(WebService):
    versao = '3.00'
    webservice = 'MDFeRecepcaoSinc'
    namespace = 'http://www.portalfiscal.inf.br/mdfe'
    wsdl = 'http://www.portalfiscal.inf.br/mdfe/wsdl/MDFeRecepcaoSinc'
    method = 'MDFeRecepcao'
    Xml = MDFe
    xml: MDFe
    Retorno = retMDFe
    retorno: retMDFe = None

    def preparar(self):
        super().preparar()
        self.xml.tpAmb = self.config.amb

    def executar(self):
        envelope = self.envelope(encoded=True)
        self.enviar(envelope)
        self.finalizar()
        self.ok = self.response.status_code == 200
        return self.ok


class RecepcaoEvento(WebService):
    versao = '3.00'
    webservice = 'MDFeRecepcaoEvento'
    namespace = 'http://www.portalfiscal.inf.br/mdfe'
    wsdl = 'http://www.portalfiscal.inf.br/mdfe/wsdl/MDFeRecepcaoEvento'
    method = 'MDFeRecepcaoEvento'
    Xml = eventoMDFe
    xml: eventoMDFe
    Retorno = retEventoMDFe
    retorno: retEventoMDFe = None

    def preparar(self):
        super().preparar()
        if not self.xml.infEvento.Id:
            self.xml.infEvento.Id = f'ID{self.xml.infEvento.tpEvento}{self.xml.infEvento.chMDFe}{str(self.xml.infEvento.nSeqEvento).zfill(2)}'
        if self.xml.Signature is None:
            self.xml.Signature = self.config.certificado.assinar(etree.fromstring(self.xml._xml()), self.xml.infEvento.Id)
        self.xml.tpAmb = self.config.amb

    def cancelar(
            self, protocolo: str, justificativa: str, orgao=None, seq=1, amp=2, cnpj=None,
            chave=None, dh=None
    ):
        from brasil.dfe.mdfe.v300 import eventoMDFe, evCancMDFe
        evento = eventoMDFe()
        inf = evento.infEvento
        inf.tpAmb = amp
        inf.cOrgao = orgao or self.config.orgao
        inf.nSeqEvento = seq
        inf.CNPJCPF = cnpj
        inf.chMDFe = chave
        inf.tpEvento = '110111'
        inf.dhEvento = dh or datetime.datetime.now()
        canc = inf.detEvento.evCancMDFe = evCancMDFe()
        canc.descEvento = 'Cancelamento'
        canc.nProt = protocolo
        canc.xJust = justificativa
        id_evento = evento.infEvento.Id = 'ID' + inf.tpEvento + inf.chMDFe + str(inf.nSeqEvento).zfill(2)
        xml = evento._xml()
        evento.Signature = self.config.certificado.assinar(xml, id_evento)
        self.xml = evento
        self.executar()
        return self


class StatusServico(WebService):
    versao = '3.00'
    webservice = 'MDFeStatusServico'
    namespace = 'http://www.portalfiscal.inf.br/mdfe'
    wsdl = 'http://www.portalfiscal.inf.br/mdfe/wsdl/MDFeStatusServico'
    method = 'MDFeStatusServico'
    Xml = consStatServMDFe
    xml: consStatServMDFe
    Retorno = retConsStatServMDFe
    retorno: retConsStatServMDFe = None
    header = None

    def preparar(self):
        super().preparar()
        self.xml.versao = self.versao
        self.xml.tpAmb = self.config.amb
        self.xml.cUF = CODIGO_UF[self.config.uf]
        self.xml.xServ = 'STATUS'
