# 이상한 문자 만들기


def solution(s):
    ans = ""
    i = 0
    for j in range(len(s)):
        if s[j] == " ":
            i = -1
        if i == -1:
            ans += s[j]
        elif i % 2 == 0:
            ans += s[j].upper()
        else:
            ans += s[j].lower()
        i += 1
    return ans
