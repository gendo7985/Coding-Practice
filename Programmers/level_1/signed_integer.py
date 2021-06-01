# 음양 더하기


def solution(absolutes, signs):
    return sum([i * (j - 0.5) * 2 for (i, j) in zip(absolutes, signs)])
