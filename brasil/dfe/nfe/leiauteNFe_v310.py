from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposBasico_v310 import *


class TEndereco(Element):
    """Tipo Dados do Endereço  // 24/10/08 - tamanho mínimo"""
    xLgr: str = Element(str)
    nro: str = Element(str)
    xCpl: str = Element(str, min_occurs=0)
    xBairro: str = Element(str)
    cMun: TCodMunIBGE = Element(TCodMunIBGE)
    xMun: str = Element(str)
    UF: TUf = Element(TUf)
    CEP: str = Element(str, min_occurs=0)
    cPais: str = Element(str, min_occurs=0)
    xPais: str = Element(str, min_occurs=0)
    fone: str = Element(str, min_occurs=0)


class TEnderEmi(Element):
    """Tipo Dados do Endereço do Emitente  // 24/10/08 - desmembrado / tamanho mínimo"""
    xLgr: str = Element(str)
    nro: str = Element(str)
    xCpl: str = Element(str, min_occurs=0)
    xBairro: str = Element(str)
    cMun: TCodMunIBGE = Element(TCodMunIBGE)
    xMun: str = Element(str)
    UF: TUfEmi = Element(TUfEmi)
    CEP: str = Element(str)
    cPais: str = Element(str, min_occurs=0)
    xPais: str = Element(str, min_occurs=0)
    fone: str = Element(str, min_occurs=0)


class TLocal(Element):
    """Tipo Dados do Local de Retirada ou Entrega // 24/10/08 - tamanho mínimo // v2.0"""
    xLgr: str = Element(str)
    nro: str = Element(str)
    xCpl: str = Element(str, min_occurs=0)
    xBairro: str = Element(str)
    cMun: TCodMunIBGE = Element(TCodMunIBGE)
    xMun: str = Element(str)
    UF: TUf = Element(TUf)


class TFinNFe(str):
    """Tipo Finalidade da NF-e (1=Normal; 2=Complementar; 3=Ajuste; 4=Devolução/Retorno)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1', '2', '3', '4'])
    pass


class TProcEmi(str):
    """Tipo processo de emissão da NF-e"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['0', '1', '2', '3'])
    pass


class TVerNFe(str):
    """Tipo Versão da NF-e - 3.10"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"3\.10", enumeration=[])
    pass


class TGuid(str):
    """Identificador único (Globally Unique Identifier)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[A-F0-9]{8}-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{12}", enumeration=[])
    pass


class TNFe(Element):
    """Tipo Nota Fiscal Eletrônica"""
    class infNFe(ComplexType):
        class ide(ComplexType):
            """Informar apenas
para tpEmis diferente de 1"""
            cUF: TCodUfIBGE = Element(TCodUfIBGE)
            cNF: str = Element(str)
            natOp: str = Element(str)
            indPag: str = Element(str)
            mod: TMod = Element(TMod)
            serie: TSerie = Element(TSerie)
            nNF: TNF = Element(TNF)
            dhEmi: TDateTimeUTC = Element(TDateTimeUTC)
            dhSaiEnt: TDateTimeUTC = Element(TDateTimeUTC, min_occurs=0)
            tpNF: str = Element(str)
            idDest: str = Element(str)
            cMunFG: TCodMunIBGE = Element(TCodMunIBGE)
            tpImp: str = Element(str)
            tpEmis: str = Element(str)
            cDV: str = Element(str)
            tpAmb: TAmb = Element(TAmb)
            finNFe: TFinNFe = Element(TFinNFe)
            indFinal: str = Element(str)
            indPres: str = Element(str)
            procEmi: TProcEmi = Element(TProcEmi)
            verProc: str = Element(str)
            dhCont: TDateTimeUTC = Element(TDateTimeUTC)
            xJust: str = Element(str)
            class NFref(ComplexType):
                pass
            NFref: NFref
        ide: ide
        class emit(ComplexType):
            """Grupo de informações de interesse da Prefeitura"""
            xNome: str = Element(str)
            xFant: str = Element(str, min_occurs=0)
            enderEmit: TEnderEmi = Element(TEnderEmi)
            IE: TIe = Element(TIe)
            IEST: TIeST = Element(TIeST, min_occurs=0)
            IM: str = Element(str)
            CNAE: str = Element(str, min_occurs=0)
            CRT: str = Element(str)
        emit: emit
        class avulsa(ComplexType):
            CNPJ: TCnpj = Element(TCnpj)
            xOrgao: str = Element(str)
            matr: str = Element(str)
            xAgente: str = Element(str)
            fone: str = Element(str, min_occurs=0)
            UF: TUfEmi = Element(TUfEmi)
            nDAR: str = Element(str, min_occurs=0)
            dEmi: TData = Element(TData, min_occurs=0)
            vDAR: TDec_1302 = Element(TDec_1302, min_occurs=0)
            repEmi: str = Element(str)
            dPag: TData = Element(TData, min_occurs=0)
        avulsa: avulsa
        class dest(ComplexType):
            xNome: str = Element(str, min_occurs=0)
            enderDest: TEndereco = Element(TEndereco, min_occurs=0)
            indIEDest: str = Element(str)
            IE: TIeDestNaoIsento = Element(TIeDestNaoIsento, min_occurs=0)
            ISUF: str = Element(str, min_occurs=0)
            IM: str = Element(str, min_occurs=0)
            email: str = Element(str, min_occurs=0)
        dest: dest
        retirada: TLocal = Element(TLocal, min_occurs=0)
        entrega: TLocal = Element(TLocal, min_occurs=0)
        class autXML(ComplexType):
            pass
        autXML: autXML
        class det(ComplexType):
            class prod(ComplexType):
                cProd: str = Element(str)
                cEAN: str = Element(str)
                xProd: str = Element(str)
                NCM: str = Element(str)
                NVE: List[str] = Element(str, min_occurs=0, max_occurs=8)
                CEST: str = Element(str, min_occurs=0)
                EXTIPI: str = Element(str, min_occurs=0)
                CFOP: str = Element(str)
                uCom: str = Element(str)
                qCom: TDec_1104v = Element(TDec_1104v)
                vUnCom: TDec_1110v = Element(TDec_1110v)
                vProd: TDec_1302 = Element(TDec_1302)
                cEANTrib: str = Element(str)
                uTrib: str = Element(str)
                qTrib: TDec_1104v = Element(TDec_1104v)
                vUnTrib: TDec_1110v = Element(TDec_1110v)
                vFrete: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
                vSeg: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
                vDesc: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
                vOutro: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
                indTot: str = Element(str)
                class DI(ComplexType):
                    nDI: str = Element(str)
                    dDI: TData = Element(TData)
                    xLocDesemb: str = Element(str)
                    UFDesemb: TUfEmi = Element(TUfEmi)
                    dDesemb: TData = Element(TData)
                    tpViaTransp: str = Element(str)
                    vAFRMM: TDec_1302 = Element(TDec_1302, min_occurs=0)
                    tpIntermedio: str = Element(str)
                    CNPJ: TCnpj = Element(TCnpj, min_occurs=0)
                    UFTerceiro: TUfEmi = Element(TUfEmi, min_occurs=0)
                    cExportador: str = Element(str)
                    class adi(ComplexType):
                        nAdicao: str = Element(str)
                        nSeqAdic: str = Element(str)
                        cFabricante: str = Element(str)
                        vDescDI: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
                        nDraw: str = Element(str, min_occurs=0)
                    adi: adi
                DI: DI
                class detExport(ComplexType):
                    nDraw: str = Element(str, min_occurs=0)
                    class exportInd(ComplexType):
                        nRE: str = Element(str)
                        chNFe: TChNFe = Element(TChNFe)
                        qExport: TDec_1104v = Element(TDec_1104v)
                    exportInd: exportInd
                detExport: detExport
                xPed: str = Element(str, min_occurs=0)
                nItemPed: str = Element(str, min_occurs=0)
                nFCI: TGuid = Element(TGuid, min_occurs=0)
            prod: prod
            class imposto(ComplexType):
                vTotTrib: TDec_1302 = Element(TDec_1302, min_occurs=0)
                class PIS(ComplexType):
                    pass
                PIS: PIS
                class PISST(ComplexType):
                    vPIS: TDec_1302 = Element(TDec_1302)
                PISST: PISST
                class COFINS(ComplexType):
                    pass
                COFINS: COFINS
                class COFINSST(ComplexType):
                    vCOFINS: TDec_1302 = Element(TDec_1302)
                COFINSST: COFINSST
                class ICMSUFDest(ComplexType):
                    vBCUFDest: TDec_1302 = Element(TDec_1302)
                    pFCPUFDest: TDec_0302a04 = Element(TDec_0302a04)
                    pICMSUFDest: TDec_0302a04 = Element(TDec_0302a04)
                    pICMSInter: str = Element(str)
                    pICMSInterPart: TDec_0302a04 = Element(TDec_0302a04)
                    vFCPUFDest: TDec_1302 = Element(TDec_1302)
                    vICMSUFDest: TDec_1302 = Element(TDec_1302)
                    vICMSUFRemet: TDec_1302 = Element(TDec_1302)
                ICMSUFDest: ICMSUFDest
            imposto: imposto
            class impostoDevol(ComplexType):
                pDevol: TDec_0302Max100 = Element(TDec_0302Max100)
                class IPI(ComplexType):
                    vIPIDevol: TDec_1302 = Element(TDec_1302)
                IPI: IPI
            impostoDevol: impostoDevol
            infAdProd: str = Element(str, min_occurs=0)
            nItem: str = Attribute(None)
        det: det
        class total(ComplexType):
            class ICMSTot(ComplexType):
                vBC: TDec_1302 = Element(TDec_1302)
                vICMS: TDec_1302 = Element(TDec_1302)
                vICMSDeson: TDec_1302 = Element(TDec_1302)
                vFCPUFDest: TDec_1302 = Element(TDec_1302, min_occurs=0)
                vICMSUFDest: TDec_1302 = Element(TDec_1302, min_occurs=0)
                vICMSUFRemet: TDec_1302 = Element(TDec_1302, min_occurs=0)
                vBCST: TDec_1302 = Element(TDec_1302)
                vST: TDec_1302 = Element(TDec_1302)
                vProd: TDec_1302 = Element(TDec_1302)
                vFrete: TDec_1302 = Element(TDec_1302)
                vSeg: TDec_1302 = Element(TDec_1302)
                vDesc: TDec_1302 = Element(TDec_1302)
                vII: TDec_1302 = Element(TDec_1302)
                vIPI: TDec_1302 = Element(TDec_1302)
                vPIS: TDec_1302 = Element(TDec_1302)
                vCOFINS: TDec_1302 = Element(TDec_1302)
                vOutro: TDec_1302 = Element(TDec_1302)
                vNF: TDec_1302 = Element(TDec_1302)
                vTotTrib: TDec_1302 = Element(TDec_1302, min_occurs=0)
            ICMSTot: ICMSTot
            class ISSQNtot(ComplexType):
                vServ: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
                vBC: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
                vISS: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
                vPIS: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
                vCOFINS: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
                dCompet: TData = Element(TData)
                vDeducao: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
                vOutro: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
                vDescIncond: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
                vDescCond: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
                vISSRet: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
                cRegTrib: str = Element(str, min_occurs=0)
            ISSQNtot: ISSQNtot
            class retTrib(ComplexType):
                vRetPIS: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
                vRetCOFINS: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
                vRetCSLL: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
                vBCIRRF: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
                vIRRF: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
                vBCRetPrev: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
                vRetPrev: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
            retTrib: retTrib
        total: total
        class transp(ComplexType):
            modFrete: str = Element(str)
            class transporta(ComplexType):
                xNome: str = Element(str, min_occurs=0)
                IE: TIeDest = Element(TIeDest, min_occurs=0)
                xEnder: str = Element(str, min_occurs=0)
                xMun: str = Element(str, min_occurs=0)
                UF: TUf = Element(TUf, min_occurs=0)
            transporta: transporta
            class retTransp(ComplexType):
                vServ: TDec_1302 = Element(TDec_1302)
                vBCRet: TDec_1302 = Element(TDec_1302)
                pICMSRet: TDec_0302a04 = Element(TDec_0302a04)
                vICMSRet: TDec_1302 = Element(TDec_1302)
                CFOP: str = Element(str)
                cMunFG: TCodMunIBGE = Element(TCodMunIBGE)
            retTransp: retTransp
            class vol(ComplexType):
                qVol: str = Element(str, min_occurs=0)
                esp: str = Element(str, min_occurs=0)
                marca: str = Element(str, min_occurs=0)
                nVol: str = Element(str, min_occurs=0)
                pesoL: TDec_1203 = Element(TDec_1203, min_occurs=0)
                pesoB: TDec_1203 = Element(TDec_1203, min_occurs=0)
                class lacres(ComplexType):
                    nLacre: str = Element(str)
                lacres: lacres
            vol: vol
        transp: transp
        class cobr(ComplexType):
            class fat(ComplexType):
                nFat: str = Element(str, min_occurs=0)
                vOrig: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
                vDesc: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
                vLiq: TDec_1302Opc = Element(TDec_1302Opc, min_occurs=0)
            fat: fat
            class dup(ComplexType):
                nDup: str = Element(str, min_occurs=0)
                dVenc: TData = Element(TData, min_occurs=0)
                vDup: TDec_1302Opc = Element(TDec_1302Opc)
            dup: dup
        cobr: cobr
        class pag(ComplexType):
            tPag: str = Element(str)
            vPag: TDec_1302 = Element(TDec_1302)
            class card(ComplexType):
                tpIntegra: str = Element(str, min_occurs=0)
                CNPJ: TCnpj = Element(TCnpj, min_occurs=0)
                tBand: str = Element(str, min_occurs=0)
                cAut: str = Element(str, min_occurs=0)
            card: card
        pag: pag
        class infAdic(ComplexType):
            infAdFisco: str = Element(str, min_occurs=0)
            infCpl: str = Element(str, min_occurs=0)
            class obsCont(ComplexType):
                xTexto: str = Element(str)
                xCampo: str = Attribute(None)
            obsCont: obsCont
            class obsFisco(ComplexType):
                xTexto: str = Element(str)
                xCampo: str = Attribute(None)
            obsFisco: obsFisco
            class procRef(ComplexType):
                nProc: str = Element(str)
                indProc: str = Element(str)
            procRef: procRef
        infAdic: infAdic
        class exporta(ComplexType):
            UFSaidaPais: TUfEmi = Element(TUfEmi)
            xLocExporta: str = Element(str)
            xLocDespacho: str = Element(str, min_occurs=0)
        exporta: exporta
        class compra(ComplexType):
            xNEmp: str = Element(str, min_occurs=0)
            xPed: str = Element(str, min_occurs=0)
            xCont: str = Element(str, min_occurs=0)
        compra: compra
        class cana(ComplexType):
            safra: str = Element(str)
            ref: str = Element(str)
            class forDia(ComplexType):
                qtde: TDec_1110v = Element(TDec_1110v)
                dia: str = Attribute(None)
            forDia: forDia
            qTotMes: TDec_1110v = Element(TDec_1110v)
            qTotAnt: TDec_1110v = Element(TDec_1110v)
            qTotGer: TDec_1110v = Element(TDec_1110v)
            class deduc(ComplexType):
                xDed: str = Element(str)
                vDed: TDec_1302 = Element(TDec_1302)
            deduc: deduc
            vFor: TDec_1302 = Element(TDec_1302)
            vTotDed: TDec_1302 = Element(TDec_1302)
            vLiqFor: TDec_1302 = Element(TDec_1302)
        cana: cana
        versao: str = Attribute(TVerNFe)
        Id: str = Attribute(None)
    infNFe: infNFe
    class infNFeSupl(ComplexType):
        qrCode: str = Element(str)
    infNFeSupl: infNFeSupl
    Signature: Signature = Element(Signature)


class TProtNFe(Element):
    """Tipo Protocolo de status resultado do processamento da NF-e"""
    class infProt(ComplexType):
        tpAmb: TAmb = Element(TAmb)
        verAplic: TVerAplic = Element(TVerAplic)
        chNFe: TChNFe = Element(TChNFe)
        dhRecbto: TDateTimeUTC = Element(TDateTimeUTC)
        nProt: TProt = Element(TProt, min_occurs=0)
        digVal: DigestValueType = Element(DigestValueType, min_occurs=0)
        cStat: TStat = Element(TStat)
        xMotivo: TMotivo = Element(TMotivo)
        Id: str = Attribute(ID)
    infProt: infProt
    Signature: Signature = Element(Signature, min_occurs=0)
    versao: str = Attribute(TVerNFe)


class TIdLote(str):
    """Tipo Identificação de Lote"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{1,15}", enumeration=[])
    pass


class TEnviNFe(Element):
    """Tipo Pedido de Concessão de Autorização da Nota Fiscal Eletrônica"""
    idLote: TIdLote = Element(TIdLote)
    indSinc: str = Element(str)
    NFe: List[TNFe] = Element(TNFe, max_occurs=50)
    versao: str = Attribute(TVerNFe)


class TRetEnviNFe(Element):
    """Tipo Retorno do Pedido de Autorização da Nota Fiscal Eletrônica"""
    tpAmb: TAmb = Element(TAmb)
    verAplic: TVerAplic = Element(TVerAplic)
    cStat: TStat = Element(TStat)
    xMotivo: TMotivo = Element(TMotivo)
    cUF: TCodUfIBGE = Element(TCodUfIBGE)
    dhRecbto: TDateTimeUTC = Element(TDateTimeUTC)
    versao: str = Attribute(TVerNFe)


class TConsReciNFe(Element):
    """Tipo Pedido de Consulta do Recido do Lote de Notas Fiscais Eletrônicas"""
    tpAmb: TAmb = Element(TAmb)
    nRec: TRec = Element(TRec)
    versao: str = Attribute(TVerNFe)


class TRetConsReciNFe(Element):
    """Tipo Retorno do Pedido de  Consulta do Recido do Lote de Notas Fiscais Eletrônicas"""
    tpAmb: TAmb = Element(TAmb)
    verAplic: TVerAplic = Element(TVerAplic)
    nRec: TRec = Element(TRec)
    cStat: TStat = Element(TStat)
    xMotivo: TMotivo = Element(TMotivo)
    cUF: TCodUfIBGE = Element(TCodUfIBGE)
    dhRecbto: TDateTimeUTC = Element(TDateTimeUTC)
    cMsg: str = Element(str)
    xMsg: str = Element(str)
    protNFe: List[TProtNFe] = Element(TProtNFe, min_occurs=0, max_occurs=50)
    versao: str = Attribute(TVerNFe)


class TNfeProc(Element):
    """Tipo da NF-e processada"""
    NFe: TNFe = Element(TNFe)
    protNFe: TProtNFe = Element(TProtNFe)
    versao: str = Attribute(TVerNFe)


class TVeiculo(Element):
    """Tipo Dados do Veículo"""
    placa: str = Element(str)
    UF: TUf = Element(TUf)
    RNTC: str = Element(str, min_occurs=0)


class Torig(str):
    """Tipo Origem da mercadoria CST ICMS  origem da mercadoria: 0-Nacional exceto as indicadas nos códigos 3, 4, 5 e 8;
1-Estrangeira - Importação direta; 2-Estrangeira - Adquirida no mercado interno; 3-Nacional, conteudo superior 40% e inferior ou igual a 70%; 4-Nacional, processos produtivos básicos; 5-Nacional, conteudo inferior 40%; 6-Estrangeira - Importação direta, com similar nacional, lista CAMEX; 7-Estrangeira - mercado interno, sem simular,lista CAMEX;8-Nacional, Conteúdo de Importação superior a 70%."""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['0', '1', '2', '3', '4', '5', '6', '7', '8'])
    pass


class TCListServ(str):
    """Tipo Código da Lista de Serviços LC 116/2003"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['01.01', '01.02', '01.03', '01.04', '01.05', '01.06', '01.07', '01.08', '02.01', '03.02', '03.03', '03.04', '03.05', '04.01', '04.02', '04.03', '04.04', '04.05', '04.06', '04.07', '04.08', '04.09', '04.10', '04.11', '04.12', '04.13', '04.14', '04.15', '04.16', '04.17', '04.18', '04.19', '04.20', '04.21', '04.22', '04.23', '05.01', '05.02', '05.03', '05.04', '05.05', '05.06', '05.07', '05.08', '05.09', '06.01', '06.02', '06.03', '06.04', '06.05', '07.01', '07.02', '07.03', '07.04', '07.05', '07.06', '07.07', '07.08', '07.09', '07.10', '07.11', '07.12', '07.13', '07.16', '07.17', '07.18', '07.19', '07.20', '07.21', '07.22', '08.01', '08.02', '09.01', '09.02', '09.03', '10.01', '10.02', '10.03', '10.04', '10.05', '10.06', '10.07', '10.08', '10.09', '10.10', '11.01', '11.02', '11.03', '11.04', '12.01', '12.02', '12.03', '12.04', '12.05', '12.06', '12.07', '12.08', '12.09', '12.10', '12.11', '12.12', '12.13', '12.14', '12.15', '12.16', '12.17', '13.02', '13.03', '13.04', '13.05', '14.01', '14.02', '14.03', '14.04', '14.05', '14.06', '14.07', '14.08', '14.09', '14.10', '14.11', '14.12', '14.13', '15.01', '15.02', '15.03', '15.04', '15.05', '15.06', '15.07', '15.08', '15.09', '15.10', '15.11', '15.12', '15.13', '15.14', '15.15', '15.16', '15.17', '15.18', '16.01', '17.01', '17.02', '17.03', '17.04', '17.05', '17.06', '17.08', '17.09', '17.10', '17.11', '17.12', '17.13', '17.14', '17.15', '17.16', '17.17', '17.18', '17.19', '17.20', '17.21', '17.22', '17.23', '17.24', '18.01', '19.01', '20.01', '20.02', '20.03', '21.01', '22.01', '23.01', '24.01', '25.01', '25.02', '25.03', '25.04', '26.01', '27.01', '28.01', '29.01', '30.01', '31.01', '32.01', '33.01', '34.01', '35.01', '36.01', '37.01', '38.01', '39.01', '40.01'])
    pass


class TIpi(Element):
    """Tipo: Dados do IPI"""
    clEnq: str = Element(str, min_occurs=0)
    CNPJProd: TCnpj = Element(TCnpj, min_occurs=0)
    cSelo: str = Element(str, min_occurs=0)
    qSelo: str = Element(str, min_occurs=0)
    cEnq: str = Element(str)


