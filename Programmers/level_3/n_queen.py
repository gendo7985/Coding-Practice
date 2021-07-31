# N-Queen


def possible(plate, n):
    ans = [True] * n
    q = len(plate)
    for i in range(len(plate)):
        ans[plate[i]] = False
        if 0 <= plate[i] - q + i < n:
            ans[plate[i] - q + i] = False
        if 0 <= plate[i] + q - i < n:
            ans[plate[i] + q - i] = False
    return [i for i in range(n) if ans[i]]


def solution(n):
    answer = 0
    stack = [[]]
    while stack:
        plate = stack.pop()
        if len(plate) == n - 1:
            answer += len(possible(plate, n))
        else:
            for i in possible(plate, n):
                stack.append(plate + [i])
    return answer