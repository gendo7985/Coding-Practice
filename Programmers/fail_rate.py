# 실패율


def solution(N, stages):
    s = sorted(stages)
    fail = [0] * N
    reach = [0] * N
    for player in s:
        if player <= N:
            fail[player - 1] += 1
            for i in range(player):
                reach[i] += 1
        else:
            for i in range(N):
                reach[i] += 1
    rate = [0] * N
    for i in range(N):
        if reach[i] > 0:
            rate[i] = fail[i] / reach[i]
    ans = [0] * N
    for i in range(N):
        ans[i] = rate.index(max(rate)) + 1
        rate[ans[i] - 1] = -1
    return ans

