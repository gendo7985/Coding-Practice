# 등굣길


def solution(m, n, puddles):
    dp = [[None] * n for _ in range(m)]
    for pos in puddles:
        dp[pos[0] - 1][pos[1] - 1] = 0
    dp[0][0] = 1
    for i in range(1, m):
        if dp[i][0] != 0:
            dp[i][0] = dp[i - 1][0]
    for j in range(1, n):
        if dp[0][j] != 0:
            dp[0][j] = dp[0][j - 1]
    for i in range(1, m):
        for j in range(1, n):
            if dp[i][j] != 0:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
    return dp[-1][-1]