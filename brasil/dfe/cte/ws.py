from lxml import etree

import brasil.dfe.ws
from brasil.dfe.utils.xml_utils import tag
from brasil.consts import CODIGO_UF
from .v400 import (
    consStatServCTe, retConsStatServCTe, consSitCTe, retConsSitCTe, enviCTe, retEnviCte, eventoCTe, retEventoCTe,
    distDFeInt, retDistDFeInt, consReciCTe, retConsReciCTe, retCTe, CTe
)


class Header(brasil.dfe.ws.Header):
    soapVersion = 'soap'
    versaoDados = '4.00'
    element = 'cteCabecMsg'


class Body(brasil.dfe.ws.Body):
    soapVersion = 'soap'
    element = 'cteDadosMsg'


class WebService(brasil.dfe.ws.BaseService):
    versao = '4.00'
    namespace = 'http://www.portalfiscal.inf.br/cte'
    header = Header
    body = Body


class Distribuicao(WebService):
    class DistribuicaoBody(Body):
        soapVersion = 'soap'
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
    webservice = 'CTeConsultaProtocolo'
    wsdl = 'http://www.portalfiscal.inf.br/cte/wsdl/CteConsulta'
    method = 'cteConsultaCT'
    Xml = consSitCTe
    xml: consSitCTe
    Retorno = retConsSitCTe
    retorno: retConsSitCTe = None

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


class Recepcao(WebService):
    versao = '4.00'
    # webservice = 'CTeRecepcao'
    webservice = 'CTeRecepcaoSinc' # mudança de nome na versão 4.00
    namespace = 'http://www.portalfiscal.inf.br/cte'
    wsdl = 'http://www.portalfiscal.inf.br/cte/wsdl/CTeRecepcaoSincV4'
    method = 'cteRecepcao'
    Xml = CTe
    xml: CTe
    Retorno = retCTe
    retorno: retCTe = None

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
    versao = '4.00'
    webservice = 'RecepcaoEvento'
    namespace = 'http://www.portalfiscal.inf.br/cte'
    wsdl = 'http://www.portalfiscal.inf.br/cte/wsdl/CteRecepcaoEvento'
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
