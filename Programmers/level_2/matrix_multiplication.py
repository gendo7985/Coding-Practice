# 행렬의 곱셈


def solution(arr1, arr2):
    arr3 = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            arr3[i][j] = sum([arr1[i][k] * arr2[k][j] for k in range(len(arr1[0]))])
    return arr3