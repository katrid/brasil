from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v300 import *



class evGTV(ComplexType):
    """Schema XML de validação do evento informações da GTV 110170"""
    descEvento: str = Element(str, documentation=['Descrição do Evento - “Informações da GTV”'])

    class infGTV(ComplexType):
        """Grupo de Informações das GTV"""
        _max_occurs = -1

        def add(self, nDoc=None, id=None, serie=None, subserie=None, dEmi=None, nDV=None, qCarga=None, infEspecie=None, rem=None, dest=None, placa=None, UF=None, RNTRC=None) -> evGTV.infGTV:
            return super().add(nDoc=nDoc, id=id, serie=serie, subserie=subserie, dEmi=dEmi, nDV=nDV, qCarga=qCarga, infEspecie=infEspecie, rem=rem, dest=dest, placa=placa, UF=UF, RNTRC=RNTRC)

        nDoc: str = Element(str, documentation=['Número da GTV'])
        id: str = Element(str, documentation=['Identificador para diferenciar GTV de mesmo número (Usar número do AIDF ou  identificador interno da empresa),'])
        serie: str = Element(str, documentation=['Série'])
        subserie: str = Element(str, documentation=['Subsérie'])
        dEmi: TData = Element(TData, documentation=['Data de Emissão', 'Formato AAAA-MM-DD'])
        nDV: str = Element(str, documentation=['Número Dígito Verificador '])
        qCarga: TDec_1104 = Element(TDec_1104, tipo="N", tam=(11, 4), documentation=['Quantidade de volumes/malotes'])

        class infEspecie(ComplexType):
            """Informações das Espécies transportadas"""
            _max_occurs = -1

            def add(self, tpEspecie=None, vEspecie=None) -> evGTV.infGTV.infEspecie:
                return super().add(tpEspecie=tpEspecie, vEspecie=vEspecie)

            tpEspecie: str = Element(str, documentation=['Tipo da Espécie', '1 - Numerário\n2 - Cheque\n3 - Moeda\n4 - Outros'])
            vEspecie: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2), documentation=['Valor Transportada em Espécie indicada'])
        infEspecie: List[infEspecie] = Element(infEspecie, max_occurs=-1, documentation=['Informações das Espécies transportadas'])

        class rem(ComplexType):
            """Informações do Remetente da GTV"""
            _choice = [['CNPJ', 'CPF']]
            CNPJ: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['Número do CNPJ', 'Em caso de empresa não estabelecida no Brasil, será informado o CNPJ com zeros.\n\t\t\t\t\t\t\t\t\t\t\t\tInformar os zeros não significativos.'])
            CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['Número do CPF', 'Informar os zeros não significativos.'])
            IE: str = Element(str, documentation=['Inscrição Estadual', 'Informar a IE do remetente ou ISENTO se remetente é contribuinte do ICMS isento de inscrição no cadastro de contribuintes do ICMS. Caso o remetente não seja contribuinte do ICMS não informar o conteúdo.'])
            UF: TUf = Element(TUf, documentation=['Sigla da UF', 'Informar EX para operações com o exterior.'])
            xNome: str = Element(str, documentation=['Razão social ou nome do remetente'])
        rem: rem = Element(rem, documentation=['Informações do Remetente da GTV'])

        class dest(ComplexType):
            """Informações do Destinatário da GTV"""
            _choice = [['CNPJ', 'CPF']]
            CNPJ: TCnpjOpc = Element(TCnpjOpc, filter=str.isdigit, documentation=['Número do CNPJ', 'Em caso de empresa não estabelecida no Brasil, será informado o CNPJ com zeros.\n\t\t\t\t\t\t\tInformar os zeros não significativos.'])
            CPF: TCpf = Element(TCpf, filter=str.isdigit, documentation=['Número do CPF', 'Informar os zeros não significativos.'])
            IE: str = Element(str, documentation=['Inscrição Estadual', 'Informar a IE do destinatário ou ISENTO se remetente é contribuinte do ICMS isento de inscrição no cadastro de contribuintes do ICMS. Caso o remetente não seja contribuinte do ICMS não informar o conteúdo.'])
            UF: TUf = Element(TUf, documentation=['Sigla da UF', 'Informar EX para operações com o exterior.'])
            xNome: str = Element(str, documentation=['Razão social ou nome do destinatário'])
        dest: dest = Element(dest, documentation=['Informações do Destinatário da GTV'])
        placa: TPlaca = Element(TPlaca, documentation=['Placa do veículo '])
        UF: TUf = Element(TUf, documentation=['UF em que veículo está licenciado', 'Sigla da UF de licenciamento do veículo.'])
        RNTRC: str = Element(str, documentation=['RNTRC do transportador'])
    infGTV: List[infGTV] = Element(infGTV, max_occurs=-1, documentation=['Grupo de Informações das GTV'])

evGTV: evGTV = Element(evGTV, documentation=['Schema XML de validação do evento informações da GTV 110170'])
