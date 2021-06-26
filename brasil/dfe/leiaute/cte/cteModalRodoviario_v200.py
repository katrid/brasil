from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
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
    RNTRC: str = Element(str, documentation=['Registro Nacional de Transportadores Rodoviários de Carga', 'Registro obrigatório do emitente do CT-e junto à ANTT para exercer a atividade de transportador rodoviário de cargas por conta de terceiros e mediante remuneração.\n\t\t\t\t\t\t'])
    dPrev: TData = Element(TData, base_type=date, documentation=['Data prevista para entrega da carga no Recebedor', 'Formato AAAA-MM-DD'])
    lota: str = Element(str, documentation=['Indicador de Lotação\n', 'Preencher com: 0 - Não; 1 - Sim \n\t\t\t\t\t\tSerá lotação quando houver um único conhecimento de transporte por veículo, ou combinação veicular, e por viagem'])
    CIOT: str = Element(str, documentation=['Código Identificador da Operação de Transporte', 'Também Conhecido como conta frete'])

    class occ(ComplexType):
        """Ordens de Coleta associados"""
        _max_occurs = 10

        def add(self, serie=None, nOcc=None, dEmi=None, emiOcc=None) -> rodo.occ:
            return super().add(serie=serie, nOcc=nOcc, dEmi=dEmi, emiOcc=emiOcc)

        serie: str = Element(str, documentation=['Série da OCC'])
        nOcc: str = Element(str, documentation=['Número da Ordem de coleta'])
        dEmi: TData = Element(TData, base_type=date, documentation=['Data de emissão da ordem de coleta', 'Formato AAAA-MM-DD'])

        class emiOcc(ComplexType):
            CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['Número do CNPJ', 'Informar os zeros não significativos.'])
            cInt: str = Element(str, documentation=['Código interno de uso da transportadora', 'Uso intermo das transportadoras.'])
            IE: TIe = Element(TIe, filter=str.isdigit, documentation=['Inscrição Estadual'])
            UF: TUf = Element(TUf, documentation=['Sigla da UF', 'Informar EX para operações com o exterior.'])
            fone: TFone = Element(TFone, filter=str.isdigit, documentation=['Telefone'])
        emiOcc: emiOcc = Element(emiOcc)
    occ: List[occ] = Element(occ, max_occurs=10, documentation=['Ordens de Coleta associados'])

    class valePed(ComplexType):
        """Informações de Vale Pedágio
Outras informações sobre Vale-Pedágio obrigatório que não tenham campos específicos devem ser informadas no campo de observações gerais de uso livre pelo contribuinte, visando atender as determinações legais vigentes."""
        _max_occurs = -1

        def add(self, CNPJForn=None, nCompra=None, CNPJPg=None, vValePed=None) -> rodo.valePed:
            return super().add(CNPJForn=CNPJForn, nCompra=nCompra, CNPJPg=CNPJPg, vValePed=vValePed)

        CNPJForn: str = Element(str, documentation=['CNPJ da empresa fornecedora do Vale-Pedágio', '- CNPJ da Empresa Fornecedora do Vale-Pedágio, ou seja, empresa que fornece ao Responsável pelo Pagamento do Vale-Pedágio os dispositivos do Vale-Pedágio.\n\t\t\t\t\t\t\t\t\t- Informar os zeros não significativos.'])
        nCompra: str = Element(str, documentation=['Número do comprovante de compra', 'Número de ordem do comprovante de compra do Vale-Pedágio fornecido para cada veículo ou combinação veicular, por viagem.'])
        CNPJPg: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['CNPJ do responsável pelo pagamento do Vale-Pedágio', '- responsável pelo pagamento do Vale Pedágio. Informar somente quando o responsável não for o emitente do CT-e.\n\t\t\t\t\t\t\t\t\t- Informar os zeros não significativos.'])
        vValePed: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor do Vale-Pedagio', 'Número de ordem do comprovante de compra do Vale-Pedágio fornecido para cada veículo ou combinação veicular, por viagem.'])
    valePed: List[valePed] = Element(valePed, max_occurs=-1, documentation=['Informações de Vale Pedágio', 'Outras informações sobre Vale-Pedágio obrigatório que não tenham campos específicos devem ser informadas no campo de observações gerais de uso livre pelo contribuinte, visando atender as determinações legais vigentes.'])

    class veic(ComplexType):
        """Dados dos Veículos
Um CT-e poderá ter vários veículos associados, ex.: cavalo + reboque.
						Só preenchido em CT-e rodoviário de lotação."""
        _max_occurs = 4

        def add(self, cInt=None, RENAVAM=None, placa=None, tara=None, capKG=None, capM3=None, tpProp=None, tpVeic=None, tpRod=None, tpCar=None, UF=None, prop=None) -> rodo.veic:
            return super().add(cInt=cInt, RENAVAM=RENAVAM, placa=placa, tara=tara, capKG=capKG, capM3=capM3, tpProp=tpProp, tpVeic=tpVeic, tpRod=tpRod, tpCar=tpCar, UF=UF, prop=prop)

        cInt: str = Element(str, documentation=['Código interno do veículo '])
        RENAVAM: str = Element(str, documentation=['RENAVAM do veículo '])
        placa: str = Element(str, documentation=['Placa do veículo '])
        tara: str = Element(str, documentation=['Tara em KG'])
        capKG: str = Element(str, documentation=['Capacidade em KG'])
        capM3: str = Element(str, documentation=['Capacidade em M3'])
        tpProp: str = Element(str, documentation=['Tipo de Propriedade de veículo', 'Preencher com: \n\t\t\t\t\t\t\t\t\tP- Próprio;\n\t\t\t\t\t\t\t\t\tT- terceiro.\n\t\t\t\t\t\t\t\t\tSerá próprio quando o proprietário, co-proprietário ou arrendatário do veículo for o  Emitente do CT-e, caso contrário será caracterizado como  de propriedade de Terceiro\n\t\t\t\t\t\t\t\t\t'])
        tpVeic: str = Element(str, documentation=['Tipo de veículo', 'Preencher com: 0-Tração; 1-Reboque'])
        tpRod: str = Element(str, documentation=['Tipo de Rodado', 'Preencher com:\n\t\t\t\t\t\t\t\t\t00 - não aplicável;\n\t\t\t\t\t\t\t\t\t01 - Truck;\n\t\t\t\t\t\t\t\t\t02 - Toco;\n\t\t\t\t\t\t\t\t\t03 - Cavalo Mecânico;\n\t\t\t\t\t\t\t\t\t04 - VAN;\n\t\t\t\t\t\t\t\t\t05 - Utilitário;\n\t\t\t\t\t\t\t\t\t06 - Outros.'])
        tpCar: str = Element(str, documentation=['Tipo de Carroceria', 'Preencher com:\n\t\t\t\t\t\t\t\t\t00 - não aplicável;\n\t\t\t\t\t\t\t\t\t01 - Aberta;\n\t\t\t\t\t\t\t\t\t02 - Fechada/Baú;\n\t\t\t\t\t\t\t\t\t03 - Granelera;\n\t\t\t\t\t\t\t\t\t04 - Porta Container;\n\t\t\t\t\t\t\t\t\t05 - Sider'])
        UF: TUf = Element(TUf, documentation=['UF em que veículo está licenciado', 'Sigla da UF de licenciamento do veículo.'])

        class prop(ComplexType):
            """Proprietários do Veículo.
									Só preenchido quando o veículo não pertencer à empresa emitente do CT-e"""
            _choice = [['CPF', 'CNPJ']]
            @property
            def CNPJCPF(self):
                return self.CPF or self.CNPJ

            @CNPJCPF.setter
            def CNPJCPF(self, value):
                value = "".join(filter(str.isdigit, value))
                if len(value) == 11:
                    self.CPF = value
                else:
                    self.CNPJ = value
            CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['Número do CPF', 'Informar os zeros não significativos.'])
            CNPJ: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['Número do CNPJ', 'Informar os zeros não significativos.'])
            RNTRC: TRNTRC = Element(TRNTRC, documentation=['Registro Nacional dos Transportadores Rodoviários de Carga', 'Registro obrigatório do proprietário, co-proprietário ou arrendatário do veículo junto à ANTT para exercer a atividade de transportador rodoviário de cargas por conta de terceiros e mediante remuneração.'])
            xNome: str = Element(str, documentation=['Razão Social ou Nome do proprietário'])
            IE: str = Element(str, documentation=['Inscrição Estadual'])
            UF: TUf = Element(TUf, documentation=['UF'])
            tpProp: str = Element(str, documentation=['Tipo Proprietário', 'Preencher com:\n\t\t\t\t\t\t\t\t\t\t\t\t0-TAC – Agregado;\n\t\t\t\t\t\t\t\t\t\t\t\t1-TAC Independente; ou \n\t\t\t\t\t\t\t\t\t\t\t\t2 – Outros.'])
        prop: prop = Element(prop, documentation=['Proprietários do Veículo.\n\t\t\t\t\t\t\t\t\tSó preenchido quando o veículo não pertencer à empresa emitente do CT-e'])
    veic: List[veic] = Element(veic, max_occurs=4, documentation=['Dados dos Veículos', 'Um CT-e poderá ter vários veículos associados, ex.: cavalo + reboque.\n\t\t\t\t\t\tSó preenchido em CT-e rodoviário de lotação.'])

    class lacRodo(ComplexType):
        """Lacres"""
        _max_occurs = -1

        def add(self, nLacre=None) -> rodo.lacRodo:
            return super().add(nLacre=nLacre)

        nLacre: str = Element(str, documentation=['Número do Lacre'])
    lacRodo: List[lacRodo] = Element(lacRodo, max_occurs=-1, documentation=['Lacres'])

    class moto(ComplexType):
        """Informações do(s) Motorista(s)
Só preenchido em CT-e rodoviário de lotação"""
        _max_occurs = -1

        def add(self, xNome=None, CPF=None) -> rodo.moto:
            return super().add(xNome=xNome, CPF=CPF)

        xNome: str = Element(str, documentation=['Nome do Motorista'])
        CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['CPF do Motorista'])
    moto: List[moto] = Element(moto, max_occurs=-1, documentation=['Informações do(s) Motorista(s)', 'Só preenchido em CT-e rodoviário de lotação'])

rodo: rodo = Element(rodo, documentation=['Informações do modal Rodoviário'])
