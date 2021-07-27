# 단속카메라 


def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[1])
    time = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][0] > time:
            answer += 1
            time = routes[i][1]
    return answer