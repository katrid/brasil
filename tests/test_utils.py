from datetime import datetime
from unittest import TestCase
from brasil.dfe.utils import gerar_codigo, gerar_chave_acesso
from brasil.utils.formulas import modulo11


class UtilsTestCase(TestCase):
    def test_gera_codigo(self):
        num = 99
        for i in range(100):
            cod = gerar_codigo(num)
            self.assertNotEqual(num, cod)
            num += i

    def test_gera_chave(self):
        for num in range(99, 199):
            chave = gerar_chave_acesso(29, datetime.now(), '99999999999999', 1, num, 1, gerar_codigo(num), 65)
            self.assertEqual(len(chave), 44)
