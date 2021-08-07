# 추석 트래픽


def solution(lines):
    start = []
    end = []
    for log in lines:
        h = int(log[11:13])
        m = int(log[14:16])
        s = float(log[17:23])
        dt = float(log[24:-1])
        start.append(3600 * h + 60 * m + s - dt + 0.001)
        end.append(3600 * h + 60 * m + s)
    ans = 1
    timeline = [(start[i], i, 1) for i in range(len(start))] + [
        (end[i], i, -1) for i in range(len(end))
    ]
    timeline.sort(key=lambda x: x[0])
    visited = [timeline[0][1]]
    ans = 1
    idx = 0
    for i in range(1, len(timeline)):
        if timeline[i][1] not in visited:
            visited.append(timeline[i][1])
        for j in range(idx, len(timeline)):
            if timeline[i][0] - timeline[j][0] < 1:
                idx = j
                break
            else:
                if timeline[j][2] == -1:
                    visited.remove(timeline[j][1])
        if len(visited) > ans:
            ans = len(visited)
    return ans