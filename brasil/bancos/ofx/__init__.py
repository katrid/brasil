from io import IOBase

from .leiaute import *
from .parser import OfxParser


def load_ofx(file: IOBase) -> OfxDocument:
    return OfxParser().parse(file)
