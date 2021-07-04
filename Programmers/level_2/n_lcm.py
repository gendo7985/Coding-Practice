# N개의 최소공배수


def solution(arr):
    ans = 1
    div = 2
    n = len(arr)
    while sum(arr) > n:
        check = list(map(lambda x: x % div == 0, arr))
        if any(check):
            ans *= div
            for i in range(n):
                if check[i]:
                    arr[i] //= div
        else:
            if div == 2:
                div += 1
            else:
                div += 2
    return ans