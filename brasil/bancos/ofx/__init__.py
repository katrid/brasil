from io import IOBase

from .leiaute import *
from .parser import OfxParser


def load_ofx(data: bytes) -> OfxDocument:
    return OfxParser().parse(data)
