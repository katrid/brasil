from typing import List

from brasil.utils.parser import Parser, XsBaseElement, XsElement


class Compiler(Parser):
    _skipped_items: List[XsBaseElement] = None

    def precompile_element(self, element: XsBaseElement):
        if not self._skipped_items:
            self._skipped_items = []
        if isinstance(element, XsElement) and element.process_contents == 'skip' and element not in self._skipped_items:
            self._skipped_items.append(element)
            self.prepare_skipped(element)

    def prepare_skipped(self, element: XsElement):
        """
        Objetos marcados como skip precisam ter tratamento especial durante a compilação
        :param element:
        :return:
        """
         # TODO adicionar classes diferentes para versões diferentes
        if self.schema.name == 'consSitMDFeTiposBasico_v3.00.xsd':
            parent = element.parent
            if parent and parent.parent and parent.parent.name == 'protMDFe':
                # forçar compilação na versão 3.00
                parent.parent.type = 'TProtMDFe'
                self.schema.includes.append('procMDFe_v3.00.xsd')
        elif self.schema.name == 'consSitCTeTiposBasico_v3.00.xsd':
            parent = element.parent
            if parent and parent.parent and parent.parent.name == 'protCTe':
                # forçar compilação na versão 3.00
                parent.parent.type = 'TProtCTe'
                self.schema.includes.append('procCTe_v3.00.xsd')
        elif self.schema.name == 'consSitCTeTiposBasico_v4.00.xsd':
            parent = element.parent
            if parent and parent.parent and parent.parent.name == 'protCTe':
                # forçar compilação na versão 4.00
                parent.parent.type = 'TProtCTe'
                self.schema.includes.append('procCTe_v4.00.xsd')
        elif self.schema.name == 'eventoCTeTiposBasico_v2.00.xsd':
            parent = element.parent
            if parent and parent.name == '_detEvento':
                # lista de eventos
                parent.sequence = [XsElement(name='evPrestDesacordo', base='evPrestDesacordo')]
                self.schema.includes.append('evPrestDesacordo_v2.00.xsd')
        elif self.schema.name == 'eventoCTeTiposBasico_v3.00.xsd':
            parent = element.parent
            if parent and parent.name == '_detEvento':
                # lista de eventos
                parent.sequence = [
                    XsElement(name='evPrestDesacordo', base='evPrestDesacordo'),
                    XsElement(name='evCancCTe', base='evCancCTe'),
                ]
                if 'evPrestDesacordo_v3.00.xsd' not in self.schema.includes:
                    self.schema.includes.append('evPrestDesacordo_v3.00.xsd')
                    self.schema.includes.append('evCancCTe_v3.00.xsd')
        elif self.schema.name == 'eventoCTeTiposBasico_v4.00.xsd':
            parent = element.parent
            if parent and parent.name == '_detEvento':
                # lista de eventos
                parent.sequence = [
                    XsElement(name='evPrestDesacordo', base='evPrestDesacordo'),
                    XsElement(name='evCancCTe', base='evCancCTe'),
                ]
                if 'evPrestDesacordo_v4.00.xsd' not in self.schema.includes:
                    self.schema.includes.append('evPrestDesacordo_v4.00.xsd')
                    self.schema.includes.append('evCancCTe_v4.00.xsd')
        elif self.schema.name == 'eventoMDFeTiposBasico_v3.00.xsd':
            parent = element.parent
            if parent and parent.name == '_detEvento':
                # lista de eventos
                parent.sequence = [
                    XsElement(name='evEncMDFe', base='evEncMDFe'),
                    XsElement(name='evCancMDFe', base='evCancMDFe'),
                ]
                if 'evEncMDFe_v3.00.xsd' not in self.schema.includes:
                    self.schema.includes.append('evEncMDFe_v3.00.xsd')
                    self.schema.includes.append('evCancMDFe_v3.00.xsd')
        elif self.schema.name == 'cteTiposBasico_v2.00.xsd':
            parent = element.parent
            if parent and parent.name == '_infModal':
                # TODO implementar os demais
                parent.sequence = [
                    XsElement(name='rodo', base='rodo'),
                    XsElement(name='aquav', base='aquav'),
                ]
                if 'cteModalRodoviario_v2.00.xsd' not in self.schema.post_includes:
                    self.schema.post_includes.append('cteModalRodoviario_v2.00.xsd')
                    self.schema.post_includes.append('cteModalAquaviario_v2.00.xsd')
        elif self.schema.name == 'cteTiposBasico_v3.00.xsd':
            parent = element.parent
            if parent and parent.name == '_infModal':
                # TODO implementar os demais
                parent.sequence = [
                    XsElement(name='rodo', base='rodo'),
                    XsElement(name='aquav', base='aquav'),
                ]
                if 'cteModalRodoviario_v3.00.xsd' not in self.schema.post_includes:
                    self.schema.post_includes.append('cteModalRodoviario_v3.00.xsd')
                    self.schema.post_includes.append('cteModalAquaviario_v3.00.xsd')
        elif self.schema.name == 'cteTiposBasico_v4.00.xsd':
            parent = element.parent
            if parent and parent.name == '_infModal':
                # TODO implementar os demais
                parent.sequence = [
                    XsElement(name='rodo', base='rodo'),
                    XsElement(name='aquav', base='aquav'),
                ]
                if 'cteModalRodoviario_v4.00.xsd' not in self.schema.post_includes:
                    self.schema.post_includes.append('cteModalRodoviario_v4.00.xsd')
                    self.schema.post_includes.append('cteModalAquaviario_v4.00.xsd')
        elif self.schema.name == 'leiauteDistMDFe_v3.00.xsd':
            parent = element.parent
            if parent and parent.name == '_infMDFe':
                parent.sequence = [
                    XsElement(name='chMDFe', base='TChMDFe'),
                ]
        elif self.schema.name == 'mdfeTiposBasico_v3.00.xsd':
            parent = element.parent
            if parent and parent.name == '_infMDFe':
                parent.sequence = [
                    XsElement(name='chMDFe', base='TChMDFe'),
                ]
        else:
            print(f"Skipping {element.parent.name} in {self.schema.name}")


def convert_dir(dirname: str):
    parser = Compiler()
    parser.compile_dir(dirname)
    return parser
