from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v200 import *

from .cteTiposBasico_v200 import *



class TRNTRC(str):
    """Tipo RNTRC - Registro Nacional Transportadores Rodoviários de Carga"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{8}|ISENTO", enumeration=[])
    pass



class TPlaca(str):
    """Tipo Placa"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[A-Z]{3}(([1-9]\d{3})|(0[1-9]\d{2})|(00[1-9]\d)|(000[1-9]))", enumeration=[])
    pass



class TCIOT(str):
    """Tipo CIOT - Código Identificador da Operação de Transporte"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{12}", enumeration=[])
    pass



class rodo(ComplexType):
    """Informações do modal Rodoviário"""
    RNTRC: str = Element(str)
    dPrev: TData = Element(TData)
    lota: str = Element(str)
    CIOT: str = Element(str)

    class occ(ComplexType):
        """Ordens de Coleta associados"""
        _max_occurs = 10

        def add(self, serie=None, nOcc=None, dEmi=None, emiOcc=None) -> rodo.occ:
            return super().add(serie=serie, nOcc=nOcc, dEmi=dEmi, emiOcc=emiOcc)

        serie: str = Element(str)
        nOcc: str = Element(str)
        dEmi: TData = Element(TData)

        class emiOcc(ComplexType):
            CNPJ: TCnpj = Element(TCnpj)
            cInt: str = Element(str)
            IE: TIe = Element(TIe)
            UF: TUf = Element(TUf)
            fone: TFone = Element(TFone)
        emiOcc: emiOcc = Element(emiOcc)
    occ: List[occ] = Element(occ, max_occurs=10)

    class valePed(ComplexType):
        """Informações de Vale Pedágio
Outras informações sobre Vale-Pedágio obrigatório que não tenham campos específicos devem ser informadas no campo de observações gerais de uso livre pelo contribuinte, visando atender as determinações legais vigentes."""
        _max_occurs = -1

        def add(self, CNPJForn=None, nCompra=None, CNPJPg=None, vValePed=None) -> rodo.valePed:
            return super().add(CNPJForn=CNPJForn, nCompra=nCompra, CNPJPg=CNPJPg, vValePed=vValePed)

        CNPJForn: str = Element(str)
        nCompra: str = Element(str)
        CNPJPg: TCnpjOpc = Element(TCnpjOpc)
        vValePed: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
    valePed: List[valePed] = Element(valePed, max_occurs=-1)

    class veic(ComplexType):
        """Dados dos Veículos
Um CT-e poderá ter vários veículos associados, ex.: cavalo + reboque.
						Só preenchido em CT-e rodoviário de lotação."""
        _max_occurs = 4

        def add(self, cInt=None, RENAVAM=None, placa=None, tara=None, capKG=None, capM3=None, tpProp=None, tpVeic=None, tpRod=None, tpCar=None, UF=None, prop=None) -> rodo.veic:
            return super().add(cInt=cInt, RENAVAM=RENAVAM, placa=placa, tara=tara, capKG=capKG, capM3=capM3, tpProp=tpProp, tpVeic=tpVeic, tpRod=tpRod, tpCar=tpCar, UF=UF, prop=prop)

        cInt: str = Element(str)
        RENAVAM: str = Element(str)
        placa: str = Element(str)
        tara: str = Element(str)
        capKG: str = Element(str)
        capM3: str = Element(str)
        tpProp: str = Element(str)
        tpVeic: str = Element(str)
        tpRod: str = Element(str)
        tpCar: str = Element(str)
        UF: TUf = Element(TUf)

        class prop(ComplexType):
            """Proprietários do Veículo.
									Só preenchido quando o veículo não pertencer à empresa emitente do CT-e"""
            _choice = [['CPF', 'CNPJ']]
            CPF: TCpf = Element(TCpf)
            CNPJ: TCnpjOpc = Element(TCnpjOpc)
            RNTRC: TRNTRC = Element(TRNTRC)
            xNome: str = Element(str)
            IE: str = Element(str)
            UF: TUf = Element(TUf)
            tpProp: str = Element(str)
        prop: prop = Element(prop)
    veic: List[veic] = Element(veic, max_occurs=4)

    class lacRodo(ComplexType):
        """Lacres"""
        _max_occurs = -1

        def add(self, nLacre=None) -> rodo.lacRodo:
            return super().add(nLacre=nLacre)

        nLacre: str = Element(str)
    lacRodo: List[lacRodo] = Element(lacRodo, max_occurs=-1)

    class moto(ComplexType):
        """Informações do(s) Motorista(s)
Só preenchido em CT-e rodoviário de lotação"""
        _max_occurs = -1

        def add(self, xNome=None, CPF=None) -> rodo.moto:
            return super().add(xNome=xNome, CPF=CPF)

        xNome: str = Element(str)
        CPF: TCpf = Element(TCpf)
    moto: List[moto] = Element(moto, max_occurs=-1)

rodo: rodo = Element(rodo)
