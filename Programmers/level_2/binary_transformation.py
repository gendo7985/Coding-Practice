# 이진 변환 반복하기


def solution(s):
    cnt = 0
    zero = 0
    while s != "1":
        cnt += 1
        n = len(s)
        s = s.replace("0", "")
        zero += n - len(s)
        s = str(bin(len(s)))[2:]
    return [cnt, zero]