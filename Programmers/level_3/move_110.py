# 110 옮기기


def solution(s):
    for i in range(len(s)):
        stack = ""
        num = 0
        for j in s[i]:
            stack += j
            if len(stack) > 2 and stack[-3:] == "110":
                num += 1
                stack = stack[:-3]
        if "0" in stack:
            ind = len(stack) - stack[::-1].find("0")
        else:
            ind = 0
        front = stack[:ind]
        end = stack[ind:]
        s[i] = front + "110" * num + end
    return s