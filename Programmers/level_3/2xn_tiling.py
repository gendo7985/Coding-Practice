# 2 x n 타일링


def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    dp = [None] * n
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    return dp[-1]