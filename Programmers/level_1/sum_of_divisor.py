# 약수의 합


def solution(n):
    if n == 0:
        return 0
    i = 2
    ans = 1
    while n > 1:
        tmp = 1
        while n % i == 0:
            tmp = i * tmp + 1
            n //= i
        ans *= tmp
        i += 1
    return ans
