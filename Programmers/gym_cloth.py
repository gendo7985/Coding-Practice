# 체육복
def solution(n, lost, reserve):
    for i in range(len(lost)):
        if lost[i] in reserve:
            reserve[reserve.index(lost[i])] = -1
            lost[i] = -1
    print(lost, reserve)
    for std in lost:
        if std - 1 in reserve:
            reserve[reserve.index(std - 1)] = -1
        elif std + 1 in reserve:
            reserve[reserve.index(std + 1)] = -1
        elif std != -1:
            n -= 1
    return n
