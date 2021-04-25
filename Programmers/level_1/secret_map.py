# [1차] 비밀지도


def solution(n, arr1, arr2):
    answer = [""] * n
    for i in range(n):
        code = arr1[i] | arr2[i]
        b = "0" * max(0, n + 2 - len(bin(code))) + bin(code)[2:]
        answer[i] = b.replace("1", "#").replace("0", " ")
    return answer
