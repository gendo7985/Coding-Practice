# 최대공약수와 최소공배수


def solution(n, m):
    for i in range(min(n, m), 0, -1):
        if n % i == m % i == 0:
            return [i, n * m // i]

