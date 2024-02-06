from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .mdfeTiposBasico_v300 import *



class aquav(ComplexType):
    """Informações do modal Aquaviário"""
    irin: str = Element(str, documentation=['Irin do navio sempre deverá ser informado'])
    tpEmb: str = Element(str, documentation=['Código do tipo de embarcação', 'Preencher com código da Tabela de Tipo de Embarcação definida no Ministério dos Transportes'])
    cEmbar: str = Element(str, documentation=['Código da embarcação'])
    xEmbar: str = Element(str, documentation=['Nome da embarcação'])
    nViag: str = Element(str, documentation=['Número da Viagem'])
    cPrtEmb: str = Element(str, documentation=['Código do Porto de Embarque', 'Preencher de acordo com Tabela de Portos definida no Ministério dos Transportes'])
    cPrtDest: str = Element(str, documentation=['Código do Porto de Destino', 'Preencher de acordo com Tabela de Portos definida no Ministério dos Transportes'])
    prtTrans: str = Element(str, documentation=['Porto de Transbordo'])
    tpNav: str = Element(str, documentation=['Tipo de Navegação', 'Preencher com: \n\t\t\t\t\t\t0 - Interior;\n\t\t\t\t\t\t1 - Cabotagem'])

    class infTermCarreg(ComplexType):
        """Grupo de informações dos terminais de carregamento."""
        _max_occurs = 5

        def add(self, cTermCarreg=None, xTermCarreg=None) -> aquav.infTermCarreg:
            return super().add(cTermCarreg=cTermCarreg, xTermCarreg=xTermCarreg)

        cTermCarreg: str = Element(str, documentation=['Código do Terminal de Carregamento', 'Preencher de acordo com a Tabela de Terminais de Carregamento. O código de cada Porto está definido no Ministério de Transportes.'])
        xTermCarreg: str = Element(str, documentation=['Nome do Terminal de Carregamento'])
    infTermCarreg: List[infTermCarreg] = Element(infTermCarreg, max_occurs=5, documentation=['Grupo de informações dos terminais de carregamento.'])

    class infTermDescarreg(ComplexType):
        """Grupo de informações dos terminais de descarregamento."""
        _max_occurs = 5

        def add(self, cTermDescarreg=None, xTermDescarreg=None) -> aquav.infTermDescarreg:
            return super().add(cTermDescarreg=cTermDescarreg, xTermDescarreg=xTermDescarreg)

        cTermDescarreg: str = Element(str, documentation=['Código do Terminal de Descarregamento', 'Preencher de acordo com a Tabela de Terminais de Descarregamento. O código de cada Porto está definido no Ministério de Transportes.'])
        xTermDescarreg: str = Element(str, documentation=['Nome do Terminal de Descarregamento'])
    infTermDescarreg: List[infTermDescarreg] = Element(infTermDescarreg, max_occurs=5, documentation=['Grupo de informações dos terminais de descarregamento.'])

    class infEmbComb(ComplexType):
        """Informações das Embarcações do Comboio"""
        _max_occurs = 30

        def add(self, cEmbComb=None, xBalsa=None) -> aquav.infEmbComb:
            return super().add(cEmbComb=cEmbComb, xBalsa=xBalsa)

        cEmbComb: str = Element(str, documentation=['Código da embarcação do comboio'])
        xBalsa: str = Element(str, documentation=['Identificador da Balsa'])
    infEmbComb: List[infEmbComb] = Element(infEmbComb, max_occurs=30, documentation=['Informações das Embarcações do Comboio'])

    class infUnidCargaVazia(ComplexType):
        """Informações das Undades de Carga vazias"""
        _max_occurs = -1

        def add(self, idUnidCargaVazia=None, tpUnidCargaVazia=None) -> aquav.infUnidCargaVazia:
            return super().add(idUnidCargaVazia=idUnidCargaVazia, tpUnidCargaVazia=tpUnidCargaVazia)

        idUnidCargaVazia: TContainer = Element(TContainer, documentation=['Identificação da unidades de carga vazia'])
        tpUnidCargaVazia: str = Element(str, documentation=['Tipo da unidade de carga vazia', '1 - Container; 2 - ULD;3 - Pallet;4 - Outros;\n\n'])
    infUnidCargaVazia: List[infUnidCargaVazia] = Element(infUnidCargaVazia, max_occurs=-1, documentation=['Informações das Undades de Carga vazias'])

    class infUnidTranspVazia(ComplexType):
        """Informações das Undades de Transporte vazias"""
        _max_occurs = -1

        def add(self, idUnidTranspVazia=None, tpUnidTranspVazia=None) -> aquav.infUnidTranspVazia:
            return super().add(idUnidTranspVazia=idUnidTranspVazia, tpUnidTranspVazia=tpUnidTranspVazia)

        idUnidTranspVazia: TContainer = Element(TContainer, documentation=['Identificação da unidades de transporte vazia'])
        tpUnidTranspVazia: str = Element(str, documentation=['Tipo da unidade de transporte vazia', 'Deve ser preenchido com “1” para Rodoviário Tração do tipo caminhão ou “2” para Rodoviário reboque do tipo carreta\n\n'])
    infUnidTranspVazia: List[infUnidTranspVazia] = Element(infUnidTranspVazia, max_occurs=-1, documentation=['Informações das Undades de Transporte vazias'])

aquav: aquav = Element(aquav, documentation=['Informações do modal Aquaviário'])
