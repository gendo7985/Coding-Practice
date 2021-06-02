# 큰 수 만들기


def solution(number, k):
    stack = [number[0]]
    for n in number[1:]:
        while stack and k > 0:
            prev = int(stack.pop())
            if prev < int(n):
                k -= 1
            else:
                stack.append(str(prev))
                break
        stack.append(n)
    for i in range(k):
        stack.pop()
    return "".join(stack)