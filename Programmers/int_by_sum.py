# 두 정수 사이의 합
def solution(a, b):
    return (a + b) * (max(a, b) - min(a, b) + 1) // 2

