# 예산


def solution(d, budget):
    s_d = sorted(d)
    cumd = [s_d[0]] * len(d)
    for i in range(1, len(d)):
        cumd[i] = cumd[i - 1] + s_d[i]
    for i in range(len(cumd)):
        if cumd[i] > budget:
            return i
    return len(d)
