# 점프와 순간이동


def solution(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return solution(n // 2)
    else:
        return solution(n // 2) + 1
