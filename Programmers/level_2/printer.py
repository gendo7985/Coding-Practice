# 프린터


def solution(priorities, location):
    answer = 0
    while True:
        J = priorities.pop(0)
        location -= 1
        if not priorities:
            return answer + 1
        elif J < max(priorities):
            priorities.append(J)
            if location == -1:
                location = len(priorities) - 1
        else:
            answer += 1
            if location == -1:
                return answer