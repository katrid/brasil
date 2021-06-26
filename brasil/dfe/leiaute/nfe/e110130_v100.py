from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *



class detEvento(ComplexType):
    """Schema XML de validação do evento de Comprovante de Entrega de NF-e"""
    descEvento: str = Element(str)
    cOrgaoAutor: TCOrgaoIBGE = Element(TCOrgaoIBGE)
    tpAutor: str = Element(str)
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo do Autor do Evento'])
    dhEntrega: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e hora do final da entrega. Formato AAAA-MMDDThh:mm:ssTZD\n\t\t\t\t'])
    nDoc: str = Element(str)
    xNome: str = Element(str, documentation=['Nome da pessoa que assinou o Comprovante de Entrega da NF-e'])
    latGPS: TLatitude = Element(TLatitude, documentation=['Latitude do ponto de entrega'])
    longGPS: TLongitude = Element(TLongitude, documentation=['Longitude do ponto de entrega'])
    hashComprovante: str = Element(str, documentation=['Hash (SHA1) no formato Base64 resultante da concatenação: Chave de acesso da NFe + Base64 da imagem capturada da entrega (Exemplo: imagem capturada da assinatura eletrônica, digital do recebedor, foto, etc)', 'O hashCSRT é o resultado das funções SHA-1 e base64 do token CSRT fornecido pelo fisco + chave de acesso do DF-e. (Implementação em futura NT)\nObservação: 28 caracteres são representados no schema como 20 bytes do tipo base64Binary'])
    dhHashComprovante: TDateTimeUTC = Element(TDateTimeUTC, base_type=datetime, documentation=['Data e hora da geração do hash do Comprovante de Entrega da NF-e. Formato AAAA-MMDDThh:mm:ssTZD.\n\t\t\t\t'])
    versao: str = Attribute(None)

detEvento: detEvento = Element(detEvento, documentation=['Schema XML de validação do evento de Comprovante de Entrega de NF-e'])
