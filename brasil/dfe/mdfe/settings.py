import os
import json
from logging import getLogger
from brasil.dfe.services import Services, BaseConfig


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'services.json'), 'rb') as f:
    mdfe_services = Services('MDFe', json.load(f))


class Config(BaseConfig):
    services = mdfe_services
    log = getLogger('SEFAZ-CTe')
