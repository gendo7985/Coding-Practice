# 카펫


def solution(brown, yellow):
    b = brown + yellow
    a = -(brown + 4) // 2
    root = int((a ** 2 - 4 * b) ** 0.5)
    return [(-a + root) // 2, (-a - root) // 2]
