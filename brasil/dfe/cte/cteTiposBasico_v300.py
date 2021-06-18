from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposGeralCTe_v300 import *


class TProtCTeOS(Element):
    """Tipo Protocolo de status resultado do processamento do CT-e OS (Modelo 67)"""
    class infProt(ComplexType):
        tpAmb: TAmb = Element(TAmb)
        verAplic: TVerAplic = Element(TVerAplic)
        chCTe: TChNFe = Element(TChNFe)
        dhRecbto: TDateTimeUTC = Element(TDateTimeUTC)
        nProt: TProt = Element(TProt, min_occurs=0)
        digVal: DigestValueType = Element(DigestValueType, min_occurs=0)
        cStat: str = Element(str)
        xMotivo: TMotivo = Element(TMotivo)
        Id: str = Attribute(ID)
    infProt: infProt
    Signature: Signature = Element(Signature, min_occurs=0)
    versao: str = Attribute(None)


class TVerCTe(str):
    """Tipo Versão do CT-e - 3.00"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"3\.00", enumeration=[])
    pass


class TRetCTeOS(Element):
    """Tipo Retorno do Pedido de Autorização de CT-e OS (Modelo 67)"""
    tpAmb: TAmb = Element(TAmb)
    cUF: TCodUfIBGE = Element(TCodUfIBGE)
    verAplic: TVerAplic = Element(TVerAplic)
    cStat: TStat = Element(TStat)
    xMotivo: TMotivo = Element(TMotivo)
    protCTe: TProtCTeOS = Element(TProtCTeOS, min_occurs=0)
    versao: str = Attribute(TVerCTe)


class TEndeEmi(Element):
    """Tipo Dados do Endereço"""
    xLgr: str = Element(str)
    nro: str = Element(str)
    xCpl: str = Element(str, min_occurs=0)
    xBairro: str = Element(str)
    cMun: TCodMunIBGE = Element(TCodMunIBGE)
    xMun: str = Element(str)
    CEP: str = Element(str, min_occurs=0)
    UF: TUF_sem_EX = Element(TUF_sem_EX)
    fone: TFone = Element(TFone, min_occurs=0)


class TEndereco(Element):
    """Tipo Dados do Endereço"""
    xLgr: str = Element(str)
    nro: str = Element(str)
    xCpl: str = Element(str, min_occurs=0)
    xBairro: str = Element(str)
    cMun: TCodMunIBGE = Element(TCodMunIBGE)
    xMun: str = Element(str)
    CEP: str = Element(str, min_occurs=0)
    UF: TUf = Element(TUf)
    cPais: str = Element(str, min_occurs=0)
    xPais: str = Element(str, min_occurs=0)


class TImp(Element):
    """Tipo Dados do Imposto CT-e"""
    pass


class TEmail(str):
    """Tipo Email"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[^@]+@[^\.]+\..+", min_length=r"1", max_length=r"60", enumeration=[])
    pass


class TRespTec(Element):
    """Tipo Dados da Responsável Técnico"""
    CNPJ: TCnpj = Element(TCnpj)
    xContato: str = Element(str)
    email: TEmail = Element(TEmail)
    fone: str = Element(str)
    idCSRT: str = Element(str)
    hashCSRT: str = Element(str)


class TCfop(str):
    """Tipo CFOP"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[123567][0-9]([0-9][1-9]|[1-9][0-9])", enumeration=[])
    pass


class TFinCTe(str):
    """Tipo Finalidade da CT-e"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['0', '1', '2', '3'])
    pass


class TModTransp(str):
    """Tipo Modal transporte"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['01', '02', '03', '04', '05', '06'])
    pass


class TProcEmi(str):
    """Tipo processo de emissão do CT-e"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['0', '3'])
    pass


class TCTe(Element):
    """Tipo Conhecimento de Transporte Eletrônico (Modelo 57)"""
    class infCte(ComplexType):
        class ide(ComplexType):
            """Informar apenas
para tpEmis diferente de 1"""
            cUF: TCodUfIBGE = Element(TCodUfIBGE)
            cCT: str = Element(str)
            CFOP: TCfop = Element(TCfop)
            natOp: str = Element(str)
            mod: TModCT = Element(TModCT)
            serie: str = Element(str)
            nCT: TNF = Element(TNF)
            dhEmi: str = Element(str)
            tpImp: str = Element(str)
            tpEmis: str = Element(str)
            cDV: str = Element(str)
            tpAmb: TAmb = Element(TAmb)
            tpCTe: TFinCTe = Element(TFinCTe)
            procEmi: TProcEmi = Element(TProcEmi)
            verProc: str = Element(str)
            indGlobalizado: str = Element(str, min_occurs=0)
            cMunEnv: TCodMunIBGE = Element(TCodMunIBGE)
            xMunEnv: str = Element(str)
            UFEnv: TUf = Element(TUf)
            modal: TModTransp = Element(TModTransp)
            tpServ: str = Element(str)
            cMunIni: TCodMunIBGE = Element(TCodMunIBGE)
            xMunIni: str = Element(str)
            UFIni: TUf = Element(TUf)
            cMunFim: TCodMunIBGE = Element(TCodMunIBGE)
            xMunFim: str = Element(str)
            UFFim: TUf = Element(TUf)
            retira: str = Element(str)
            xDetRetira: str = Element(str, min_occurs=0)
            indIEToma: str = Element(str)
            dhCont: TDateTimeUTC = Element(TDateTimeUTC)
            xJust: str = Element(str)
        ide: ide
        class compl(ComplexType):
            xCaracAd: str = Element(str, min_occurs=0)
            xCaracSer: str = Element(str, min_occurs=0)
            xEmi: str = Element(str, min_occurs=0)
            class fluxo(ComplexType):
                xOrig: str = Element(str, min_occurs=0)
                class pass_(ComplexType):
                    xPass: str = Element(str, min_occurs=0)
                pass_: pass_
                xDest: str = Element(str, min_occurs=0)
                xRota: str = Element(str, min_occurs=0)
            fluxo: fluxo
            class Entrega(ComplexType):
                pass
            Entrega: Entrega
            origCalc: str = Element(str, min_occurs=0)
            destCalc: str = Element(str, min_occurs=0)
            xObs: str = Element(str, min_occurs=0)
            class ObsCont(ComplexType):
                xTexto: str = Element(str)
                xCampo: str = Attribute(None)
            ObsCont: ObsCont
            class ObsFisco(ComplexType):
                xTexto: str = Element(str)
                xCampo: str = Attribute(None)
            ObsFisco: ObsFisco
        compl: compl
        class emit(ComplexType):
            CNPJ: TCnpj = Element(TCnpj)
            IE: str = Element(str)
            IEST: str = Element(str, min_occurs=0)
            xNome: str = Element(str)
            xFant: str = Element(str, min_occurs=0)
            enderEmit: TEndeEmi = Element(TEndeEmi)
        emit: emit
        class rem(ComplexType):
            IE: str = Element(str, min_occurs=0)
            xNome: str = Element(str)
            xFant: str = Element(str, min_occurs=0)
            fone: TFone = Element(TFone, min_occurs=0)
            enderReme: TEndereco = Element(TEndereco)
            email: str = Element(str, min_occurs=0)
        rem: rem
        class exped(ComplexType):
            IE: str = Element(str, min_occurs=0)
            xNome: str = Element(str)
            fone: TFone = Element(TFone, min_occurs=0)
            enderExped: TEndereco = Element(TEndereco)
            email: TEmail = Element(TEmail, min_occurs=0)
        exped: exped
        class receb(ComplexType):
            IE: str = Element(str, min_occurs=0)
            xNome: str = Element(str)
            fone: TFone = Element(TFone, min_occurs=0)
            enderReceb: TEndereco = Element(TEndereco)
            email: TEmail = Element(TEmail, min_occurs=0)
        receb: receb
        class dest(ComplexType):
            IE: str = Element(str, min_occurs=0)
            xNome: str = Element(str)
            fone: TFone = Element(TFone, min_occurs=0)
            ISUF: str = Element(str, min_occurs=0)
            enderDest: TEndereco = Element(TEndereco)
            email: TEmail = Element(TEmail, min_occurs=0)
        dest: dest
        class vPrest(ComplexType):
            vTPrest: TDec_1302 = Element(TDec_1302)
            vRec: TDec_1302 = Element(TDec_1302)
            class Comp(ComplexType):
                xNome: str = Element(str)
                vComp: TDec_1302 = Element(TDec_1302)
            Comp: Comp
        vPrest: vPrest
        class imp(ComplexType):
            ICMS: TImp = Element(TImp)
            vTotTrib: TDec_1302 = Element(TDec_1302, min_occurs=0)
            infAdFisco: str = Element(str, min_occurs=0)
            class ICMSUFFim(ComplexType):
                vBCUFFim: TDec_1302 = Element(TDec_1302)
                pFCPUFFim: TDec_0302 = Element(TDec_0302)
                pICMSUFFim: TDec_0302 = Element(TDec_0302)
                pICMSInter: TDec_0302 = Element(TDec_0302)
                pICMSInterPart: TDec_0302 = Element(TDec_0302)
                vFCPUFFim: TDec_1302 = Element(TDec_1302)
                vICMSUFFim: TDec_1302 = Element(TDec_1302)
                vICMSUFIni: TDec_1302 = Element(TDec_1302)
            ICMSUFFim: ICMSUFFim
        imp: imp
        class autXML(ComplexType):
            pass
        autXML: autXML
        infRespTec: TRespTec = Element(TRespTec, min_occurs=0)
        versao: str = Attribute(None)
        Id: str = Attribute(None)
    infCte: infCte
    Signature: Signature = Element(Signature)


class TImpOS(Element):
    """Tipo Dados do Imposto para CT-e OS"""
    pass


class TModTranspOS(str):
    """Tipo Modal transporte Outros Serviços"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['01', '02', '03', '04'])
    pass


class TCTeOS(Element):
    """Tipo Conhecimento de Transporte Eletrônico Outros Serviços (Modelo 67)"""
    class infCte(ComplexType):
        class ide(ComplexType):
            """Informar apenas
para tpEmis diferente de 1"""
            cUF: TCodUfIBGE = Element(TCodUfIBGE)
            cCT: str = Element(str)
            CFOP: TCfop = Element(TCfop)
            natOp: str = Element(str)
            mod: TModCTOS = Element(TModCTOS)
            serie: str = Element(str)
            nCT: TNF = Element(TNF)
            dhEmi: str = Element(str)
            tpImp: str = Element(str)
            tpEmis: str = Element(str)
            cDV: str = Element(str)
            tpAmb: TAmb = Element(TAmb)
            tpCTe: TFinCTe = Element(TFinCTe)
            procEmi: TProcEmi = Element(TProcEmi)
            verProc: str = Element(str)
            cMunEnv: TCodMunIBGE = Element(TCodMunIBGE)
            xMunEnv: str = Element(str)
            UFEnv: TUf = Element(TUf)
            modal: TModTranspOS = Element(TModTranspOS)
            tpServ: str = Element(str)
            indIEToma: str = Element(str)
            cMunIni: TCodMunIBGE = Element(TCodMunIBGE, min_occurs=0)
            xMunIni: str = Element(str, min_occurs=0)
            UFIni: TUf = Element(TUf, min_occurs=0)
            cMunFim: TCodMunIBGE = Element(TCodMunIBGE, min_occurs=0)
            xMunFim: str = Element(str, min_occurs=0)
            UFFim: TUf = Element(TUf, min_occurs=0)
            class infPercurso(ComplexType):
                UFPer: TUf = Element(TUf)
            infPercurso: infPercurso
            dhCont: TDateTimeUTC = Element(TDateTimeUTC)
            xJust: str = Element(str)
        ide: ide
        class compl(ComplexType):
            xCaracAd: str = Element(str, min_occurs=0)
            xCaracSer: str = Element(str, min_occurs=0)
            xEmi: str = Element(str, min_occurs=0)
            xObs: str = Element(str, min_occurs=0)
            class ObsCont(ComplexType):
                xTexto: str = Element(str)
                xCampo: str = Attribute(None)
            ObsCont: ObsCont
            class ObsFisco(ComplexType):
                xTexto: str = Element(str)
                xCampo: str = Attribute(None)
            ObsFisco: ObsFisco
        compl: compl
        class emit(ComplexType):
            CNPJ: TCnpj = Element(TCnpj)
            IE: str = Element(str)
            IEST: str = Element(str, min_occurs=0)
            xNome: str = Element(str)
            xFant: str = Element(str, min_occurs=0)
            enderEmit: TEndeEmi = Element(TEndeEmi)
        emit: emit
        class toma(ComplexType):
            IE: str = Element(str, min_occurs=0)
            xNome: str = Element(str)
            xFant: str = Element(str, min_occurs=0)
            fone: TFone = Element(TFone, min_occurs=0)
            enderToma: TEndereco = Element(TEndereco)
            email: str = Element(str, min_occurs=0)
        toma: toma
        class vPrest(ComplexType):
            vTPrest: TDec_1302 = Element(TDec_1302)
            vRec: TDec_1302 = Element(TDec_1302)
            class Comp(ComplexType):
                xNome: str = Element(str)
                vComp: TDec_1302 = Element(TDec_1302)
            Comp: Comp
        vPrest: vPrest
        class imp(ComplexType):
            ICMS: TImpOS = Element(TImpOS)
            vTotTrib: TDec_1302 = Element(TDec_1302, min_occurs=0)
            infAdFisco: str = Element(str, min_occurs=0)
            class ICMSUFFim(ComplexType):
                vBCUFFim: TDec_1302 = Element(TDec_1302)
                pFCPUFFim: TDec_0302 = Element(TDec_0302)
                pICMSUFFim: TDec_0302 = Element(TDec_0302)
                pICMSInter: TDec_0302 = Element(TDec_0302)
                pICMSInterPart: TDec_0302 = Element(TDec_0302)
                vFCPUFFim: TDec_1302 = Element(TDec_1302)
                vICMSUFFim: TDec_1302 = Element(TDec_1302)
                vICMSUFIni: TDec_1302 = Element(TDec_1302)
            ICMSUFFim: ICMSUFFim
            class infTribFed(ComplexType):
                vPIS: TDec_1302 = Element(TDec_1302, min_occurs=0)
                vCOFINS: TDec_1302 = Element(TDec_1302, min_occurs=0)
                vIR: TDec_1302 = Element(TDec_1302, min_occurs=0)
                vINSS: TDec_1302 = Element(TDec_1302, min_occurs=0)
                vCSLL: TDec_1302 = Element(TDec_1302, min_occurs=0)
            infTribFed: infTribFed
        imp: imp
        class autXML(ComplexType):
            pass
        autXML: autXML
        infRespTec: TRespTec = Element(TRespTec, min_occurs=0)
        versao: str = Attribute(None)
        Id: str = Attribute(None)
    infCte: infCte
    Signature: Signature = Element(Signature)
    versao: str = Attribute(None)


class TIdLote(str):
    """Tipo Identificador de controle do envio do lote. Número seqüencial auto-incremental, de controle correspondente ao identificador único do lote enviado. A responsabilidade de gerar e controlar esse número é do próprio contribuinte."""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{1,15}", enumeration=[])
    pass


class TEnviCTe(Element):
    """Tipo Pedido de Concessão de Autorização da CT-e"""
    idLote: TIdLote = Element(TIdLote)
    CTe: List[TCTe] = Element(TCTe, max_occurs=50)
    versao: str = Attribute(TVerCTe)


class TRetEnviCTe(Element):
    """Tipo Retorno do Pedido de Concessão de Autorização da CT-e"""
    tpAmb: TAmb = Element(TAmb)
    cUF: TCodUfIBGE = Element(TCodUfIBGE)
    verAplic: TVerAplic = Element(TVerAplic)
    cStat: TStat = Element(TStat)
    xMotivo: TMotivo = Element(TMotivo)
    class infRec(ComplexType):
        nRec: TRec = Element(TRec)
        dhRecbto: TDateTimeUTC = Element(TDateTimeUTC)
        tMed: str = Element(str)
    infRec: infRec
    versao: str = Attribute(TVerCTe)


class TEndernac(Element):
    """Tipo Dados do Endereço"""
    xLgr: str = Element(str)
    nro: str = Element(str)
    xCpl: str = Element(str, min_occurs=0)
    xBairro: str = Element(str)
    cMun: TCodMunIBGE = Element(TCodMunIBGE)
    xMun: str = Element(str)
    CEP: str = Element(str, min_occurs=0)
    UF: TUf = Element(TUf)


class TEndOrg(Element):
    """Tipo Dados do Endereço"""
    xLgr: str = Element(str)
    nro: str = Element(str)
    xCpl: str = Element(str, min_occurs=0)
    xBairro: str = Element(str)
    cMun: TCodMunIBGE = Element(TCodMunIBGE)
    xMun: str = Element(str)
    CEP: str = Element(str, min_occurs=0)
    UF: TUf = Element(TUf)
    cPais: str = Element(str, min_occurs=0)
    xPais: str = Element(str, min_occurs=0)
    fone: TFone = Element(TFone, min_occurs=0)


class TLocal(Element):
    """Tipo Dados do Local de Origem ou Destino"""
    cMun: TCodMunIBGE = Element(TCodMunIBGE)
    xMun: str = Element(str)
    UF: TUf = Element(TUf)


class TEndReEnt(Element):
    """Tipo Dados do Local de Retirada ou Entrega"""
    xNome: str = Element(str)
    xLgr: str = Element(str)
    nro: str = Element(str)
    xCpl: str = Element(str, min_occurs=0)
    xBairro: str = Element(str)
    cMun: TCodMunIBGE = Element(TCodMunIBGE)
    xMun: str = Element(str)
    UF: TUf = Element(TUf)


class TContainer(str):
    """Tipo Número do Container"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[A-Z0-9]+", min_length=r"1", max_length=r"20", enumeration=[])
    pass


class TUnidCarga(Element):
    """Tipo Dados Unidade de Carga"""
    tpUnidCarga: TtipoUnidCarga = Element(TtipoUnidCarga)
    idUnidCarga: TContainer = Element(TContainer)
    class lacUnidCarga(ComplexType):
        nLacre: str = Element(str)
    lacUnidCarga: lacUnidCarga
    qtdRat: TDec_0302_0303 = Element(TDec_0302_0303, min_occurs=0)


class TUnidadeTransp(Element):
    """Tipo Dados Unidade de Transporte"""
    tpUnidTransp: TtipoUnidTransp = Element(TtipoUnidTransp)
    idUnidTransp: TContainer = Element(TContainer)
    class lacUnidTransp(ComplexType):
        nLacre: str = Element(str)
    lacUnidTransp: lacUnidTransp
    infUnidCarga: List[TUnidCarga] = Element(TUnidCarga, min_occurs=0, max_occurs=-1)
    qtdRat: TDec_0302_0303 = Element(TDec_0302_0303, min_occurs=0)


class TCListServ(str):
    """Tipo Código da Lista de Serviços LC 116/2003"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['101', '102', '103', '104', '105', '106', '107', '108', '201', '302', '303', '304', '305', '401', '402', '403', '404', '405', '406', '407', '408', '409', '410', '411', '412', '413', '414', '415', '416', '417', '418', '419', '420', '421', '422', '423', '501', '502', '503', '504', '505', '506', '507', '508', '509', '601', '602', '603', '604', '605', '701', '702', '703', '704', '705', '706', '707', '708', '709', '710', '711', '712', '713', '716', '717', '718', '719', '720', '721', '722', '801', '802', '901', '902', '903', '1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1009', '1010', '1101', '1102', '1103', '1104', '1201', '1202', '1203', '1204', '1205', '1206', '1207', '1208', '1209', '1210', '1211', '1212', '1213', '1214', '1215', '1216', '1217', '1302', '1303', '1304', '1305', '1401', '1402', '1403', '1404', '1405', '1406', '1407', '1408', '1409', '1410', '1411', '1412', '1413', '1501', '1502', '1503', '1504', '1505', '1506', '1507', '1508', '1509', '1510', '1511', '1512', '1513', '1514', '1515', '1516', '1517', '1518', '1601', '1701', '1702', '1703', '1704', '1705', '1706', '1708', '1709', '1710', '1711', '1712', '1713', '1714', '1715', '1716', '1717', '1718', '1719', '1720', '1721', '1722', '1723', '1724', '1801', '1901', '2001', '2002', '2003', '2101', '2201', '2301', '2401', '2501', '2502', '2503', '2504', '2601', '2701', '2801', '2901', '3001', '3101', '3201', '3301', '3401', '3501', '3601', '3701', '3801', '3901', '4001'])
    pass


class TDocAssoc(str):
    """Tipo Documento Associado"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['07', '08', '09', '10', '11', '12', '13'])
    pass


class TFinCTeOS(str):
    """Tipo Finalidade da CT-e Outros Serviços"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['0', '1'])
    pass


class TModDoc(str):
    """Tipo Modelo do Documento"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['01', '1B', '02', '2D', '2E', '04', '06', '07', '08', '8B', '09', '10', '11', '13', '14', '15', '16', '17', '18', '20', '21', '22', '23', '24', '25', '26', '27', '28', '55'])
    pass


class TRNTRC(str):
    """Tipo RNTRC - Registro Nacional Transportadores Rodoviários de Carga"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{8}|ISENTO", enumeration=[])
    pass


class TCIOT(str):
    """Tipo CIOT - Código Identificador da Operação de Transporte"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{12}", enumeration=[])
    pass


class TTime(str):
    """Tipo hora"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])", enumeration=[])
    pass


