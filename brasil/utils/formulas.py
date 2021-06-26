from itertools import cycle


def modulo11(s: str, peso=9) -> int:
    mult = cycle(range(2, peso + 1))
    res = (sum(int(s[i - 2]) * next(mult) for i in range(len(s) + 1, 1, -1)) % 11)
    if res < 2:
        return 0
    return 11 - res
