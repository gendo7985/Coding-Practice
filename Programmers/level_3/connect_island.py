# 섬 연결하기


def solution(n, costs):
    costs.sort(key=lambda x: x[-1])
    connected = [False] * n
    b = costs.pop(0)
    connected[b[0]] = connected[b[1]] = True
    money = b[2]
    while not all(connected):
        for i in range(len(costs)):
            if connected[costs[i][0]] ^ connected[costs[i][1]]:
                b = costs.pop(i)
                connected[b[0]] = connected[b[1]] = True
                money += b[2]
                break
    return money