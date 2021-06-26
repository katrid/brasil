from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .eventoCTeTiposBasico_v300 import *



class evCECTe(ComplexType):
    """Schema XML de validação do evento comprovante de entrega eletrônico do CT-e 
110180"""
    descEvento: str = Element(str, documentation=['Descrição do Evento - “Comprovante de Entrega do CT-e”'])
    nProt: TProt = Element(TProt, documentation=['Número do Protocolo de autorização do CT-e'])
    dhEntrega: str = Element(str, documentation=['Data e hora de conclusão da entrega da NF-e', 'Formato AAAA-MM-DDTHH:MM:DD TZD'])
    nDoc: str = Element(str, documentation=['Número do Documento de identificação da pessoa que recebeu a entrega'])
    xNome: str = Element(str, documentation=['Nome da pessoa que recebeu a entrega'])
    latitude: TLatitude = Element(TLatitude, documentation=['Latitude do ponto de entrega'])
    longitude: TLongitude = Element(TLongitude, documentation=['Longitude do ponto de entrega'])
    hashEntrega: str = Element(str, documentation=['Hash (SHA1) no formato Base64 resultante da concatenação: Chave de acesso do CT-e + Base64 da imagem capturada da entrega (Exemplo: imagem capturada da assinatura eletrônica, digital do recebedor, foto, etc)', 'O hashCSRT é o resultado das funções SHA-1 e base64 do token CSRT fornecido pelo fisco + chave de acesso do DF-e. (Implementação em futura NT)\nObservação: 28 caracteres são representados no schema como 20 bytes do tipo base64Binary'])
    dhHashEntrega: str = Element(str, documentation=['Data e hora de geração do hash entrega', 'Formato AAAA-MM-DDTHH:MM:DD TZD'])

    class infEntrega(ComplexType):
        """Grupo de informações das NF-e que foram entregues ao Destinatário
Informar o grupo apenas para CT-e com tipo de serviço Normal"""
        _max_occurs = 2000

        def add(self, chNFe=None) -> evCECTe.infEntrega:
            return super().add(chNFe=chNFe)

        chNFe: TChNFe = Element(TChNFe, documentation=['Chave de acesso da NF-e entregue'])
    infEntrega: List[infEntrega] = Element(infEntrega, max_occurs=2000, documentation=['Grupo de informações das NF-e que foram entregues ao Destinatário', 'Informar o grupo apenas para CT-e com tipo de serviço Normal'])

evCECTe: evCECTe = Element(evCECTe, documentation=['Schema XML de validação do evento comprovante de entrega eletrônico do CT-e \n110180'])
