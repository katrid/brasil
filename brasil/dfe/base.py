import os
import sys
import brasil


class DocumentoFiscal:
    _path_pdf_lib = os.path.join(os.path.dirname(os.path.abspath(brasil.__file__)), '..', 'pdf', 'lib')
    _pdf_lib = None
    pdf_output_path = '.'

    @property
    def pdf_lib(self):
        from ctypes import cdll, c_char_p
        if sys.platform == 'win32':
            lib_name = os.path.join(self._path_pdf_lib, 'acbrpdf.dll')
        else:
            lib_name = os.path.join(self._path_pdf_lib, 'libacbrpdf.so')
        self._pdf_lib = cdll.LoadLibrary(lib_name)
        self._pdf_lib.setPdfPath.argtypes = [c_char_p]
        self._pdf_lib.setPdfPath(self.pdf_output_path.encode('utf-8'))
        self._pdf_lib.nfePdf.argtypes = [c_char_p]
        self._pdf_lib.nfeEventoPdf.argtypes = [c_char_p]
        self._pdf_lib.ctePdf.argtypes = [c_char_p]
        return self._pdf_lib
