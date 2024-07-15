import lxml.etree

from .mdfe import *


def merge_prot(xml: str, prot: str):
    """
    Mesclar um xml MDFe com um protocolo de autorização
    :param xml:
    :param prot:
    :return:
    """
    mdf = lxml.etree.fromstring(xml)
    if mdf.tag == '{http://www.portalfiscal.inf.br/mdfe}mdfeProc':
        xml = lxml.etree.tostring(mdf.find('.//{http://www.portalfiscal.inf.br/mdfe}MDFe'))
    if isinstance(xml, bytes):
        xml = xml.decode('utf-8')
    prot = lxml.etree.tostring(lxml.etree.fromstring(prot).find('.//{http://www.portalfiscal.inf.br/mdfe}protMDFe')).decode('utf-8')
    return '<mdfeProc versao="3.00" xmlns="http://www.portalfiscal.inf.br/mdfe">' + xml + prot + '</mdfeProc>'
