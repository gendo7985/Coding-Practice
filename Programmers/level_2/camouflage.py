# 위장


def solution(clothes):
    closet = {}
    for i in clothes:
        if i[1] in closet:
            closet[i[1]] += 1
        else:
            closet[i[1]] = 1
    answer = 1
    for i in closet.values():
        answer *= i + 1
    return answer - 1