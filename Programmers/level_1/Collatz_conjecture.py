# 콜라츠 추측


def solution(num):
    n = 0
    while n < 500:
        if num == 1:
            return n
        else:
            n += 1
            if num % 2 == 0:
                num //= 2
            else:
                num = 3 * num + 1
    return -1
