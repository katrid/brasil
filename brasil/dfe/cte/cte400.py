from .v400 import CTe, CTeSimp
from .settings import Config
from .ws import Recepcao, RecepcaoSimp, Consulta, RetornoRecepcao, RecepcaoEvento, eventoCTe


class Conhecimento:
    """
    Simplifica a integração do CTe e CTeSimp com os web services
    """

    def __init__(self, cte: CTe | CTeSimp = None, config: Config = None):
        self.cte = cte
        self.config: Config = config
        if cte is not None:
            cte._config = config

    def enviar(self, xml: str = None):
        svc = Recepcao(self.config)
        svc.xml = xml or self.cte
        svc.executar()
        return svc

    def enviar_simp(self, xml: str = None):
        svc = RecepcaoSimp(self.config)
        svc.xml = xml or self.cte
        svc.executar()
        return svc
