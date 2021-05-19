# 조이스틱


def solution(name):
    A = [1, 0]
    start = -1
    end = -1
    for i in range(len(name)):
        if name[i] == "A":
            if start == -1:
                start = i
        else:
            end = i - 1
            if start != -1:
                if A[1] < end - start + 1:
                    A = [start, end - start + 1]
                start = -1
    cursor = (
        min(len(name) + 1, A[0] + len(name) - A[1], len(name) - A[0] - A[1] + len(name) - A[1]) - 2
    )
    print(cursor)
    for i in name:
        if i != "A":
            move = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(i)
            if move > 13:
                move = 26 - move
            cursor += move
    return cursor