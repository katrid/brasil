import datetime
from typing import TypedDict

__all__ = [
    "OfxHeader",
    "OfxBody",
    "StmtTrn",
    "BankTranList",
    "StmtRs",
    "StmtTrnRs",
    "BankMsgSrsv1",
    "OfxDocument",
]


class OfxHeader(TypedDict):
    OFXHEADER: str
    DATA: str
    VERSION: str
    SECURITY: str
    ENCODING: str
    CHARSET: str
    COMPRESSION: str
    OLDFILEUID: str
    NEWFILEUID: str


class StmtTrn(TypedDict):
    TRNTYPE: str
    DTPOSTED: str
    TRNAMT: str
    FITID: str
    NAME: str
    MEMO: str
    REFNUM: str


class BankTranList(TypedDict):
    DTSTART: str
    DTEND: str
    STMTTRN: list[StmtTrn]


class BankAcctFrom(TypedDict):
    BANKID: str
    ACCTID: str
    ACCTTYPE: str
    BRANCHID: str


class StmtRs(TypedDict):
    CURDEF: str
    BANKACCTFROM: BankAcctFrom
    BANKTRANLIST: BankTranList
    LEDGERBAL: dict
    AVAILBAL: dict


class StmtTrnRs(TypedDict):
    TRNUID: str
    STATUS: dict
    STMTRS: StmtRs


class BankMsgSrsv1(TypedDict):
    STMTTRNRS: StmtTrnRs


class OfxBody(TypedDict):
    SIGNONMSGSRSV1: dict
    BANKMSGSRSV1: BankMsgSrsv1


class OfxDocument:
    header: OfxHeader
    body: OfxBody
