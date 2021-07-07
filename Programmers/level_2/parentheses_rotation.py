# 괄호 회전하기


def parentheses(s):
    while s.find("()") + s.find("[]") + s.find("{}") > -3:
        s = s.replace("()", "")
        s = s.replace("[]", "")
        s = s.replace("{}", "")
    return len(s) == 0


def solution(s):
    if len(s) % 2 == 1:
        return 0
    answer = 0
    for i in range(len(s)):
        answer += parentheses(s)
        s = s[1:] + s[0]
    return answer