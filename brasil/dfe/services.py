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

    def get(self, servico: str, uf: str, amb: str, versao: str):
        amb = str(amb)
        if amb == '1':
            amb = 'P'
        elif amb == '2':
            amb = 'H'
        chave = f'{self.tipo}_{uf}_{amb}'
        servico += '_' + versao
        return self._svcs[chave][servico]


class BaseConfig:
    certificado: Certificado
    services: Services
    versao: str = None

    def __init__(
            self, xml_path: str=None, cert_file: str=None, cert_senha: str=None, uf: str=None, versao=None, tp_amb=2
    ):
        self.uf = uf
        if versao:
            self.versao = versao
        self.amb = tp_amb
        self.xml_path = xml_path
        self.cert_file = cert_file
        self.cert_senha = cert_senha
        self.certificado = Certificado(cert_file, cert_senha)
