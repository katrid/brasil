import brasil.dfe.ws
from .v400 import (
    consStatServ, retConsStatServ, enviNFe, retEnviNFe, consReciNFe, retConsReciNFe, consSitNFe, retConsSitNFe,
    envEvento, retEnvEvento, inutNFe
)


class Header(brasil.dfe.ws.Header):
    versaoDados = '4.00'
    element = 'nfeCabecMsg'


class Body(brasil.dfe.ws.Body):
    element = 'nfeDadosMsg'


class WebService(brasil.dfe.ws.BaseService):
    versao = '4.00'
    namespace = 'http://www.portalfiscal.inf.br/nfe'
    header = None
    body = Body


class Autorizacao(WebService):
    webservice = 'NfeAutorizacao'
    namespace = 'http://www.portalfiscal.inf.br/nfe'
    wsdl = 'http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4'
    method = 'nfeAutorizacaoLote'
    Xml = enviNFe
    xml: enviNFe
    Retorno = retEnviNFe
    retorno: retEnviNFe = None

    def preparar(self):
        super().preparar()
        self.xml.versao = self.versao
        self.xml.tpAmb = self.config.amb


class RecepcaoEvento(WebService):
    webservice = 'RecepcaoEvento'
    namespace = 'http://www.portalfiscal.inf.br/nfe'
    wsdl = 'http://www.portalfiscal.inf.br/nfe/wsdl/NFeRecepcaoEvento4'
    method = 'nfeRecepcaoEvento'
    Xml = envEvento
    xml: envEvento
    Retorno = retEnvEvento
    retorno: retEnvEvento = None

    def preparar(self):
        super().preparar()
        self.xml.versao = '1.00'
        self.xml.tpAmb = self.config.amb


class RetAutorizacao(WebService):
    webservice = 'NFeRetAutorizacao'
    namespace = 'http://www.portalfiscal.inf.br/nfe'
    wsdl = 'http://www.portalfiscal.inf.br/nfe/wsdl/NFeRetAutorizacao4'
    method = 'nfeRetRecepcao'
    Xml = consReciNFe
    xml: consReciNFe
    Retorno = retConsReciNFe
    retorno: retConsReciNFe = None

    def preparar(self):
        super().preparar()
        self.xml.versao = self.versao
        self.xml.tpAmb = self.config.amb


class Inutiliza(WebService):
    webservice = 'NFeInutilizacao'
    namespace = 'http://www.portalfiscal.inf.br/nfe'
    wsdl = 'http://www.portalfiscal.inf.br/nfe/wsdl/NFeInutilizacao4'
    method = 'nfeInutilizacaoNF'
    Xml = consReciNFe
    xml: consReciNFe
    Retorno = retConsReciNFe
    retorno: retConsReciNFe = None

    def preparar(self):
        super().preparar()
        self.xml.versao = self.versao
        self.xml.tpAmb = self.config.amb


class Consulta(WebService):
    webservice = 'NfeConsultaProtocolo'
    namespace = 'http://www.portalfiscal.inf.br/nfe'
    wsdl = 'http://www.portalfiscal.inf.br/nfe/wsdl/NFeConsultaProtocolo4'
    method = 'nfeConsultaNF'
    Xml = consSitNFe
    xml: consSitNFe
    Retorno = retConsSitNFe
    retorno: retConsSitNFe = None

    def preparar(self):
        super().preparar()
        self.xml.versao = self.versao
        self.xml.tpAmb = self.config.amb
        self.xml.xServ = 'CONSULTAR'


class StatusServico(WebService):
    webservice = 'NfeStatusServico'
    namespace = 'http://www.portalfiscal.inf.br/nfe'
    wsdl = 'http://www.portalfiscal.inf.br/nfe/wsdl/NFeStatusServico4'
    method = 'nfeStatusServicoNF'
    Xml = consStatServ
    xml: consStatServ
    Retorno = retConsStatServ
    retorno: retConsStatServ = None

    def preparar(self):
        super().preparar()
        self.xml.versao = self.versao
        self.xml.tpAmb = self.config.amb
        self.xml.xServ = 'STATUS'
