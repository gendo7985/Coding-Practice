# 배달


def solution(N, road, K):
    dist = [-1] * N
    dist[0] = 0
    graph = [[0] * N for _ in range(N)]
    for r in road:
        a, b, c = r[0] - 1, r[1] - 1, r[2]
        if graph[a][b] == 0:
            graph[a][b] = graph[b][a] = c
        else:
            graph[a][b] = graph[b][a] = min(c, graph[a][b])
    queue = [0]
    while queue:
        src = queue.pop()
        for dest in range(N):
            if graph[src][dest] != 0:
                if dist[dest] == -1:
                    dist[dest] = dist[src] + graph[src][dest]
                    queue.append(dest)
                else:
                    if dist[dest] > dist[src] + graph[src][dest]:
                        dist[dest] = dist[src] + graph[src][dest]
                        queue.append(dest)
    return sum(map(lambda x: x <= K, dist))
