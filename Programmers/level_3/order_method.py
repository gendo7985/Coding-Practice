# 줄 서는 방법


def solution(n, k):
    answer = []
    num = list(range(1, n + 1))
    fact = [1] * n
    for i in range(1, n):
        fact[i] = fact[i - 1] * i
    for i in range(n - 1, -1, -1):
        answer.append(num.pop((k - 1) // fact[i]))
        k = ((k - 1) % fact[i]) + 1
    return answer