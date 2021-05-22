# 소수 찾기

from itertools import permutations


def isprime(number):
    if number < 2:
        return False
    for d in range(2, int(number ** 0.5) + 1):
        if number % d == 0:
            return False
    return True


def solution(numbers):
    pieces = list(numbers)
    candidate = set()
    for i in range(1, len(numbers) + 1):
        possible = map(int, map(lambda x: "".join(x), permutations(pieces, i)))
        candidate.update(list(possible))
    return len(list(filter(isprime, list(candidate))))