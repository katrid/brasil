from __future__ import annotations
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime


class TCodUfIBGE(str):
    """Tipo Código da UF da tabela do IBGE"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53'])
    pass



class TCodMunIBGE(str):
    """Tipo Código do Município da tabela do IBGE"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{7}", enumeration=[])
    pass



class TChNFe(str):
    """Tipo Chave da Nota Fiscal Eletrônica"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{44}", enumeration=[])
    pass



class TProt(str):
    """Tipo Número do Protocolo de Status"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{15}", enumeration=[])
    pass



class TRec(str):
    """Tipo Número do Recibo do envio de lote de NF-e"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{15}", enumeration=[])
    pass



class TStat(str):
    """Tipo Código da Mensagem enviada"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{3}", enumeration=[])
    pass



class TCnpj(str):
    """Tipo Número do CNPJ"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{14}", enumeration=[])
    pass



class TCnpjVar(str):
    """Tipo Número do CNPJ tmanho varíavel (3-14)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{3,14}", enumeration=[])
    pass



class TCnpjOpc(str):
    """Tipo Número do CNPJ Opcional"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{0}|[0-9]{14}", max_length=r"14", enumeration=[])
    pass



class TCpf(str):
    """Tipo Número do CPF"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{11}", enumeration=[])
    pass



class TCpfVar(str):
    """Tipo Número do CPF de tamanho variável (3-11)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{3,11}", enumeration=[])
    pass



class TDec_0302(str):
    """Tipo Decimal com 5 dígitos, sendo 3 de corpo e 2 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?", enumeration=[])
    pass



class TDec_0302Opc(str):
    """Tipo Decimal com 5 dígitos, sendo 3 de corpo e 2 decimais, utilizado em tags opcionais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?", enumeration=[])
    pass



class TDec_0803(str):
    """Tipo Decimal com 11 dígitos, sendo 8 de corpo e 3 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,7}(\.[0-9]{3})?", enumeration=[])
    pass



class TDec_0803Opc(str):
    """Tipo Decimal com 11 dígitos, sendo 8 de corpo e 3 decimais utilizado em tags opcionais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0\.[1-9]{1}[0-9]{2}|0\.[0-9]{2}[1-9]{1}|0\.[0-9]{1}[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,7}(\.[0-9]{3})?", enumeration=[])
    pass



class TDec_0804(str):
    """Tipo Decimal com 12 dígitos, sendo 8 de corpo e 4decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,7}(\.[0-9]{4})?", enumeration=[])
    pass



class TDec_0804Opc(str):
    """Tipo Decimal com 12 dígitos, sendo 8 de corpo e 4 decimais, utilizado em tags opcionais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0\.[1-9]{1}[0-9]{3}|0\.[0-9]{3}[1-9]{1}|0\.[0-9]{2}[1-9]{1}[0-9]{1}|0\.[0-9]{1}[1-9]{1}[0-9]{2}|[1-9]{1}[0-9]{0,7}(\.[0-9]{4})?", enumeration=[])
    pass



class TDec_1104(str):
    """Tipo Decimal com 15 dígitos, sendo 11 de corpo e 4 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?", enumeration=[])
    pass



class TDec_1104Opc(str):
    """Tipo Decimal com 15 dígitos, sendo 11 de corpo e 4 decimais, utilizado em tags opcionais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0\.[1-9]{1}[0-9]{3}|0\.[0-9]{3}[1-9]{1}|0\.[0-9]{2}[1-9]{1}[0-9]{1}|0\.[0-9]{1}[1-9]{1}[0-9]{2}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?", enumeration=[])
    pass



class TDec_1203(str):
    """Tipo Decimal com 15 dígitos, sendo 12 de corpo e 3 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,11}(\.[0-9]{3})?", enumeration=[])
    pass



class TDec_1203Opc(str):
    """Tipo Decimal com 15 dígitos, sendo 12 de corpo e 3 decimais, utilizado em tags opcionais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0\.[1-9]{1}[0-9]{2}|0\.[0-9]{2}[1-9]{1}|0\.[0-9]{1}[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,11}(\.[0-9]{3})?", enumeration=[])
    pass



class TDec_1204(str):
    """Tipo Decimal com 16 dígitos, sendo 12 de corpo e 4 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,11}|[1-9]{1}[0-9]{0,11}(\.[0-9]{1,4})?", enumeration=[])
    pass



class TDec_1204Opc(str):
    """Tipo Decimal com 16 dígitos, sendo 12 de corpo e 4 decimais, utilizado em tags opcionais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0\.[1-9]{1}[0-9]{3}|0\.[0-9]{3}[1-9]{1}|0\.[0-9]{2}[1-9]{1}[0-9]{1}|0\.[0-9]{1}[1-9]{1}[0-9]{2}|[1-9]{1}[0-9]{0,11}(\.[0-9]{4})?", enumeration=[])
    pass



class TDec_1302(str):
    """Tipo Decimal com 15 dígitos, sendo 13 de corpo e 2 decimais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?", enumeration=[])
    pass



class TDec_1302Opc(str):
    """Tipo Decimal com 15 dígitos, sendo 13 de corpo e 2 decimais, utilizado em tags opcionais"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?", enumeration=[])
    pass



class TDec_1110(str):
    """Tipo Decimal com até  21 dígitos, sendo 11 de corpo e até 10 decimais // aperfeiçoamento v2.0"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{1,10}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,10})?", enumeration=[])
    pass



class TDec_1104v(str):
    """Tipo Decimal com até 15 dígitos, sendo 11 de corpo e até 4 decimais  // aperfeiçoamento v2.0"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,4})?", enumeration=[])
    pass



class TIeDest(str):
    """Tipo Inscrição Estadual do Destinatário // alterado para aceitar vazio ou ISENTO - maio/2010 v2.0"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"ISENTO|[0-9]{0,14}", enumeration=[])
    pass



class TIeST(str):
    """Tipo Inscrição Estadual do ST // acrescentado EM 24/10/08"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{2,14}", enumeration=[])
    pass



class TIe(str):
    """Tipo Inscrição Estadual do Emitente // alterado EM 24/10/08 para aceitar ISENTO"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{2,14}|ISENTO", enumeration=[])
    pass



class TMod(str):
    """Tipo Modelo Documento Fiscal"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['55'])
    pass



class TNF(str):
    """Tipo Número do Documento Fiscal"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[1-9]{1}[0-9]{0,8}", enumeration=[])
    pass



class TSerie(str):
    """Tipo Série do Documento Fiscal"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"0|[1-9]{1}[0-9]{0,2}", enumeration=[])
    pass



class Tpais(str):
    """Tipo Código do Pais 
// PL_005d - 11/08/09
eliminado:
 4235-LEBUAN, ILHAS - 
acrescentado:
7200 SAO TOME E PRINCIPE, ILHAS,
8958 ZONA DO CANAL DO PANAMA               
9903 PROVISAO DE NAVIOS E AERONAVES        
9946 A DESIGNAR                            
9950 BANCOS CENTRAIS                       
9970 ORGANIZACOES INTERNACIONAIS
 // PL_005b - 24/10/08
 // Acrescentado:
 4235 - LEBUAN,ILHAS
 4885 - MAYOTTE (ILHAS FRANCESAS)  
// NT2011/004
 acrescentado a tabela de paises
//PL_006t - 21/03/2014
acrescentado:
5780 - Palestina
7600 - Sudão do Sul"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['132', '175', '230', '310', '370', '400', '418', '434', '477', '531', '590', '639', '647', '655', '698', '728', '736', '779', '809', '817', '833', '850', '876', '884', '906', '930', '973', '981', '0132', '0175', '0230', '0310', '0370', '0400', '0418', '0434', '0477', '0531', '0590', '0639', '0647', '0655', '0698', '0728', '0736', '0779', '0809', '0817', '0833', '0850', '0876', '0884', '0906', '0930', '0973', '0981', '1015', '1058', '1082', '1112', '1155', '1198', '1279', '1376', '1414', '1457', '1490', '1504', '1508', '1511', '1538', '1546', '1589', '1600', '1619', '1635', '1651', '1694', '1732', '1775', '1830', '1872', '1902', '1937', '1953', '1961', '1988', '1996', '2291', '2321', '2356', '2399', '2402', '2437', '2445', '2453', '2461', '2470', '2496', '2518', '2534', '2550', '2593', '2674', '2712', '2755', '2810', '2852', '2895', '2917', '2933', '2976', '3018', '3050', '3093', '3131', '3174', '3255', '3298', '3310', '3344', '3379', '3417', '3450', '3514', '3557', '3573', '3595', '3611', '3654', '3697', '3727', '3751', '3794', '3832', '3867', '3913', '3964', '3999', '4030', '4111', '4200', '4235', '4260', '4278', '4316', '4340', '4383', '4405', '4421', '4456', '4472', '4499', '4502', '4525', '4553', '4588', '4618', '4642', '4677', '4723', '4740', '4766', '4774', '4855', '4880', '4885', '4901', '4936', '4944', '4952', '4979', '4985', '4995', '5010', '5053', '5070', '5088', '5118', '5177', '5215', '5258', '5282', '5312', '5355', '5380', '5428', '5452', '5487', '5517', '5568', '5665', '5738', '5754', '5762', '5780', '5800', '5860', '5894', '5932', '5991', '6033', '6076', '6114', '6238', '6254', '6289', '6408', '6475', '6602', '6653', '6700', '6750', '6769', '6777', '6781', '6858', '6874', '6904', '6912', '6955', '6971', '7005', '7056', '7102', '7153', '7200', '7285', '7315', '7358', '7370', '7412', '7447', '7480', '7501', '7544', '7560', '7595', '7600', '7641', '7676', '7706', '7722', '7765', '7803', '7820', '7838', '7889', '7919', '7951', '8001', '8052', '8109', '8150', '8206', '8230', '8249', '8273', '8281', '8311', '8338', '8451', '8478', '8486', '8508', '8583', '8630', '8664', '8702', '8737', '8885', '8907', '8958', '9903', '9946', '9950', '9970'])
    pass



class TUf(str):
    """Tipo Sigla da UF"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO', 'EX'])
    pass



class TUfEmi(str):
    """Tipo Sigla da UF de emissor // acrescentado em 24/10/08"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO'])
    pass



class TAmb(str):
    """Tipo Ambiente"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", enumeration=['1', '2'])
    pass



class TVerAplic(TString):
    """Tipo Versão do Aplicativo"""
    _restriction = Restriction(base=r"nfe:TString", min_length=r"1", max_length=r"20", enumeration=[])
    pass



class TMotivo(TString):
    """Tipo Motivo"""
    _restriction = Restriction(base=r"nfe:TString", min_length=r"1", max_length=r"255", enumeration=[])
    pass



class TJust(TString):
    """Tipo Justificativa"""
    _restriction = Restriction(base=r"nfe:TString", min_length=r"15", max_length=r"255", enumeration=[])
    pass



class TServ(TString):
    """Tipo Serviço solicitado"""
    _restriction = Restriction(base=r"nfe:TString", enumeration=[])
    pass



class Tano(str):
    """Tipo ano"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{2}", enumeration=[])
    pass



class TMed(str):
    """Tipo temp médio em segundos"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[0-9]{1,4}", enumeration=[])
    pass



class TString(str):
    """Tipo string genérico"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"[!-ÿ]{1}[ -ÿ]*[!-ÿ]{1}|[!-ÿ]{1}", enumeration=[])
    pass



class TData(str):
    """Tipo data AAAA-MM-DD"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))", enumeration=[])
    pass



class TTime(str):
    """Tipo hora HH:MM:SS // tipo acrescentado na v2.0"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])", enumeration=[])
    pass



class TDateTimeUTC(str):
    """Data e Hora, formato UTC (AAAA-MM-DDThh:mm:ssTZD, onde TZD = +hh:mm ou -hh:mm)"""
    _restriction = Restriction(base=r"xs:string", white_space=r"preserve", pattern=r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))", enumeration=[])
    pass


