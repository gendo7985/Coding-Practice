# [1차] 다트 게임


def solution(dartResult):
    total = 0
    before = 0
    while dartResult:
        if dartResult[:2] == "10":
            score = 10
            dartResult = dartResult[2:]
        else:
            score = int(dartResult[0])
            dartResult = dartResult[1:]
        bonus = dartResult[0]
        dartResult = dartResult[1:]
        if bonus == "D":
            score **= 2
        elif bonus == "T":
            score **= 3
        if dartResult and dartResult[0] in "*#":
            option = dartResult[0]
            dartResult = dartResult[1:]
            if option == "*":
                total += before
                score *= 2
            else:
                score *= -1
        total += score
        before = score
    return total

