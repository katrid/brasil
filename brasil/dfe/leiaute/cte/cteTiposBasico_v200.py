from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .xmldsig_core_schema_v101 import *

from .tiposGeralCTe_v200 import *



class TEndeEmi(Element):
    """Tipo Dados do Endereço"""
    xLgr: str = Element(str)
    nro: str = Element(str)
    xCpl: str = Element(str)
    xBairro: str = Element(str)
    cMun: TCodMunIBGE = Element(TCodMunIBGE)
    xMun: str = Element(str)
    CEP: str = Element(str)
    UF: TUF_sem_EX = Element(TUF_sem_EX)
    fone: TFone = Element(TFone)



class TEndereco(Element):
    """Tipo Dados do Endereço"""
    xLgr: str = Element(str)
    nro: str = Element(str)
    xCpl: str = Element(str)
    xBairro: str = Element(str)
    cMun: TCodMunIBGE = Element(TCodMunIBGE)
    xMun: str = Element(str)
    CEP: str = Element(str)
    UF: TUf = Element(TUf)
    cPais: str = Element(str)
    xPais: str = Element(str)



class TImp(Element):
    """Tipo Dados do Imposto"""
    _choice = [['ICMS00', 'ICMS20', 'ICMS45', 'ICMS60', 'ICMS90', 'ICMSOutraUF', 'ICMSSN']]

    class ICMS00(ComplexType):
        """Prestação sujeito à tributação normal do ICMS"""
        CST: str = Element(str)
        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
        pICMS: TDec_0302 = Element(TDec_0302, tipo="N", tam=(3, 2))
        vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
    ICMS00: ICMS00 = Element(ICMS00)

    class ICMS20(ComplexType):
        """Prestação sujeito à tributação com redução de BC do ICMS"""
        CST: str = Element(str)
        pRedBC: TDec_0302Opc = Element(TDec_0302Opc, tipo="N", tam=(3, 2))
        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
        pICMS: TDec_0302 = Element(TDec_0302, tipo="N", tam=(3, 2))
        vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
    ICMS20: ICMS20 = Element(ICMS20)

    class ICMS45(ComplexType):
        """ICMS  Isento, não Tributado ou diferido"""
        CST: str = Element(str)
    ICMS45: ICMS45 = Element(ICMS45)

    class ICMS60(ComplexType):
        """Tributação pelo ICMS60 - ICMS cobrado por substituição tributária.Responsabilidade do recolhimento do ICMS atribuído ao tomador ou 3º por ST"""
        CST: str = Element(str)
        vBCSTRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
        vICMSSTRet: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
        pICMSSTRet: TDec_0302 = Element(TDec_0302, tipo="N", tam=(3, 2))
        vCred: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
    ICMS60: ICMS60 = Element(ICMS60)

    class ICMS90(ComplexType):
        """ICMS Outros"""
        CST: str = Element(str)
        pRedBC: TDec_0302Opc = Element(TDec_0302Opc, tipo="N", tam=(3, 2))
        vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
        pICMS: TDec_0302 = Element(TDec_0302, tipo="N", tam=(3, 2))
        vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
        vCred: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
    ICMS90: ICMS90 = Element(ICMS90)

    class ICMSOutraUF(ComplexType):
        """ICMS devido à UF de origem da prestação, quando  diferente da UF do emitente"""
        CST: str = Element(str)
        pRedBCOutraUF: TDec_0302Opc = Element(TDec_0302Opc, tipo="N", tam=(3, 2))
        vBCOutraUF: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
        pICMSOutraUF: TDec_0302 = Element(TDec_0302, tipo="N", tam=(3, 2))
        vICMSOutraUF: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
    ICMSOutraUF: ICMSOutraUF = Element(ICMSOutraUF)

    class ICMSSN(ComplexType):
        """Simples Nacional"""
        indSN: str = Element(str)
    ICMSSN: ICMSSN = Element(ICMSSN)



class TContainer(str):
    """Tipo Número do Container"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[A-Z0-9]+", min_length=r"1", max_length=r"20", enumeration=[])
    pass



class TUnidCarga(Element):
    """Tipo Dados Unidade de Carga"""
    tpUnidCarga: TtipoUnidCarga = Element(TtipoUnidCarga)
    idUnidCarga: TContainer = Element(TContainer)

    class lacUnidCarga(ComplexType):
        """Lacres das Unidades de Carga"""
        _max_occurs = -1

        def add(self, nLacre=None) -> TUnidCarga.lacUnidCarga:
            return super().add(nLacre=nLacre)

        nLacre: str = Element(str)
    lacUnidCarga: List[lacUnidCarga] = Element(lacUnidCarga, max_occurs=-1)
    qtdRat: TDec_0302_0303 = Element(TDec_0302_0303, tipo="N", tam=(3, 2))



class TUnidadeTransp(Element):
    """Tipo Dados Unidade de Transporte"""
    tpUnidTransp: TtipoUnidTransp = Element(TtipoUnidTransp)
    idUnidTransp: TContainer = Element(TContainer)

    class lacUnidTransp(ComplexType):
        """Lacres das Unidades de Transporte"""
        _max_occurs = -1

        def add(self, nLacre=None) -> TUnidadeTransp.lacUnidTransp:
            return super().add(nLacre=nLacre)

        nLacre: str = Element(str)
    lacUnidTransp: List[lacUnidTransp] = Element(lacUnidTransp, max_occurs=-1)
    infUnidCarga: List[TUnidCarga] = Element(TUnidCarga, max_occurs=-1)
    qtdRat: TDec_0302_0303 = Element(TDec_0302_0303, tipo="N", tam=(3, 2))



class TCfop(str):
    """Tipo CFOP"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[123567][0-9]([0-9][1-9]|[1-9][0-9])", enumeration=[])
    pass



class TDocAssoc(str):
    """Tipo Documento Associado"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '99'])
    pass



class TEmail(str):
    """Tipo Email"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[^@]+@[^\.]+\..+", min_length=r"1", max_length=r"60", enumeration=[])
    pass



class TFinCTe(str):
    """Tipo Finalidade da CT-e"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['0', '1', '2', '3'])
    pass



class TModDoc(str):
    """Tipo Modelo do Documento"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['01', '1B', '02', '2D', '2E', '04', '06', '07', '08', '8B', '09', '10', '11', '13', '14', '15', '16', '17', '18', '20', '21', '22', '23', '24', '25', '26', '27', '28', '55'])
    pass



class TModTransp(str):
    """Tipo Modal transporte"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['01', '02', '03', '04', '05', '06'])
    pass



class TProcEmi(str):
    """Tipo processo de emissão do CT-e"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['0', '1', '2', '3'])
    pass



class TTime(str):
    """Tipo hora"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])", enumeration=[])
    pass



class TCTe(Element):
    """Tipo Conhecimento de Transporte Eletrônico"""

    class infCte(ComplexType):
        """Informações do CT-e"""
        _choice = [['infCTeNorm', 'infCteComp', 'infCteAnu']]

        class ide(ComplexType):
            """Identificação do CT-e"""
            _choice = [['toma03', 'toma4']]
            cUF: TCodUfIBGE = Element(TCodUfIBGE)
            cCT: str = Element(str)
            CFOP: TCfop = Element(TCfop)
            natOp: str = Element(str)
            forPag: str = Element(str)
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
            refCTE: TChNFe = Element(TChNFe)
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
            xDetRetira: str = Element(str)

            class toma03(ComplexType):
                """Indicador do \"papel\" do tomador do serviço no CT-e"""
                toma: str = Element(str)
            toma03: toma03 = Element(toma03)

            class toma4(ComplexType):
                """Indicador do \"papel\" do tomador do serviço no CT-e"""
                _choice = [['CNPJ', 'CPF']]
                toma: str = Element(str)
                CNPJ: TCnpjOpc = Element(TCnpjOpc)
                CPF: TCpf = Element(TCpf)
                IE: TIeDest = Element(TIeDest)
                xNome: str = Element(str)
                xFant: str = Element(str)
                fone: TFone = Element(TFone)
                enderToma: TEndereco = Element(TEndereco)
                email: TEmail = Element(TEmail)
            toma4: toma4 = Element(toma4)
            dhCont: str = Element(str)
            xJust: str = Element(str)
        ide: ide = Element(ide)

        class compl(ComplexType):
            """Dados complementares do CT-e para fins operacionais ou comerciais"""
            xCaracAd: str = Element(str)
            xCaracSer: str = Element(str)
            xEmi: str = Element(str)

            class fluxo(ComplexType):
                """Previsão do fluxo da carga
Preenchimento obrigatório para o modal aéreo."""
                xOrig: str = Element(str)

                class pass_(ComplexType):
                    _max_occurs = -1

                    def add(self, xPass=None) -> TCTe.infCte.compl.fluxo.pass_:
                        return super().add(xPass=xPass)

                    xPass: str = Element(str)
                pass_: List[pass_] = Element(pass_, max_occurs=-1)
                xDest: str = Element(str)
                xRota: str = Element(str)
            fluxo: fluxo = Element(fluxo)

            class Entrega(ComplexType):
                """Informações ref. a previsão de entrega"""
                _choice = [['semData', 'comData', 'noPeriodo'], ['semHora', 'comHora', 'noInter']]

                class semData(ComplexType):
                    """Entrega sem data definida
Esta opção é proibida para o modal aéreo."""
                    tpPer: str = Element(str)
                semData: semData = Element(semData)

                class comData(ComplexType):
                    """Entrega com data definida"""
                    tpPer: str = Element(str)
                    dProg: TData = Element(TData)
                comData: comData = Element(comData)

                class noPeriodo(ComplexType):
                    """Entrega no período definido"""
                    tpPer: str = Element(str)
                    dIni: TData = Element(TData)
                    dFim: TData = Element(TData)
                noPeriodo: noPeriodo = Element(noPeriodo)

                class semHora(ComplexType):
                    """Entrega sem hora definida"""
                    tpHor: str = Element(str)
                semHora: semHora = Element(semHora)

                class comHora(ComplexType):
                    """Entrega com hora definida"""
                    tpHor: str = Element(str)
                    hProg: TTime = Element(TTime)
                comHora: comHora = Element(comHora)

                class noInter(ComplexType):
                    """Entrega no intervalo de horário definido"""
                    tpHor: str = Element(str)
                    hIni: TTime = Element(TTime)
                    hFim: TTime = Element(TTime)
                noInter: noInter = Element(noInter)
            Entrega: Entrega = Element(Entrega)
            origCalc: str = Element(str)
            destCalc: str = Element(str)
            xObs: str = Element(str)

            class ObsCont(ComplexType):
                """Campo de uso livre do contribuinte
Informar o nome do campo no atributo xCampo e o conteúdo do campo no XTexto"""
                _max_occurs = 10

                def add(self, xTexto=None, xCampo=None) -> TCTe.infCte.compl.ObsCont:
                    return super().add(xTexto=xTexto, xCampo=xCampo)

                xTexto: str = Element(str)
                xCampo: str = Attribute(None)
            ObsCont: List[ObsCont] = Element(ObsCont, max_occurs=10)

            class ObsFisco(ComplexType):
                """Campo de uso livre do contribuinte
Informar o nome do campo no atributo xCampo e o conteúdo do campo no XTexto"""
                _max_occurs = 10

                def add(self, xTexto=None, xCampo=None) -> TCTe.infCte.compl.ObsFisco:
                    return super().add(xTexto=xTexto, xCampo=xCampo)

                xTexto: str = Element(str)
                xCampo: str = Attribute(None)
            ObsFisco: List[ObsFisco] = Element(ObsFisco, max_occurs=10)
        compl: compl = Element(compl)

        class emit(ComplexType):
            """Identificação do Emitente do CT-e"""
            CNPJ: TCnpj = Element(TCnpj)
            IE: str = Element(str)
            xNome: str = Element(str)
            xFant: str = Element(str)
            enderEmit: TEndeEmi = Element(TEndeEmi)
        emit: emit = Element(emit)

        class rem(ComplexType):
            """Informações do Remetente das mercadorias transportadas pelo CT-e
Poderá não ser informado para os CT-e de redespacho intermediário. Nos demais casos deverá sempre ser informado."""
            _choice = [['CNPJ', 'CPF']]
            CNPJ: TCnpjOpc = Element(TCnpjOpc)
            CPF: TCpf = Element(TCpf)
            IE: TIeDest = Element(TIeDest)
            xNome: str = Element(str)
            xFant: str = Element(str)
            fone: TFone = Element(TFone)
            enderReme: TEndereco = Element(TEndereco)
            email: str = Element(str)
        rem: rem = Element(rem)

        class exped(ComplexType):
            """Informações do Expedidor da Carga"""
            _choice = [['CNPJ', 'CPF']]
            CNPJ: TCnpjOpc = Element(TCnpjOpc)
            CPF: TCpf = Element(TCpf)
            IE: TIeDest = Element(TIeDest)
            xNome: str = Element(str)
            fone: TFone = Element(TFone)
            enderExped: TEndereco = Element(TEndereco)
            email: TEmail = Element(TEmail)
        exped: exped = Element(exped)

        class receb(ComplexType):
            """Informações do Recebedor da Carga"""
            _choice = [['CNPJ', 'CPF']]
            CNPJ: TCnpjOpc = Element(TCnpjOpc)
            CPF: TCpf = Element(TCpf)
            IE: TIeDest = Element(TIeDest)
            xNome: str = Element(str)
            fone: TFone = Element(TFone)
            enderReceb: TEndereco = Element(TEndereco)
            email: TEmail = Element(TEmail)
        receb: receb = Element(receb)

        class dest(ComplexType):
            """Informações do Destinatário do CT-e
Só pode ser omitido em caso de redespacho intermediário"""
            _choice = [['CNPJ', 'CPF']]
            CNPJ: TCnpjOpc = Element(TCnpjOpc)
            CPF: TCpf = Element(TCpf)
            IE: str = Element(str)
            xNome: str = Element(str)
            fone: TFone = Element(TFone)
            ISUF: str = Element(str)
            enderDest: TEndereco = Element(TEndereco)
            email: TEmail = Element(TEmail)
        dest: dest = Element(dest)

        class vPrest(ComplexType):
            """Valores da Prestação de Serviço"""
            vTPrest: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
            vRec: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))

            class Comp(ComplexType):
                """Componentes do Valor da Prestação"""
                _max_occurs = -1

                def add(self, xNome=None, vComp=None) -> TCTe.infCte.vPrest.Comp:
                    return super().add(xNome=xNome, vComp=vComp)

                xNome: str = Element(str)
                vComp: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
            Comp: List[Comp] = Element(Comp, max_occurs=-1)
        vPrest: vPrest = Element(vPrest)

        class imp(ComplexType):
            """Informações relativas aos Impostos"""
            ICMS: TImp = Element(TImp)
            vTotTrib: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
            infAdFisco: str = Element(str)

            class ICMSUFFim(ComplexType):
                """Informações do ICMS de partilha com a UF de término do serviço de transporte na operação interestadual
Grupo a ser informado nas prestações interestaduais para consumidor final, não contribuinte do ICMS"""
                vBCUFFim: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                pFCPUFFim: TDec_0302 = Element(TDec_0302, tipo="N", tam=(3, 2))
                pICMSUFFim: TDec_0302 = Element(TDec_0302, tipo="N", tam=(3, 2))
                pICMSInter: TDec_0302 = Element(TDec_0302, tipo="N", tam=(3, 2))
                pICMSInterPart: TDec_0302 = Element(TDec_0302, tipo="N", tam=(3, 2))
                vFCPUFFim: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vICMSUFFim: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vICMSUFIni: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
            ICMSUFFim: ICMSUFFim = Element(ICMSUFFim)
        imp: imp = Element(imp)

        class infCTeNorm(ComplexType):
            """Grupo de informações do CT-e Normal e Substituto"""

            class infCarga(ComplexType):
                """Informações da Carga do CT-e"""
                vCarga: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                proPred: str = Element(str)
                xOutCat: str = Element(str)

                class infQ(ComplexType):
                    """Informações de quantidades da Carga do CT-e
Para o Aéreo é obrigatório o preenchimento desse campo da seguinte forma.
1 - Peso Bruto, sempre em quilogramas (obrigatório);
2 - Peso Cubado; sempre em quilogramas;
3 - Quantidade de volumes, sempre em unidades (obrigatório);
4 - Cubagem, sempre em metros cúbicos (obrigatório apenas quando for impossível preencher as dimensões da(s) embalagem(ens) na tag xDime do leiaute do Aéreo)."""
                    _max_occurs = -1

                    def add(self, cUnid=None, tpMed=None, qCarga=None) -> TCTe.infCte.infCTeNorm.infCarga.infQ:
                        return super().add(cUnid=cUnid, tpMed=tpMed, qCarga=qCarga)

                    cUnid: str = Element(str)
                    tpMed: str = Element(str)
                    qCarga: TDec_1104 = Element(TDec_1104, tipo="N", tam=(11, 4))
                infQ: List[infQ] = Element(infQ, max_occurs=-1)
            infCarga: infCarga = Element(infCarga)

            class infDoc(ComplexType):
                """Informações dos documentos transportados pelo CT-e
Opcional para Redespacho Intermediario e Serviço vinculado a multimodal.
Poderá não ser informado para os CT-e de redespacho intermediário. Nos demais casos deverá sempre ser informado."""
                _choice = [['infNF', 'infNFe', 'infOutros']]

                class infNF(ComplexType):
                    """Informações das NF
Este grupo deve ser informado quando o documento originário for NF"""
                    _max_occurs = -1
                    _choice = [['infUnidTransp', 'infUnidCarga']]

                    def add(self, nRoma=None, nPed=None, mod=None, serie=None, nDoc=None, dEmi=None, vBC=None, vICMS=None, vBCST=None, vST=None, vProd=None, vNF=None, nCFOP=None, nPeso=None, PIN=None, dPrev=None, infUnidTransp=None, infUnidCarga=None) -> TCTe.infCte.infCTeNorm.infDoc.infNF:
                        return super().add(nRoma=nRoma, nPed=nPed, mod=mod, serie=serie, nDoc=nDoc, dEmi=dEmi, vBC=vBC, vICMS=vICMS, vBCST=vBCST, vST=vST, vProd=vProd, vNF=vNF, nCFOP=nCFOP, nPeso=nPeso, PIN=PIN, dPrev=dPrev, infUnidTransp=infUnidTransp, infUnidCarga=infUnidCarga)

                    nRoma: str = Element(str)
                    nPed: str = Element(str)
                    mod: TModNF = Element(TModNF)
                    serie: str = Element(str)
                    nDoc: str = Element(str)
                    dEmi: TData = Element(TData)
                    vBC: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    vICMS: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    vBCST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    vST: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    vProd: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    vNF: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                    nCFOP: TCfop = Element(TCfop)
                    nPeso: TDec_1203Opc = Element(TDec_1203Opc, tipo="N", tam=(12, 3))
                    PIN: str = Element(str)
                    dPrev: TData = Element(TData)
                    infUnidTransp: List[TUnidadeTransp] = Element(TUnidadeTransp, max_occurs=-1)
                    infUnidCarga: List[TUnidCarga] = Element(TUnidCarga, max_occurs=-1)
                infNF: List[infNF] = Element(infNF, max_occurs=-1)

                class infNFe(ComplexType):
                    """Informações das NF-e"""
                    _max_occurs = -1
                    _choice = [['infUnidTransp', 'infUnidCarga']]

                    def add(self, chave=None, PIN=None, dPrev=None, infUnidTransp=None, infUnidCarga=None) -> TCTe.infCte.infCTeNorm.infDoc.infNFe:
                        return super().add(chave=chave, PIN=PIN, dPrev=dPrev, infUnidTransp=infUnidTransp, infUnidCarga=infUnidCarga)

                    chave: TChNFe = Element(TChNFe)
                    PIN: str = Element(str)
                    dPrev: TData = Element(TData)
                    infUnidTransp: List[TUnidadeTransp] = Element(TUnidadeTransp, max_occurs=-1)
                    infUnidCarga: List[TUnidCarga] = Element(TUnidCarga, max_occurs=-1)
                infNFe: List[infNFe] = Element(infNFe, max_occurs=-1)

                class infOutros(ComplexType):
                    """Informações dos demais documentos"""
                    _max_occurs = -1
                    _choice = [['infUnidTransp', 'infUnidCarga']]

                    def add(self, tpDoc=None, descOutros=None, nDoc=None, dEmi=None, vDocFisc=None, dPrev=None, infUnidTransp=None, infUnidCarga=None) -> TCTe.infCte.infCTeNorm.infDoc.infOutros:
                        return super().add(tpDoc=tpDoc, descOutros=descOutros, nDoc=nDoc, dEmi=dEmi, vDocFisc=vDocFisc, dPrev=dPrev, infUnidTransp=infUnidTransp, infUnidCarga=infUnidCarga)

                    tpDoc: str = Element(str)
                    descOutros: str = Element(str)
                    nDoc: str = Element(str)
                    dEmi: TData = Element(TData)
                    vDocFisc: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                    dPrev: TData = Element(TData)
                    infUnidTransp: List[TUnidadeTransp] = Element(TUnidadeTransp, max_occurs=-1)
                    infUnidCarga: List[TUnidCarga] = Element(TUnidCarga, max_occurs=-1)
                infOutros: List[infOutros] = Element(infOutros, max_occurs=-1)
            infDoc: infDoc = Element(infDoc)

            class docAnt(ComplexType):
                """Documentos de Transporte Anterior"""

                class emiDocAnt(ComplexType):
                    """Emissor do documento anterior"""
                    _max_occurs = -1
                    _choice = [['CNPJ', 'CPF']]

                    def add(self, CNPJ=None, CPF=None, IE=None, UF=None, xNome=None, idDocAnt=None) -> TCTe.infCte.infCTeNorm.docAnt.emiDocAnt:
                        return super().add(CNPJ=CNPJ, CPF=CPF, IE=IE, UF=UF, xNome=xNome, idDocAnt=idDocAnt)

                    CNPJ: TCnpjOpc = Element(TCnpjOpc)
                    CPF: TCpf = Element(TCpf)
                    IE: TIe = Element(TIe)
                    UF: TUf = Element(TUf)
                    xNome: str = Element(str)

                    class idDocAnt(ComplexType):
                        """Informações de identificação dos documentos de Transporte Anterior"""
                        _max_occurs = 2
                        _choice = [['idDocAntPap', 'idDocAntEle']]

                        def add(self, idDocAntPap=None, idDocAntEle=None) -> TCTe.infCte.infCTeNorm.docAnt.emiDocAnt.idDocAnt:
                            return super().add(idDocAntPap=idDocAntPap, idDocAntEle=idDocAntEle)


                        class idDocAntPap(ComplexType):
                            """Documentos de transporte anterior em papel"""
                            _max_occurs = -1

                            def add(self, tpDoc=None, serie=None, subser=None, nDoc=None, dEmi=None) -> TCTe.infCte.infCTeNorm.docAnt.emiDocAnt.idDocAnt.idDocAntPap:
                                return super().add(tpDoc=tpDoc, serie=serie, subser=subser, nDoc=nDoc, dEmi=dEmi)

                            tpDoc: TDocAssoc = Element(TDocAssoc)
                            serie: str = Element(str)
                            subser: str = Element(str)
                            nDoc: str = Element(str)
                            dEmi: TData = Element(TData)
                        idDocAntPap: List[idDocAntPap] = Element(idDocAntPap, max_occurs=-1)

                        class idDocAntEle(ComplexType):
                            """Documentos de transporte anterior eletrônicos"""
                            _max_occurs = -1

                            def add(self, chave=None) -> TCTe.infCte.infCTeNorm.docAnt.emiDocAnt.idDocAnt.idDocAntEle:
                                return super().add(chave=chave)

                            chave: TChNFe = Element(TChNFe)
                        idDocAntEle: List[idDocAntEle] = Element(idDocAntEle, max_occurs=-1)
                    idDocAnt: List[idDocAnt] = Element(idDocAnt, max_occurs=2)
                emiDocAnt: List[emiDocAnt] = Element(emiDocAnt, max_occurs=-1)
            docAnt: docAnt = Element(docAnt)

            class seg(ComplexType):
                """Informações de Seguro da Carga"""
                _max_occurs = -1

                def add(self, respSeg=None, xSeg=None, nApol=None, nAver=None, vCarga=None) -> TCTe.infCte.infCTeNorm.seg:
                    return super().add(respSeg=respSeg, xSeg=xSeg, nApol=nApol, nAver=nAver, vCarga=vCarga)

                respSeg: str = Element(str)
                xSeg: str = Element(str)
                nApol: str = Element(str)
                nAver: str = Element(str)
                vCarga: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
            seg: List[seg] = Element(seg, max_occurs=-1)

            class infModal(ComplexType):
                """Informações do modal"""
                versaoModal: str = Attribute(None)
            infModal: infModal = Element(infModal)

            class peri(ComplexType):
                """Preenchido quando for  transporte de produtos classificados pela ONU como perigosos.
Não deve ser preenchido para modal dutoviário.
												Observação para o modal aéreo:
												- O preenchimento desses campos não desobriga a empresa aérea de emitir os demais documentos que constam na legislação vigente."""
                _max_occurs = -1

                def add(self, nONU=None, xNomeAE=None, xClaRisco=None, grEmb=None, qTotProd=None, qVolTipo=None, pontoFulgor=None) -> TCTe.infCte.infCTeNorm.peri:
                    return super().add(nONU=nONU, xNomeAE=xNomeAE, xClaRisco=xClaRisco, grEmb=grEmb, qTotProd=qTotProd, qVolTipo=qVolTipo, pontoFulgor=pontoFulgor)

                nONU: str = Element(str)
                xNomeAE: str = Element(str)
                xClaRisco: str = Element(str)
                grEmb: str = Element(str)
                qTotProd: str = Element(str)
                qVolTipo: str = Element(str)
                pontoFulgor: str = Element(str)
            peri: List[peri] = Element(peri, max_occurs=-1)

            class veicNovos(ComplexType):
                """informações dos veículos transportados"""
                _max_occurs = -1

                def add(self, chassi=None, cCor=None, xCor=None, cMod=None, vUnit=None, vFrete=None) -> TCTe.infCte.infCTeNorm.veicNovos:
                    return super().add(chassi=chassi, cCor=cCor, xCor=xCor, cMod=cMod, vUnit=vUnit, vFrete=vFrete)

                chassi: str = Element(str)
                cCor: str = Element(str)
                xCor: str = Element(str)
                cMod: str = Element(str)
                vUnit: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                vFrete: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
            veicNovos: List[veicNovos] = Element(veicNovos, max_occurs=-1)

            class cobr(ComplexType):
                """Dados da cobrança do CT-e"""

                class fat(ComplexType):
                    """Dados da fatura"""
                    nFat: str = Element(str)
                    vOrig: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                    vDesc: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                    vLiq: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                fat: fat = Element(fat)

                class dup(ComplexType):
                    """Dados das duplicatas"""
                    _max_occurs = -1

                    def add(self, nDup=None, dVenc=None, vDup=None) -> TCTe.infCte.infCTeNorm.cobr.dup:
                        return super().add(nDup=nDup, dVenc=dVenc, vDup=vDup)

                    nDup: str = Element(str)
                    dVenc: TData = Element(TData)
                    vDup: TDec_1302Opc = Element(TDec_1302Opc, tipo="N", tam=(13, 2))
                dup: List[dup] = Element(dup, max_occurs=-1)
            cobr: cobr = Element(cobr)

            class infCteSub(ComplexType):
                """Informações do CT-e de substituição"""
                _choice = [['tomaICMS', 'tomaNaoICMS']]
                chCte: str = Element(str)

                class tomaICMS(ComplexType):
                    """Tomador é contribuinte do ICMS"""
                    _choice = [['refNFe', 'refNF', 'refCte']]
                    refNFe: TChNFe = Element(TChNFe)

                    class refNF(ComplexType):
                        """Informação da NF ou CT emitido pelo Tomador"""
                        _choice = [['CNPJ', 'CPF']]
                        CNPJ: TCnpj = Element(TCnpj)
                        CPF: TCpf = Element(TCpf)
                        mod: TModDoc = Element(TModDoc)
                        serie: TSerie = Element(TSerie)
                        subserie: TSerie = Element(TSerie)
                        nro: str = Element(str)
                        valor: TDec_1302 = Element(TDec_1302, tipo="N", tam=(13, 2))
                        dEmi: TData = Element(TData)
                    refNF: refNF = Element(refNF)
                    refCte: TChNFe = Element(TChNFe)
                tomaICMS: tomaICMS = Element(tomaICMS)

                class tomaNaoICMS(ComplexType):
                    """Tomador não é contribuinte do ICMS"""
                    refCteAnu: str = Element(str)
                tomaNaoICMS: tomaNaoICMS = Element(tomaNaoICMS)
            infCteSub: infCteSub = Element(infCteSub)
        infCTeNorm: infCTeNorm = Element(infCTeNorm)

        class infCteComp(ComplexType):
            """Detalhamento do CT-e complementado"""
            chave: TChNFe = Element(TChNFe)
        infCteComp: infCteComp = Element(infCteComp)

        class infCteAnu(ComplexType):
            """Detalhamento do CT-e do tipo Anulação"""
            chCte: str = Element(str)
            dEmi: TData = Element(TData)
        infCteAnu: infCteAnu = Element(infCteAnu)

        class autXML(ComplexType):
            """Autorizados para download do XML do DF-e
Informar CNPJ ou CPF. Preencher os zeros não significativos."""
            _max_occurs = 10
            _choice = [['CNPJ', 'CPF']]

            def add(self, CNPJ=None, CPF=None) -> TCTe.infCte.autXML:
                return super().add(CNPJ=CNPJ, CPF=CPF)

            CNPJ: TCnpj = Element(TCnpj)
            CPF: TCpf = Element(TCpf)
        autXML: List[autXML] = Element(autXML, max_occurs=10)
        versao: str = Attribute(None)
        Id: str = Attribute(None)
    infCte: infCte = Element(infCte)
    Signature: Signature = Element(Signature)



class TIdLote(str):
    """Tipo Identificador de controle do envio do lote. Número seqüencial auto-incremental, de controle correspondente ao identificador único do lote enviado. A responsabilidade de gerar e controlar esse número é do próprio contribuinte."""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{1,15}", enumeration=[])
    pass



class TVerCTe(str):
    """Tipo Versão do CT-e - 2.00"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"2\.00", enumeration=[])
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
        """Dados do Recibo do Lote"""
        nRec: TRec = Element(TRec)
        dhRecbto: dateTime = Element(dateTime)
        tMed: str = Element(str)
    infRec: infRec = Element(infRec)
    versao: str = Attribute(TVerCTe)



class TEndernac(Element):
    """Tipo Dados do Endereço"""
    xLgr: str = Element(str)
    nro: str = Element(str)
    xCpl: str = Element(str)
    xBairro: str = Element(str)
    cMun: TCodMunIBGE = Element(TCodMunIBGE)
    xMun: str = Element(str)
    CEP: str = Element(str)
    UF: TUf = Element(TUf)



class TEndOrg(Element):
    """Tipo Dados do Endereço"""
    xLgr: str = Element(str)
    nro: str = Element(str)
    xCpl: str = Element(str)
    xBairro: str = Element(str)
    cMun: TCodMunIBGE = Element(TCodMunIBGE)
    xMun: str = Element(str)
    CEP: str = Element(str)
    UF: TUf = Element(TUf)
    cPais: str = Element(str)
    xPais: str = Element(str)
    fone: TFone = Element(TFone)



class TLocal(Element):
    """Tipo Dados do Local de Origem ou Destino"""
    cMun: TCodMunIBGE = Element(TCodMunIBGE)
    xMun: str = Element(str)
    UF: TUf = Element(TUf)



class TEndReEnt(Element):
    """Tipo Dados do Local de Retirada ou Entrega"""
    _choice = [['CNPJ', 'CPF']]
    CNPJ: TCnpj = Element(TCnpj)
    CPF: TCpf = Element(TCpf)
    xNome: str = Element(str)
    xLgr: str = Element(str)
    nro: str = Element(str)
    xCpl: str = Element(str)
    xBairro: str = Element(str)
    cMun: TCodMunIBGE = Element(TCodMunIBGE)
    xMun: str = Element(str)
    UF: TUf = Element(TUf)



class TCListServ(str):
    """Tipo Código da Lista de Serviços LC 116/2003"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['101', '102', '103', '104', '105', '106', '107', '108', '201', '302', '303', '304', '305', '401', '402', '403', '404', '405', '406', '407', '408', '409', '410', '411', '412', '413', '414', '415', '416', '417', '418', '419', '420', '421', '422', '423', '501', '502', '503', '504', '505', '506', '507', '508', '509', '601', '602', '603', '604', '605', '701', '702', '703', '704', '705', '706', '707', '708', '709', '710', '711', '712', '713', '716', '717', '718', '719', '720', '721', '722', '801', '802', '901', '902', '903', '1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1009', '1010', '1101', '1102', '1103', '1104', '1201', '1202', '1203', '1204', '1205', '1206', '1207', '1208', '1209', '1210', '1211', '1212', '1213', '1214', '1215', '1216', '1217', '1302', '1303', '1304', '1305', '1401', '1402', '1403', '1404', '1405', '1406', '1407', '1408', '1409', '1410', '1411', '1412', '1413', '1501', '1502', '1503', '1504', '1505', '1506', '1507', '1508', '1509', '1510', '1511', '1512', '1513', '1514', '1515', '1516', '1517', '1518', '1601', '1701', '1702', '1703', '1704', '1705', '1706', '1708', '1709', '1710', '1711', '1712', '1713', '1714', '1715', '1716', '1717', '1718', '1719', '1720', '1721', '1722', '1723', '1724', '1801', '1901', '2001', '2002', '2003', '2101', '2201', '2301', '2401', '2501', '2502', '2503', '2504', '2601', '2701', '2801', '2901', '3001', '3101', '3201', '3301', '3401', '3501', '3601', '3701', '3801', '3901', '4001'])
    pass


