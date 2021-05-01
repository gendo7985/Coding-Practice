# 기능개발


from math import ceil


def solution(progresses, speeds):
    answer = []
    times = [ceil((100 - i) / j) for (i, j) in zip(progresses, speeds)]
    m = times[0]
    ind = 0
    for i in range(len(times)):
        if times[i] > m:
            answer.append(i - ind)
            ind = i
            m = times[i]
    return answer + [len(progresses) - sum(answer)]