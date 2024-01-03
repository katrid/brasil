from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v400 import *



class evIECTe(ComplexType):
    """Schema XML de validação do evento insucesso na entrega eletrônico do CT-e 
110190"""
    descEvento: str = Element(str, documentation=['Descrição do Evento - “Insucesso na Entrega do CT-e”'])
    nProt: TProt = Element(TProt, documentation=['Número do Protocolo de autorização do CT-e'])
    dhTentativaEntrega: str = Element(str, documentation=['Data e hora da tentativa da entrega da NF-e', 'Formato AAAA-MM-DDTHH:MM:DD TZD'])
    nTentativa: str = Element(str, documentation=['Número da tentativa de entrega que não teve insucesso'])
    tpMotivo: str = Element(str, documentation=['Motivo do insucesso', '1- Recebedor não encontrado;\n2- Recusa do recebedor;\n3- Endereço inexistente;\n4- Outros (exige informar justificativa)'])
    xJustMotivo: str = Element(str, documentation=['Justificativa do Motivo de insucesso, informar apenas para tpMotivo = 4'])
    latitude: TLatitude = Element(TLatitude, documentation=['Latitude do ponto de entrega'])
    longitude: TLongitude = Element(TLongitude, documentation=['Longitude do ponto de entrega'])
    hashTentativaEntrega: str = Element(str, documentation=['Hash (SHA1) no formato Base64 resultante da concatenação: Chave de acesso do CT-e + Base64 da imagem capturada da tentativa com insucesso da entrega (Exemplo: foto do local que não recebeu a entrega ou do local sem recebedor)', 'O hashCSRT é o resultado das funções SHA-1 e base64 do token CSRT fornecido pelo fisco + chave de acesso do DF-e. (Implementação em futura NT)\nObservação: 28 caracteres são representados no schema como 20 bytes do tipo base64Binary'])
    dhHashTentativaEntrega: str = Element(str, documentation=['Data e hora de geração do hash tentativa entrega', 'Formato AAAA-MM-DDTHH:MM:DD TZD'])

    class infEntrega(ComplexType):
        """Grupo de informações das NF-e que não tiveram sucesso na entrega ao Destinatário
Informar o grupo apenas para CT-e com tipo de serviço Normal"""
        _max_occurs = 2000

        def add(self, chNFe=None) -> evIECTe.infEntrega:
            return super().add(chNFe=chNFe)

        chNFe: TChDFe = Element(TChDFe, documentation=['Chave de acesso da NF-e com insucesso na tentativa de entrega'])
    infEntrega: List[infEntrega] = Element(infEntrega, max_occurs=2000, documentation=['Grupo de informações das NF-e que não tiveram sucesso na entrega ao Destinatário', 'Informar o grupo apenas para CT-e com tipo de serviço Normal'])

evIECTe: evIECTe = Element(evIECTe, documentation=['Schema XML de validação do evento insucesso na entrega eletrônico do CT-e \n110190'])
