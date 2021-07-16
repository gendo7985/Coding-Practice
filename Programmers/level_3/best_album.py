# 베스트 앨범


def solution(genres, plays):
    dic = {}
    for i in range(len(genres)):
        g, p = genres[i], plays[i]
        if g in dic:
            dic[g][0] += p
            dic[g].append(i)
        else:
            dic[g] = [p, i]
    key = list(dic.keys())
    key.sort(key=lambda x: -dic[x][0])
    answer = []
    for i in key:
        if len(dic[i]) == 1:
            answer.append(dic[i][1])
        else:
            dic[i].pop(0)
            dic[i].sort(key=lambda x: -plays[x])
            answer.extend(dic[i][:2])
    return answer