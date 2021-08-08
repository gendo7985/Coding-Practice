# 보석 쇼핑


def solution(gems):
    n = len(list(set(gems)))
    current = {}
    for i in range(len(gems)):
        if gems[i] not in current:
            current[gems[i]] = 1
        else:
            current[gems[i]] += 1
        if len(current.keys()) == n:
            course_old, course = [1, i + 1], [1, i + 1]
            while current[gems[course[0] - 1]] > 1:
                current[gems[course[0] - 1]] -= 1
                course[0] += 1
            course_old[0] = course[0]
            break
    for i in range(course[1], len(gems)):
        current[gems[i]] += 1
        course[1] += 1
        while current[gems[course[0] - 1]] > 1:
            current[gems[course[0] - 1]] -= 1
            course[0] += 1
        if course[1] - course[0] < course_old[1] - course_old[0]:
            course_old[0], course_old[1] = course[0], course[1]
    return course_old