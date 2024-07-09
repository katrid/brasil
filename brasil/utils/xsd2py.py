from brasil.utils.parser import Parser


def convert_dir(dirname: str):
    parser = Parser()
    parser.compile_dir(dirname)
    return parser
