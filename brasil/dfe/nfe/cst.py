from dataclasses import dataclass


@dataclass(slots=True)
class CSTCIBS:
    ind_gIBSCBS: int
    ind_gIBSCBSMono: int
    ind_gRed: int
    ind_gDif: int
    ind_gTransfCred: int
    ind_gCredPresIBSZFM: int
    ind_gAjusteCompet: int
    ind_RedutorBC: int


cst_cibs: dict[int, CSTCIBS] = {
    0: CSTCIBS(1, 0, 0, 0, 0, 0, 0, 0),
    10: CSTCIBS(1, 0, 0, 0, 0, 0, 0, 0),
    11: CSTCIBS(1, 0, 1, 0, 0, 0, 0, 0),
    200: CSTCIBS(1, 0, 1, 0, 0, 0, 0, 0),
    220: CSTCIBS(1, 0, 0, 0, 0, 0, 0, 0),
    222: CSTCIBS(1, 0, 0, 0, 0, 0, 0, 1),
    221: CSTCIBS(1, 0, 0, 0, 0, 0, 0, 0),
    400: CSTCIBS(0, 0, 0, 0, 0, 0, 0, 0),
    410: CSTCIBS(0, 0, 0, 0, 0, 0, 0, 0),
    510: CSTCIBS(1, 0, 0, 1, 0, 0, 0, 0),
    515: CSTCIBS(1, 0, 1, 1, 0, 0, 0, 0),
    550: CSTCIBS(1, 0, 0, 0, 0, 0, 0, 0),
    620: CSTCIBS(0, 1, 0, 0, 0, 0, 0, 0),
    800: CSTCIBS(0, 0, 0, 0, 1, 0, 0, 0),
    810: CSTCIBS(0, 0, 0, 0, 0, 1, 0, 0),
    811: CSTCIBS(0, 0, 0, 0, 0, 0, 1, 0),
    820: CSTCIBS(0, 0, 0, 0, 0, 0, 0, 0),
    830: CSTCIBS(1, 0, 0, 0, 0, 0, 0, 0),
}
