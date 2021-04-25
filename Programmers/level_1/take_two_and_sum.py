# 두 개 뽑아서 더하기


def solution(numbers):
    answer = []
    N = len(numbers)
    for i in range(N):
        for j in range(i + 1, N):
            s = numbers[i] + numbers[j]
            if s not in answer:
                answer.append(s)
    answer.sort()
    return answer


if __name__ == "__main__":
    numbers = [2, 1, 3, 4, 1]
    result = [2, 3, 4, 5, 6, 7]
    print(solution(numbers) == result)
    numbers = [5, 0, 2, 7]
    result = [2, 5, 7, 9, 12]
    print(solution(numbers) == result)
