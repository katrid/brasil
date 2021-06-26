import os
import json
from brasil.dfe.services import Services, BaseConfig


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'services.json'), 'rb') as f:
    cte_services = Services('CTe', json.load(f))


class Config(BaseConfig):
    services = cte_services

