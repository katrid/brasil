import datetime
import os

from lxml import etree

from brasil.utils.text import remover_acentos
from .settings import Config
from .v300 import MDFe, mdfeProc
from .ws import Recepcao, Consulta, RetornoRecepcao, RecepcaoEvento, eventoMDFe
from ..base import DocumentoFiscal


class _MDFe:
    MDFe: MDFe = None
    mdfeProc: mdfeProc = None

    def __init__(self, mdfe=None, proc=None):
        if mdfe:
            self.MDFe = mdfe
        elif proc:
            self.mdfeProc = proc
            self.MDFe = self.mdfeProc.MDFe

    @property
    def chave(self):
        return self.MDFe.infMDFe.Id[4:]


class Manifestos(list):
    def __init__(self, config):
        super().__init__()
        self._config = config

    def add(self, xml: str = None):
        if xml:
            xml = etree.fromstring(xml)
            if xml.tag == '{http://www.portalfiscal.inf.br/mdfe}mdfeProc':
                proc = mdfeProc()
                proc._read_xml(xml)
                item = _MDFe(proc=proc)
                self.append(item)
                return item
            elif xml.tag == '{http://www.portalfiscal.inf.br/mdfe}MDFe':
                mdfe = MDFe()
                mdfe._config = self._config
                mdfe._read_xml(xml)
                item = _MDFe(mdfe=mdfe)
                self.append(item)
                return item
            raise Exception('Impossível carregar os dados do xml')
        mdfe = _MDFe(mdfe=MDFe())
        mdfe.MDFe._config = self._config
        self.append(mdfe)
        return mdfe


class Manifesto(DocumentoFiscal):
    manifestos: Manifestos

    def __init__(self, xml=None, config: Config = None):
        self.config: Config = config
        self.manifestos = Manifestos(config)
        if xml:
            self.manifestos.add(xml)

    def to_xml(self, doc: MDFe=None):
        return doc.to_string()

    def enviar_(self, lote: int):
        svc = Recepcao(self.config)
        for ct in self.manifestos:
            svc.xml.MDFe.append(ct.MDFe)
        svc.xml.idLote = lote
        svc.executar()
        return svc

    def enviar(self):
        svc = Recepcao(self.config)
        svc.xml = self.manifesto.MDFe
        svc.executar()
        return svc

    @property
    def manifesto(self):
        return self.manifestos[0]

    def assinar(self, root, ref):
        if isinstance(root, str):
            root = etree.fromstring(root)
        for child in root:
            if child.tag.endswith('infMDFe'):
                return self.config.certificado.assinar(child, ref)

    def from_xml(self, xml: str):
        return self.manifestos.add(xml)

    def consultar(self, chave: str) -> RetornoRecepcao:
        """
        Consulta situação do MDFe pela chave.
        """
        svc = Consulta(self.config)
        svc.chave = chave
        svc.xml._xmlns = 'http://www.portalfiscal.inf.br/mdfe'
        svc.executar()
        return svc

    def cancelar(self, justificativa: str, protocolo: str | int,
                cnpjcpf: str | int, dh_emis: datetime.datetime | str, orgao: str=None, seq:int | str="1"
                 ) -> RecepcaoEvento:
        """
        Prepara e envia evento de cancelamento do MDFe informado.
        :param str justificativa: Justificativa para o cancelamento.
        :param str protocolo: Numero de protocolo do MDFe a ser cancelado.
        :param str cnpjcpf: Documento, CPF ou CNPJ, do solicitante do cancelamento.
        :param str dh_mis: Data e hora da emissão do evento de cancelamento.
        :param str orgao: Código do órgão de recepção do Evento. Utilizar a Tabela do IBGE estendida.
        :param str seq: Sequencial do evento para o mesmo tipo de evento. Para maioria dos eventos será 1, nos casos em que possa existir mais de um evento o autor do evento deve numerar de forma sequencial.
        """
        from brasil.dfe.leiaute.mdfe.evCancMDFe_v300 import evCancMDFe
        evento = eventoMDFe()
        evento.versao = '3.00'
        evento._xmlns = "http://www.portalfiscal.inf.br/mdfe"
        inf = evento.infEvento
        inf.tpEvento = '110111'
        inf.dhEvento = dh_emis.strftime('%Y-%m-%dT%H:%M:%S') + '-03:00' if isinstance(dh_emis, datetime.datetime) else dh_emis
        inf.tpAmb = self.config.amb
        inf.nSeqEvento = seq
        inf.CNPJ_CPF = cnpjcpf
        inf.cOrgao = orgao or self.config.orgao
        inf.chMDFe = self.manifesto.chave
        inf.tpAmb = self.config.amb
        inf.Id = 'ID' + inf.tpEvento + inf.chMDFe + seq.zfill(2)
        inf.detEvento.evCancMDFe = evCancMDFe()
        inf.detEvento.versaoEvento = '3.00'
        canc_ev = inf.detEvento.evCancMDFe
        canc_ev.xJust = remover_acentos(justificativa).decode('utf-8')
        canc_ev.nProt = protocolo
        canc_ev.descEvento = 'Cancelamento'
        # validar xml específico do evento de cancelamento        
        # canc_schema = etree.XMLSchema(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'schemas', 'mdfe', 'evCancMDFe_v3.00.xsd'))
        # if not canc_schema.validate(etree.fromstring(canc_ev._xml())):
        #     raise AssertionError(canc_schema.error_log.last_error.message)
        return self.enviar_evento(evento)
    
    def encerrar(self, protocolo: str | int, dt: str | datetime.datetime, uf: str | int, cMun: str | int,
                cnpjcpf: str | int, dh_emis: datetime.datetime | str, orgao: str=None, seq:int | str="1"
                 ) -> RecepcaoEvento:
        """
        Prepara e envia evento de encerramento do MDFe informado.
        :param str protocolo: Numero de protocolo do MDFe a ser encerrado.
        :param: str|datetime dt: Data de encerramento do MDFe.
        :param str uf: UF de encerramento do manifesto.
        :param str cMun: Código do município de encerramento do manifesto.
        :param str cnpjcpf: Documento, CPF ou CNPJ, do solicitante do encerramento.
        :param str dh_mis: Data e hora da emissão do evento de encerramento.
        :param str orgao: Código do órgão de recepção do Evento. Utilizar a Tabela do IBGE estendida.
        :param str seq: Sequencial do evento para o mesmo tipo de evento. Para maioria dos eventos será 1, nos casos em que possa existir mais de um evento o autor do evento deve numerar de forma sequencial.
        """
        ev = eventoMDFe()
        ev.versao = '3.00'
        inf = ev.infEvento
        inf.tpAmb = self.config.amb
        inf.cOrgao = orgao or self.config.orgao
        inf.CNPJ_CPF = cnpjcpf
        inf.chMDFe = self.manifesto.chave
        inf.dhEvento = dh_emis.strftime('%Y-%m-%dT%H:%M:%S') + '-03:00' if isinstance(dh_emis, datetime.datetime) else dh_emis
        inf.tpEvento = '110112'
        inf.nSeqEvento = seq
        enc = inf.detEvento.evEncMDFe
        inf.detEvento.versaoEvento = '3.00'
        inf.Id = 'ID' + inf.tpEvento + inf.chMDFe + seq.zfill(2)
        enc.descEvento = 'Encerramento'
        enc.nProt = protocolo
        enc.dtEnc = dt.strftime('%Y-%m-%d') if isinstance(dt, datetime.datetime) else dt
        enc.cUF = uf
        enc.cMun = cMun
        # validar xml específico do evento de encerramento        
        # ev_schema = etree.XMLSchema(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'schemas', 'mdfe', 'evEncMDFe_v3.00.xsd'))
        # if not ev_schema.validate(etree.fromstring(ev.to_string())):
        #     raise AssertionError(ev_schema.error_log.last_error.message)
        return self.enviar_evento(ev)

    def enviar_evento(self, evento: eventoMDFe) -> RecepcaoEvento:
        """
        Recebe objeto de evento, assina e faz a transmissão para a Sefaz.
        """
        # valida evento antes de enviar
        schema = etree.XMLSchema(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'schemas', 'mdfe', 'eventoMDFe_v3.00.xsd'))
        evento_xml = evento._xml()
        evento.Signature = self.config.certificado.assinar(evento_xml, evento.infEvento.Id)
        if not schema.validate(etree.fromstring(evento._xml())):
            raise AssertionError(schema.error_log.last_error.message)
        
        svc = RecepcaoEvento(self.config)
        svc.xml = evento
        svc.executar()
        return svc
