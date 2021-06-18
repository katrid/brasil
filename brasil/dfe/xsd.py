

def SimpleType(type):
    pass


def ComplexType(type):
    pass


class Element:
    _restriction = None

    def __init__(self, *args, **kwargs):
        pass


class Attribute:
    def __init__(self, type):
        self.type = type


class TString(str):
    pass


class Restriction:
    def __init__(self, **kwargs):
        pass


class SimpleTypeElement(Element):
    pass


class ID(SimpleTypeElement):
    pass


class base64Binary(SimpleTypeElement):
    pass


class anyURI(SimpleTypeElement):
    pass


class string(SimpleTypeElement):
    pass


class dateTime(SimpleTypeElement):
    pass
