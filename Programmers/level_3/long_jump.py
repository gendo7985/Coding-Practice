# 멀리뛰기


def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    a, b = 1, 2
    for i in range(n - 2):
        a, b = b, (a + b) % 1234567
    return b