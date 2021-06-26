import decimal
import os
from lxml import etree

from brasil.utils.text import remover_acentos
import brasil.dfe.leiaute.nfe.nfe_v400


class NFe(brasil.dfe.leiaute.nfe.nfe_v400.NFe):
    _xmlns = 'http://www.portalfiscal.inf.br/nfe'
    schema = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.infNFe.versao = '4.00'

    def _validate_schema(self):
        if NFe.schema is None:
            NFe.schema = etree.XMLSchema(
                file=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'schemas', 'nfe',
                                  'nfe_v4.00.xsd')
            )
        if not self.schema.validate(etree.fromstring(self._xml())):
            return self.schema.error_log.last_error.message

    @property
    def chave(self):
        if self.infNFe.Id:
            return self.infCte.Id[3:]

    @chave.setter
    def chave(self, value):
        self.infNFe.ide.cDV = value[-1]
        self.infNFe.Id = 'NFe' + value

    def _xml(self, name=None):
        return remover_acentos(super()._xml(name)).decode('utf-8')
