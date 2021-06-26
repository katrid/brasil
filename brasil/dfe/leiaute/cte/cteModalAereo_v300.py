from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v300 import *



class aereo(ComplexType):
    """Informações do modal Aéreo"""
    nMinu: str = Element(str, documentation=['Número da Minuta', 'Documento que precede o CT-e, assinado pelo expedidor, espécie de pedido de serviço'])
    nOCA: str = Element(str, documentation=['Número Operacional do Conhecimento Aéreo', 'Representa o número de controle comumente utilizado pelo conhecimento aéreo composto por uma sequência numérica de onze dígitos. Os três primeiros dígitos representam um código que os operadores de transporte aéreo associados à IATA possuem. Em seguida um número de série de sete dígitos determinados pelo operador de transporte aéreo. Para finalizar, um dígito verificador, que é um sistema de módulo sete imponderado o qual divide o número de série do conhecimento aéreo por sete e usa o resto como dígito de verificação. '])
    dPrevAereo: TData = Element(TData, base_type=date, documentation=['Data prevista da entrega', 'Formato AAAA-MM-DD'])

    class natCarga(ComplexType):
        """Natureza da carga"""
        xDime: str = Element(str, documentation=['Dimensão', 'Formato:1234X1234X1234 (cm). Esse campo deve sempre que possível ser preenchido. Entretanto, quando for impossível o preenchimento das dimensões, fica obrigatório o preenchimento da cubagem em metro cúbico do leiaute do CT-e da estrutura genérica (infQ).\n'])
        cInfManu: List[str] = Element(str, max_occurs=-1, documentation=['Informações de manuseio', '01 - certificado do expedidor para embarque de animal vivo;\n\n02 - artigo perigoso conforme Declaração do Expedidor anexa;\n\n03 - somente em aeronave cargueira; \n\n04 - artigo perigoso - declaração do expedidor não requerida; \n\n05 - artigo perigoso em quantidade isenta;\n\n06 - gelo seco para refrigeração (especificar no campo observações a quantidade); \n\n07 - não restrito (especificar a Disposição Especial no campo observações);\n\n08 - artigo perigoso em carga consolidada (especificar a quantidade no campo observações)\n;\n09 - autorização da autoridade governamental anexa (especificar no campo observações); \n\n10 – baterias de íons de lítio em conformidade com a Seção II da PI965 – CAO\n; \n11 - baterias de íons de lítio em conformidade com a Seção II da PI966\n; \n12 - baterias de íons de lítio em conformidade com a Seção II da PI967\n; \n13 – baterias de metal lítio em conformidade com a Seção II da PI968 — CAO; \n\n14 - baterias de metal lítio em conformidade com a Seção II da PI969; \n\n15 - baterias de metal lítio em conformidade com a Seção II da PI970\n; \n99 - outro (especificar no campo observações)\n.'])
    natCarga: natCarga = Element(natCarga, documentation=['Natureza da carga'])

    class tarifa(ComplexType):
        """Informações de tarifa"""
        CL: str = Element(str, documentation=['Classe', 'Preencher com:\n\t\t\t\t\t\t\t\t\tM - Tarifa Mínima;\n\t\t\t\t\t\t\t\t\tG - Tarifa Geral;\n\t\t\t\t\t\t\t\t\tE - Tarifa Específica'])
        cTar: str = Element(str, documentation=['Código da Tarifa', 'Deverão ser incluídos os códigos de três dígitos, correspondentes à tarifa.'])
        vTar: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), base_type=Decimal, documentation=['Valor da Tarifa', 'Valor da tarifa por kg quando for o caso.'])
    tarifa: tarifa = Element(tarifa, documentation=['Informações de tarifa'])

    class peri(ComplexType):
        """Preenchido quando for  transporte de produtos classificados pela ONU como perigosos.
O preenchimento desses campos não desobriga a empresa aérea de emitir os demais documentos que constam na legislação vigente."""
        _max_occurs = -1

        def add(self, nONU=None, qTotEmb=None, infTotAP=None) -> aereo.peri:
            return super().add(nONU=nONU, qTotEmb=qTotEmb, infTotAP=infTotAP)

        nONU: str = Element(str, documentation=['Número ONU/UN', 'Ver a legislação de transporte de produtos perigosos aplicadas ao modal  '])
        qTotEmb: str = Element(str, documentation=['Quantidade total de volumes contendo artigos perigosos', 'Preencher com o número de volumes (unidades) de artigos perigosos, ou seja, cada embalagem devidamente marcada e etiquetada (por ex.: número de caixas, de tambores, de bombonas, dentre outros). Não deve ser preenchido com o número de ULD, pallets ou containers.'])

        class infTotAP(ComplexType):
            """Grupo de informações das quantidades totais de artigos perigosos
Preencher conforme a legislação de transporte de produtos perigosos aplicada ao modal"""
            qTotProd: TDec_1104 = Element(TDec_1104, tipo="N", tam=(11, 4), base_type=Decimal, documentation=['Quantidade total de artigos perigosos', '15 posições, sendo 11 inteiras e 4 decimais. \nDeve indicar a quantidade total do artigo perigoso, tendo como base a unidade referenciada na Tabela 3-1 do Doc 9284, por exemplo: litros; quilogramas; quilograma bruto etc. O preenchimento não deve, entretanto, incluir a unidade de medida. No caso de transporte de material radioativo, deve-se indicar o somatório dos Índices de Transporte (TI). Não indicar a quantidade do artigo perigoso por embalagem.'])
            uniAP: str = Element(str, documentation=['Unidade de medida', '1 – KG; \n2 – KG G (quilograma bruto);\n3 – LITROS;\n4 – TI (índice de transporte para radioativos); 5- Unidades (apenas para artigos perigosos medidos em unidades que não se enquadram nos itens acima. Exemplo: baterias, celulares, equipamentos, veículos, dentre outros)'])
        infTotAP: infTotAP = Element(infTotAP, documentation=['Grupo de informações das quantidades totais de artigos perigosos', 'Preencher conforme a legislação de transporte de produtos perigosos aplicada ao modal'])
    peri: List[peri] = Element(peri, max_occurs=-1, documentation=['Preenchido quando for  transporte de produtos classificados pela ONU como perigosos.', 'O preenchimento desses campos não desobriga a empresa aérea de emitir os demais documentos que constam na legislação vigente.'])

aereo: aereo = Element(aereo, documentation=['Informações do modal Aéreo'])
