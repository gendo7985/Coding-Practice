# 방문 길이


def solution(dirs):
    visited = []
    pos = [0, 0]
    for i in dirs:
        if i == "U" and pos[1] < 5:
            pos[1] += 1
            if (pos[0], pos[1] - 1, "U") not in visited:
                visited.append((pos[0], pos[1] - 1, "U"))
                visited.append((pos[0], pos[1], "D"))
        elif i == "D" and pos[1] > -5:
            pos[1] -= 1
            if (pos[0], pos[1] + 1, "D") not in visited:
                visited.append((pos[0], pos[1], "U"))
                visited.append((pos[0], pos[1] + 1, "D"))
        elif i == "L" and pos[0] > -5:
            pos[0] -= 1
            if (pos[0] + 1, pos[1], "L") not in visited:
                visited.append((pos[0], pos[1], "R"))
                visited.append((pos[0] + 1, pos[1], "L"))
        elif i == "R" and pos[0] < 5:
            pos[0] += 1
            if (pos[0] - 1, pos[1], "R") not in visited:
                visited.append((pos[0] - 1, pos[1], "R"))
                visited.append((pos[0], pos[1], "L"))
    return len(visited) // 2
