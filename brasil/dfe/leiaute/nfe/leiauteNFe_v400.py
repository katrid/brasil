from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposBasico_v400 import *



class TEndereco(Element):
    """Tipo Dados do Endereço  // 24/10/08 - tamanho mínimo"""
    xLgr: str = Element(str)
    nro: str = Element(str)
    xCpl: str = Element(str)
    xBairro: str = Element(str)
    cMun: TCodMunIBGE = Element(TCodMunIBGE)
    xMun: str = Element(str)
    UF: TUf = Element(TUf)
    CEP: str = Element(str)
    cPais: str = Element(str)
    xPais: str = Element(str)
    fone: str = Element(str)



class TEnderEmi(Element):
    """Tipo Dados do Endereço do Emitente  // 24/10/08 - desmembrado / tamanho mínimo"""
    xLgr: str = Element(str)
    nro: str = Element(str)
    xCpl: str = Element(str)
    xBairro: str = Element(str)
    cMun: TCodMunIBGE = Element(TCodMunIBGE)
    xMun: str = Element(str)
    UF: TUfEmi = Element(TUfEmi)
    CEP: str = Element(str)
    cPais: str = Element(str)
    xPais: str = Element(str)
    fone: str = Element(str)



class TLocal(Element):
    """Tipo Dados do Local de Retirada ou Entrega // 24/10/08 - tamanho mínimo // v2.0"""
    _choice = [['CNPJ', 'CPF']]
    CNPJ: TCnpjOpc = Element(TCnpjOpc)
    CPF: TCpf = Element(TCpf)
    xNome: str = Element(str)
    xLgr: str = Element(str)
    nro: str = Element(str)
    xCpl: str = Element(str)
    xBairro: str = Element(str)
    cMun: TCodMunIBGE = Element(TCodMunIBGE)
    xMun: str = Element(str)
    UF: TUf = Element(TUf)
    CEP: str = Element(str)
    cPais: str = Element(str)
    xPais: str = Element(str)
    fone: str = Element(str)
    email: str = Element(str)
    IE: TIe = Element(TIe)



class TInfRespTec(Element):
    """Grupo de informações do responsável técnico pelo sistema de emissão de DF-e"""
    CNPJ: TCnpjOpc = Element(TCnpjOpc)
    xContato: str = Element(str)
    email: str = Element(str)
    fone: str = Element(str)
    idCSRT: str = Element(str)
    hashCSRT: str = Element(str)



class TVeiculo(Element):
    """Tipo Dados do Veículo"""
    placa: str = Element(str)
    UF: TUf = Element(TUf)
    RNTC: str = Element(str)



class Torig(str):
    """Tipo Origem da mercadoria CST ICMS  origem da mercadoria: 0-Nacional exceto as indicadas nos códigos 3, 4, 5 e 8;
1-Estrangeira - Importação direta; 2-Estrangeira - Adquirida no mercado interno; 3-Nacional, conteudo superior 40% e inferior ou igual a 70%; 4-Nacional, processos produtivos básicos; 5-Nacional, conteudo inferior 40%; 6-Estrangeira - Importação direta, com similar nacional, lista CAMEX; 7-Estrangeira - mercado interno, sem simular,lista CAMEX;8-Nacional, Conteúdo de Importação superior a 70%."""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['0', '1', '2', '3', '4', '5', '6', '7', '8'])
    pass



class TFinNFe(str):
    """Tipo Finalidade da NF-e (1=Normal; 2=Complementar; 3=Ajuste; 4=Devolução/Retorno)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1', '2', '3', '4'])
    pass



class TProcEmi(str):
    """Tipo processo de emissão da NF-e"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['0', '1', '2', '3'])
    pass



class TCListServ(str):
    """Tipo Código da Lista de Serviços LC 116/2003"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['01.01', '01.02', '01.03', '01.04', '01.05', '01.06', '01.07', '01.08', '01.09', '02.01', '03.02', '03.03', '03.04', '03.05', '04.01', '04.02', '04.03', '04.04', '04.05', '04.06', '04.07', '04.08', '04.09', '04.10', '04.11', '04.12', '04.13', '04.14', '04.15', '04.16', '04.17', '04.18', '04.19', '04.20', '04.21', '04.22', '04.23', '05.01', '05.02', '05.03', '05.04', '05.05', '05.06', '05.07', '05.08', '05.09', '06.01', '06.02', '06.03', '06.04', '06.05', '06.06', '07.01', '07.02', '07.03', '07.04', '07.05', '07.06', '07.07', '07.08', '07.09', '07.10', '07.11', '07.12', '07.13', '07.16', '07.17', '07.18', '07.19', '07.20', '07.21', '07.22', '08.01', '08.02', '09.01', '09.02', '09.03', '10.01', '10.02', '10.03', '10.04', '10.05', '10.06', '10.07', '10.08', '10.09', '10.10', '11.01', '11.02', '11.03', '11.04', '12.01', '12.02', '12.03', '12.04', '12.05', '12.06', '12.07', '12.08', '12.09', '12.10', '12.11', '12.12', '12.13', '12.14', '12.15', '12.16', '12.17', '13.02', '13.03', '13.04', '13.05', '14.01', '14.02', '14.03', '14.04', '14.05', '14.06', '14.07', '14.08', '14.09', '14.10', '14.11', '14.12', '14.13', '14.14', '15.01', '15.02', '15.03', '15.04', '15.05', '15.06', '15.07', '15.08', '15.09', '15.10', '15.11', '15.12', '15.13', '15.14', '15.15', '15.16', '15.17', '15.18', '16.01', '16.02', '17.01', '17.02', '17.03', '17.04', '17.05', '17.06', '17.08', '17.09', '17.10', '17.11', '17.12', '17.13', '17.14', '17.15', '17.16', '17.17', '17.18', '17.19', '17.20', '17.21', '17.22', '17.23', '17.24', '17.25', '18.01', '19.01', '20.01', '20.02', '20.03', '21.01', '22.01', '23.01', '24.01', '25.01', '25.02', '25.03', '25.04', '25.05', '26.01', '27.01', '28.01', '29.01', '30.01', '31.01', '32.01', '33.01', '34.01', '35.01', '36.01', '37.01', '38.01', '39.01', '40.01'])
    pass



class TVerNFe(str):
    """Tipo Versão da NF-e - 4.00"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"4\.00", enumeration=[])
    pass



class TGuid(str):
    """Identificador único (Globally Unique Identifier)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[A-F0-9]{8}-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{12}", enumeration=[])
    pass



class TIpi(Element):
    """Tipo: Dados do IPI"""
    _choice = [['IPITrib', 'IPINT']]
    CNPJProd: TCnpj = Element(TCnpj)
    cSelo: str = Element(str)
    qSelo: str = Element(str)
    cEnq: str = Element(str)

    class IPITrib(ComplexType):
        _choice = [[]]
        CST: str = Element(str)
        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
        pIPI: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
        qUnid: TDec_1204v = Element(TDec_1204v, tipo="N", tam=(12, 4))
        vUnid: TDec_1104 = Element(TDec_1104, tipo="N", tam=(11, 4))
        vIPI: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
    IPITrib: IPITrib = Element(IPITrib)

    class IPINT(ComplexType):
        CST: str = Element(str)
    IPINT: IPINT = Element(IPINT)



class TNFe(Element):
    """Tipo Nota Fiscal Eletrônica"""

    class infNFe(ComplexType):
        """Informações da Nota Fiscal eletrônica"""

        class ide(ComplexType):
            """identificação da NF-e"""
            cUF: TCodUfIBGE = Element(TCodUfIBGE)
            cNF: str = Element(str)
            natOp: str = Element(str)
            mod: TMod = Element(TMod)
            serie: TSerie = Element(TSerie)
            nNF: TNF = Element(TNF)
            dhEmi: TDateTimeUTC = Element(TDateTimeUTC)
            dhSaiEnt: TDateTimeUTC = Element(TDateTimeUTC)
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
            indIntermed: str = Element(str)
            procEmi: TProcEmi = Element(TProcEmi)
            verProc: str = Element(str)
            dhCont: TDateTimeUTC = Element(TDateTimeUTC)
            xJust: str = Element(str)

            class NFref(ComplexType):
                """Grupo de infromações da NF referenciada"""
                _max_occurs = 500
                _choice = [['refNFe', 'refNF', 'refNFP', 'refCTe', 'refECF']]

                def add(self, refNFe=None, refNF=None, refNFP=None, refCTe=None, refECF=None) -> TNFe.infNFe.ide.NFref:
                    return super().add(refNFe=refNFe, refNF=refNF, refNFP=refNFP, refCTe=refCTe, refECF=refECF)

                refNFe: TChNFe = Element(TChNFe)

                class refNF(ComplexType):
                    """Dados da NF modelo 1/1A referenciada ou NF modelo 2 referenciada"""
                    cUF: TCodUfIBGE = Element(TCodUfIBGE)
                    AAMM: str = Element(str)
                    CNPJ: TCnpj = Element(TCnpj)
                    mod: str = Element(str)
                    serie: TSerie = Element(TSerie)
                    nNF: TNF = Element(TNF)
                refNF: refNF = Element(refNF)

                class refNFP(ComplexType):
                    """Grupo com as informações NF de produtor referenciada"""
                    _choice = [['CNPJ', 'CPF']]
                    cUF: TCodUfIBGE = Element(TCodUfIBGE)
                    AAMM: str = Element(str)
                    CNPJ: TCnpj = Element(TCnpj)
                    CPF: TCpf = Element(TCpf)
                    IE: TIeDest = Element(TIeDest)
                    mod: str = Element(str)
                    serie: TSerie = Element(TSerie)
                    nNF: TNF = Element(TNF)
                refNFP: refNFP = Element(refNFP)
                refCTe: TChNFe = Element(TChNFe)

                class refECF(ComplexType):
                    """Grupo do Cupom Fiscal vinculado à NF-e"""
                    mod: str = Element(str)
                    nECF: str = Element(str)
                    nCOO: str = Element(str)
                refECF: refECF = Element(refECF)
            NFref: List[NFref] = Element(NFref, max_occurs=500)
        ide: ide = Element(ide)

        class emit(ComplexType):
            """Identificação do emitente"""
            _choice = [['CNPJ', 'CPF']]
            CNPJ: TCnpj = Element(TCnpj)
            CPF: TCpf = Element(TCpf)
            xNome: str = Element(str)
            xFant: str = Element(str)
            enderEmit: TEnderEmi = Element(TEnderEmi)
            IE: TIe = Element(TIe)
            IEST: TIeST = Element(TIeST)
            IM: str = Element(str)
            CNAE: str = Element(str)
            CRT: str = Element(str)
        emit: emit = Element(emit)

        class avulsa(ComplexType):
            """Emissão de avulsa, informar os dados do Fisco emitente"""
            CNPJ: TCnpj = Element(TCnpj)
            xOrgao: str = Element(str)
            matr: str = Element(str)
            xAgente: str = Element(str)
            fone: str = Element(str)
            UF: TUfEmi = Element(TUfEmi)
            nDAR: str = Element(str)
            dEmi: TData = Element(TData)
            vDAR: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
            repEmi: str = Element(str)
            dPag: TData = Element(TData)
        avulsa: avulsa = Element(avulsa)

        class dest(ComplexType):
            """Identificação do Destinatário"""
            _choice = [['CNPJ', 'CPF', 'idEstrangeiro']]
            CNPJ: TCnpj = Element(TCnpj)
            CPF: TCpf = Element(TCpf)
            idEstrangeiro: str = Element(str)
            xNome: str = Element(str)
            enderDest: TEndereco = Element(TEndereco)
            indIEDest: str = Element(str)
            IE: TIeDestNaoIsento = Element(TIeDestNaoIsento)
            ISUF: str = Element(str)
            IM: str = Element(str)
            email: str = Element(str)
        dest: dest = Element(dest)
        retirada: TLocal = Element(TLocal)
        entrega: TLocal = Element(TLocal)

        class autXML(ComplexType):
            """Pessoas autorizadas para o download do XML da NF-e"""
            _max_occurs = 10
            _choice = [['CNPJ', 'CPF']]

            def add(self, CNPJ=None, CPF=None) -> TNFe.infNFe.autXML:
                return super().add(CNPJ=CNPJ, CPF=CPF)

            CNPJ: TCnpj = Element(TCnpj)
            CPF: TCpf = Element(TCpf)
        autXML: List[autXML] = Element(autXML, max_occurs=10)

        class det(ComplexType):
            """Dados dos detalhes da NF-e"""
            _max_occurs = 990

            def add(self, prod=None, imposto=None, impostoDevol=None, infAdProd=None, nItem=None) -> TNFe.infNFe.det:
                return super().add(prod=prod, imposto=imposto, impostoDevol=impostoDevol, infAdProd=infAdProd, nItem=nItem)


            class prod(ComplexType):
                """Dados dos produtos e serviços da NF-e"""
                _choice = [['veicProd', 'med', 'arma', 'comb', 'nRECOPI']]
                cProd: str = Element(str)
                cEAN: str = Element(str)
                cBarra: str = Element(str)
                xProd: str = Element(str)
                NCM: str = Element(str)
                NVE: List[str] = Element(str, max_occurs=8)
                CEST: str = Element(str)
                indEscala: str = Element(str)
                CNPJFab: TCnpj = Element(TCnpj)
                cBenef: str = Element(str)
                EXTIPI: str = Element(str)
                CFOP: str = Element(str)
                uCom: str = Element(str)
                qCom: TDec_1104v = Element(TDec_1104v, tipo="N", tam=(11, 4))
                vUnCom: TDec_1110v = Element(TDec_1110v, tipo="N", tam=(11, 10))
                vProd: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                cEANTrib: str = Element(str)
                cBarraTrib: str = Element(str)
                uTrib: str = Element(str)
                qTrib: TDec_1104v = Element(TDec_1104v, tipo="N", tam=(11, 4))
                vUnTrib: TDec_1110v = Element(TDec_1110v, tipo="N", tam=(11, 10))
                vFrete: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                vSeg: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                vDesc: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                vOutro: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                indTot: str = Element(str)

                class DI(ComplexType):
                    """Delcaração de Importação
(NT 2011/004)"""
                    _max_occurs = 100

                    def add(self, nDI=None, dDI=None, xLocDesemb=None, UFDesemb=None, dDesemb=None, tpViaTransp=None, vAFRMM=None, tpIntermedio=None, CNPJ=None, UFTerceiro=None, cExportador=None, adi=None) -> TNFe.infNFe.det.prod.DI:
                        return super().add(nDI=nDI, dDI=dDI, xLocDesemb=xLocDesemb, UFDesemb=UFDesemb, dDesemb=dDesemb, tpViaTransp=tpViaTransp, vAFRMM=vAFRMM, tpIntermedio=tpIntermedio, CNPJ=CNPJ, UFTerceiro=UFTerceiro, cExportador=cExportador, adi=adi)

                    nDI: str = Element(str)
                    dDI: TData = Element(TData)
                    xLocDesemb: str = Element(str)
                    UFDesemb: TUfEmi = Element(TUfEmi)
                    dDesemb: TData = Element(TData)
                    tpViaTransp: str = Element(str)
                    vAFRMM: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    tpIntermedio: str = Element(str)
                    CNPJ: TCnpj = Element(TCnpj)
                    UFTerceiro: TUfEmi = Element(TUfEmi)
                    cExportador: str = Element(str)

                    class adi(ComplexType):
                        """Adições (NT 2011/004)"""
                        _max_occurs = 999

                        def add(self, nAdicao=None, nSeqAdic=None, cFabricante=None, vDescDI=None, nDraw=None) -> TNFe.infNFe.det.prod.DI.adi:
                            return super().add(nAdicao=nAdicao, nSeqAdic=nSeqAdic, cFabricante=cFabricante, vDescDI=vDescDI, nDraw=nDraw)

                        nAdicao: str = Element(str)
                        nSeqAdic: str = Element(str)
                        cFabricante: str = Element(str)
                        vDescDI: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                        nDraw: str = Element(str)
                    adi: List[adi] = Element(adi, max_occurs=999)
                DI: List[DI] = Element(DI, max_occurs=100)

                class detExport(ComplexType):
                    """Detalhe da exportação"""
                    _max_occurs = 500

                    def add(self, nDraw=None, exportInd=None) -> TNFe.infNFe.det.prod.detExport:
                        return super().add(nDraw=nDraw, exportInd=exportInd)

                    nDraw: str = Element(str)

                    class exportInd(ComplexType):
                        """Exportação indireta"""
                        nRE: str = Element(str)
                        chNFe: TChNFe = Element(TChNFe)
                        qExport: TDec_1104v = Element(TDec_1104v, tipo="N", tam=(11, 4))
                    exportInd: exportInd = Element(exportInd)
                detExport: List[detExport] = Element(detExport, max_occurs=500)
                xPed: str = Element(str)
                nItemPed: str = Element(str)
                nFCI: TGuid = Element(TGuid)

                class rastro(ComplexType):
                    _max_occurs = 500

                    def add(self, nLote=None, qLote=None, dFab=None, dVal=None, cAgreg=None) -> TNFe.infNFe.det.prod.rastro:
                        return super().add(nLote=nLote, qLote=qLote, dFab=dFab, dVal=dVal, cAgreg=cAgreg)

                    nLote: str = Element(str)
                    qLote: TDec_0803v = Element(TDec_0803v, tipo="N", tam=(8, 3))
                    dFab: TData = Element(TData)
                    dVal: TData = Element(TData)
                    cAgreg: str = Element(str)
                rastro: List[rastro] = Element(rastro, max_occurs=500)

                class veicProd(ComplexType):
                    """Veículos novos"""
                    tpOp: str = Element(str)
                    chassi: str = Element(str)
                    cCor: str = Element(str)
                    xCor: str = Element(str)
                    pot: str = Element(str)
                    cilin: str = Element(str)
                    pesoL: str = Element(str)
                    pesoB: str = Element(str)
                    nSerie: str = Element(str)
                    tpComb: str = Element(str)
                    nMotor: str = Element(str)
                    CMT: str = Element(str)
                    dist: str = Element(str)
                    anoMod: str = Element(str)
                    anoFab: str = Element(str)
                    tpPint: str = Element(str)
                    tpVeic: str = Element(str)
                    espVeic: str = Element(str)
                    VIN: str = Element(str)
                    condVeic: str = Element(str)
                    cMod: str = Element(str)
                    cCorDENATRAN: str = Element(str)
                    lota: str = Element(str)
                    tpRest: str = Element(str)
                veicProd: veicProd = Element(veicProd)

                class med(ComplexType):
                    """grupo do detalhamento de Medicamentos e de matérias-primas farmacêuticas"""
                    cProdANVISA: str = Element(str)
                    xMotivoIsencao: str = Element(str)
                    vPMC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                med: med = Element(med)

                class arma(ComplexType):
                    """Armamentos"""
                    _max_occurs = 500

                    def add(self, tpArma=None, nSerie=None, nCano=None, descr=None) -> TNFe.infNFe.det.prod.arma:
                        return super().add(tpArma=tpArma, nSerie=nSerie, nCano=nCano, descr=descr)

                    tpArma: str = Element(str)
                    nSerie: str = Element(str)
                    nCano: str = Element(str)
                    descr: str = Element(str)
                arma: List[arma] = Element(arma, max_occurs=500)

                class comb(ComplexType):
                    """Informar apenas para operações com combustíveis líquidos"""
                    cProdANP: str = Element(str)
                    descANP: str = Element(str)
                    pGLP: TDec_0302a04Max100 = Element(TDec_0302a04Max100, tipo="N", tam=(3, 2))
                    pGNn: TDec_0302a04Max100 = Element(TDec_0302a04Max100, tipo="N", tam=(3, 2))
                    pGNi: TDec_0302a04Max100 = Element(TDec_0302a04Max100, tipo="N", tam=(3, 2))
                    vPart: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    CODIF: str = Element(str)
                    qTemp: TDec_1204temperatura = Element(TDec_1204temperatura, tipo="N", tam=(12, 4))
                    UFCons: TUf = Element(TUf)

                    class CIDE(ComplexType):
                        """CIDE Combustíveis"""
                        qBCProd: TDec_1204v = Element(TDec_1204v, tipo="N", tam=(12, 4))
                        vAliqProd: TDec_1104 = Element(TDec_1104, tipo="N", tam=(11, 4))
                        vCIDE: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    CIDE: CIDE = Element(CIDE)

                    class encerrante(ComplexType):
                        """Informações do grupo de \"encerrante\""""
                        nBico: str = Element(str)
                        nBomba: str = Element(str)
                        nTanque: str = Element(str)
                        vEncIni: TDec_1203 = Element(TDec_1203, tipo="N", tam=(12, 3))
                        vEncFin: TDec_1203 = Element(TDec_1203, tipo="N", tam=(12, 3))
                    encerrante: encerrante = Element(encerrante)
                comb: comb = Element(comb)
                nRECOPI: str = Element(str)
            prod: prod = Element(prod)

            class imposto(ComplexType):
                """Tributos incidentes nos produtos ou serviços da NF-e"""
                _choice = [[]]
                vTotTrib: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))

                class ICMS(ComplexType):
                    """Dados do ICMS Normal e ST"""
                    _choice = [['ICMS00', 'ICMS10', 'ICMS20', 'ICMS30', 'ICMS40', 'ICMS51', 'ICMS60', 'ICMS70', 'ICMS90', 'ICMSPart', 'ICMSST', 'ICMSSN101', 'ICMSSN102', 'ICMSSN201', 'ICMSSN202', 'ICMSSN500', 'ICMSSN900']]

                    class ICMS00(ComplexType):
                        """Tributação pelo ICMS
00 - Tributada integralmente"""
                        orig: Torig = Element(Torig)
                        CST: str = Element(str)
                        modBC: str = Element(str)
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pICMS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pFCP: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vFCP: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    ICMS00: ICMS00 = Element(ICMS00)

                    class ICMS10(ComplexType):
                        """Tributação pelo ICMS
10 - Tributada e com cobrança do ICMS por substituição tributária"""
                        orig: Torig = Element(Torig)
                        CST: str = Element(str)
                        modBC: str = Element(str)
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pICMS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vBCFCP: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pFCP: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vFCP: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        modBCST: str = Element(str)
                        pMVAST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        pRedBCST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vBCST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pICMSST: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vICMSST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vBCFCPST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pFCPST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vFCPST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vICMSSTDeson: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        motDesICMSST: str = Element(str)
                    ICMS10: ICMS10 = Element(ICMS10)

                    class ICMS20(ComplexType):
                        """Tributção pelo ICMS
20 - Com redução de base de cálculo"""
                        orig: Torig = Element(Torig)
                        CST: str = Element(str)
                        modBC: str = Element(str)
                        pRedBC: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pICMS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vBCFCP: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pFCP: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vFCP: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vICMSDeson: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        motDesICMS: str = Element(str)
                    ICMS20: ICMS20 = Element(ICMS20)

                    class ICMS30(ComplexType):
                        """Tributação pelo ICMS
30 - Isenta ou não tributada e com cobrança do ICMS por substituição tributária"""
                        orig: Torig = Element(Torig)
                        CST: str = Element(str)
                        modBCST: str = Element(str)
                        pMVAST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        pRedBCST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vBCST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pICMSST: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vICMSST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vBCFCPST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pFCPST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vFCPST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vICMSDeson: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        motDesICMS: str = Element(str)
                    ICMS30: ICMS30 = Element(ICMS30)

                    class ICMS40(ComplexType):
                        """Tributação pelo ICMS
40 - Isenta 
41 - Não tributada 
50 - Suspensão"""
                        orig: Torig = Element(Torig)
                        CST: str = Element(str)
                        vICMSDeson: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        motDesICMS: str = Element(str)
                    ICMS40: ICMS40 = Element(ICMS40)

                    class ICMS51(ComplexType):
                        """Tributção pelo ICMS
51 - Diferimento
A exigência do preenchimento das informações do ICMS diferido fica à critério de cada UF."""
                        orig: Torig = Element(Torig)
                        CST: str = Element(str)
                        modBC: str = Element(str)
                        pRedBC: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pICMS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vICMSOp: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pDif: TDec_0302a04Max100 = Element(TDec_0302a04Max100, tipo="N", tam=(3, 2))
                        vICMSDif: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vBCFCP: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pFCP: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vFCP: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pFCPDif: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vFCPDif: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vFCPEfet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    ICMS51: ICMS51 = Element(ICMS51)

                    class ICMS60(ComplexType):
                        """Tributação pelo ICMS
60 - ICMS cobrado anteriormente por substituição tributária"""
                        orig: Torig = Element(Torig)
                        CST: str = Element(str)
                        vBCSTRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vICMSSubstituto: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vICMSSTRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vBCFCPSTRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pFCPSTRet: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vFCPSTRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pRedBCEfet: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vBCEfet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pICMSEfet: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vICMSEfet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    ICMS60: ICMS60 = Element(ICMS60)

                    class ICMS70(ComplexType):
                        """Tributação pelo ICMS 
70 - Com redução de base de cálculo e cobrança do ICMS por substituição tributária"""
                        orig: Torig = Element(Torig)
                        CST: str = Element(str)
                        modBC: str = Element(str)
                        pRedBC: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pICMS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vBCFCP: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pFCP: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vFCP: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        modBCST: str = Element(str)
                        pMVAST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        pRedBCST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vBCST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pICMSST: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vICMSST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vBCFCPST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pFCPST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vFCPST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vICMSDeson: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        motDesICMS: str = Element(str)
                        vICMSSTDeson: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        motDesICMSST: str = Element(str)
                    ICMS70: ICMS70 = Element(ICMS70)

                    class ICMS90(ComplexType):
                        """Tributação pelo ICMS
90 - Outras"""
                        orig: Torig = Element(Torig)
                        CST: str = Element(str)
                        modBC: str = Element(str)
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pRedBC: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        pICMS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vBCFCP: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pFCP: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vFCP: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        modBCST: str = Element(str)
                        pMVAST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        pRedBCST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vBCST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pICMSST: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vICMSST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vBCFCPST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pFCPST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vFCPST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vICMSDeson: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        motDesICMS: str = Element(str)
                        vICMSSTDeson: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        motDesICMSST: str = Element(str)
                    ICMS90: ICMS90 = Element(ICMS90)

                    class ICMSPart(ComplexType):
                        """Partilha do ICMS entre a UF de origem e UF de destino ou a UF definida na legislação
Operação interestadual para consumidor final com partilha do ICMS  devido na operação entre a UF de origem e a UF do destinatário ou ou a UF definida na legislação. (Ex. UF da concessionária de entrega do  veículos)"""
                        orig: Torig = Element(Torig)
                        CST: str = Element(str)
                        modBC: str = Element(str)
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pRedBC: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        pICMS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        modBCST: str = Element(str)
                        pMVAST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        pRedBCST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vBCST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pICMSST: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vICMSST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pBCOp: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        UFST: TUf = Element(TUf)
                    ICMSPart: ICMSPart = Element(ICMSPart)

                    class ICMSST(ComplexType):
                        """Grupo de informação do ICMSST devido para a UF de destino, nas operações interestaduais de produtos que tiveram retenção antecipada de ICMS por ST na UF do remetente. Repasse via Substituto Tributário."""
                        orig: Torig = Element(Torig)
                        CST: str = Element(str)
                        vBCSTRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vICMSSubstituto: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vICMSSTRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vBCFCPSTRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pFCPSTRet: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vFCPSTRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vBCSTDest: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vICMSSTDest: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pRedBCEfet: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vBCEfet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pICMSEfet: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vICMSEfet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    ICMSST: ICMSST = Element(ICMSST)

                    class ICMSSN101(ComplexType):
                        """Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=101 (v.2.0)"""
                        orig: Torig = Element(Torig)
                        CSOSN: str = Element(str)
                        pCredSN: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vCredICMSSN: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    ICMSSN101: ICMSSN101 = Element(ICMSSN101)

                    class ICMSSN102(ComplexType):
                        """Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=102, 103, 300 ou 400 (v.2.0))"""
                        orig: Torig = Element(Torig)
                        CSOSN: str = Element(str)
                    ICMSSN102: ICMSSN102 = Element(ICMSSN102)

                    class ICMSSN201(ComplexType):
                        """Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=201 (v.2.0)"""
                        orig: Torig = Element(Torig)
                        CSOSN: str = Element(str)
                        modBCST: str = Element(str)
                        pMVAST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        pRedBCST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vBCST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pICMSST: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vICMSST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vBCFCPST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pFCPST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vFCPST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pCredSN: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vCredICMSSN: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    ICMSSN201: ICMSSN201 = Element(ICMSSN201)

                    class ICMSSN202(ComplexType):
                        """Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=202 ou 203 (v.2.0)"""
                        orig: Torig = Element(Torig)
                        CSOSN: str = Element(str)
                        modBCST: str = Element(str)
                        pMVAST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        pRedBCST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vBCST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pICMSST: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vICMSST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vBCFCPST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pFCPST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vFCPST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    ICMSSN202: ICMSSN202 = Element(ICMSSN202)

                    class ICMSSN500(ComplexType):
                        """Tributação do ICMS pelo SIMPLES NACIONAL,CRT=1 – Simples Nacional e CSOSN=500 (v.2.0)"""
                        orig: Torig = Element(Torig)
                        CSOSN: str = Element(str)
                        vBCSTRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vICMSSubstituto: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vICMSSTRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vBCFCPSTRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pFCPSTRet: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vFCPSTRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pRedBCEfet: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vBCEfet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pICMSEfet: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vICMSEfet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    ICMSSN500: ICMSSN500 = Element(ICMSSN500)

                    class ICMSSN900(ComplexType):
                        """Tributação do ICMS pelo SIMPLES NACIONAL, CRT=1 – Simples Nacional e CSOSN=900 (v2.0)"""
                        orig: Torig = Element(Torig)
                        CSOSN: str = Element(str)
                        modBC: str = Element(str)
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pRedBC: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        pICMS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        modBCST: str = Element(str)
                        pMVAST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        pRedBCST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vBCST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pICMSST: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vICMSST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        vBCFCPST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pFCPST: TDec_0302a04Opc = Element(TDec_0302a04Opc, tipo="N", tam=(3, 2))
                        vFCPST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pCredSN: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vCredICMSSN: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    ICMSSN900: ICMSSN900 = Element(ICMSSN900)
                ICMS: ICMS = Element(ICMS)
                IPI: TIpi = Element(TIpi)

                class II(ComplexType):
                    """Dados do Imposto de Importação"""
                    vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    vDespAdu: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    vII: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    vIOF: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                II: II = Element(II)
                IPI: TIpi = Element(TIpi)

                class ISSQN(ComplexType):
                    """ISSQN"""
                    vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    vAliq: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                    vISSQN: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    cMunFG: TCodMunIBGE = Element(TCodMunIBGE)
                    cListServ: TCListServ = Element(TCListServ)
                    vDeducao: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                    vOutro: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                    vDescIncond: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                    vDescCond: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                    vISSRet: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                    indISS: str = Element(str)
                    cServico: str = Element(str)
                    cMun: TCodMunIBGE = Element(TCodMunIBGE)
                    cPais: str = Element(str)
                    nProcesso: str = Element(str)
                    indIncentivo: str = Element(str)
                ISSQN: ISSQN = Element(ISSQN)

                class PIS(ComplexType):
                    """Dados do PIS"""
                    _choice = [['PISAliq', 'PISQtde', 'PISNT', 'PISOutr']]

                    class PISAliq(ComplexType):
                        """Código de Situação Tributária do PIS.
 01 – Operação Tributável - Base de Cálculo = Valor da Operação Alíquota Normal (Cumulativo/Não Cumulativo);
02 - Operação Tributável - Base de Calculo = Valor da Operação (Alíquota Diferenciada);"""
                        CST: str = Element(str)
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pPIS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vPIS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    PISAliq: PISAliq = Element(PISAliq)

                    class PISQtde(ComplexType):
                        """Código de Situação Tributária do PIS.
03 - Operação Tributável - Base de Calculo = Quantidade Vendida x Alíquota por Unidade de Produto;"""
                        CST: str = Element(str)
                        qBCProd: TDec_1204v = Element(TDec_1204v, tipo="N", tam=(12, 4))
                        vAliqProd: TDec_1104v = Element(TDec_1104v, tipo="N", tam=(11, 4))
                        vPIS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    PISQtde: PISQtde = Element(PISQtde)

                    class PISNT(ComplexType):
                        """Código de Situação Tributária do PIS.
04 - Operação Tributável - Tributação Monofásica - (Alíquota Zero);
06 - Operação Tributável - Alíquota Zero;
07 - Operação Isenta da contribuição;
08 - Operação Sem Incidência da contribuição;
09 - Operação com suspensão da contribuição;"""
                        CST: str = Element(str)
                    PISNT: PISNT = Element(PISNT)

                    class PISOutr(ComplexType):
                        """Código de Situação Tributária do PIS.
99 - Outras Operações."""
                        _choice = [[]]
                        CST: str = Element(str)
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pPIS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        qBCProd: TDec_1204v = Element(TDec_1204v, tipo="N", tam=(12, 4))
                        vAliqProd: TDec_1104v = Element(TDec_1104v, tipo="N", tam=(11, 4))
                        vPIS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    PISOutr: PISOutr = Element(PISOutr)
                PIS: PIS = Element(PIS)

                class PISST(ComplexType):
                    """Dados do PIS Substituição Tributária"""
                    _choice = [[]]
                    vBC: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                    pPIS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                    qBCProd: TDec_1204 = Element(TDec_1204, tipo="N", tam=(12, 4))
                    vAliqProd: TDec_1104 = Element(TDec_1104, tipo="N", tam=(11, 4))
                    vPIS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    indSomaPISST: str = Element(str)
                PISST: PISST = Element(PISST)

                class COFINS(ComplexType):
                    """Dados do COFINS"""
                    _choice = [['COFINSAliq', 'COFINSQtde', 'COFINSNT', 'COFINSOutr']]

                    class COFINSAliq(ComplexType):
                        """Código de Situação Tributária do COFINS.
 01 – Operação Tributável - Base de Cálculo = Valor da Operação Alíquota Normal (Cumulativo/Não Cumulativo);
02 - Operação Tributável - Base de Calculo = Valor da Operação (Alíquota Diferenciada);"""
                        CST: str = Element(str)
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pCOFINS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        vCOFINS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    COFINSAliq: COFINSAliq = Element(COFINSAliq)

                    class COFINSQtde(ComplexType):
                        """Código de Situação Tributária do COFINS.
03 - Operação Tributável - Base de Calculo = Quantidade Vendida x Alíquota por Unidade de Produto;"""
                        CST: str = Element(str)
                        qBCProd: TDec_1204v = Element(TDec_1204v, tipo="N", tam=(12, 4))
                        vAliqProd: TDec_1104v = Element(TDec_1104v, tipo="N", tam=(11, 4))
                        vCOFINS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    COFINSQtde: COFINSQtde = Element(COFINSQtde)

                    class COFINSNT(ComplexType):
                        """Código de Situação Tributária do COFINS:
04 - Operação Tributável - Tributação Monofásica - (Alíquota Zero);
06 - Operação Tributável - Alíquota Zero;
07 - Operação Isenta da contribuição;
08 - Operação Sem Incidência da contribuição;
09 - Operação com suspensão da contribuição;"""
                        CST: str = Element(str)
                    COFINSNT: COFINSNT = Element(COFINSNT)

                    class COFINSOutr(ComplexType):
                        """Código de Situação Tributária do COFINS:
49 - Outras Operações de Saída
50 - Operação com Direito a Crédito - Vinculada Exclusivamente a Receita Tributada no Mercado Interno
51 - Operação com Direito a Crédito – Vinculada Exclusivamente a Receita Não Tributada no Mercado Interno
52 - Operação com Direito a Crédito - Vinculada Exclusivamente a Receita de Exportação
53 - Operação com Direito a Crédito - Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno
54 - Operação com Direito a Crédito - Vinculada a Receitas Tributadas no Mercado Interno e de Exportação
55 - Operação com Direito a Crédito - Vinculada a Receitas Não-Tributadas no Mercado Interno e de Exportação
56 - Operação com Direito a Crédito - Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno, e de Exportação
60 - Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita Tributada no Mercado Interno
61 - Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita Não-Tributada no Mercado Interno
62 - Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita de Exportação
63 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno
64 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas no Mercado Interno e de Exportação
65 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas Não-Tributadas no Mercado Interno e de Exportação
66 - Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno, e de Exportação
67 - Crédito Presumido - Outras Operações
70 - Operação de Aquisição sem Direito a Crédito
71 - Operação de Aquisição com Isenção
72 - Operação de Aquisição com Suspensão
73 - Operação de Aquisição a Alíquota Zero
74 - Operação de Aquisição sem Incidência da Contribuição
75 - Operação de Aquisição por Substituição Tributária
98 - Outras Operações de Entrada
99 - Outras Operações."""
                        _choice = [[]]
                        CST: str = Element(str)
                        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        pCOFINS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                        qBCProd: TDec_1204v = Element(TDec_1204v, tipo="N", tam=(12, 4))
                        vAliqProd: TDec_1104v = Element(TDec_1104v, tipo="N", tam=(11, 4))
                        vCOFINS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    COFINSOutr: COFINSOutr = Element(COFINSOutr)
                COFINS: COFINS = Element(COFINS)

                class COFINSST(ComplexType):
                    """Dados do COFINS da
Substituição Tributaria;"""
                    _choice = [[]]
                    vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    pCOFINS: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                    qBCProd: TDec_1204 = Element(TDec_1204, tipo="N", tam=(12, 4))
                    vAliqProd: TDec_1104 = Element(TDec_1104, tipo="N", tam=(11, 4))
                    vCOFINS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    indSomaCOFINSST: str = Element(str)
                COFINSST: COFINSST = Element(COFINSST)

                class ICMSUFDest(ComplexType):
                    """Grupo a ser informado nas vendas interestarduais para consumidor final, não contribuinte de ICMS"""
                    vBCUFDest: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    vBCFCPUFDest: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    pFCPUFDest: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                    pICMSUFDest: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                    pICMSInter: str = Element(str)
                    pICMSInterPart: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                    vFCPUFDest: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    vICMSUFDest: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    vICMSUFRemet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                ICMSUFDest: ICMSUFDest = Element(ICMSUFDest)
            imposto: imposto = Element(imposto)

            class impostoDevol(ComplexType):
                pDevol: TDec_0302Max100 = Element(TDec_0302Max100, tipo="N", tam=(3, 2))

                class IPI(ComplexType):
                    """Informação de IPI devolvido"""
                    vIPIDevol: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                IPI: IPI = Element(IPI)
            impostoDevol: impostoDevol = Element(impostoDevol)
            infAdProd: str = Element(str)
            nItem: str = Attribute(None)
        det: List[det] = Element(det, max_occurs=990)

        class total(ComplexType):
            """Dados dos totais da NF-e"""

            class ICMSTot(ComplexType):
                """Totais referentes ao ICMS"""
                vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vICMSDeson: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vFCPUFDest: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vICMSUFDest: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vICMSUFRemet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vFCP: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vBCST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vFCPST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vFCPSTRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vProd: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vFrete: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vSeg: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vDesc: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vII: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vIPI: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vIPIDevol: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vPIS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vCOFINS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vOutro: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vNF: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vTotTrib: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
            ICMSTot: ICMSTot = Element(ICMSTot)

            class ISSQNtot(ComplexType):
                """Totais referentes ao ISSQN"""
                vServ: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                vBC: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                vISS: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                vPIS: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                vCOFINS: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                dCompet: TData = Element(TData)
                vDeducao: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                vOutro: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                vDescIncond: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                vDescCond: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                vISSRet: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                cRegTrib: str = Element(str)
            ISSQNtot: ISSQNtot = Element(ISSQNtot)

            class retTrib(ComplexType):
                """Retenção de Tributos Federais"""
                vRetPIS: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                vRetCOFINS: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                vRetCSLL: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                vBCIRRF: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                vIRRF: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                vBCRetPrev: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                vRetPrev: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
            retTrib: retTrib = Element(retTrib)
        total: total = Element(total)

        class transp(ComplexType):
            """Dados dos transportes da NF-e"""
            _choice = [['vagao', 'balsa']]
            modFrete: str = Element(str)

            class transporta(ComplexType):
                """Dados do transportador"""
                _choice = [['CNPJ', 'CPF']]
                CNPJ: TCnpj = Element(TCnpj)
                CPF: TCpf = Element(TCpf)
                xNome: str = Element(str)
                IE: TIeDest = Element(TIeDest)
                xEnder: str = Element(str)
                xMun: str = Element(str)
                UF: TUf = Element(TUf)
            transporta: transporta = Element(transporta)

            class retTransp(ComplexType):
                """Dados da retenção  ICMS do Transporte"""
                vServ: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vBCRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                pICMSRet: TDec_0302a04 = Element(TDec_0302a04, tipo="N", tam=(3, 2))
                vICMSRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                CFOP: str = Element(str)
                cMunFG: TCodMunIBGE = Element(TCodMunIBGE)
            retTransp: retTransp = Element(retTransp)
            veicTransp: TVeiculo = Element(TVeiculo)
            reboque: List[TVeiculo] = Element(TVeiculo, max_occurs=5)
            vagao: str = Element(str)
            balsa: str = Element(str)

            class vol(ComplexType):
                """Dados dos volumes"""
                _max_occurs = 5000

                def add(self, qVol=None, esp=None, marca=None, nVol=None, pesoL=None, pesoB=None, lacres=None) -> TNFe.infNFe.transp.vol:
                    return super().add(qVol=qVol, esp=esp, marca=marca, nVol=nVol, pesoL=pesoL, pesoB=pesoB, lacres=lacres)

                qVol: str = Element(str)
                esp: str = Element(str)
                marca: str = Element(str)
                nVol: str = Element(str)
                pesoL: TDec_1203 = Element(TDec_1203, tipo="N", tam=(12, 3))
                pesoB: TDec_1203 = Element(TDec_1203, tipo="N", tam=(12, 3))

                class lacres(ComplexType):
                    _max_occurs = 5000

                    def add(self, nLacre=None) -> TNFe.infNFe.transp.vol.lacres:
                        return super().add(nLacre=nLacre)

                    nLacre: str = Element(str)
                lacres: List[lacres] = Element(lacres, max_occurs=5000)
            vol: List[vol] = Element(vol, max_occurs=5000)
        transp: transp = Element(transp)

        class cobr(ComplexType):
            """Dados da cobrança da NF-e"""

            class fat(ComplexType):
                """Dados da fatura"""
                nFat: str = Element(str)
                vOrig: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vDesc: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vLiq: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
            fat: fat = Element(fat)

            class dup(ComplexType):
                """Dados das duplicatas NT 2011/004"""
                _max_occurs = 120

                def add(self, nDup=None, dVenc=None, vDup=None) -> TNFe.infNFe.cobr.dup:
                    return super().add(nDup=nDup, dVenc=dVenc, vDup=vDup)

                nDup: str = Element(str)
                dVenc: TData = Element(TData)
                vDup: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
            dup: List[dup] = Element(dup, max_occurs=120)
        cobr: cobr = Element(cobr)

        class pag(ComplexType):
            """Dados de Pagamento. Obrigatório apenas para (NFC-e) NT 2012/004"""

            class detPag(ComplexType):
                """Grupo de detalhamento da forma de pagamento."""
                _max_occurs = 100

                def add(self, indPag=None, tPag=None, xPag=None, vPag=None, card=None) -> TNFe.infNFe.pag.detPag:
                    return super().add(indPag=indPag, tPag=tPag, xPag=xPag, vPag=vPag, card=card)

                indPag: str = Element(str)
                tPag: str = Element(str)
                xPag: str = Element(str)
                vPag: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))

                class card(ComplexType):
                    """Grupo de Cartões"""
                    tpIntegra: str = Element(str)
                    CNPJ: TCnpj = Element(TCnpj)
                    tBand: str = Element(str)
                    cAut: str = Element(str)
                card: card = Element(card)
            detPag: List[detPag] = Element(detPag, max_occurs=100)
            vTroco: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
        pag: pag = Element(pag)

        class infIntermed(ComplexType):
            """Grupo de Informações do Intermediador da Transação"""
            CNPJ: TCnpj = Element(TCnpj)
            idCadIntTran: str = Element(str)
        infIntermed: infIntermed = Element(infIntermed)

        class infAdic(ComplexType):
            """Informações adicionais da NF-e"""
            infAdFisco: str = Element(str)
            infCpl: str = Element(str)

            class obsCont(ComplexType):
                """Campo de uso livre do contribuinte
informar o nome do campo no atributo xCampo
e o conteúdo do campo no xTexto"""
                _max_occurs = 10

                def add(self, xTexto=None, xCampo=None) -> TNFe.infNFe.infAdic.obsCont:
                    return super().add(xTexto=xTexto, xCampo=xCampo)

                xTexto: str = Element(str)
                xCampo: str = Attribute(None)
            obsCont: List[obsCont] = Element(obsCont, max_occurs=10)

            class obsFisco(ComplexType):
                """Campo de uso exclusivo do Fisco
informar o nome do campo no atributo xCampo
e o conteúdo do campo no xTexto"""
                _max_occurs = 10

                def add(self, xTexto=None, xCampo=None) -> TNFe.infNFe.infAdic.obsFisco:
                    return super().add(xTexto=xTexto, xCampo=xCampo)

                xTexto: str = Element(str)
                xCampo: str = Attribute(None)
            obsFisco: List[obsFisco] = Element(obsFisco, max_occurs=10)

            class procRef(ComplexType):
                """Grupo de informações do  processo referenciado"""
                _max_occurs = 100

                def add(self, nProc=None, indProc=None) -> TNFe.infNFe.infAdic.procRef:
                    return super().add(nProc=nProc, indProc=indProc)

                nProc: str = Element(str)
                indProc: str = Element(str)
            procRef: List[procRef] = Element(procRef, max_occurs=100)
        infAdic: infAdic = Element(infAdic)

        class exporta(ComplexType):
            """Informações de exportação"""
            UFSaidaPais: TUfEmi = Element(TUfEmi)
            xLocExporta: str = Element(str)
            xLocDespacho: str = Element(str)
        exporta: exporta = Element(exporta)

        class compra(ComplexType):
            """Informações de compras  (Nota de Empenho, Pedido e Contrato)"""
            xNEmp: str = Element(str)
            xPed: str = Element(str)
            xCont: str = Element(str)
        compra: compra = Element(compra)

        class cana(ComplexType):
            """Informações de registro aquisições de cana"""
            safra: str = Element(str)
            ref: str = Element(str)

            class forDia(ComplexType):
                """Fornecimentos diários"""
                _max_occurs = 31

                def add(self, qtde=None, dia=None) -> TNFe.infNFe.cana.forDia:
                    return super().add(qtde=qtde, dia=dia)

                qtde: TDec_1110v = Element(TDec_1110v, tipo="N", tam=(11, 10))
                dia: str = Attribute(None)
            forDia: List[forDia] = Element(forDia, max_occurs=31)
            qTotMes: TDec_1110v = Element(TDec_1110v, tipo="N", tam=(11, 10))
            qTotAnt: TDec_1110v = Element(TDec_1110v, tipo="N", tam=(11, 10))
            qTotGer: TDec_1110v = Element(TDec_1110v, tipo="N", tam=(11, 10))

            class deduc(ComplexType):
                """Deduções - Taxas e Contribuições"""
                _max_occurs = 10

                def add(self, xDed=None, vDed=None) -> TNFe.infNFe.cana.deduc:
                    return super().add(xDed=xDed, vDed=vDed)

                xDed: str = Element(str)
                vDed: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
            deduc: List[deduc] = Element(deduc, max_occurs=10)
            vFor: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
            vTotDed: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
            vLiqFor: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
        cana: cana = Element(cana)
        infRespTec: TInfRespTec = Element(TInfRespTec)
        versao: str = Attribute(TVerNFe)
        Id: str = Attribute(None)
    infNFe: infNFe = Element(infNFe)

    class infNFeSupl(ComplexType):
        """Informações suplementares Nota Fiscal"""
        qrCode: str = Element(str)
        urlChave: str = Element(str)
    infNFeSupl: infNFeSupl = Element(infNFeSupl)
    Signature: Signature = Element(Signature)



class TProtNFe(Element):
    """Tipo Protocolo de status resultado do processamento da NF-e"""

    class infProt(ComplexType):
        """Dados do protocolo de status"""
        tpAmb: TAmb = Element(TAmb)
        verAplic: TVerAplic = Element(TVerAplic)
        chNFe: TChNFe = Element(TChNFe)
        dhRecbto: TDateTimeUTC = Element(TDateTimeUTC)
        nProt: TProt = Element(TProt)
        digVal: DigestValueType = Element(DigestValueType)
        cStat: TStat = Element(TStat)
        xMotivo: TMotivo = Element(TMotivo)
        cMsg: str = Element(str)
        xMsg: str = Element(str)
        Id: str = Attribute(ID)
    infProt: infProt = Element(infProt)
    Signature: Signature = Element(Signature)
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
    _choice = [['infRec', 'protNFe']]
    tpAmb: TAmb = Element(TAmb)
    verAplic: TVerAplic = Element(TVerAplic)
    cStat: TStat = Element(TStat)
    xMotivo: TMotivo = Element(TMotivo)
    cUF: TCodUfIBGE = Element(TCodUfIBGE)
    dhRecbto: TDateTimeUTC = Element(TDateTimeUTC)

    class infRec(ComplexType):
        """Dados do Recibo do Lote"""
        nRec: TRec = Element(TRec)
        tMed: TMed = Element(TMed)
    infRec: infRec = Element(infRec)
    protNFe: TProtNFe = Element(TProtNFe)
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
    protNFe: List[TProtNFe] = Element(TProtNFe, max_occurs=50)
    versao: str = Attribute(TVerNFe)



class TNfeProc(Element):
    """Tipo da NF-e processada"""
    NFe: TNFe = Element(TNFe)
    protNFe: TProtNFe = Element(TProtNFe)
    versao: str = Attribute(TVerNFe)


