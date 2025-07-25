import os
from unittest import TestCase

from brasil.utils.parser import Parser
from brasil.utils.xsd2py import convert_dir


class ParserTestCase(TestCase):
    def _test_parse(self):
        xsd_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'schemas', 'nfe', 'retDistDFeInt_v1.01.xsd')
        parser = Parser()
        parser.fromfile(xsd_filename)
        parser.compile()
        schema = parser.schemas['retDistDFeInt_v1.01.xsd']
        schema.to_python()
        xsd_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'schemas', 'nfe', 'leiauteNFe_v4.00.xsd')
        parser = Parser()
        parser.fromfile(xsd_filename)
        parser.compile()
        schema = parser.schemas['leiauteNFe_v4.00.xsd']
        schema.to_python()

    def _test_convert_nfe(self):
        parser = convert_dir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'schemas', 'nfe'))
        base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'brasil', 'dfe', 'leiaute', 'nfe')
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        for m in parser.schemas.values():
            with open(os.path.join(base_dir, m.module_name + '.py'), 'w') as f:
                f.write(m.to_python())

        # for filename, content in res.items():
        #     filename = get_module(filename)
        #     print(os.path.join(base_dir, filename + '.py'))
        #     with open(os.path.join(base_dir, filename + '.py'), 'w') as f:
        #         f.write(content)

    def test_convert_cte(self):
        parser = convert_dir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'schemas', 'cte'))
        base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'brasil', 'dfe', 'leiaute', 'cte')
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        for m in parser.schemas.values():
            with open(os.path.join(base_dir, m.module_name + '.py'), 'w') as f:
                f.write(m.to_python())

    def _test_convert_mdfe(self):
        parser = convert_dir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'schemas', 'mdfe'))
        base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'brasil', 'dfe', 'leiaute', 'mdfe')
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        for m in parser.schemas.values():
            with open(os.path.join(base_dir, m.module_name + '.py'), 'w') as f:
                f.write(m.to_python())

    def _test_convert_cte(self):
        res = convert_dir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'schemas', 'cte'))
        base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'brasil', 'dfe', 'leiaute', 'cte')
        for filename, content in res.items():
            filename = get_module(filename)
            print(os.path.join(base_dir, filename + '.py'))
            with open(os.path.join(base_dir, filename + '.py'), 'w') as f:
                f.write(content)
