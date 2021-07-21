# 가장 먼 노드


def solution(n, edge):
    g = {}
    for x, y in edge:
        if x - 1 in g:
            g[x - 1].append(y - 1)
        else:
            g[x - 1] = [y - 1]
        if y - 1 in g:
            g[y - 1].append(x - 1)
        else:
            g[y - 1] = [x - 1]
    visited = [False] * n
    visited[0] = True
    queue = [0]
    while queue:
        num = len(queue)
        for node in range(num):
            for i in g[queue[node]]:
                if (not visited[i]) and (i not in queue):
                    queue.append(i)
                    visited[i] = True
        queue = queue[num:]
    return num