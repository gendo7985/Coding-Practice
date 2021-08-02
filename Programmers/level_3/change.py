# 거스름돈


def solution(n, money):
    m = len(money)
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        c = money[i]
        dp[i][c - 1] += 1
        for j in range(n):
            if i - 1 >= 0:
                dp[i][j] += dp[i - 1][j]
            if j - c >= 0:
                dp[i][j] += dp[i][j - c]
    return dp[-1][-1]