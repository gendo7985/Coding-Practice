# 풍선 터트리기


def solution(a):
    n = len(a)
    answer = [False] * n
    answer[0] = answer[-1] = True
    left, right = a[0], a[-1]
    for i in range(1, n - 1):
        if a[i] <= left:
            answer[i] = True
            left = a[i]
    for i in range(n - 2, 0, -1):
        if a[i] <= right:
            answer[i] = True
            right = a[i]
    return sum(answer)