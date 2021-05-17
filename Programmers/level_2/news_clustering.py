# 뉴스 클러스터링

from collections import Counter


def solution(str1, str2):
    list1 = [str1[i : i + 2] for i in range(len(str1) - 1)]
    list2 = [str2[i : i + 2] for i in range(len(str2) - 1)]
    a = Counter(list(map(lambda s: s.lower(), filter(lambda s: s.isalpha(), list1))))
    b = Counter(list(map(lambda s: s.lower(), filter(lambda s: s.isalpha(), list2))))
    ss = set(a.keys()).union(set(b.keys()))
    if not ss:
        return 65536
    intersection = 0
    union = 0
    for i in ss:
        intersection += min(a[i], b[i])
        union += max(a[i], b[i])
    return int(intersection / union * 65536)