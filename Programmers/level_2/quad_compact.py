# 쿼드압축 후 개수 세기


def solution(arr):
    ans = [0, 0]
    n = len(arr)
    if n == 2:
        for i in arr:
            for j in i:
                ans[j] += 1
        if ans[0] == 4:
            ans[0] = 1
        elif ans[1] == 4:
            ans[1] = 1
        return ans
    n = len(arr)
    for x, y in [(0, 0), (0, n // 2), (n // 2, 0), (n // 2, n // 2)]:
        sub = solution([arr[i][y : y + n // 2] for i in range(x, x + n // 2)])
        ans[0], ans[1] = ans[0] + sub[0], ans[1] + sub[1]
    if ans == [4, 0]:
        ans[0] = 1
    elif ans == [0, 4]:
        ans[1] = 1
    return ans
