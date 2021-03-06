from lxml import etree

import brasil.dfe.ws
from brasil.dfe.utils.xml_utils import tag
from .v300 import (
    consStatServCte, retConsStatServCte, consSitCTe, retConsSitCTe, enviCTe, retEnviCte, eventoCTe, retEventoCTe,
    distDFeInt, retDistDFeInt,
)


class Header(brasil.dfe.ws.Header):
    soapVersion = 'soap'
    versaoDados = '3.00'
    element = 'cteCabecMsg'


class Body(brasil.dfe.ws.Body):
    soapVersion = 'soap'
    element = 'cteDadosMsg'


class WebService(brasil.dfe.ws.BaseService):
    versao = '3.00'
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
    namespace = 'http://www.portalfiscal.inf.br/cte'
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


class Recepcao(WebService):
    versao = '3.00'
    webservice = 'CTeRecepcao'
    namespace = 'http://www.portalfiscal.inf.br/cte'
    wsdl = 'http://www.portalfiscal.inf.br/cte/wsdl/CteRecepcao'
    method = 'cteRecepcaoLote'
    Xml = enviCTe
    xml: enviCTe
    Retorno = retEnviCte
    retorno: retEnviCte = None

    def preparar(self):
        super().preparar()
        self.xml.tpAmb = self.config.amb


class Evento(WebService):
    versao = '3.00'
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
        if not self.xml.Signature:
            self.xml.Signature = self.config.certificado.assinar(etree.fromstring(self.xml._xml()), self.xml.infEvento.Id)
        self.xml.tpAmb = self.config.amb


class StatusServico(WebService):
    versao = '3.00'
    webservice = 'CTeStatusServico'
    namespace = 'http://www.portalfiscal.inf.br/cte'
    wsdl = 'http://www.portalfiscal.inf.br/cte/wsdl/CteStatusServico'
    method = 'cteStatusServicoCT'
    Xml = consStatServCte
    xml: consStatServCte
    Retorno = retConsStatServCte
    retorno: retConsStatServCte = None

    def preparar(self):
        super().preparar()
        self.xml.versao = self.versao
        self.xml.tpAmb = self.config.amb
        self.xml.xServ = 'STATUS'
