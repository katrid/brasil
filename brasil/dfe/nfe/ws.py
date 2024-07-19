import brasil.dfe.ws
from brasil.dfe.utils.xml_utils import tag
from .v400 import (
    consStatServ, retConsStatServ, enviNFe, retEnviNFe, consReciNFe, retConsReciNFe, consSitNFe, retConsSitNFe,
    envEvento, retEnvEvento,
    distDFeInt, retDistDFeInt,
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


class Distribuicao(WebService):
    class DistribuicaoBody(Body):
        soapVersion = 'soap12'
        element = 'nfeDadosMsg'

        def __str__(self):
            v = str(self.soapVersion) + ':' if self.soapVersion else ''
            kwargs = {}
            if self.xmlns:
                kwargs['xmlns'] = self.xmlns
            return tag(
                v + 'Body',
                tag(
                    'nfeDistDFeInteresse',
                    tag(
                        self.element,
                        self.xml,
                    ),
                    **kwargs
                ),
                )

    body = DistribuicaoBody
    header = None
    versao = '1.01'
    webservice = 'NFeDistribuicaoDFe'
    namespace = 'http://www.portalfiscal.inf.br/nfe'
    wsdl = 'http://www.portalfiscal.inf.br/nfe/wsdl/NFeDistribuicaoDFe'
    method = 'nfeDistDFeInteresse'
    Xml = distDFeInt
    xml: distDFeInt
    Retorno = retDistDFeInt
    retorno: retDistDFeInt = None
    uf = 'AN'  # uf da distribuição é Ambiente Nacional

