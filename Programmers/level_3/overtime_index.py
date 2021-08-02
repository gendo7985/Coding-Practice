# 야근 지수


def solution(n, works):
    if sum(works) <= n:
        return 0
    works.sort(reverse = True)
    k = len(works)
    while n > 0:
        m = works[0]
        cnt = works.count(m)
        if cnt <= n:
            n -= cnt
            for i in range(cnt):
                works[i] -= 1
        else:
            for i in range(n):
                works[i] -= 1
            break
    return sum([i**2 for i in works])