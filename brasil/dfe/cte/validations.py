""""
Validações obrigatórias feitas conforme especificado no "Manual de Orientação do Contribuinte
Anexo I – Leiaute e Regras de Validação do CTe Versão 4.00 – agosto de 2022" localizado em https://dfe-portal.svrs.rs.gov.br/Cte/Documentos#
"""
import os
from math import isclose
from lxml import etree
from brasil.dfe.base import Validator
from brasil.consts import UF, CIDADES, CODIGO_UF
from .rejections import rejections
from brasil.utils.formulas import modulo11
from brasil.dfe.utils.dfe_utils import parse_chave_acesso, validar_cnpj, validar_cpf
from .consts import *


MODAL_SCHEMAS = {
    '01': 'cteModalRodoviario_v4.00.xsd',
    '02': 'cteModalAereo_v4.00.xsd',
    '03': 'cteModalAquaviario_v4.00.xsd',
    '04': 'cteModalFerroviario_v4.00.xsd',
    '05': 'cteModalDutoviario_v4.00.xsd',
    '06': 'cteMultiModal_v4.00.xsd',
}


class CTeValidator(Validator):
    def __init__(self, cte):
        self.documento = cte
        super().__init__()

    @property
    def mensagem(self):
        if self.codigo:
            return rejections.get(self.codigo)['mensagem'] + '\n' + 'cStat: ' + str(rejections.get(self.codigo)['cStat'])
    
    @property
    def is_interestadual(self):
        return self.documento.infCte.ide.UFIni != self.documento.infCte.ide.UFFim
    
    @property
    def is_exterior(self):
        return (self.documento.infCte.ide.UFIni == 'EX') or (self.documento.infCte.ide.UFFim == 'EX')
        
    def get_tomador(self):
        tp_toma = self.documento.infCte.ide.toma3.toma
        if tp_toma == '0':
            return self.documento.infCte.rem, self.documento.infCte.rem.enderReme.UF
        elif tp_toma == '1':
            return self.documento.infCte.exped, self.documento.infCte.exped.enderExped.UF
        elif tp_toma == '2':
            return self.documento.infCte.receb, self.documento.infCte.receb.enderReceb.UF
        elif tp_toma == '3':
            return self.documento.infCte.dest, self.documento.infCte.dest.enderDest.UF
        elif tp_toma == '4':
            return self.documento.infCte.ide.toma4, self.documento.infCte.ide.toma4.enderToma.UF

    def _valida_ator(self, ator, cods: list):
        if ator.CNPJ is not None:
            self.codigo = cods[0]
            assert validar_cnpj(ator.CNPJ)
        if ator._name != 'emit' and ator.CPF is not None:
            self.codigo = cods[1]
            assert validar_cpf(ator.CPF)
        self.codigo = cods[2]
        if ator._name == 'rem':
            ender = getattr(ator, 'ender' + 'Reme')
        elif ator._name == 'toma4':
            ender = getattr(ator, 'ender' + 'Toma')
        else:
            ender = getattr(ator, 'ender' + ator._name.capitalize())
        uf = ender.cUF if hasattr(ender, 'cUF') else CODIGO_UF.get(ender.UF)
        assert uf == ender.cMun[0:2]
        self.codigo = cods[3]
        mun = CIDADES.get(ender.cMun)
        assert mun is not None
        # TODO verificar validação da IE, varia de acordo com a UF

    def _validate_modal_xml(self):
        schema_doc = etree.parse(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'schemas', 'cte',
                                MODAL_SCHEMAS.get(self.documento.infCte.ide.modal)))
        modal_schema = etree.XMLSchema(schema_doc)
        if not modal_schema.validate(etree.fromstring(self.documento.infCte.infCTeNorm.infModal._xmltmp)):
            raise AssertionError(modal_schema.error_log.last_error.message)
        
    def _validar_chave(self, chave: str, modelo: str):
        if len(chave) == 44:
            res = parse_chave_acesso(chave)
            assert res['uf'] == self.documento.infCte.ide.cUF, 'UF inválida'
            assert res['modelo'] == modelo, 'Modelo Inválido'
            assert validar_cnpj(res['cnpj']) or validar_cpf(res['cnpj']), 'CNPJ Inválido'
            assert res['numero'] != '000000000', 'Numero do documento zerado'
        else:
            raise AssertionError('Chave com menos de 44 caracteres')

    class ValidationList:
        # VALIDAÇÕES GERAIS
        def validate_razao_homolog_emit(self):
            self.codigo = 'G002'
            if self.documento.infCte.ide.tpAmb == 2 and self.documento.infCte.ide.tpEmis != '3' and self.documento.infCte.emit:
                assert self.documento.infCte.emit.xNome == 'CTE EMITIDO EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL'

        def validate_razao_homolog_exp(self):
            self.codigo = 'G003'
            if self.documento.infCte.ide.tpAmb == 2 and self.documento.infCte.ide.tpEmis != '3' and self.documento.infCte.exped:
                assert self.documento.infCte.exped.xNome == 'CTE EMITIDO EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL'
        
        def validate_razao_homolog_receb(self):
            self.codigo = 'G004'
            if self.documento.infCte.ide.tpAmb == 2 and self.documento.infCte.ide.tpEmis != '3' and self.documento.infCte.exped:
                assert self.documento.infCte.exped.xNome == 'CTE EMITIDO EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL'

        def validate_razao_homolog_dest(self):
            self.codigo = 'G005'
            if self.documento.infCte.ide.tpAmb == 2 and self.documento.infCte.ide.tpEmis != '3' and self.documento.infCte.dest:
                assert self.documento.infCte.dest.xNome == 'CTE EMITIDO EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL'

        def validate_serie(self):
            self.codigo = 'G006'
            if self.documento.infCte.ide.tpEmis != '3':
                assert int(self.documento.infCte.ide.serie) not in range(890, 899)

        def validate_uf(self):
            self.codigo = 'G007'
            if self.documento.infCte.ide.tpEmis != '3':
                assert self.documento.infCte.emit.enderEmit.UF == UF.get(self.documento.chave[0:2])

        def validate_fsda(self):
            self.codigo = 'G008'
            if self.documento.infCte.ide.tpEmis != '5':
                assert not self.documento.infCte.ide.dhCont and not self.documento.infCte.ide.xJust
            else:
                self.codigo = 'G009'
                assert self.documento.infCte.ide.dhCont and self.documento.infCte.ide.xJust

        def validate_dt_cont(self):
            self.codigo = 'G010'
            if self.documento.infCte.ide.dhCont:
                assert self.documento.infCte.ide.dhCont <= self.documento.infCte.ide.dhEmi

        def validate_amb_aut(self):
            self.codigo = 'G011'
            if 'SVC' in self.documento._config.uf:
                assert self.documento.infCte.ide.tpEmis in ('5', '7', '8')
                self.codigo = 'G012'
                assert self.documento.infCte.ide.tpCTe == '0'

        def validate_chave_modelo(self):
            self.codigo = 'G013'
            assert self.documento.chave[20:22] == '57'

        def validate_id(self):
            self.codigo = 'G014'
            assert self.documento.infCte.Id == 'CTe' + self.documento.chave

        def validate_dv(self):
            self.codigo = 'G015'   
            assert self.documento.chave[43] == str(modulo11(self.documento.chave))
        
        def validate_cte_norm(self):
            self.codigo = 'G016'
            if self.documento.infCte.ide.tpCTe in ('0', '3'):
                assert self.documento.infCte.infCTeNorm is not None

        def validate_cte_comp(self):
            self.codigo = 'G017'
            if self.documento.infCte.ide.tpCTe == '1':
                assert self.documento.infCte.infCteComp is not None

        def validate_toma_rem(self):
            self.codigo = 'G018'
            if self.documento.infCte.ide.toma3.toma == '0':
                assert self.documento.infCte.rem is not None

        def validate_toma_exped(self):
            self.codigo = 'G019'
            if self.documento.infCte.ide.toma3.toma == '1':
                assert self.documento.infCte.exped is not None

        def validate_toma_receb(self):
            self.codigo = 'G020'
            if self.documento.infCte.ide.toma3.toma == '2':
                assert self.documento.infCte.receb is not None

        def validate_toma_dest(self):
            self.codigo = 'G021'
            if self.documento.infCte.ide.toma3.toma == '3':
                assert self.documento.infCte.dest is not None

        def validate_toma_ie(self):
            self.codigo = 'G022'
            tomador, tomador_uf = self.validator.get_tomador()
            if self.documento.infCte.ide.indIEToma == '1':
                assert tomador.IE is not None and tomador.IE != 'ISENTO'
            elif self.documento.infCte.ide.indIEToma == '2':
                self.codigo = 'G023'
                assert tomador.IE is not None and tomador.IE == 'ISENTO'
                self.codigo = 'G024'
                assert tomador_uf not in ('AM', 'BA', 'CE', 'GO', 'MG', 'MS', 'MT', 'PE', 'RN', 'SE', 'SP')

        # VALIDAÇÕES MODAIS
        def validate_versao_modal(self):
            self.codigo = 'G025'
            if self.documento.infCte.ide.tpCTe in ('0', '3'):
                # TODO verificar como assegurar que a versão é garantida, temporariamente verificaremos estaticamente
                assert self.documento.infCte.infCTeNorm.infModal.versaoModal == '4.00'

        def validate_schema_modal(self):
            # TODO verificar porque validação do xml do modal está falhando
            self.codigo = 'G026'
            # if self.documento.infCte.ide.tpCTe in ('0', '3'):
            #     self._validate_modal_xml()

        def validate_vl_carga(self):
            self.codigo = 'G027'
            if self.documento.infCte.ide.tpCTe in ('0', '3') and self.documento.infCte.ide.modal != '05':
                assert self.documento.infCte.infCTeNorm.infCarga is not None

        def validate_aqua(self):
            self.codigo = 'G028'
            if self.documento.infCte.ide.tpCTe in ('0', '3') and self.documento.infCte.ide.modal == '03' and self.documento.infCte.ide.tpServ in ('3', '4'):
                assert self.documento.infCte.infCTeNorm.infModal.aquav.detCont is not None

        # TODO adicionar validações da seção "Validações do Tráfego Mútuo (Modal Ferroviário)" do leiaute, regras G029 a G035

        # VALIDAÇÕES DOS DOCUMENTOS TRANSPORTADOS
        def validate_infdoc(self):
            self.codigo = 'G036'
            if self.documento.infCte.ide.tpCTe in ('0', '3'):
                if self.documento.infCte.ide.tpServ not in ('3', '4'):
                    assert self.documento.infCte.infCTeNorm.infDoc is not None
                else:
                    self.codigo = 'G037'
                    assert self.documento.infCte.infCTeNorm.infDoc is None
                if self.documento.infCte.infCTeNorm.infDoc is not None:
                    self.codigo = 'G038'
                    assert all([len(doc._list) <= 2000 for doc in (self.documento.infCte.infCTeNorm.infDoc.infNF, self.documento.infCte.infCTeNorm.infDoc.infNFe, self.documento.infCte.infCTeNorm.infDoc.infOutros)])

                    if len(self.documento.infCte.infCTeNorm.infDoc.infNFe._list) > 0:
                        self.codigo = 'G039'
                        chaves = [nf.chave for nf in self.documento.infCte.infCTeNorm.infDoc.infNFe._list]
                        assert len(chaves) == len(set(chaves))
                        self.codigo = 'G040'
                        for chave in chaves:
                            self.validator._validar_chave(chave, '55')
                            # self.codigo = 'G041'
                            # if self.documento._config.amb == '1':
                            #     res = NotaFiscal.public_consultar(chave, self._nfe_config)
                            #     assert res.retorno.cStat == '100', res.retorno.xMotivo + f'\nNFe: {chave}'
                    
                    infOutros = self.documento.infCte.infCTeNorm.infDoc.infOutros._list
                    if len(infOutros) > 0 and self.validator.is_interestadual:
                        self.codigo = 'G045'
                        for obj in infOutros:
                            assert obj.tpDoc in ('59', '65')
        
        # VALIDAÇÕES DE VALORES
        def validate_vl_serv(self):
            self.codigo = 'G046'
            if self.documento.infCte.ide.tpCTe in ('0', '3'):
                assert float(self.documento.infCte.vPrest.vTPrest) <= VALOR_MAX_SERVICO

        def validate_bc_icms(self):
            self.codigo = 'G47'
            icms = self.documento.infCte.imp.ICMS
            if icms.ICMS00.CST is not None:
                assert isclose(icms.ICMS00.vICMS, (icms.ICMS00.vBC * icms.ICMS00.pICMS), TOLERANCIA_ICMS)
            elif icms.ICMS20.CST is not None:
                assert isclose(icms.ICMS20.vICMS, (icms.ICMS20.vBC * icms.ICMS20.pICMS), TOLERANCIA_ICMS)
            elif icms.ICMS60.CST is not None:
                assert isclose(icms.ICMS60.vICMSSTRet, (icms.ICMS60.vBCSTRet * icms.ICMS60.pICMSSTRet), TOLERANCIA_ICMS)
            elif icms.ICMS90.CST is not None:
                assert isclose(icms.ICMS90.vICMS, (icms.ICMS90.vBC * icms.ICMS90.pICMS), TOLERANCIA_ICMS)
            elif icms.ICMSOutraUF.CST is not None:
                assert isclose(icms.ICMSOutraUF.vICMSOutraUF, (icms.ICMSOutraUF.vBC * icms.ICMSOutraUF.pICMSOutraUF), TOLERANCIA_ICMS)

        def validate_vrec(self):
            self.codigo = 'G048'
            assert self.documento.infCte.vPrest.vRec <= self.documento.infCte.vPrest.vTPrest

        # VALIDAÇÕES CFOP
        def validate_cfop_op(self):
            self.codigo = 'G049'
            assert self.documento.infCte.ide.CFOP in CFOPS_VALIDOS_CTE

        def validate_ini_cfop(self):
            self.codigo = 'G050'
            if self.documento.infCte.ide.UFFim != 'EX':
                if self.validator.is_interestadual:
                    assert self.documento.infCte.ide.CFOP[0] == '6'
                else:
                    assert self.documento.infCte.ide.CFOP[0] == '5'
            else:
                assert self.documento.infCte.ide.CFOP[0] == '7'

        def validate_uf_emit(self):
            self.codigo = 'G051'
            if self.documento.infCte.ide.tpEmis != '3' and not self.validator.is_exterior:
                if self.documento.infCte.emit.enderEmit.UF != self.documento.infCte.ide.UFIni:
                    assert self.documento.infCte.ide.CFOP in ('5932', '6932')
                else:
                    self.codigo = 'G052'
                    assert self.documento.infCte.ide.CFOP not in ('5932', '6932')
        
        # VALIDAÇÕES CTE SUBSTITUIÇÃO
        def validate_tp_emis(self):
            self.codigo = 'G076'
            if self.documento.infCte.ide.tpCTe == '3':
                assert self.documento.infCte.ide.tpEmis == '1'

        def validate_grupo_subs(self):
            self.codigo = 'G077'
            if self.documento.infCte.ide.tpCTe == '3':
                sub = self.documento.infCte.infCTeNorm.infCteSub
                assert sub is not None and sub.chCte is not None 

        def validate_chave_cte(self):
            self.codigo = 'G078'
            if self.documento.infCte.ide.tpCTe == '3':
                self.validator._validar_chave(self.documento.chave, '57')

        # VALIDAÇÕES EMITENTE
        def validate_emit(self):
            self.validator._valida_ator(self.documento.infCte.emit, ['G104', None, 'G112', 'G113', 'G106'])
            self.codigo = 'G105'
            assert self.documento.infCte.emit.IE is not None

        # VALIDAÇÕES REMETENTE
        def validate_rem(self):
            if self.documento.infCte.rem._xmltmp is not None:
                self.validator._valida_ator(self.documento.infCte.rem, ['G114', 'G115', 'G116', 'G117', 'G118'])

        # VALIDAÇÕES DESTINATÁRIO
        def validate_dest(self):
            if self.documento.infCte.dest._xmltmp is not None:
                self.validator._valida_ator(self.documento.infCte.dest, ['G122', 'G123', 'G124', 'G125', 'G126'])

        # VALIDAÇÕES EXPEDIDOR
        def validate_exped(self):
            if self.documento.infCte.exped._xmltmp is not None:
                self.validator._valida_ator(self.documento.infCte.exped, ['G132', 'G133', 'G134', 'G135', 'G136'])

        # VALIDAÇÕES RECEBEDOR
        def validate_receb(self):
            if self.documento.infCte.receb._xmltmp is not None:
                self.validator._valida_ator(self.documento.infCte.receb, ['G140', 'G141', 'G142', 'G143', 'G144'])

        # VALIDAÇÕES TOMADOR
        def validate_toma(self):
            if self.documento.infCte.ide.toma4._xmltmp is not None:
                self.validator._valida_ator(self.documento.infCte.toma4, ['G148', 'G149', 'G150', 'G151', 'G152'])

        # VALIDAÇÕES CTE COMPLEMENTAR
        def validate_comp_chave(self):
            self.codigo = 'G161'
            if self.documento.infCte.ide.tpCTe == '1':
                self.validator._validar_chave(self.documento.infCte.infCteComp.chCTe, '57')
        
        # TODO verificar validação G177, como fica a estrutura do xml em casos onde o CTe complementar tem mais de uma nota complementada, não está claro no leiaute

        # VALIDAÇÕES INICIO E FIM DA PRESTAÇÃO
        def validate_uf_env(self):
            self.codigo = 'G178'
            assert self.documento.infCte.ide.cMunEnv[0:2] == CODIGO_UF.get(self.documento.infCte.ide.UFEnv)
            self.codigo = 'G179'
            assert CIDADES.get(self.documento.infCte.ide.cMunEnv) is not None
        
        def validate_uf_ini(self):
            self.codigo = 'G180'
            assert self.documento.infCte.ide.cMunIni[0:2] == CODIGO_UF.get(self.documento.infCte.ide.UFIni)
            self.codigo = 'G181'
            assert CIDADES.get(self.documento.infCte.ide.cMunIni) is not None

        def validate_uf_fim(self):
            self.codigo = 'G182'
            assert self.documento.infCte.ide.cMunFim[0:2] == CODIGO_UF.get(self.documento.infCte.ide.UFFim)
            self.codigo = 'G183'
            assert CIDADES.get(self.documento.infCte.ide.cMunFim) is not None