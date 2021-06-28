import decimal
import os
from lxml import etree

from brasil.utils.text import remover_acentos
import brasil.dfe.leiaute.nfe.nfe_v400
from brasil.dfe.leiaute.nfe.procNFe_v400 import nfeProc, TNFe
from brasil.dfe.leiaute.nfe.consStatServ_v400 import consStatServ
from brasil.dfe.leiaute.nfe.retConsStatServ_v400 import retConsStatServ
from brasil.dfe.leiaute.nfe.enviNFe_v400 import enviNFe
from brasil.dfe.leiaute.nfe.retEnviNFe_v400 import retEnviNFe
from brasil.dfe.leiaute.nfe.consReciNFe_v400 import consReciNFe
from brasil.dfe.leiaute.nfe.retConsReciNFe_v400 import retConsReciNFe
from brasil.dfe.leiaute.nfe.consSitNFe_v400 import consSitNFe
from brasil.dfe.leiaute.nfe.retConsSitNFe_v400 import retConsSitNFe


class NFe(brasil.dfe.leiaute.nfe.nfe_v400.NFe):
    _xmlns = 'http://www.portalfiscal.inf.br/nfe'
    schema = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.infNFe.versao = '4.00'
        self.infNFe.emit.CRT = 3

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
            return self.infNFe.Id[3:]

    @chave.setter
    def chave(self, value):
        self.infNFe.ide.cDV = value[-1]
        self.infNFe.Id = 'NFe' + value

    def _xml(self, name=None):
        for i, det in enumerate(self.infNFe.det._list):
            det.nItem = i + 1
        return remover_acentos(super()._xml(name)).decode('utf-8')

