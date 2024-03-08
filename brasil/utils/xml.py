from typing import Iterable
import re
from lxml import etree


class NodeProxy:
    def __init__(self, node):
        if not isinstance(node, list):
            node = [node]
        self._node = node

    def __getattr__(self, item):
        if len(self._node) > 0:
            node = self._node[0]
            if item in node.attrib:
                return node.attrib[item]
            elif hasattr(node, item):
                return getattr(node, item)
            nodes = node.findall('{http://www.portalfiscal.inf.br/nfe}' + item)
            if len(nodes):
                return NodeProxy(nodes)
        return None

    def __iter__(self):
        return iter([NodeProxy(n) for n in self._node])

    def __getitem__(self, item):
        return self._node[item]

    @classmethod
    def to_dict(cls, element: etree.Element) -> dict:
        ret = {}
        if element.getchildren() == []:
            tag = re.sub('{.*}', '', element.tag)
            ret[tag] = element.text
        else:
            count = {}
            for elem in element.getchildren():
                subdict = cls.to_dict(elem)
                tag = re.sub('{.*}', '', element.tag)
                subtag = re.sub('{.*}', '', elem.tag)
                if ret.get(tag, False) and subtag in ret[tag].keys():
                    count[subtag] = count[subtag] + 1 if count.get(subtag, False) else 1
                    elemtag = subtag + str(count[subtag])
                    subdict = {elemtag: subdict[subtag]}
                if ret.get(tag, False):
                    ret[tag].update(subdict)
                else:
                    ret[tag] = subdict
        return ret

# Tags NFE
TAG_NFEPROC = '{http://www.portalfiscal.inf.br/nfe}nfeProc'
TAG_NFE = '{http://www.portalfiscal.inf.br/nfe}NFe'
TAG_ENVINFE = '{http://www.portalfiscal.inf.br/nfe}enviNFe'
TAG_PROTNFE = '{http://www.portalfiscal.inf.br/nfe}protNFe'
TAG_EVENTO = '{http://www.portalfiscal.inf.br/nfe}procEventoNFe'

# Tags CTe
TAG_CTEPROC = '{http://www.portalfiscal.inf.br/cte}cteProc'
TAG_CTE = '{http://www.portalfiscal.inf.br/cte}CTe'
TAG_PROTCTE = '{http://www.portalfiscal.inf.br/cte}protCTe'

# Tags MDFe
TAG_MDFEPROC = '{http://www.portalfiscal.inf.br/mdfe}mdfeProc'
TAG_MDFE = '{http://www.portalfiscal.inf.br/mdfe}MDFe'
TAG_PROTMDFE = '{http://www.portalfiscal.inf.br/mdfe}protMDFe'


class Documento:
    """
    Classe para parsing de documentos fiscais a partir de string XML retornando uma árvore
    de nós estruturados utilizando LXML.
    """
    _docs: [NodeProxy] = None

    def __iter__(self):
        return iter(self._docs)

    def __getitem__(self, item):
        return self._docs[item]

    @classmethod
    def fromstring(cls, xml: bytes) -> Iterable[NodeProxy]:
        return cls(etree.fromstring(xml))


class NotasFiscais(Documento):
    """
    Classe para parsing de notas fiscais a partir da string do XML retornando uma árvore de nós
    estruturados no padrão lxml Element
    """
    def __init__(self, xml=None):
        if (xml is not None) and xml.tag == TAG_ENVINFE:
            self._docs = [NodeProxy(n) for n in xml.findall(TAG_NFE)]
        elif (xml is not None) and xml.tag == TAG_NFEPROC:
            nfe_el = xml.findall(TAG_NFE)
            prot_el = xml.findall(TAG_PROTNFE)
            self._docs = [NodeProxy(n) for n in (nfe_el, prot_el)]
        elif (xml is not None) and ((xml.tag == TAG_NFE) or (xml.tag == 'procEventoNFe')):
            self._docs = [NodeProxy(xml)]
        else:
            self._docs = []


class CTe(Documento):
    """
    Classe para parsing de CTe a partir da string do XML retornando uma árvore de nós
    estruturados no padrão lxml Element
    """
    def __init__(self, xml=None):
        if (xml is not None) and xml.tag == TAG_CTEPROC:
            cte_el = xml.findall(TAG_CTE)
            prot_el = xml.findall(TAG_PROTCTE)
            self._docs = [NodeProxy(n) for n in (cte_el, prot_el)]
        elif (xml is not None) and xml.tag == TAG_CTE:
            self._docs = [NodeProxy(xml)]
        else:
            self._docs = []


class MDFe(Documento):
    """
    Classe para parsing de MDFe a partir da string do XML retornando uma árvore de nós
    estruturados no padrão lxml Element
    """
    def __init__(self, xml=None):
        if (xml is not None) and xml.tag == TAG_MDFEPROC:
            cte_el = xml.findall(TAG_MDFE)
            prot_el = xml.findall(TAG_PROTMDFE)
            self._docs = [NodeProxy(n) for n in (cte_el, prot_el)]
        elif (xml is not None) and xml.tag == TAG_MDFE:
            self._docs = [NodeProxy(xml)]
        else:
            self._docs = []
