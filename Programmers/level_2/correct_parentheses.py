# 올바른 괄호


def solution(s):
    check = 0
    for i in s:
        if i == "(":
            check += 1
        elif i == ")":
            check -= 1
        if check < 0:
            return False
    return check == 0