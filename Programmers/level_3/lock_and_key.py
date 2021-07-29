# 자물쇠와 열쇠


def check(key, x, y, lock):
    M = len(key)
    N = len(lock)
    for i in range(N):
        for j in range(N):
            if 0 <= i - x < M and 0 <= j - y < M:
                if not key[i - x][j - y] ^ lock[i][j]:
                    return False
            else:
                if not lock[i][j]:
                    return False
    return True


def rotate(key, k):
    if k == 0:
        return key
    M = len(key)
    newkey = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            if key[i][j]:
                newkey[j][M - i - 1] = 1
    return newkey


def solution(key, lock):
    M = len(key)
    N = len(lock)
    for i in range(4):
        key = rotate(key, i)
        for x in range(-M + 1, N):
            for y in range(-M + 1, N):
                if check(key, x, y, lock):
                    return True
    return False