from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v300 import *



class evGTV(ComplexType):
    """Schema XML de validação do evento informações da GTV 110170"""
    descEvento: str = Element(str)

    class infGTV(ComplexType):
        """Grupo de Informações das GTV"""
        _max_occurs = -1

        def add(self, nDoc=None, id=None, serie=None, subserie=None, dEmi=None, nDV=None, qCarga=None, infEspecie=None, rem=None, dest=None, placa=None, UF=None, RNTRC=None) -> evGTV.infGTV:
            return super().add(nDoc=nDoc, id=id, serie=serie, subserie=subserie, dEmi=dEmi, nDV=nDV, qCarga=qCarga, infEspecie=infEspecie, rem=rem, dest=dest, placa=placa, UF=UF, RNTRC=RNTRC)

        nDoc: str = Element(str)
        id: str = Element(str)
        serie: str = Element(str)
        subserie: str = Element(str)
        dEmi: TData = Element(TData)
        nDV: str = Element(str)
        qCarga: TDec_1104 = Element(TDec_1104, tipo="N", tam=(11, 4))

        class infEspecie(ComplexType):
            """Informações das Espécies transportadas"""
            _max_occurs = -1

            def add(self, tpEspecie=None, vEspecie=None) -> evGTV.infGTV.infEspecie:
                return super().add(tpEspecie=tpEspecie, vEspecie=vEspecie)

            tpEspecie: str = Element(str)
            vEspecie: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
        infEspecie: List[infEspecie] = Element(infEspecie, max_occurs=-1)

        class rem(ComplexType):
            """Informações do Remetente da GTV"""
            _choice = [['CNPJ', 'CPF']]
            CNPJ: TCnpjOpc = Element(TCnpjOpc)
            CPF: TCpf = Element(TCpf)
            IE: str = Element(str)
            UF: TUf = Element(TUf)
            xNome: str = Element(str)
        rem: rem = Element(rem)

        class dest(ComplexType):
            """Informações do Destinatário da GTV"""
            _choice = [['CNPJ', 'CPF']]
            CNPJ: TCnpjOpc = Element(TCnpjOpc)
            CPF: TCpf = Element(TCpf)
            IE: str = Element(str)
            UF: TUf = Element(TUf)
            xNome: str = Element(str)
        dest: dest = Element(dest)
        placa: TPlaca = Element(TPlaca)
        UF: TUf = Element(TUf)
        RNTRC: str = Element(str)
    infGTV: List[infGTV] = Element(infGTV, max_occurs=-1)

evGTV: evGTV = Element(evGTV)
