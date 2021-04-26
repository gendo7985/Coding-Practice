# 124 나라의 숫자


def solution(n):
    ans = ""
    while n > 0:
        n -= 1
        d = n % 3
        if d == 0:
            ans = "1" + ans
        elif d == 1:
            ans = "2" + ans
        else:
            ans = "4" + ans
        n //= 3
    return ans