import brasil.dfe.ws
from .v300 import consStatServCte, retConsStatServCte, consSitCTe, retConsSitCTe, enviCTe, retEnviCte, eventoCTe, retEventoCTe


class Header(brasil.dfe.ws.Header):
    soapVersion = 'soap'
    versaoDados = '3.00'
    element = 'cteCabecMsg'


class Body(brasil.dfe.ws.Body):
    soapVersion = 'soap'
    element = 'cteDadosMsg'


class WebService(brasil.dfe.ws.BaseService):
    namespace = 'http://www.portalfiscal.inf.br/cte'
    header = Header
    body = Body


class Consulta(WebService):
    versao = '3.00'
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
