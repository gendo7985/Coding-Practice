# 순위 검색

from itertools import product


def binsearch(data, score):
    a, b = 0, len(data) - 1
    mid = (a + b) // 2
    while True:
        if data[mid] >= score and data[mid + 1] < score:
            return mid + 1
        elif data[mid] < score:
            b = mid
            mid = (a + b) // 2
        else:
            a = mid
            mid = (a + b) // 2


def solution(info, query):
    answer = []
    n = len(info)
    df = {}
    products = product(
        ["cpp", "java", "python", "-"],
        ["backend", "frontend", "-"],
        ["junior", "senior", "-"],
        ["chicken", "pizza", "-"],
    )
    for i in products:
        df[i] = []
    for i in range(n):
        (lang, work, year, food, score) = info[i].split()
        score = int(score)
        for key in df:
            if (
                (key[0] == "-" or key[0] == lang)
                and (key[1] == "-" or key[1] == work)
                and (key[2] == "-" or key[2] == year)
                and (key[3] == "-" or key[3] == food)
            ):
                df[key].append(score)
    for key in df:
        df[key].sort(reverse=True)
    for q in query:
        a = q.split()
        data = a[0], a[2], a[4], a[6]
        score = int(a[-1])
        if len(df[data]) == 0:
            answer.append(0)
        elif score <= df[data][-1]:
            answer.append(len(df[data]))
        elif score > df[data][0]:
            answer.append(0)
        else:
            answer.append(binsearch(df[data], score))
    return answer