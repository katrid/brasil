import os
from typing import Annotated

from lxml import etree

from brasil.dfe.xsd import Element
from brasil.dfe.leiaute.cte.cte_v400 import CTe as CTe400
from brasil.dfe.leiaute.cte.cteSimp_v400 import CTeSimp as CTeSimp400, TCTeSimp  # noqa
from brasil.dfe.leiaute.cte.cteModalRodoviario_v400 import rodo
from brasil.dfe.leiaute.cte.procCTe_v400 import cteProc  # noqa
from brasil.dfe.leiaute.cte.retConsStatServCTe_v400 import retConsStatServCTe  # noqa
from brasil.dfe.leiaute.cte.consSitCTe_v400 import consSitCTe  # noqa
from brasil.dfe.leiaute.cte.retConsSitCTe_v400 import retConsSitCTe  # noqa
from brasil.dfe.leiaute.cte.consStatServCTe_v400 import consStatServCTe  # noqa
from brasil.dfe.leiaute.cte.enviCTe_v300 import enviCTe  # noqa
from brasil.dfe.leiaute.cte.retEnviCTe_v300 import retEnviCte  # noqa
from brasil.dfe.leiaute.cte.eventoCTe_v400 import eventoCTe  # noqa
from brasil.dfe.leiaute.cte.retEventoCTe_v400 import retEventoCTe  # noqa
from brasil.dfe.leiaute.cte.distDFeInt_v100 import distDFeInt  # noqa
from brasil.dfe.leiaute.cte.retDistDFeInt_v100 import retDistDFeInt  # noqa
from brasil.dfe.leiaute.cte.consReciCTe_v300 import consReciCTe  # noqa
from brasil.dfe.leiaute.cte.retConsReciCTe_v300 import retConsReciCTe  # noqa
from brasil.dfe.leiaute.cte.retCTe_v400 import retCTe  # noqa
from brasil.dfe.leiaute.cte.retCTeSimp_v400 import retCTeSimp  # noqa
from brasil.dfe.leiaute.cte.evCancCTe_v400 import evCancCTe  # noqa
from brasil.dfe.leiaute.cte.evCCeCTe_v400 import evCCeCTe  # noqa
from brasil.utils.text import remover_acentos  # noqa
from brasil.dfe.utils.dfe_utils import gerar_chave_acesso, gerar_codigo


class CTeMixin:
    _schema = None
    _config = None
    _xsd_file: str = None
    infCte: CTe400._infCte

    def gerar_chave(self):
        """
        Gerar a chave de acesso do CTe
        :return:
        """
        self._validar_chave()
        if self.infCte.ide.cCT is None:
            self.infCte.ide.cCT = gerar_codigo(self.infCte.ide.nCT)
        self.chave = gerar_chave_acesso(
            self.infCte.ide.cUF,
            self.infCte.ide.dhEmi,
            self.infCte.emit.CNPJ_CPF,
            self.infCte.ide.serie,
            self.infCte.ide.nCT,
            self.infCte.ide.tpEmis,
            self.infCte.ide.cCT,
            self.infCte.ide.mod,
        )

    def _validar_chave(self):
        ide = self.infCte.ide
        emit = self.infCte.emit
        assert ide.cUF, 'CTe: O campo cUF é obrigatório'
        assert ide.dhEmi, 'CTe: O campo dhEmi é obrigatório'
        assert emit.CNPJ_CPF, 'CTe: O campo CNPJ_CPF do emitente é obrigatório'
        assert ide.serie is not None, 'CTe: O campo serie é obrigatório'
        assert ide.nCT, 'CTe: O campo nCT é obrigatório'
        assert ide.tpEmis, 'CTe: O campo tpEmis é obrigatório'
        assert ide.mod, 'CTe: O campo mod é obrigatório'

    def _prepare(self):
        if self._config:
            config = self._config
            if self.infCte.ide.tpAmb == '2':
                if str(self.infCte.ide.tpEmis) == '8' and config.orgao in (31, 41, 50, 51):
                    url = config.services.get('URL-QRCode', config.get_uf_emis(), config.amb)
                else:
                    url = config.services.get('URL-QRCode', config.uf, config.amb)
            else:
                url = config.services.get('URL-QRCode', config.uf, config.amb)
            if '?' not in url:
                url += '?'
            url += f'chCTe={self.chave}&tpAmb={config.amb}'
            self.infCTeSupl.qrCodCTe = f'<![CDATA[{url.replace(" ", "")}]]>'

    @property
    def chave(self):
        if self.infCte.Id is None:
            self.gerar_chave()
        return self.infCte.Id[3:]

    @chave.setter
    def chave(self, value):
        self.infCte.Id = 'CTe' + value
        self.infCte.ide.cDV = value[-1]

    def _validate_schema(self):
        if self.__class__._schema is None:  # cache schema validation
            self.__class__._schema = etree.XMLSchema(
                file=os.path.join(
                    os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'schemas', 'cte', self._xsd_file,
                )
            )
        xml = self.to_string()
        if not self._schema.validate(etree.fromstring(xml)):
            return self._schema.error_log.last_error.message


class CTe(CTe400, CTeMixin):
    _xsd_file = 'cte_v4.00.xsd'

    # Redefinindo a classe infCte para adicionar o modal rodo
    # não vem automaticamente através do xsd
    class _infCte(CTe400._infCte):
        class _infCTeNorm(CTe400._infCte._infCTeNorm):
            class _infModal(CTe400._infCte._infCTeNorm._infModal):
                rodo: rodo = None
                # TODO implementar demais modais

            _infModal.versaoModal = '4.00'
            infModal: Annotated[_infModal, Element] = None

        infCTeNorm: Annotated[_infCTeNorm, Element] = None

    _infCte.versao = '4.00'
    infCte: Annotated[_infCte, Element] = None

    @property
    def rodo(self) -> rodo:
        """
        Atalho para o modal rodoviário em infCte.infCTeNorm.infModal.rodo
        :return:
        """
        if self.infCte.infCTeNorm.infModal.rodo is None:
            self.infCte.infCTeNorm.infModal.rodo = rodo()
        return self.infCte.infCTeNorm.infModal.rodo

    def to_string(self):
        self._prepare()  # preparar tags especiais antes de gerar o xml
        return super().to_string()


class CTeSimp(CTeSimp400, CTeMixin):
    _xsd_file = 'cteSimp_v4.00.xsd'

    # Redefinindo a classe infCte para adicionar o modal rodo
    # não vem automaticamente através do xsd
    class _infCte(CTeSimp400._infCte):
        class _infModal(CTeSimp400._infCte._infModal):
            rodo: rodo = None
            # TODO implementar demais modais

        _infModal.versaoModal = '4.00'
        infModal: Annotated[_infModal, Element] = None

    _infCte.versao = '4.00'
    infCte: Annotated[_infCte, Element] = None

    @property
    def rodo(self) -> rodo:
        """
        Atalho para o modal rodoviário em infCte.infModal.rodo
        :return:
        """
        if self.infCte.infModal.rodo is None:
            self.infCte.infModal.rodo = rodo()
        return self.infCte.infModal.rodo

    def to_string(self):
        self._prepare()  # preparar tags especiais antes de gerar o xml
        return super().to_string()
