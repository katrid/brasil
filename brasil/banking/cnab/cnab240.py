from typing import Annotated, List
import re

from .base import Record, Arquivo


class Arquivo240(Arquivo):
    def re_debug(self, line: str):
        # tentar determinar segmento objetivando depurar conteúdo
        if len(line) == 240:
            seg = line[13]
            if seg:
                print('  Segmento ' + seg)
            if seg == 'T':
                self.SegmentoT.re_debug(line)
            elif seg == 'U':
                self.SegmentoU.re_debug(line)
        else:
            raise ValueError('Formato da linha inválido, por favor verifique o arquivo e tente novamente.')
