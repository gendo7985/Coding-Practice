# 소수 찾기
def solution(n):
    ans = [True] * (n+1)
    ans[0] = ans[1] = False
    for i in range(2,n+1):
        if ans[i]:
            for j in range(i*2, n+1, i):
                ans[j] = False
    return sum(ans)