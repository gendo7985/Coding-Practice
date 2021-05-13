# 타겟 넘버


def solution(numbers, target):
    if len(numbers) == 0:
        return int(0 == target)
    arr = numbers[1:]
    number = numbers[0]
    return solution(arr, target + number) + solution(arr, target - number)
