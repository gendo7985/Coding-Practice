# N으로 표현


def solution(N, number):
    if all(map(lambda x: x == str(N), str(number))):
        return len(str(number))
    dp = [[N]]
    while len(dp) < 8:
        dp.append([])
        dp[-1].append(dp[-2][0] * 10 + N)
        for i in range(len(dp) - 1):
            for x in dp[i]:
                for y in dp[len(dp) - 2 - i]:
                    if x + y not in dp[-1]:
                        dp[-1].append(x + y)
                    if x - y not in dp[-1]:
                        dp[-1].append(x - y)
                    if x * y not in dp[-1]:
                        dp[-1].append(x * y)
                    if y != 0 and x // y not in dp[-1]:
                        dp[-1].append(x // y)
        if number in dp[-1]:
            return len(dp)
    return -1