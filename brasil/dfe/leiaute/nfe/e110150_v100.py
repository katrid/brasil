from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *



class detEvento(ComplexType):
    """Schema XML de validação do evento de Ator Interessado na NF-e - Transportador (110150)”"""
    descEvento: str = Element(str, documentation=['Descrição do Evento - "Ator interessado na NF-e”"'])
    cOrgaoAutor: TCodUfIBGE = Element(TCodUfIBGE)
    tpAutor: str = Element(str, documentation=['Tipo do Órgão Autor do Evento. Informar uma das opções 1=Geração do Evento pelo Emitente; 2=Geração do Evento pelo Destinatário; 3=Geração do Evento pelo Transportador\nOutros valores: 1=Empresa Emitente, 2=Empresa destinatária; 3=Empresa; 5=Fisco; 6=RFB; 9=Outros Órgãos;'])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do aplicativo do Autor do Evento.'])

    class autXML(ComplexType):
        """Pessoas autorizadas a acessar o XML da NF-e"""
        _choice = [['CNPJ', 'CPF']]
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
        CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit)
        CPF: TCpf = Element(TCpf, filter=str.isdigit)
    autXML: autXML = Element(autXML, documentation=['Pessoas autorizadas a acessar o XML da NF-e'])
    tpAutorizacao: str = Element(str, documentation=['0 – Não permite; 1 – Permite o transportador autorizado pelo emitente ou destinatário autorizar outros transportadores para ter acesso ao download da NF-e\n\t\t\t\t\t\t'])
    xCondUso: str = Element(str, documentation=['Texto Fixo com as Condição de uso do tipo de autorização para o transportador: '])
    versao: str = Attribute(None)

detEvento: detEvento = Element(detEvento, documentation=['Schema XML de validação do evento de Ator Interessado na NF-e - Transportador (110150)”'])
