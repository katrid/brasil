from datetime import date
from decimal import Decimal
from unittest import TestCase

from brasil.sped.fiscal import RegistroE110, Registro0200, RegistroE100


class RegistroTestCase(TestCase):
    def test_registro(self):
        reg = RegistroE110()
        reg.VL_TOT_AJ_DEBITOS = 0
        reg.VL_TOT_DEBITOS = Decimal('3')
        reg.VL_TOT_CREDITOS = 3.00
        reg0200 = Registro0200()
        reg0200.ALIQ_ICMS = 3.00
        regE100 = RegistroE100()
        regE100.DT_INI = date.today()
        regE100.DT_FIN = date.today()
