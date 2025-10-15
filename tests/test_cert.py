import os
from unittest import TestCase

from brasil.dfe.utils.certs import Certificado


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class CertTestCase(TestCase):
    def test_cert(self):
        with open(os.path.join(BASE_DIR, 'test.pfx'), 'rb') as f:
            cert = Certificado(f.read(), '12345678')

        xml = '<test><assinar Id="id-assinar"></assinar></test>'
        xml_signature = cert.assinar(xml, 'id-assinar')
        self.assertIsNotNone(xml_signature)

        # invalid password
        cert = Certificado(cert.pfx, 'wrong-password')
        with self.assertRaises(ValueError):
            cert.assinar(xml, 'id-assinar')
