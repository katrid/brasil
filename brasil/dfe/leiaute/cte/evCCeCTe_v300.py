from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v300 import *



class evCCeCTe(ComplexType):
    """Schema XML de validação do evento carta de correção 
110110"""
    descEvento: str = Element(str, documentation=['Descrição do Evento - “Carta de Correção”'])

    class infCorrecao(ComplexType):
        """Grupo de Informações de Correção"""
        _max_occurs = -1

        def add(self, grupoAlterado=None, campoAlterado=None, valorAlterado=None, nroItemAlterado=None) -> evCCeCTe.infCorrecao:
            return super().add(grupoAlterado=grupoAlterado, campoAlterado=campoAlterado, valorAlterado=valorAlterado, nroItemAlterado=nroItemAlterado)

        grupoAlterado: str = Element(str, documentation=['Indicar o grupo de informações que pertence o campoAlterado. Ex: ide'])
        campoAlterado: str = Element(str, documentation=['Nome do campo modificado do CT-e Original.'])
        valorAlterado: str = Element(str, documentation=['Valor correspondente à alteração.'])
        nroItemAlterado: str = Element(str, documentation=['Preencher com o indice do item alterado caso a alteração ocorra em uma lista. \nOBS: O indice inicia sempre  em 1'])
    infCorrecao: List[infCorrecao] = Element(infCorrecao, max_occurs=-1, documentation=['Grupo de Informações de Correção'])
    xCondUso: str = Element(str, documentation=['Condições de uso da Carta de Correção,', 'informar a literal :Condições de uso da Carta de Correção, informar a literal:\n“A Carta de Correção é disciplinada pelo Art. 58-B do CONVÊNIO/SINIEF 06/89: Fica permitida a utilização de carta de correção, para regularização de erro ocorrido na emissão de documentos fiscais relativos à prestação de serviço de transporte, desde que o erro não esteja relacionado com: I - as variáveis que determinam o valor do imposto tais como: base de cálculo, alíquota, diferença de preço, quantidade, valor da prestação;II - a correção de dados cadastrais que implique mudança do emitente, tomador, remetente ou do destinatário;III - a data de emissão ou de saída.” (texto com acentuação)  ou “A Carta de Correcao e disciplinada pelo Art. 58-B do CONVENIO/SINIEF 06/89: Fica permitida a utilizacao de carta de correcao, para regularizacao de erro ocorrido na emissao de documentos fiscais relativos a prestacao de servico de transporte, desde que o erro nao esteja relacionado com: I - as variaveis que determinam o valor do imposto tais como: base de calculo, aliquota, diferenca de preco, quantidade, valor da prestacao;II - a correcao de dados cadastrais que implique mudança do emitente, tomador, remetente ou do destinatario;III - a data de emissao ou de saida.” (texto sem acentuação)'])

evCCeCTe: evCCeCTe = Element(evCCeCTe, documentation=['Schema XML de validação do evento carta de correção \n110110'])
