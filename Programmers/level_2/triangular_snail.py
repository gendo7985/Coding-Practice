# 삼각 달팽이


def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]
    num = 1
    for i in range(n):
        if i % 3 == 0:
            for j in range(2 * i // 3, n - i // 3):
                answer[j][i // 3] = num
                num += 1
        elif i % 3 == 1:
            for j in range(i // 3 + 1, n - 2 * i // 3):
                answer[n - i // 3 - 1][j] = num
                num += 1
        else:
            for j in range(n - i // 3 - 2, 2 * (i // 3), -1):
                answer[j][j - i // 3] = num
                num += 1
    res = []
    for i in answer:
        res += i
    return res