# 최고의 집합

from math import ceil


def solution(n, s):
    if s < n:
        return [-1]
    a = ceil(s / n)
    b = a - 1
    n1 = s - b * n
    n2 = n - n1
    return [b] * n2 + [a] * n1
