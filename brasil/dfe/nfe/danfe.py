import os
from datetime import datetime
import json

try:
    from reptile.bands import Report
    from reptile.exports.pdf import PDF
    from reptile.utils.text import format_mask, format_number
except:
    pass

from brasil.dfe.nfe import NotaFiscal
from brasil.dfe.leiaute.nfe.nfe_v400 import NFe
from brasil.dfe.leiaute.nfe.procEventoNFe_v100 import TProcEvento
from brasil.dfe.leiaute.nfe import e110110_v100
from brasil.dfe.leiaute.nfe import e110111_v100
from brasil.dfe.nfe.consts import EVENTOS
from brasil.dfe.consts import AMBIENTE

__all__ = ['print_pdf', 'evento_pdf']


def mascara_doc(doc: str) -> str:
    if not doc:
        return ''
    if len(doc) == 14:
        return f'{doc[:2]}.{doc[2:5]}.{doc[5:8]}/{doc[8:12]}-{doc[12:]}'
    elif len(doc) == 11:
        return f'{doc[:3]}.{doc[3:6]}.{doc[6:9]}/{doc[9:13]}'
    return doc


def get_imposto(imp: NFe._infNFe._det._imposto):
    return {
        'icms': get_icms(imp),
        'ipi': imp.IPI,
    }


def get_icms(imp: NFe._infNFe._det._imposto):
    if imp.ICMS.ICMS00.CST == '00':
        return imp.ICMS.ICMS00
    if imp.ICMS.ICMS10.CST == '10':
        return imp.ICMS.ICMS10
    if imp.ICMS.ICMS20.CST == '20':
        return imp.ICMS.ICMS20
    if imp.ICMS.ICMS30.CST == '30':
        return imp.ICMS.ICMS30
    if imp.ICMS.ICMS40.CST == '40':
        return imp.ICMS.ICMS40
    if imp.ICMS.ICMS51.CST == '51':
        return imp.ICMS.ICMS51
    if imp.ICMS.ICMS60.CST == '60':
        return imp.ICMS.ICMS60
    if imp.ICMS.ICMS70.CST == '70':
        return imp.ICMS.ICMS70
    if imp.ICMS.ICMS90.CST == '90':
        return imp.ICMS.ICMS90


# inicializar configurações reptile
try:
    from reptile.env import EnvironmentSettings

    EnvironmentSettings.DecimalSettings.decimal_pos = 2
    EnvironmentSettings.DecimalSettings.thousand_sep = '.'
    EnvironmentSettings.DecimalSettings.decimal_sep = ','
except ModuleNotFoundError:
    pass


def print_pdf(xml: str | bytes, template_name='danfe-retrato.json', logo: bytes = None) -> bytes:
    """Gerar o PDF do DANFE"""
    # carregar template
    template_name = os.path.join(os.path.dirname(__file__), f'../templates/{template_name}')
    with open(template_name, 'rb') as f:
        template = json.load(f)
    rep = Report(template)
    # carregar xmls
    nf = NotaFiscal(xml).nota
    emit = nf.NFe.infNFe.emit
    imp = nf.NFe.infNFe.total.ICMSTot
    transp = nf.NFe.infNFe.transp
    inf_adic = nf.NFe.infNFe.infAdic.infCpl
    if inf_adic:
        inf_adic = inf_adic.replace(';', '\n')
    if emit.CRT == '0':
        descr_cst = 'CSOSN / CST'
    else:
        descr_cst = 'CST'
    rep.context['descr_cst'] = descr_cst
    rep.context['vols'] = transp.vol
    rep.context['descr_total'] = 'LÍQUIDO'
    rep.context['descr_desconto'] = 'VALOR'  # todo parametrizar %
    mensagem_sefaz = nf.nfeProc.protNFe.infProt.xMsg if nf.nfeProc else None
    rep.context['mensagem_sefaz'] = mensagem_sefaz
    rep.context['ide'] = nf.NFe.infNFe.ide
    rep.context['emit'] = emit
    rep.context['dest'] = nf.NFe.infNFe.dest
    rep.context['imp'] = imp
    rep.context['transp'] = transp
    rep.context['transporta'] = transp.transporta
    rep.context['chave'] = nf.chave
    prods = [{'prod': det.prod, 'imp': get_imposto(det.imposto)} for det in nf.NFe.infNFe.det]
    rep.context['prods'] = prods
    rep.context['mascara_doc'] = mascara_doc
    rep.context['inf_adic'] = [{'obs': inf_adic}]
    if nf.nfeProc:
        rep.context['protocolo'] = nf.nfeProc.protNFe.infProt.nProt + ' ' + datetime.fromisoformat(
            nf.nfeProc.protNFe.infProt.dhRecbto).strftime('%d/%m/%Y %H:%M:%S')
    else:
        rep.context['protocolo'] = 'SEM VALOR FISCAL'
    end = emit.enderEmit
    rep.context[
        'emit_endereco'] = f'{end.xLgr} {end.nro}, {end.xCpl or ""}, {end.xBairro} {end.xMun} - {end.UF} - CEP: {format_mask("99999-999", end.CEP)}\nFone: {(end.fone and format_mask("(99)99999-9999", end.fone)) or ""}'

    # formatar resumo do canhoto
    vl = format_number(',0.00', nf.NFe.infNFe.total.ICMSTot.vNF)
    rep.context[
        'resumo_canhoto'] = f'Emissão: {datetime.fromisoformat(nf.NFe.infNFe.ide.dhEmi).strftime('%d/%m/%Y')}  Dest/Reme: {nf.NFe.infNFe.dest.xNome}  Valor Total R$ ' + vl

    # tratar logo
    if not logo:
        elEmit = rep.find_object('memDadosEmitente')
        elEmit.left = 6
        elEmit.width += 85

    doc = rep.prepare()
    # gerar pdf
    return PDF(doc).export_bytes()


def evento_pdf(xml, xml_evento: str | bytes) -> bytes:
    """Gerar o PDF do evento"""
    # carregar template
    template_name = os.path.join(os.path.dirname(__file__), '../templates/danfe-evento.json')
    with open(template_name, 'rb') as f:
        template = json.load(f)
    rep = Report(template)
    # carregar xmls
    nf = NotaFiscal(xml).nota
    ev = TProcEvento.fromstring(xml_evento)
    ret_evento = ev.retEvento and ev.retEvento.infEvento
    evento = ev.evento.infEvento
    evento.desc_evento = EVENTOS.get(ret_evento.tpEvento, ret_evento.tpEvento)
    evento.ambiente = AMBIENTE[evento.tpAmb].upper()
    rep.set_data('evento', [evento])
    if evento.tpEvento == '110110':
        det_evento = e110110_v100.detEvento.fromstring(evento.detEvento)
        rep.context['xCondUso'] = det_evento.xCondUso.replace('com: I', 'com:\nI').replace(';', '\n')
        rep.context['xCorrecao'] = det_evento.xCorrecao.replace(';', '\n')
    elif evento.tpEvento == '110111':
        det_evento = e110111_v100.detEvento.fromstring(evento.detEvento)
        rep.context['xJust'] = det_evento.xJust.replace(';', '\n')
    rep.context['mascara_doc'] = mascara_doc
    rep.context['nfe'] = nf
    rep.context['retEvento'] = ret_evento
    rep.context['dest'] = nf.NFe.infNFe.dest
    rep.context['emit'] = nf.NFe.infNFe.emit
    # processar template
    doc = rep.prepare()
    # gerar pdf
    return PDF(doc).export_bytes()
