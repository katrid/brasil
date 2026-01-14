import os
from unittest import TestCase

from brasil.bancos.ofx.parser import OfxParser


class OfxTestCase(TestCase):
    def test_parser(self):
        with open(os.path.join(os.path.dirname(__file__), 'samples', 'bradesco.ofx'), 'rb') as f:
            ofx_parser = OfxParser()
            doc = ofx_parser.parse(f)
        self.assertEqual(doc.header['OFXHEADER'], '100')
        self.assertEqual(doc.header['VERSION'], '102')
        self.assertEqual(len(doc.body['BANKMSGSRSV1']['STMTTRNRS']['STMTRS']['BANKTRANLIST']['STMTTRN']), 110)
