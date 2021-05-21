# 행렬 테두리 회전하기


def solution(rows, columns, queries):
    result = []
    matrix = [[(i - 1) * columns + j for j in range(1, columns + 1)] for i in range(1, rows + 1)]
    for rotation in queries:
        x1, y1, x2, y2 = rotation[0] - 1, rotation[1] - 1, rotation[2] - 1, rotation[3] - 1
        initial = matrix[x1][y1]
        m = initial
        for i in range(x1 + 1, x2 + 1):
            matrix[i - 1][y1] = matrix[i][y1]
            if matrix[i][y1] < m:
                m = matrix[i][y1]
        for j in range(y1 + 1, y2 + 1):
            matrix[x2][j - 1] = matrix[x2][j]
            if matrix[x2][j] < m:
                m = matrix[x2][j]
        for i in range(x2 - 1, x1 - 1, -1):
            matrix[i + 1][y2] = matrix[i][y2]
            if matrix[i][y2] < m:
                m = matrix[i][y2]
        for j in range(y2 - 1, y1, -1):
            matrix[x1][j + 1] = matrix[x1][j]
            if matrix[x1][j] < m:
                m = matrix[x1][j]
        matrix[x1][y1 + 1] = initial
        result.append(m)
    return result