# 소수 만들기


def solution(nums):
    ans = 0
    arr = sorted(nums)
    isPrime = [True] * (arr[-1] + arr[-2] + arr[-3] + 1)
    isPrime[0] = isPrime[1] = False
    for i in range(2, len(isPrime)):
        if isPrime[i]:
            for j in range(i + i, len(isPrime), i):
                isPrime[j] = False
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                if isPrime[arr[i] + arr[j] + arr[k]]:
                    ans += 1
    return ans
