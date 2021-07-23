# 네트워크


def solution(n, computers):
    cnt = 0
    visited = [False] * n
    for i in range(n):
        computers[i][i] = 0
    while not all(visited):
        stack = [visited.index(False)]
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                for comp in range(n):
                    if computers[node][comp] == 1 and not visited[comp]:
                        stack.append(comp)
        cnt += 1
    return cnt