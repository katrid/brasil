import os
import json
import dateutil.parser
from reptile.bands import Report
from brasil.dfe.utils.dfe_utils import *
from brasil.utils.xml import NotasFiscais, NodeProxy 


class DANFE:
    def __init__(self, xml: str) -> None:
        self._xml = NotasFiscais.fromstring(xml)
        self.id = self._xml._docs[0]._node[0].find('{http://www.portalfiscal.inf.br/nfe}infNFe').get('Id')
        self.xml = {}
        for doc in self._xml._docs:
            self.xml = {**self.xml, **NodeProxy.to_dict(doc._node[0])}
        if 'protNFe' in self.xml:
            self.xml = {'nfeProc': self.xml}

    def export(self, output_path: str) -> str:
        from reptile.exports.pdf import PDF
        templ, filename = self.prepare()
        rep = Report(templ)
        doc = rep.prepare()
        PDF(doc).export(os.path.join(output_path, filename))
        return os.path.basename(filename)

    def prepare(self):
        with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'DANFERetrato.json'), 'r') as f:
            templ = json.load(f)

        prepared = self.prepared_xml
        if 'nfeProc' in prepared:
            infNFe = prepared['nfeProc']['NFe']['infNFe']
            del templ['report']['watermark']
        else:
            infNFe = prepared['NFe']['infNFe']
        
        infNFe['transp']['tp_frete'] = FRETE.get(infNFe['transp']['modFrete'])
        templ['report']['datasources'] = [
            { 
                'name': 'dados', 
                'data': [prepared] 
            }, 
            { 
                'name': 'itens', 
                'data': [] 
            },
            {
                'name': 'dest',
                'data': [infNFe['dest']],
            },
            {
                'name': 'imposto',
                'data': [infNFe['total']['ICMSTot']]
            },
            {
                'name': 'transporte',
                'data': [infNFe['transp']]
            },
            {
                'name': 'infcomplementares',
                'data': [infNFe['infAdic']]
            }
        ]
        templ['report']['datasources']
        if 'retirada' in infNFe:
            templ['report']['datasources'].append(
                {
                    'name': 'retirada',
                    'data': [infNFe['retirada']]
                },
            )
        if 'entrega' in infNFe:
            templ['report']['datasources'].append(
                {
                    'name': 'entrega',
                    'data': [infNFe['entrega']]
                },
            )
        if infNFe['transp'].get('vol'):
            templ['report']['datasources'].append(
                {
                    'name': 'volumes',
                    'data': [infNFe['transp'].get('vol')]
                },
            )
        # add itens datasource
        if not isinstance(infNFe['det'], list):
            infNFe['det'] = [infNFe['det']]

        for item in infNFe['det']:
            templ['report']['datasources'][1]['data'].append(item)
            
        return templ, self.id + '.pdf'
    
    @property
    def prepared_xml(self):
        # format specific fields for diplay needs only
        formatted = self.xml.copy()
        if 'nfeProc' in formatted:
            infNFe = formatted['nfeProc']['NFe'] 
            formatted['NFe'] = infNFe
        else:
            infNFe = formatted['NFe']

        dhEmi = dateutil.parser.isoparse(infNFe['infNFe']['ide']['dhEmi'])
        formatted['dtEmi'] = dhEmi.date().strftime('%d/%m/%Y')
        formatted['hEmi'] = dhEmi.time().strftime('%H:%M:%S')        
        formatted['serie'] = infNFe['infNFe']['ide']['serie'].zfill(3)
        numero = infNFe['infNFe']['ide']['nNF'].zfill(9)
        formatted['numero'] = '.'.join([numero[i:i + 3] for i in range(0, len(numero), 3)])
        dhSaiEnt = dateutil.parser.isoparse(infNFe['infNFe']['ide']['dhSaiEnt'])
        formatted['dtSaiEnt'] = dhSaiEnt.date().strftime('%d/%m/%Y')
        formatted['hSaiEnt'] = dhSaiEnt.time().strftime('%H:%M:%S')
        formatted['docEmit'] = format_doc(infNFe['infNFe']['emit'])
        formatted['docDest'] = format_doc(infNFe['infNFe']['dest'])

        if 'nfeProc' in formatted: # se nf transmitida
            chave = formatted['nfeProc']['protNFe']['infProt']['chNFe']
            formatted['barcode'] = f'{chave}'
            formatted['chave'] = ' '.join([chave[i:i + 4] for i in range(0, len(chave), 4)])
            if 'dhRecbto' in formatted['nfeProc']['protNFe']['infProt']:
                dhAut = dateutil.parser.isoparse(formatted['nfeProc']['protNFe']['infProt']['dhRecbto'])
                formatted['dtAut'] = dhAut.date().strftime('%d/%m/%Y')
                formatted['hAut'] = dhAut.time().strftime('%H:%M:%S')
            else:
                formatted['dtAut'] = None
                formatted['hAut'] = None

        itens = infNFe['infNFe']['det']
        if not isinstance(itens, list):
            itens = [itens]
        for item in itens:
            item['imposto']['ICMS'] = self.get_icms(item)
            item['imposto']['IPI'] = self.get_ipi(item)

        formatted['resumo'] = f'Emissão: {formatted["dtEmi"]} Dest/Reme: {infNFe["infNFe"]["dest"]["xNome"]} Valor Total: {infNFe["infNFe"]["total"]["ICMSTot"]["vNF"]}'
        
        # format all number values
        formatted = format_all_numbers(formatted)
        return formatted
        
    def get_icms(self, item: dict):
        icms = item['imposto']['ICMS'].copy()
        if 'ICMS' in icms:
            return icms['ICMS']
        elif 'ICMS00' in icms:
            return icms['ICMS00']
        elif 'ICMS10' in icms:
            return icms['ICMS10']
        elif 'ICMS20' in icms:
            return icms['ICMS20']
        elif 'ICMS30' in icms:
            return {
                'vBC': icms['ICMS30']['vBCST'],
                'pICMS': icms['ICMS30']['pICMSST'],
                'vICMS': icms['ICMS30']['vICMSST'],
                'CST': icms['ICMS30']['CST'],
            }
        elif 'ICMS40' in icms:
            return {
                'vBC': '0,00',
                'pICMS': '0,00',
                'vICMS': icms['ICMS40'].get('vICMSDeson') or '0,00',
                'CST': icms['ICMS40']['CST'],
            }
        elif 'ICMS51' in icms:
            return {'vICMS': '0,00', **icms['ICMS51']}
        elif 'ICMS60' in icms:
            return {
                'vBC': icms['ICMS60']['vBCEfet'],
                'pICMS': icms['ICMS60']['pICMSEfet'],
                'vICMS': icms['ICMS60']['vICMSEfet'],
                'CST': icms['ICMS60']['CST'],
            }
        elif 'ICMS70' in icms:
            return icms['ICMS70']
        elif 'ICMS90' in icms:
            return icms['ICMS90']
        elif 'ICMSPart' in icms:
            return icms['ICMSPart']
        elif 'ICMSST' in icms:
            return {
                'vBC': icms['ICMSST']['vBCSTDest'],
                'pICMS': icms['ICMSST']['pST'],
                'vICMS': icms['ICMSST']['vICMSSTDest'],
                'CST': icms['ICMSST']['CST'],
            }
        else:
            return {
                'vBC': '0,00',
                'pICMS': '0,00',
                'vICMS': '0,00',
                'CST': icms['CST'],
            }
    
    def get_ipi(self, item: dict):
        if 'IPI' in item['imposto']:
            ipi = item['imposto']['IPI'].copy()
            return list(ipi.values())[0]
        else:
            return {
                'pIPI': '0,00',
                'vIPI': '0,00'
            }