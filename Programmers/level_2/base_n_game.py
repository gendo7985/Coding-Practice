# N진수 게임


def StrtoNum(num):
    if num.isdigit():
        return int(num)
    else:
        return ord(num) - 55


def NumtoStr(num):
    if num < 10:
        return str(num)
    else:
        return chr(num + 55)


def nextnum(n, num):
    if len(num) == 1:
        if StrtoNum(num) == n - 1:
            return "10"
        else:
            return NumtoStr(StrtoNum(num) + 1)
    elif StrtoNum(num[-1]) == n - 1:
        return nextnum(n, num[:-1]) + "0"
    else:
        return num[:-1] + nextnum(n, num[-1])


def generator(n):
    num = "0"
    while True:
        for i in num:
            yield i
        num = nextnum(n, num)


def solution(n, t, m, p):
    ans = ""
    cur = 1
    cnt = 0
    for i in generator(n):
        if cur == p:
            ans += i
            cnt += 1
        if cnt == t:
            return ans
        cur += 1
        if cur > m:
            cur = 1
