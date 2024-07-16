import os

# schemas não constantes na versão 4.00
import brasil.dfe.leiaute.cte.cte_v400
from brasil.dfe.leiaute.cte.procCTe_v400 import cteProc
from brasil.dfe.leiaute.cte.retConsStatServCTe_v400 import retConsStatServCTe
from brasil.dfe.leiaute.cte.consSitCTe_v400 import consSitCTe
from brasil.dfe.leiaute.cte.retConsSitCTe_v400 import retConsSitCTe
from brasil.dfe.leiaute.cte.consStatServCTe_v400 import consStatServCTe
from brasil.dfe.leiaute.cte.enviCTe_v300 import enviCTe
from brasil.dfe.leiaute.cte.retEnviCTe_v300 import retEnviCte
from brasil.dfe.leiaute.cte.eventoCTe_v400 import eventoCTe
from brasil.dfe.leiaute.cte.retEventoCTe_v400 import retEventoCTe
from brasil.dfe.leiaute.cte.distDFeInt_v100 import distDFeInt
from brasil.dfe.leiaute.cte.retDistDFeInt_v100 import retDistDFeInt
from brasil.dfe.leiaute.cte.consReciCTe_v300 import consReciCTe
from brasil.dfe.leiaute.cte.retConsReciCTe_v300 import retConsReciCTe
from brasil.dfe.leiaute.cte.retCTe_v400 import retCTe
from brasil.dfe.leiaute.cte.evCancCTe_v400 import evCancCTe
from brasil.dfe.leiaute.cte.cteModalRodoviario_v400 import rodo
from brasil.utils.text import remover_acentos


class CTe(brasil.dfe.leiaute.cte.cte_v400.CTe):
    _config = None
    _schema = None

    # def validate(self, _nfe_config=None):
    #     self._nfe_config = _nfe_config
    #     validator = CTeValidator(self)
    #     self._validate_schema()
    #     validator.run_validations(_nfe_config=_nfe_config)
    #
    def _validate_schema(self):
        # if CTe.schema is None:
        #     CTe.schema = etree.XMLSchema(
        #         file=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'schemas', 'cte',
        #                           'cte_v4.00.xsd')
        #     )
        # xml = self._xml()
        # if not self.schema.validate(etree.fromstring(xml)):
        #     return self.schema.error_log.last_error.message
        pass

    @property
    def rodo(self) -> rodo:
        return self.infCte.infCTeNorm.infModal.rodo
    
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

    def to_string(self):
        self._prepare()
        return super().to_string()

    @property
    def chave(self):
        return self.infCte.Id[3:]
