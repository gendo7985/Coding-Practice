# H-Index


def solution(citations):
    a = sorted(citations, reverse=True)
    for h in range(len(a), -1, -1):
        if a[h - 1] >= h:
            return h