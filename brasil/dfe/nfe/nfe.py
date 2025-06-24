from __future__ import annotations

import datetime

from lxml import etree

from brasil.dfe.leiaute.nfe.eventoCancNFe_v100 import evento as TEventoCanc
from .settings import Config
from .v400 import NFe, nfeProc
from .ws import StatusServico, Autorizacao, RetAutorizacao, Consulta, RecepcaoEvento, Inutiliza
from ..base import DocumentoFiscal
from ..xsd import EmptyTag  # noqa


class _NFe:
    NFe: NFe = None
    nfeProc: nfeProc = None

    def __init__(self, nfe=None, proc=None):
        if nfe:
            self.NFe = nfe
        elif proc:
            self.nfeProc = proc
            self.NFe = self.nfeProc.NFe

    @property
    def chave(self):
        return self.NFe.infNFe.Id[3:]


class NotasFiscais(list[_NFe]):
    def __init__(self, config: Config):
        super().__init__()
        self._config = config

    def add(self, xml=None):
        if xml:
            if isinstance(xml, str):
                xml = xml.replace(' xmlns="http://www.portalfiscal.inf.br/nfe"', '')
                xml = etree.fromstring(xml)
            if xml.tag == 'nfeProc':
                proc = nfeProc()
                proc._read_xml(xml)
                item = _NFe(proc=proc)
                self.append(item)
                return item
            elif xml.tag == 'NFe':
                nfe = NFe()
                nfe._config = self._config
                nfe._read_xml(xml)
                item = _NFe(nfe=nfe)
                self.append(item)
                return item
            raise Exception('Impossível carregar os dados do xml')
        nfe = _NFe(nfe=NFe())
        nfe.NFe._config = self._config
        self.append(nfe)
        return nfe


class NotaFiscal(DocumentoFiscal):
    notas: NotasFiscais[_NFe]

    def __init__(self, xml=None, config: Config = None, tp_emis='1'):
        self.config: Config = config
        self.notas = NotasFiscais(config)
        if xml:
            self.notas.add(xml)
        self.tp_emis = tp_emis

    @property
    def tp_emis(self):
        return self._tp_emis

    @tp_emis.setter
    def tp_emis(self, value):
        self._tp_emis = value
        if value == '6':
            self.config.uf = 'SVC-AN'
        elif value == '7':
            self.config.uf = 'SVC-RS'

    def to_xml(self, doc: NFe=None):
        return doc._xml()

    @property
    def nota(self):
        return self.notas[0]

    def enviar(self, lote: str, sincrono=False):
        # mudar o tipo de emissão da configuração
        svc = Autorizacao(self.config)
        amb = self.config.amb
        for nota in self.notas:
            nf = nota.NFe
            svc.xml.NFe.append(nf)
        svc.xml.idLote = str(lote)
        svc.xml.indSinc = '1' if sincrono else '0'
        svc.executar()
        return svc

    def cancelar(self, justificativa: str, lote, seq="1", cnpjcpf=None, dh=None, chave=None, orgao=None, protocolo=None, amb=2):
        if dh is None:
            dh = datetime.datetime.now()
        assert dh, 'O campo data/hora do evento é obrigatório'
        evento = TEventoCanc()
        evento.versao = '1.00'
        inf = evento.infEvento
        inf.detEvento.xJust = justificativa
        inf.dhEvento = dh
        inf.tpAmb = amb
        inf.nSeqEvento = seq
        inf.tpEvento = '110111'
        inf.detEvento.descEvento = 'Cancelamento'
        inf.detEvento.versao = '1.00'
        inf.CNPJ_CPF = cnpjcpf
        inf.cOrgao = orgao or self.config.orgao
        inf.verEvento = '1.00'
        if chave:
            inf.chNFe = chave
            inf.tpAmb = amb
            inf.detEvento.nProt = protocolo
        elif len(self.notas):
            nota = self.nota
            inf.chNFe = nota.chave
            inf.tpAmb = nota.NFe.infNFe.ide.tpAmb
            inf.detEvento.nProt = nota.nfeProc.protNFe.infProt.nProt
        return self.enviar_evento(lote, evento)

    def enviar_evento(self, lote, evento: TEventoCanc):
        svc = RecepcaoEvento(self.config)
        id_evento = evento.infEvento.Id = 'ID' + evento.infEvento.tpEvento + evento.infEvento.chNFe + str(evento.infEvento.nSeqEvento).zfill(2)
        svc.xml.idLote = lote
        svc.xml.evento.append(evento)
        evento.Signature = self.config.certificado.assinar(etree.fromstring(evento.to_string()), id_evento)
        svc.executar()
        return svc

    def consultar(self, chave=None):
        svc = Consulta(self.config)
        svc.xml.chNFe = chave or self.nota.NFe.chave
        svc.executar()
        return svc

    def consultar_recibo(self, recibo):
        svc = RetAutorizacao(self.config)
        svc.xml.nRec = recibo
        svc.executar()
        return svc

    def inutilizar_nfe(self, orgao=None, ano=None, cnpj=None, mod=55, serie=None, nf_ini=None, nf_fim=None, justificativa=None) -> Inutiliza:
        from brasil.dfe.leiaute.nfe.inutNFe_v400 import inutNFe
        inut = inutNFe()
        if not orgao:
            orgao = self.config.orgao
        ano = str(ano)[-2:]
        inut.infInut.tpAmb = self.config.amb
        inut.infInut.xServ = 'INUTILIZAR'
        inut.infInut.cUF = orgao
        inut.infInut.serie = serie
        inut.infInut.mod = mod
        cnpj = cnpj.zfill(14)
        inut.infInut.CNPJ = cnpj
        inut.infInut.ano = ano
        inut.infInut.nNFIni = nf_ini
        inut.infInut.nNFFin = nf_fim
        inut.infInut.xJust = justificativa
        id = inut.infInut.Id = 'ID' + str(orgao).zfill(2) + ano + cnpj + str(mod).zfill(2) + str(serie).zfill(3) + str(nf_ini).zfill(9) + str(nf_fim).zfill(9)
        # assinar o XML de inutilização
        inut.Signature = self.config.certificado.assinar(inut.to_string(), id)
        svc = Inutiliza(self.config)
        svc.xml = inut
        svc.executar()
        return svc

    def assinar(self):
        for nota in self.notas:
            nota.NFe.assinar()

    def status_servico(self, uf):
        st = StatusServico(self.config)
        st.xml.cUF = uf
        st.executar()
        return st

