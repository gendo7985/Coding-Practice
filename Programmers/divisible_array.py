# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = list(filter(lambda x: x % divisor == 0, arr))
    answer.sort()
    if answer == []:
        answer = [-1]
    return answer
