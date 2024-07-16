import decimal

import brasil.dfe.leiaute.nfe.nfe_v400


class NFe(brasil.dfe.leiaute.nfe.nfe_v400.NFe):
    _config = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.infNFe.versao = '4.00'
        self.infNFe.emit.CRT = 3

    def _validate_schema(self, xml=None):
        # if NFe.schema is None:
        #     NFe.schema = etree.XMLSchema(
        #         file=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'schemas', 'nfe',
        #                           'nfe_v4.00.xsd')
        #     )
        # if not self.schema.validate(etree.fromstring(xml or self._xml())):
        #     return self.schema.error_log.last_error.message
        pass

    @property
    def chave(self):
        if self.infNFe.Id:
            return self.infNFe.Id[3:]

    @chave.setter
    def chave(self, value):
        self.infNFe.ide.cDV = value[-1]
        self.infNFe.Id = 'NFe' + value

    def _prepare(self):
        if self.infNFe.ide.tpAmb == '2':
            self.infNFe.dest.xNome = 'NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL'

    def _xml(self, name=None):
        self._prepare()
        for i, det in enumerate(self.infNFe.det):
            det.nItem = i + 1
        return super()._xml(name)

    def assinar(self):
        self._prepare()
        self.Signature = self._config.certificado.assinar(self.to_string(), self.infNFe.Id)
