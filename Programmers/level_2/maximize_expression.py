# [카카오 인턴] 수식 최대화


def calc(expression, order):
    ind = [-1]
    for i in range(len(expression)):
        if not expression[i].isdigit():
            ind.append(i)
    number = []
    operator = []
    for i in range(len(ind) - 1):
        number.append(int(expression[ind[i] + 1 : ind[i + 1]]))
        operator.append(expression[ind[i + 1]])
    number.append(int(expression[ind[-1] + 1 :]))
    for first in order:
        while first in operator:
            ind = operator.index(first)
            operator.pop(ind)
            if first == "*":
                number[ind] *= number[ind + 1]
                number.pop(ind + 1)
            elif first == "+":
                number[ind] += number[ind + 1]
                number.pop(ind + 1)
            else:
                number[ind] -= number[ind + 1]
                number.pop(ind + 1)
    return abs(number[0])


def solution(expression):
    expr = [0] * 6
    expr[0] = calc(expression, ["*", "+", "-"])
    expr[1] = calc(expression, ["*", "-", "+"])
    expr[2] = calc(expression, ["+", "*", "-"])
    expr[3] = calc(expression, ["+", "-", "*"])
    expr[4] = calc(expression, ["-", "*", "+"])
    expr[5] = calc(expression, ["-", "+", "*"])
    return max(expr)