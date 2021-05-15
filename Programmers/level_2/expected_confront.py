# 예상 대진표


def solution(n, a, b):
    if a > b:
        a, b = b, a
    answer = 1
    while not (a % 2 == 1 and b - a == 1):
        answer += 1
        a = (a + 1) // 2
        b = (b + 1) // 2

    return answer