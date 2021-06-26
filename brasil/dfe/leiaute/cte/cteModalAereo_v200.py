from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v200 import *



class aereo(ComplexType):
    """Informações do modal Aéreo"""
    nMinu: str = Element(str, documentation=['Número da Minuta', 'Documento que precede o CT-e, assinado pelo expedidor, espécie de pedido de serviço'])
    nOCA: str = Element(str, documentation=['Número Operacional do Conhecimento Aéreo', 'Os três primeiros dígitos representam um código que os operadores de transporte aéreo associados à IATA possuem. Em seguida um número de série de sete dígitos determinados pelo operador de tansporte aéreo. Para finalizar, um dígito verificador'])
    dPrevAereo: TData = Element(TData, documentation=['Data prevista da entrega', 'Formato AAAA-MM-DD'])
    xLAgEmi: str = Element(str, documentation=['Identificação do Emissor', 'Preencher com o nome da filial, da franquia ou da representante legal emissora do CT-e da empresa de transporte aéreo. '])
    IdT: str = Element(str, documentation=['Identificação Interna do Tomador', 'Preencher com o código identificador entre o cliente tomador e a empresa aérea. Exemplo: CNPJ, conta corrente, etc.'])

    class tarifa(ComplexType):
        """Informações de tarifa"""
        CL: str = Element(str, documentation=['Classe', 'Preencher com:\n\t\t\t\t\t\t\t\t\tM - Tarifa Mínima;\n\t\t\t\t\t\t\t\t\tG - Tarifa Geral;\n\t\t\t\t\t\t\t\t\tE - Tarifa Específica'])
        cTar: str = Element(str, documentation=['Código da Tarifa', 'Deverão ser incluídos os códigos de três dígitos, correspondentes à tarifa.'])
        vTar: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), documentation=['Valor da Tarifa', 'Valor da tarifa por kg quando for o caso.'])
    tarifa: tarifa = Element(tarifa, documentation=['Informações de tarifa'])

    class natCarga(ComplexType):
        """Natureza da carga"""
        xDime: str = Element(str, documentation=['Dimensão', 'Formato:1234X1234X1234 (cm)\n\nEsse campo deve sempre que possível ser preenchido. Entretanto, quando for impossível o preenchimento das dimensões, fica obrigatório o preechimento da cubagem em metro cúbico da infQ do leiaute do CT-e da estrutura genérica.'])
        cInfManu: List[str] = Element(str, max_occurs=-1, documentation=['Informações de manuseio', '1 - certificado do expedidor para embarque de animal vivo;\n\t\t\t\t\t\t\t\t\t2 - artigo perigoso conforme Declaração do Expedidor anexa;\n\t\t\t\t\t\t\t\t\t3 - somente em aeronave cargueira;  \n\t\t\t\t\t\t\t\t\t4 - artigo perigoso - declaração do expedidor não requerida; \n\t\t\t\t\t\t\t\t\t5 - artigo perigoso em quantidade isenta;\n\t\t\t\t\t\t\t\t\t6 - gelo seco para refrigeração (especificar no campo observações a quantidade)\n\t\t\t\t\t\t\t\t\t7 - não restrito (especificar a Disposição Especial no campo observações)\n\t\t\t\t\t\t\t\t\t8 - artigo perigoso em carga consolidada (especificar a quantidade no campo observações)\n\t\t\t\t\t\t\t\t\t9 - autorização da autoridade governamental anexa (especificar no campo observações)\n\t\t\t\t\t\t\t\t\t99 - outro (especificar no campo observações)'])
        cIMP: List[str] = Element(str, max_occurs=-1, documentation=['Carga especial', 'Informar o código Interline Message Procedure - IMP'])
    natCarga: natCarga = Element(natCarga, documentation=['Natureza da carga'])

aereo: aereo = Element(aereo, documentation=['Informações do modal Aéreo'])
