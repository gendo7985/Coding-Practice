# 가장 큰 수


def solution(numbers):
    if all(map(lambda x: x == 0, numbers)):
        return "0"
    a = sorted(list(map(str, numbers)), reverse=True, key=lambda x: (x * 4)[:4])
    return "".join(a)