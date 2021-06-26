import os
from unittest import TestCase
from brasil.utils.xsd2py import convert_dir, get_module


class ConverterTestCase(TestCase):
    def test_convert_nfe(self):
        res = convert_dir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'schemas', 'nfe'))
        base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'brasil', 'dfe', 'leiaute', 'nfe')
        for filename, content in res.items():
            filename = get_module(filename)
            print(os.path.join(base_dir, filename + '.py'))
            with open(os.path.join(base_dir, filename + '.py'), 'w') as f:
                f.write(content)

    def test_convert_cte(self):
        res = convert_dir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'schemas', 'cte'))
        base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'brasil', 'dfe', 'leiaute', 'cte')
        for filename, content in res.items():
            filename = get_module(filename)
            print(os.path.join(base_dir, filename + '.py'))
            with open(os.path.join(base_dir, filename + '.py'), 'w') as f:
                f.write(content)
