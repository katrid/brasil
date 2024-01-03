"""Constantes úteis para rotinas de CTe v400
"""

VALOR_MAX_SERVICO = 9999999.99 # Valor maximo permitido para o total de serviços no Cte
TOLERANCIA_ICMS = 0.01 # Margem de erro permitida entre o valor do icms e o produto bc * aliquota
# Lista de CFOPs validos para autorização de CTe de acordo com o MOC 4.00
CFOPS_VALIDOS_CTE = (
    '5351',
    '5352',
    '5353',
    '5354',
    '5355',
    '5356',
    '5357',
    '5359',
    '5360',
    '5601',
    '5602',
    '5603',
    '5605',
    '5606',
    '5932',
    '5949',
    '6351',
    '6352',
    '6353',
    '6354',
    '6355',
    '6356',
    '6357',
    '6359',
    '6360',
    '6603',
    '6932',
    '6949',
    '7358',
    '7949'
)