# 하노이의 탑


def solution(n, start=1, end=3):
    if n == 1:
        return [[start, end]]
    else:
        if start == 1:
            tmp = 5 - end
        elif start == 2:
            tmp = 4 - end
        else:
            tmp = 3 - end
        ans = solution(n - 1, start, tmp)
        ans.append([start, end])
        ans += solution(n - 1, tmp, end)
    return ans