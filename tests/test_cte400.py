import datetime
from unittest import TestCase
import base64
import gzip

from brasil.dfe.cte.cte400 import Conhecimento, CTeSimp, Config
from brasil.dfe.utils.dfe_utils import gerar_codigo
from brasil.dfe.cte.ws import Recepcao


class CTeTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.xml_path = './xml'
        cls.pfx_password = '12345678'
        cls.config = Config(
            xml_path=cls.xml_path, cert_file='./test.pfx', cert_senha=cls.pfx_password, uf='BA',
        )

    def test_cte_simp(self):
        cte = CTeSimp()
        xml = cte.to_string()
        # xml não preenchido
        self.assertFalse(xml)
        cte.infCte.ide.cUF = '29'
        # verificar se o qualquer alteração no cte reflete no xml
        xml = cte.to_string()
        self.assertEqual(xml, '<CTeSimp xmlns="http://www.portalfiscal.inf.br/cte"><infCte><ide><cUF>29</cUF></ide></infCte></CTeSimp>')
        # testar geração da chave
        cte.infCte.ide.nCT = '1'
        cte.infCte.ide.tpEmis = '1'
        cte.infCte.ide.dhEmi = datetime.datetime.now()
        cte.infCte.ide.tpCTe = '4'
        cte.infCte.emit.CNPJ_CPF = '12345678901234'
        cte.infCte.ide.tpAmb = '1'
        cte.infCte.ide.serie = '1'
        cte.infCte.ide.mod = '57'
        cte.infCte.ide.cCT = str(gerar_codigo(cte.infCte.ide.nCT))
        # chave deve ser gerada automaticamente
        chave1 = cte.chave
        cte.gerar_chave()
        chave = cte.chave
        self.assertEqual(chave, chave1)  # chave deve ser a mesma
        # o conhecimento deve introduzir as configurações necessárias para gerar as tags de especiais (qrcode)
        conhecimento = Conhecimento(cte=cte, config=self.config)
        xml = cte.to_string()
        self.assertIn('<qrCodCTe>', xml)

        # verificar det
        det = cte.infCte.det.add()
        det.nItem = 1
        det.vPrest = 100
        xml = cte.to_string()
        self.assertIn('<det nItem="1">', xml)

        # testar assinatura
        cte.Signature = self.config.certificado.assinar(cte.to_string(), cte.infCte.Id)
        self.assertIn('<Signature xmlns="http://www.w3.org/2000/09/xmldsig#">', cte.to_string())

        # testar envelope
        xml = cte.to_string()
        ws = Recepcao(self.config)
        ws.xml = cte
        bxml = ws.envelope()
        self.assertTrue(bxml.startswith(b'<?xml'))
        # objeto precisa estar compactado
        bxml = bxml.split(b'<soap12:Body><cteDadosMsg xmlns="http://www.portalfiscal.inf.br/cte/wsdl/CTeRecepcaoSincV4">', 1)[1]
        bxml = bxml.split(b'</cteDadosMsg></soap12:Body>', 1)[0]
        bxml = gzip.decompress(base64.decodebytes(bxml)).decode('utf-8')
        # o conteúdo do xml precisa ser preservado
        self.assertEqual(bxml, xml)

    def test_consulta(self):
        pass
