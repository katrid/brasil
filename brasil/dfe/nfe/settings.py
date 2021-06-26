import os
import json
from brasil.dfe.services import Services, BaseConfig


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'services.json'), 'rb') as f:
    nfe_services = Services('NFe', json.load(f))


class Config(BaseConfig):
    versao = '4.00'
    services = nfe_services

