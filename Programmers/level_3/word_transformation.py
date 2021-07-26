# 단어 변환


def connected(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return a[i + 1 :] == b[i + 1 :]
    return False


def solution(begin, target, words):
    if target not in words:
        return 0
    visited = []
    queue = [(begin, 0)]
    while queue:
        node, path = queue.pop(0)
        for word in words:
            if word not in visited and connected(node, word):
                if word == target:
                    return path + 1
                else:
                    queue.append((word, path + 1))
                    visited.append(word)
    return 0
