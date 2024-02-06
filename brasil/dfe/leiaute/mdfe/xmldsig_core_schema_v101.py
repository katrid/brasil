from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime


class SignatureValueType(Element):
    pass



class TTransformURI(anyURI):
    _restriction = Restriction(base=r"anyURI", enumeration=['http://www.w3.org/2000/09/xmldsig#enveloped-signature', 'http://www.w3.org/TR/2001/REC-xml-c14n-20010315'])
    pass



class TransformType(Element):
    XPath: string = Element(string)
    Algorithm: str = Attribute(TTransformURI)



class TransformsType(Element):
    Transform: List[TransformType] = Element(TransformType, min_occurs=2, max_occurs=2)



class DigestValueType(base64Binary):
    _restriction = Restriction(base=r"base64Binary", enumeration=[])
    pass



class ReferenceType(Element):
    Transforms: TransformsType = Element(TransformsType)

    class DigestMethod(ComplexType):
        Algorithm: str = Attribute(anyURI)
    DigestMethod: DigestMethod = Element(DigestMethod)
    DigestValue: DigestValueType = Element(DigestValueType)
    Id: str = Attribute(ID)
    URI: str = Attribute(None)
    Type: str = Attribute(anyURI)



class SignedInfoType(Element):

    class CanonicalizationMethod(ComplexType):
        Algorithm: str = Attribute(anyURI)
    CanonicalizationMethod: CanonicalizationMethod = Element(CanonicalizationMethod)

    class SignatureMethod(ComplexType):
        Algorithm: str = Attribute(anyURI)
    SignatureMethod: SignatureMethod = Element(SignatureMethod)
    Reference: ReferenceType = Element(ReferenceType)
    Id: str = Attribute(ID)



class X509DataType(Element):
    X509Certificate: base64Binary = Element(base64Binary)



class KeyInfoType(Element):
    X509Data: X509DataType = Element(X509DataType)
    Id: str = Attribute(ID)



class SignatureType(Element):
    SignedInfo: SignedInfoType = Element(SignedInfoType)
    SignatureValue: SignatureValueType = Element(SignatureValueType)
    KeyInfo: KeyInfoType = Element(KeyInfoType)
    Id: str = Attribute(ID)


class Signature(SignatureType):
    pass

