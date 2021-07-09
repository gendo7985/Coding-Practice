# 숫자의 표현


def solution(n):
    while n % 2 == 0:
        n //= 2
    d = 3
    answer = 1
    while n > 1:
        cnt = 1
        while n % d == 0:
            cnt += 1
            n //= d
        answer *= cnt
        d += 2
    return answer