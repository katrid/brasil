import os
import json
from brasil.dfe.nfe import NotaFiscal
from brasil.dfe.leiaute.nfe.procEventoNFe_v100 import TProcEvento

EVENTOS = {
    '110110': 'CARTA DE CORREÇÃO',
    '110111': 'CANCELAMENTO',
}

AMBIENTE = {
    '1': 'PRODUÇÃO',
    '2': 'HOMOLOGAÇÃO',
}


def mascara_doc(doc: str) -> str:
    if not doc:
        return ''
    if len(doc) == 14:
        return f'{doc[:2]}.{doc[2:5]}.{doc[5:8]}/{doc[8:12]}-{doc[12:]}'
    elif len(doc) == 11:
        return f'{doc[:3]}.{doc[3:6]}.{doc[6:9]}/{doc[9:13]}'
    return doc


def print_pdf(xml: str | bytes) -> bytes:
    """Gerar o PDF do DANFE"""
    from reptile.bands import Report
    from reptile.exports.pdf import PDF
    rep = Report(self.prepare())
    doc = rep.prepare()
    PDF(doc).export(output_path)


def evento_pdf(xml, xml_evento: str | bytes) -> bytes:
    """Gerar o PDF do evento"""
    from reptile.bands import Report
    from reptile.exports.pdf import PDF
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
    evento.ambiente = AMBIENTE[evento.tpAmb]
    rep.set_data('evento', [evento])
    rep.context['mascara_doc'] = mascara_doc
    rep.context['nfe'] = nf
    rep.context['retEvento'] = ret_evento
    rep.context['dest'] = nf.NFe.infNFe.dest
    rep.context['emit'] = nf.NFe.infNFe.emit
    # processar template
    doc = rep.prepare()
    # gerar pdf
    return PDF(doc).export_bytes()
