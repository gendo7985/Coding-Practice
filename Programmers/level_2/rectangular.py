# 멀쩡한 사각형


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def solution(w, h):
    d = gcd(w, h)
    dw = w // d
    dh = h // d
    return w * h - d * (dw + dh - 1)