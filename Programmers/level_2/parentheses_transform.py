# 괄호 변환


def right(p):
    cnt = 0
    for i in p:
        if i == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True


def reverse(p):
    ans = ""
    for i in p:
        if i == "(":
            ans += ")"
        else:
            ans += "("
    return ans


def solution(p):
    if p == "":
        return p
    cnt = 0
    for i in range(len(p)):
        if p[i] == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            u, v = p[: i + 1], p[i + 1 :]
            break
    if right(u):
        return u + solution(v)
    else:
        ans = "(" + solution(v) + ")"
        return ans + reverse(u[1 : len(u) - 1])
