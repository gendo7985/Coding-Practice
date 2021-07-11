# 스킬트리


def solution(skill, skill_trees):
    answer = []
    for i in skill_trees:
        answer.append([])
        for j in skill:
            answer[-1].append(i.find(j))
    cnt = 0
    for i in answer:
        for j in range(len(i) - 1):
            if i[j] != -1 and i[j] > i[j + 1] and i[j + 1] != -1:
                break
            elif i[j] == -1 and i[j + 1] != -1:
                break
        else:
            cnt += 1
    return cnt