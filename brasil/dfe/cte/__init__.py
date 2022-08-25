import lxml.etree

from .cte import *


def merge_prot(xml: str, prot: str):
    cte = lxml.etree.fromstring(xml)
    if cte.tag == '{http://www.portalfiscal.inf.br/cte}cteProc':
        xml = lxml.etree.tostring(cte.find('.//{http://www.portalfiscal.inf.br/cte}CTe'))
    if isinstance(xml, bytes):
        xml = xml.decode('utf-8')
    prot = lxml.etree.tostring(lxml.etree.fromstring(prot).find('.//{http://www.portalfiscal.inf.br/cte}protCTe')).decode('utf-8')
    return '<cteProc versao="3.00" xmlns="http://www.portalfiscal.inf.br/cte">' + xml + prot + '</cteProc>'
