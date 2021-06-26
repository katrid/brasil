from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *



class TVerDownloadNFe(str):
    """Tipo Versão da consultaNFeDest"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1.00'])
    pass



class TDownloadNFe(Element):
    """Tipo Pedido de Download de NF-e"""
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    xServ: str = Element(str, documentation=['Serviço Solicitado'])
    CNPJ: TCnpj = Element(TCnpj, filter=str.isdigit, documentation=['CNPJ do destinatário da NF-e'])
    chNFe: List[TChNFe] = Element(TChNFe, max_occurs=10, documentation=['Chave de Acesso da NF-e objeto de download'])
    versao: str = Attribute(TVerDownloadNFe)



class TRetDownloadNFe(Element):
    """Tipo Retorno do pedido de Download de NF-e"""
    tpAmb: TAmb = Element(TAmb, documentation=['Identificação do Ambiente:\n1 - Produção\n2 - Homologação'])
    verAplic: TVerAplic = Element(TVerAplic, documentation=['Versão do Aplicativo que processou a NF-e'])
    cStat: TStat = Element(TStat, documentation=['Código do status da mensagem enviada.'])
    xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do serviço solicitado.'])
    dhResp: dateTime = Element(dateTime, documentation=['Data e hora da resposta à solicitação, no formato AAAA-MM-DDTHH:MM:SS'])

    class retNFe(ComplexType):
        """Conjunto de informação das  NF-e localizadas"""
        _max_occurs = 10
        _choice = [['procNFeGrupoZip', 'procNFeZip', 'procNFe']]

        def add(self, chNFe=None, cStat=None, xMotivo=None, procNFeGrupoZip=None, procNFeZip=None, procNFe=None) -> TRetDownloadNFe.retNFe:
            return super().add(chNFe=chNFe, cStat=cStat, xMotivo=xMotivo, procNFeGrupoZip=procNFeGrupoZip, procNFeZip=procNFeZip, procNFe=procNFe)

        chNFe: TChNFe = Element(TChNFe, documentation=['Chaves de acesso da NF-e consultada'])
        cStat: TStat = Element(TStat, documentation=['Código do status da mensagem enviada.'])
        xMotivo: TMotivo = Element(TMotivo, documentation=['Descrição literal do status do serviço solicitado.'])

        class procNFeGrupoZip(ComplexType):
            NFeZip: base64Binary = Element(base64Binary, documentation=['XML NFe compactado no padrão gZIP'])
            protNFeZip: base64Binary = Element(base64Binary, documentation=['XML protNFe compactado no padrão gZIP'])
        procNFeGrupoZip: procNFeGrupoZip = Element(procNFeGrupoZip)
        procNFeZip: base64Binary = Element(base64Binary, documentation=['XML do procNFe compactado no padrão gZIP'])

        class procNFe(ComplexType):
            schema: str = Attribute(string)
        procNFe: procNFe = Element(procNFe)
    retNFe: List[retNFe] = Element(retNFe, max_occurs=10, documentation=['Conjunto de informação das  NF-e localizadas'])
    versao: str = Attribute(TVerDownloadNFe)


