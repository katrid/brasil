import os
import sys
from brasil.utils.xsd2py import convert_dir, get_module

if len(sys.argv) == 1:
    raise TypeError('Must provide arg.')

def main():
    dir = sys.argv[1]
    root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    res = convert_dir(os.path.join(root, 'schemas', dir))
    base_dir = os.path.join(root, 'brasil', 'dfe', 'leiaute', dir)
    for filename, content in res.items():
        filename = get_module(filename)
        if not os.path.isfile(os.path.join(base_dir, filename + '.py')):
            with open(os.path.join(base_dir, filename + '.py'), 'w') as f:
                f.write(content)

if __name__ == '__main__':
    main()