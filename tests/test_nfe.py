"""
Para rodar os testes, é necessário obter um certificado de teste através do script test-pfxgen.sh
"""
import os
import datetime
from unittest import TestCase

from brasil.dfe.nfe.settings import Config
from brasil.dfe.nfe import NotaFiscal
from brasil.dfe.leiaute.nfe.nfe_v400 import NFe
from brasil.dfe.utils.dfe_utils import gerar_chave_acesso


class NFeTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Gerar o pfx com a senha 12345678
        cls.pfx_password = '12345678'
        # gerar os xmls de teste na pasta ./xml
        cls.xml_path = './xml'
        cls.config = Config(
            xml_path=cls.xml_path, cert_file='./test.pfx', cert_senha=cls.pfx_password, uf='BA',
        )
        if not os.path.isdir(cls.xml_path):
            os.mkdir(cls.xml_path)

    def _test_cons_stat(self):
        nf = NotaFiscal(config=self.config)
        st = nf.status_servico(29)
        self.assertTrue(st.ok)
        ret = st.retorno
        self.assertEqual(ret.cStat, '107')
        self.assertEqual(ret.cUF, '29')

    def test_leiaute(self):
        # gerar xml
        nfe = NFe()
        nfe.infNFe.ide.cUF = '29'
        self.assertEqual(nfe._xml(), '<NFe xmlns="http://www.portalfiscal.inf.br/nfe"><infNFe><ide><cUF>29</cUF></ide></infNFe></NFe>')
        nfe.infNFe.emit.xNome = 'EMPRESA TESTE'
        self.assertEqual(nfe._xml(), '<NFe xmlns="http://www.portalfiscal.inf.br/nfe"><infNFe><ide><cUF>29</cUF></ide><emit><xNome>EMPRESA TESTE</xNome></emit></infNFe></NFe>')
        # ler xml
        nfe2 = NFe.fromstring('<NFe xmlns="http://www.portalfiscal.inf.br/nfe"><infNFe><ide><cUF>29</cUF></ide><emit><xNome>EMPRESA TESTE</xNome></emit></infNFe></NFe>')
        self.assertEqual(nfe2._xml(), '<NFe xmlns="http://www.portalfiscal.inf.br/nfe"><infNFe><ide><cUF>29</cUF></ide><emit><xNome>EMPRESA TESTE</xNome></emit></infNFe></NFe>')
        # preencher e assinar xml
        nfe.infNFe.emit.CNPJ_CPF = '12345678901234'
        nfe.infNFe.ide.dhEmi = datetime.datetime.now()
        nfe.infNFe.Id = 'NFe' + gerar_chave_acesso(
            nfe.infNFe.ide.cUF, nfe.infNFe.ide.dhEmi, nfe.infNFe.emit.CNPJ_CPF, 1, 1, 1, 55, 55
        )
        nfe.Signature = self.config.certificado.assinar(nfe.to_string(), nfe.infNFe.Id)
        xml = nfe.to_string()
        nfe2 = NFe.fromstring(xml)
        # o conteúdo do xml precisa ser preservado
        self.assertEqual(nfe2.to_string(), xml)
