# 프렌즈 4블록


def erase(m, n, nb):
    deleted = set()
    for i in range(1, m):
        for j in range(1, n):
            if nb[i][j] and nb[i - 1][j - 1] == nb[i - 1][j] == nb[i][j - 1] == nb[i][j]:
                deleted.update([(i, j), (i - 1, j), (i, j - 1), (i - 1, j - 1)])
    for (x, y) in deleted:
        nb[x][y] = False
    return len(deleted)


def gravity(m, n, nb):
    for i in range(m - 2, -1, -1):
        for j in range(n):
            if nb[i][j] and (not nb[i + 1][j]):
                k = 1
                while not nb[i + k][j]:
                    k += 1
                    if i + k > m - 1:
                        break
                nb[i][j], nb[i + k - 1][j] = nb[i + k - 1][j], nb[i][j]


def solution(m, n, board):
    nb = [[j for j in i] for i in board]
    ans = 0
    while True:
        erased = erase(m, n, nb)
        if erased == 0:
            return ans
        else:
            ans += erased
            gravity(m, n, nb)