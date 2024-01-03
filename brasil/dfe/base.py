import os
import sys
import inspect
import brasil


class DocumentoFiscal:
    pdf_output_path = '.'


class Validator:
    documento = None
    mensagem = None
    codigo = None
    _nfe_config = None

    def __init__(self) -> None:
        self.validation_list = self.ValidationList()
        self.validation_list.documento = self.documento
        self.validation_list.validator = self

    @property
    def validations(self):
        attrs = [getattr(self.validation_list, attr) for attr in dir(self.validation_list)]
        return filter(lambda x: inspect.ismethod(x) and x.__name__.startswith('validate'), attrs)

    def run_validations(self, _nfe_config=None):
        self._nfe_config = _nfe_config
        for validation in self.validations:
            try:
                validation()
            except AssertionError as e:
                raise AssertionError(self.mensagem + '\n' + str(e))
            
    class ValidationList:
        documento = None
        validator = None