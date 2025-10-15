import os
from unittest import TestCase

from brasil.dfe.mdfe.v300 import MDFe
from brasil.dfe.mdfe import Manifesto


class ManifestoTestCase(TestCase):
    def test_manifesto(self):
        pass

    def test_mdfe(self):
        mdfe = MDFe()
        mdfe.infMDFe.ide.cUF = '35'
        self.assertEqual(mdfe._xml(), '''<MDFe xmlns="http://www.portalfiscal.inf.br/mdfe"><infMDFe versao="3.00"><ide><cUF>35</cUF></ide></infMDFe></MDFe>''')
        rodo = mdfe.rodo
        rodo.veicReboque.add().placa = 'ABC1234'
        self.assertEqual(mdfe._xml(), '''<MDFe xmlns="http://www.portalfiscal.inf.br/mdfe"><infMDFe versao="3.00"><ide><cUF>35</cUF></ide><infModal versaoModal="3.00"><rodo><veicReboque><placa>ABC1234</placa></veicReboque></rodo></infModal></infMDFe></MDFe>''')
        descarga = mdfe.infMDFe.infDoc.infMunDescarga.add('2919553', 'LUIS EDUARDO MAGALHAES')
        self.assertEqual(descarga._xml('infMunDescarga'), '''<infMunDescarga><cMunDescarga>2919553</cMunDescarga><xMunDescarga>LUIS EDUARDO MAGALHAES</xMunDescarga></infMunDescarga>''')

    def test_chave(self):
        chave = '29999999999999999999999999999999999999999999'
        mdfe = MDFe()
        mdfe.chave = chave
        self.assertEqual(mdfe._xml(), '''<MDFe xmlns="http://www.portalfiscal.inf.br/mdfe"><infMDFe versao="3.00" Id="MDFe29999999999999999999999999999999999999999999"><ide><cDV>9</cDV></ide></infMDFe></MDFe>''')
        self.assertEqual(mdfe.chave, chave)
