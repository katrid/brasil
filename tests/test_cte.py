import os
from unittest import TestCase

from brasil.dfe.cte.ws import StatusServico, Consulta, Recepcao
from brasil.dfe.cte.settings import Config
from brasil.dfe.cte.cte import CTe


class CTeTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if not os.path.isdir('./temp'):
            os.makedirs('./temp')
        cls.config = Config(
            xml_path='./temp', cert_file=os.environ['CERT_TEST'], cert_senha=os.environ['CERT_PASSWORD'], uf='BA',
            versao='4.00'
        )

    def test_cons_stat(self):
        st = StatusServico(self.config)
        res = st.executar()
        ret = st.retorno
        self.assertEqual(ret.cStat, '107')
        self.assertEqual(ret.cUF, '29')

    # def test_enviar(self):
    #     recep = Recepcao(self.config)
    #     with open(os.environ['CTE_XML_TEST'], 'rb') as f:
    #         cte = CTe()
    #         cte._read_xml(f.read())
    #         recep.xml.CTe.append(cte)
    #
    #     print(recep.xml._xml())
    #     self.assertTrue(recep.executar())
    #     self.assertEqual(recep.retorno.cStat, '100')

    def test_consulta(self):
        consulta = Consulta(self.config)
        consulta.chave = os.environ['CHAVE_CTE_TEST']
        self.assertTrue(consulta.executar())
        self.assertEqual(consulta.retorno.cStat, '100')
