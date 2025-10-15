from .v400 import CTe, CTeSimp
from .settings import Config
from .ws import Recepcao, Consulta, RetornoRecepcao, RecepcaoEvento, eventoCTe


class Conhecimento:
    """
    Simplifica a integração do CTe e CTeSimp com os web services
    """

    def __init__(self, cte: CTe | CTeSimp = None, config: Config=None):
        self.cte = cte
        self.config: Config = config
        if cte is not None:
            cte._config = config

    def enviar(self):
        svc = Recepcao(self.config)
        svc.xml = self.cte
        svc.executar()
        return svc

