# 3진법 뒤집기


def solution(n):
    ternary = []
    while n > 0:
        ternary.append(n % 3)
        n //= 3
    return sum([ternary[-i - 1] * 3 ** i for i in range(len(ternary))])

