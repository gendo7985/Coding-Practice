# 모의고사


def solution(answers):
    answer = []
    student1 = [1, 2, 3, 4, 5] * (len(answers) // 5 + 1)
    student2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers) // 8 + 1)
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers) // 10 + 1)

    result = [
        sum([answers[i] == student1[i] for i in range(len(answers))]),
        sum([answers[i] == student2[i] for i in range(len(answers))]),
        sum([answers[i] == student3[i] for i in range(len(answers))]),
    ]
    M = max(result)
    answer.append(result.index(M) + 1)
    result[result.index(M)] = -1
    if max(result) == M:
        answer.append(result.index(M) + 1)
        result[result.index(M)] = -1
    if max(result) == M:
        answer.append(result.index(M) + 1)
        result[result.index(M)] = -1
    return sorted(answer)
