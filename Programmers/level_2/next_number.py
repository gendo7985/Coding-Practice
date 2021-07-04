# 다음 큰 숫자


def solution(n):
    b = str(bin(n))[2:]
    b = b[::-1]
    if not "0" in b:
        b = b[1:] + "01"
    elif len(b) - b[::-1].find("0") <= b.find("1"):
        ones = b.count("1")
        b = "1" * (ones - 1) + "0" * (len(b) - ones) + "01"
    else:
        ind = b.find("10")
        b = b.replace("10", "01", 1)
        ones = b[:ind].count("1")
        b = "1" * ones + "0" * (ind - ones) + b[ind:]
    return sum([int(b[i]) * 2 ** i for i in range(len(b))])
