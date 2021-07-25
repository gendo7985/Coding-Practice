# 여행경로


def solution(tickets):
    airport = {}
    n = len(tickets)
    for i in range(n):
        if tickets[i][0] in airport.keys():
            airport[tickets[i][0]].append(i)
        else:
            airport[tickets[i][0]] = [i]
    for key in airport.keys():
        airport[key].sort(key=lambda x: tickets[x][1], reverse=True)
    stack = [("ICN", ["ICN"], [])]  # node, path, used ticket
    while stack:
        node, path, used = stack.pop()
        if len(used) == n:
            return path
        if node in airport:
            for i in airport[node]:
                if i not in used:
                    dest = tickets[i][1]
                    stack.append((dest, path + [dest], used + [i]))