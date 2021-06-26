from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v310 import *



class TVerConsStatServ(token):
    """Tipo versão do leiuate da Consulta Status do Serviço 3.10"""
    _restriction = Restriction(base=r"xs:token", pattern=r"3\.10", enumeration=[])
    pass



class TConsStatServ(Element):
    """Tipo Pedido de Consulta do Status do Serviço"""
    tpAmb: TAmb = Element(TAmb)
    cUF: TCodUfIBGE = Element(TCodUfIBGE)
    xServ: str = Element(str)
    versao: str = Attribute(TVerConsStatServ)



class TRetConsStatServ(Element):
    """Tipo Resultado da Consulta do Status do Serviço"""
    tpAmb: TAmb = Element(TAmb)
    verAplic: TVerAplic = Element(TVerAplic)
    cStat: TStat = Element(TStat)
    xMotivo: TMotivo = Element(TMotivo)
    cUF: TCodUfIBGE = Element(TCodUfIBGE)
    dhRecbto: TDateTimeUTC = Element(TDateTimeUTC)
    tMed: TMed = Element(TMed)
    dhRetorno: TDateTimeUTC = Element(TDateTimeUTC)
    xObs: TMotivo = Element(TMotivo)
    versao: str = Attribute(TVerConsStatServ)


