# 게임 맵 최단거리


from collections import deque

def solution(maps):
    queue = deque()
    queue.append((0, 0))
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    cnt = 1
    while queue:
        for i in range(len(queue)):
            (x, y) = queue.popleft()
            if (x, y) == (len(maps) - 1, len(maps[0]) - 1):
                return cnt
            for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= x + dx <= len(maps) - 1 and 0 <= y + dy <= len(maps[0]) - 1:
                    if not visited[x+dx][y+dy]:
                        if maps[x + dx][y + dy] == 1:
                            visited[x+dx][y+dy] = True
                            queue.append((x + dx, y + dy))
        cnt += 1
        
    return -1