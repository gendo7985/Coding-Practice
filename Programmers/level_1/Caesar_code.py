# 시저 암호


def solution(s, n):
    Al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    al = Al.lower()
    ans = ""
    for i in s:
        if i in Al:
            ans += Al[(Al.find(i) + n) % 26]
        elif i in al:
            ans += al[(al.find(i) + n) % 26]
        else:
            ans += i
    return ans
