import os
from unittest import TestCase

from brasil.dfe.nfe.settings import Config
from brasil.dfe.nfe import NotaFiscal


class NFeTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.config = Config(
            xml_path='./', cert_file=os.environ['CERT_TEST'], cert_senha=os.environ['CERT_PASSWORD'], uf='BA',
        )

    def test_cons_stat(self):
        nf = NotaFiscal(config=self.config)
        st = nf.status_servico(29)
        self.assertTrue(st.ok)
        ret = st.retorno
        self.assertEqual(ret.cStat, '107')
        self.assertEqual(ret.cUF, '29')

