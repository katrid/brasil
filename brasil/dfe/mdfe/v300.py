import os
from inspect import get_annotations
from typing import Annotated
from lxml import etree

from brasil.dfe.xsd import Element, XmlProp
import brasil.dfe.leiaute.mdfe.mdfe_v300
import brasil.dfe.leiaute.mdfe.procMDFe_v300
from brasil.dfe.leiaute.mdfe.consStatServMDFe_v300 import consStatServMDFe
from brasil.dfe.leiaute.mdfe.retMDFe_v300 import retMDFe
from brasil.dfe.leiaute.mdfe.retConsStatServMDFe_v300 import retConsStatServMDFe
from brasil.dfe.leiaute.mdfe.consSitMDFe_v300 import consSitMDFe
from brasil.dfe.leiaute.mdfe.retConsSitMDFe_v300 import retConsSitMDFe
from brasil.dfe.leiaute.mdfe.eventoMDFe_v300 import eventoMDFe
from brasil.dfe.leiaute.mdfe.evCancMDFe_v300 import evCancMDFe
from brasil.dfe.leiaute.mdfe.retEventoMDFe_v300 import retEventoMDFe

from brasil.dfe.leiaute.mdfe.distMDFe_v300 import distMDFe
from brasil.dfe.leiaute.mdfe.retDistMDFe_v300 import retDistMDFe
from brasil.dfe.leiaute.mdfe.procMDFe_v300 import mdfeProc

from brasil.dfe.leiaute.mdfe.consReciMDFe_v300 import consReciMDFe
from brasil.dfe.leiaute.mdfe.retConsReciMDFe_v300 import retConsReciMDFe
from brasil.dfe.leiaute.mdfe.retEnviMDFe_v300 import retEnviMDFe
from brasil.dfe.leiaute.mdfe.enviMDFe_v300 import enviMDFe

import brasil.dfe.leiaute.mdfe.mdfeModalRodoviario_v300
import brasil.dfe.leiaute.mdfe.mdfeModalAquaviario_v300
from brasil.utils.text import remover_acentos
# from brasil.dfe.mdfe.validations import MDFeValidator # TODO fazer validacoes


# adicionar modal (não é possível adicionar via interpretação do xsd)
brasil.dfe.leiaute.mdfe.mdfe_v300.MDFe._infMDFe._infModal._props = brasil.dfe.leiaute.mdfe.mdfe_v300.MDFe._infMDFe._infModal._props or {}
brasil.dfe.leiaute.mdfe.mdfe_v300.MDFe._infMDFe._infModal._props['rodo'] = XmlProp('rodo', Annotated[brasil.dfe.leiaute.mdfe.mdfeModalRodoviario_v300.rodo, Element])


class MDFe(brasil.dfe.leiaute.mdfe.mdfe_v300.MDFe):
    _config = None
    _schema = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # atribuir informação de versão
        self.infMDFe.versao = '3.00'
        self.infMDFe.infModal.versaoModal = '3.00'

    def validate(self, config=None):
        self._config = config
        # validator = MDFeValidator(self)
        self._validate_schema()
        # validator.run_validations(_nfe_config=_nfe_config)

    def _validate_schema(self):
        if MDFe._schema is None:
            MDFe._schema = etree.XMLSchema(
                file=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'schemas', 'mdfe',
                                  'mdfe_v3.00.xsd')
            )
        if not self._schema.validate(etree.fromstring(self._xml())):
            return self._schema.error_log.last_error.message

    def _prepare(self):
        if self._config:
            config = self._config
            if self.infMDFe.ide.tpAmb == '2':
                if str(self.infMDFe.ide.tpEmis) == '8' and config.orgao in (31, 41, 50, 51):
                    url = config.services.get('URL-QRCode', config.get_uf_emis(), config.amb)
                else:
                    url = config.services.get('URL-QRCode', config.uf, config.amb)
            else:
                url = config.services.get('URL-QRCode', config.uf, config.amb)
            if '?' not in url:
                url += '?'
            url += f'chMDFe={self.chave}&tpAmb={config.amb}'
            if str(self.infMDFe.ide.tpEmis) == '2':
                url += f'&sign={self._get_sign()}'
            self.infMDFeSupl.qrCodMDFe = f'<![CDATA[{url.replace(" ", "")}]]>'

    def _xml(self, name=None):
        self._prepare()
        return remover_acentos(super()._xml(name)).decode('utf-8')

    @property
    def rodo(self) -> brasil.dfe.leiaute.mdfe.mdfeModalRodoviario_v300.rodo:
        return self.infMDFe.infModal.rodo

    @property
    def aquav(self) -> brasil.dfe.leiaute.mdfe.mdfeModalAquaviario_v300.aquav:
        return self.infMDFe.infModal.aquav

    @property
    def chave(self):
        return self.infMDFe.Id[4:]

    @chave.setter
    def chave(self, value):
        self.infMDFe.ide.cDV = value[-1]
        self.infMDFe.Id = 'MDFe' + value
