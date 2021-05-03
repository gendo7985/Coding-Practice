# 다리를 지나는 트럭


def solution(bridge_length, weight, truck_weights):
    queue = [0] * bridge_length
    answer = 0
    while truck_weights:
        answer += 1
        queue.pop(0)
        if sum(queue) + truck_weights[0] <= weight:
            queue.append(truck_weights.pop(0))
        else:
            queue.append(0)
    return answer + len(queue)