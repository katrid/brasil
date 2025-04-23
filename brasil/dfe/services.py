import os
from logging import getLogger

from brasil.consts import CODIGO_UF
from brasil.dfe.utils.certs import Certificado


class Services:
    def __init__(self, tipo: str, svcs: dict):
        self.tipo = tipo
        self._svcs = svcs
        for k, v in svcs.items():
            if 'Usar' in v:
                new_dict = {}
                new_dict.update(v)
                new_dict.update(svcs[v['Usar']])
                svcs[k] = new_dict
                del new_dict['Usar']
            svc = svcs[k]
            for sk, sv in tuple(svc.items()):
                svc[sk.lower()] = sv

    def get(self, servico: str, uf: str, amb: str, versao: str = None):
        amb = str(amb)
        if amb == '1':
            amb = 'P'
        elif amb == '2':
            amb = 'H'
        chave = f'{self.tipo}_{uf}_{amb}'
        if versao:
            servico += '_' + versao
        return self._svcs[chave][servico.lower()]


class BaseConfig:
    certificado: Certificado
    services: Services
    versao: str = None
    log = getLogger('DFe')
    on_save_file: callable = None

    def __init__(
            self, xml_path: str=None, cert_file: str=None, cert_senha: str=None, uf: str=None, versao=None, tp_amb=2
    ):
        self.uf = uf
        self.orgao = CODIGO_UF[uf]
        if versao:
            self.versao = versao
        self.amb = str(tp_amb)
        self.xml_path = xml_path
        self.cert_file = cert_file
        self.cert_senha = cert_senha
        self.certificado = Certificado(cert_file, cert_senha)
        self.salvar_arquivos = True
        self.salvar_soap = True

    def salvar_arquivo(self, xml, arquivo):
        if self.on_save_file:
            return self.on_save_file(xml, arquivo)
        mode = 'w'
        if isinstance(xml, bytes):
            mode += 'b'
        with open(os.path.join(self.xml_path, arquivo), mode) as f:
            self.log.debug('Salvar arquivo', arquivo)
            f.write(xml)
