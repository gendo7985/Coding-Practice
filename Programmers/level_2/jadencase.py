# JadenCase 문자열 만들기


def solution(s):
    answer = ""
    tmp = " "
    for i in s:
        if tmp == " ":
            answer += i.upper()
        else:
            answer += i.lower()
        tmp = i
    return answer