# 정수 삼각형


def solution(triangle):
    if len(triangle) == 1:
        return triangle[0][0]
    for i in range(1, len(triangle)):
        triangle[i][0] += triangle[i - 1][0]
        triangle[i][-1] += triangle[i - 1][-1]
    for i in range(2, len(triangle)):
        for j in range(1, i):
            triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1])
    return max(triangle[-1])