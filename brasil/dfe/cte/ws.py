import base64
import datetime
import gzip
import os

from lxml import etree

import brasil.dfe.ws
from brasil.consts import CODIGO_UF
from brasil.dfe.utils.xml_utils import tag
from .v400 import (
    consStatServCTe, retConsStatServCTe, consSitCTe, retConsSitCTe, eventoCTe, retEventoCTe,
    distDFeInt, retDistDFeInt, consReciCTe, retConsReciCTe, retCTe, CTe, CTeSimp, retCTeSimp
)


class Header(brasil.dfe.ws.Header):
    soapVersion = 'soap12'
    versaoDados = '4.00'
    element = 'cteCabecMsg'


class Body(brasil.dfe.ws.Body):
    soapVersion = 'soap12'
    element = 'cteDadosMsg'


class WebService(brasil.dfe.ws.BaseService):
    versao = '4.00'
    namespace = 'http://www.portalfiscal.inf.br/cte'
    header = Header
    body = Body


class Distribuicao(WebService):
    class DistribuicaoBody(Body):
        soapVersion = 'soap12'
        element = 'cteDadosMsg'

        def __str__(self):
            v = str(self.soapVersion) + ':' if self.soapVersion else ''
            kwargs = {}
            if self.xmlns:
                kwargs['xmlns'] = self.xmlns
            return tag(
                v + 'Body',
                tag(
                    'cteDistDFeInteresse',
                    tag(
                        self.element,
                        self.xml,
                    ),
                    **kwargs
                ),
            )

    body = DistribuicaoBody
    header = None
    versao = '1.00'
    webservice = 'CTeDistribuicaoDFe'
    namespace = 'http://www.portalfiscal.inf.br/cte'
    wsdl = 'http://www.portalfiscal.inf.br/cte/wsdl/CTeDistribuicaoDFe'
    method = 'cteDistDFeInteresse'
    Xml = distDFeInt
    xml: distDFeInt
    Retorno = retDistDFeInt
    retorno: retDistDFeInt = None


class Consulta(WebService):
    versao = '4.00'
    webservice = 'CTeConsultaProtocolo'
    wsdl = 'http://www.portalfiscal.inf.br/cte/wsdl/CTeConsultaV4'
    method = 'cteConsultaCT'
    Xml = consSitCTe
    xml: consSitCTe
    Retorno = retConsSitCTe
    retorno: retConsSitCTe = None
    header = None

    def preparar(self):
        super().preparar()
        self.xml.versao = self.versao
        self.xml.tpAmb = self.config.amb
        self.xml.xServ = 'CONSULTAR'

    @property
    def chave(self):
        return self.xml.chCTe

    @chave.setter
    def chave(self, value):
        self.xml.chCTe = value


class RetornoRecepcao(WebService):
    webservice = 'CTeRetRecepcao'
    wsdl = 'http://www.portalfiscal.inf.br/cte/wsdl/CteRetRecepcao'
    method = 'cteRetRecepcao'
    Xml = consReciCTe
    xml: consReciCTe
    Retorno = retConsReciCTe
    retorno: retConsReciCTe = None

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


class RecepcaoBody(Body):
    def __str__(self):
        """Retornar os dados do corpo do XML compactados e codificados em base64."""
        b = base64.b64encode((gzip.compress(self.xml.encode('utf-8')))).decode('utf-8')
        return tag(
            self.soapVersion + ':Body',
            tag(self.element, b, xmlns=self.xmlns),
        )


class Recepcao(WebService):
    versao = '4.00'
    body = RecepcaoBody
    webservice = 'CTeRecepcaoSinc'  # mudança de nome na versão 4.00
    namespace = 'http://www.portalfiscal.inf.br/cte'
    wsdl = 'http://www.portalfiscal.inf.br/cte/wsdl/CTeRecepcaoSincV4'
    method = 'cteRecepcao'
    Xml = CTe
    xml: CTe
    Retorno = retCTe
    retorno: retCTe = None


class RecepcaoSimp(Recepcao):
    webservice = 'CTeRecepcaoSimp'
    namespace = 'http://www.portalfiscal.inf.br/cte'
    wsdl = 'http://www.portalfiscal.inf.br/cte/wsdl/CTeRecepcaoSimpV4'
    method = 'cteRecepcao'
    Xml = CTeSimp
    xml: CTeSimp
    Retorno = retCTeSimp
    retorno: retCTeSimp = None


class RecepcaoEvento(WebService):
    versao = '4.00'
    webservice = 'RecepcaoEvento'
    namespace = 'http://www.portalfiscal.inf.br/cte'
    wsdl = 'http://www.portalfiscal.inf.br/cte/wsdl/CTeRecepcaoEventoV4'
    method = 'cteRecepcaoEvento'
    Xml = eventoCTe
    xml: eventoCTe
    Retorno = retEventoCTe
    retorno: retEventoCTe = None

    def preparar(self):
        super().preparar()
        if not self.xml.infEvento.Id:
            self.xml.infEvento.Id = f'ID{self.xml.infEvento.tpEvento}{self.xml.infEvento.chCTe}{str(self.xml.infEvento.nSeqEvento).zfill(2)}'
        if self.xml.Signature is None:
            self.xml.Signature = self.config.certificado.assinar(etree.fromstring(self.xml._xml()), self.xml.infEvento.Id)
        self.xml.tpAmb = self.config.amb

    def cancelar(
            self, protocolo: str, justificativa: str, orgao=None, seq=1, amp=2, cnpj=None,
            chave=None, dh=None
    ):
        evento = eventoCTe()
        evento.versao = '4.00'
        inf = evento.infEvento
        inf.tpAmb = amp
        inf.cOrgao = orgao or self.config.orgao
        inf.nSeqEvento = seq
        inf.CNPJ_CPF = cnpj
        inf.chCTe = chave
        inf.tpEvento = '110111'
        inf.dhEvento = dh or datetime.datetime.now()
        canc = inf.detEvento.evCancCTe
        inf.detEvento.versaoEvento = '4.00'
        canc.descEvento = 'Cancelamento'
        canc.nProt = protocolo
        canc.xJust = justificativa
        id_evento = evento.infEvento.Id = 'ID' + inf.tpEvento + inf.chCTe + str(inf.nSeqEvento).zfill(3)
        xml = evento._xml()
        evento.Signature = self.config.certificado.assinar(xml, id_evento)
        self.xml = evento
        canc_schema = etree.XMLSchema(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'schemas', 'cte', 'eventoCTe_v4.00.xsd'))
        if not canc_schema.validate(etree.fromstring(self.xml._xml())):
            raise AssertionError(canc_schema.error_log.last_error.message)
        self.executar()
        return self


class StatusServico(WebService):
    versao = '4.00'
    webservice = 'CTeStatusServico'
    namespace = 'http://www.portalfiscal.inf.br/cte'
    wsdl = 'http://www.portalfiscal.inf.br/cte/wsdl/CTeStatusServicoV4'
    method = 'cteStatusServicoCT'
    Xml = consStatServCTe
    xml: consStatServCTe
    Retorno = retConsStatServCTe
    retorno: retConsStatServCTe = None
    header = None

    def preparar(self):
        super().preparar()
        self.xml.versao = self.versao
        self.xml.tpAmb = self.config.amb
        self.xml.cUF = CODIGO_UF[self.config.uf]
        self.xml.xServ = 'STATUS'
