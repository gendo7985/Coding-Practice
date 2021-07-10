# 2개 이하로 다른 비트


def solution(numbers):
    answer = []
    for x in numbers:
        if x % 2 == 0:
            answer.append(x + 1)
        else:
            answer.append(x + ((x ^ (x + 1)) + 1) // 4)
    return answer