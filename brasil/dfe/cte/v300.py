import decimal
import os
from lxml import etree

from brasil.dfe.xsd import Alias
import brasil.dfe.leiaute.cte.cte_v300
from brasil.dfe.leiaute.cte.consStatServCTe_v300 import consStatServCte
from brasil.dfe.leiaute.cte.retConsStatServCTe_v300 import retConsStatServCte
from brasil.dfe.leiaute.cte.consSitCTe_v300 import consSitCTe
from brasil.dfe.leiaute.cte.retConsSitCTe_v300 import retConsSitCTe
from brasil.dfe.leiaute.cte.enviCTe_v300 import enviCTe
from brasil.dfe.leiaute.cte.retEnviCTe_v300 import retEnviCte
from brasil.dfe.leiaute.cte.cteModalRodoviario_v300 import rodo
from brasil.utils.text import remover_acentos


brasil.dfe.leiaute.cte.cte_v300.CTe.infCte.infCTeNorm.infModal._add_to_class('rodo', rodo)


class CTe(brasil.dfe.leiaute.cte.cte_v300.CTe):
    _xmlns = 'http://www.portalfiscal.inf.br/cte'
    schema = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.infCte.infCTeNorm.infModal.versaoModal = '3.00'

    def _validate_schema(self):
        if CTe.schema is None:
            CTe.schema = etree.XMLSchema(
                file=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'schemas', 'cte',
                                  'cte_v3.00.xsd')
            )
        if not self.schema.validate(etree.fromstring(self._xml())):
            return self.schema.error_log.last_error.message

    @property
    def chave(self):
        if self.infCte.Id:
            return self.infCte.Id[3:]

    @chave.setter
    def chave(self, value):
        self.infCte.Id = 'CTe' + value

    @property
    def rodo(self) -> rodo:
        return self.infCte.infCTeNorm.infModal.rodo

    def _prepare(self):
        if isinstance(self.infCte.infCTeNorm.cobr.fat.vLiq, (float, decimal.Decimal)):
            self.infCte.infCTeNorm.cobr.fat.vLiq = '{:.2f}'.format(self.infCte.infCTeNorm.cobr.fat.vLiq)

    def _xml(self, name=None):
        self._prepare()
        return remover_acentos(super()._xml(name)).decode('utf-8')
