import datetime

from lxml import etree

from brasil.utils.text import remover_acentos
from .settings import Config
from .v400 import CTe, cteProc, CTeSimp
from .ws import Recepcao, Consulta, RetornoRecepcao, RecepcaoEvento, eventoCTe
from ..base import DocumentoFiscal


class _CTe:
    CTe: CTe = None
    CTeSimp: CTeSimp = None
    cteProc: cteProc = None

    def __init__(self, cte=None, proc=None, cte_simp=None):
        if cte:
            self.CTe = cte
        elif proc:
            self.cteProc = proc
            self.CTe = self.cteProc.CTe
        elif cte_simp:
            self.CTeSimp = cte_simp

    @property
    def chave(self):
        if self.CTeSimp is not None:
            return self.CTeSimp.infCte.Id[3:]
        return self.CTe.infCte.Id[3:]

    @chave.setter
    def chave(self, value):
        if self.CTe is not None:
            self.CTe.infCte.Id = 'CTe' + value
            self.CTe.infCte.ide.cDV = value[-1]
        elif self.CTeSimp is not None:
            self.CTeSimp.infCte.Id = 'CTe' + value
            self.CTeSimp.infCte.ide.cDV = value[-1]

    @property
    def rodo(self):
        return self.CTe.infCte.infCTeNorm.infModal.rodo

    @property
    def aquav(self):
        return self.CTe.infCte.infCTeNorm.infModal.aquav

    def to_xml(self):
        if self.CTe is not None:
            return self.CTe._xml()
        elif self.CTeSimp is not None:
            return self.CTeSimp._xml()
        elif self.cteProc is not None:
            return self.cteProc._xml()
        return None


class Conhecimentos(list):
    """Classe com um conjunto de utilitários para lidar com uma lista de ct-e"""

    def __init__(self, config):
        super().__init__()
        self._config = config

    def add(self, xml: str = None, simplificado=False):
        """
        Adiciona um CTe a lista de conhecimentos
        :param xml:
        :param simplificado: indica se o CTe é simplificado
        :return:
        """
        if xml:
            xml = etree.fromstring(xml)
            if xml.tag == '{http://www.portalfiscal.inf.br/cte}cteProc':
                proc = cteProc()
                proc._read_xml(xml)
                item = _CTe(proc=proc)
                self.append(item)
                return item
            elif xml.tag == '{http://www.portalfiscal.inf.br/cte}CTe':
                cte = CTe()
                cte._config = self._config
                cte._read_xml(xml)
                item = _CTe(cte=cte)
                self.append(item)
                return item
            raise Exception('Impossível carregar os dados do xml')
        if simplificado:
            cte = _CTe(cte_simp=CTeSimp())
            # automaticamente versão 4.00
            cte.CTeSimp.infCte.versao = '4.00'
            cte._config = self._config
            self.append(cte)
            return cte
        else:
            cte = _CTe(cte=CTe())
            # automaticamente versão 4.00
            cte.CTe.infCte.versao = '4.00'
            cte.CTe.infCte.infCTeNorm.infModal.versaoModal = '4.00'
            cte.CTe._config = self._config
            self.append(cte)
            return cte


class Conhecimento(DocumentoFiscal):
    conhecimentos: Conhecimentos

    def __init__(self, xml=None, config: Config = None):
        self.config: Config = config
        self.conhecimentos = Conhecimentos(config)
        if xml:
            self.conhecimentos.add(xml)

    def to_xml(self, doc: CTe | CTeSimp = None):
        return doc.to_string()

    def enviar(self):
        svc = Recepcao(self.config)
        svc.xml = self.conhecimento.CTe
        svc.executar()
        return svc

    @property
    def conhecimento(self):
        return self.conhecimentos[0]

    def from_xml(self, xml: str):
        doc = etree.fromstring(xml)
        doc.tag.endswith('cteProc')

    def consultar(self, chave: str) -> RetornoRecepcao:
        svc = Consulta(self.config)
        svc.chave = chave
        svc.executar()
        return svc

    def cancelar(
            self, justificativa: str, lote, seq="1", cnpjcpf: str = None, dh=None, chave=None, orgao=None,
            protocolo=None, amb=2
    ) -> RecepcaoEvento:
        if dh is None:
            dh = datetime.datetime.now()
        evento = eventoCTe()
        inf = evento.infEvento
        inf.tpEvento = '110111'
        # inf.detEvento.evCancCTe = evCancCTe()
        inf.detEvento.evCancCTe.xJust = remover_acentos(justificativa).decode('utf-8')
        inf.dhEvento = dh
        inf.tpAmb = amb
        inf.nSeqEvento = seq
        cnpjcpf = ''.join(filter(str.isdigit, cnpjcpf))
        if len(cnpjcpf) == 11:
            inf.CPF = cnpjcpf
        else:
            inf.CNPJ = cnpjcpf
        inf.cOrgao = orgao or self.config.orgao
        if chave:
            inf.chNFe = chave
            inf.tpAmb = amb
            inf.detEvento.evCancCTe.nProt = protocolo
        elif len(self.conhecimentos):
            nota = self.conhecimento
            inf.chCTe = nota.chave
            inf.tpAmb = self.config.amb
            inf.detEvento.evCancCTe.nProt = nota.cteProc.protCTe.infProt.nProt
        return self.enviar_evento(lote, evento)

    def enviar_evento(self, lote, evento):
        svc = RecepcaoEvento(self.config)
        id_evento = evento.infEvento.Id
        if not id_evento:
            id_evento = evento.infEvento.Id = 'ID' + evento.infEvento.tpEvento + evento.infEvento.chCTe + str(
                evento.infEvento.nSeqEvento).zfill(3)
        evento.idLote = lote
        svc.xml = evento
        xml = evento._xml()
        evento.Signature = self.config.certificado.assinar(xml, id_evento)
        svc.executar()
        return svc

    def validar_assinatura(self):
        self.config.certificado.verificar_assinatura(self.conhecimento.to_xml())
