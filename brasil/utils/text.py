import unicodedata


def only_number(s):
    return ''.join([c for c in s if c.isdigit()])


def remover_acentos(s):
    return unicodedata.normalize('NFD', s).encode('ascii', 'ignore')
