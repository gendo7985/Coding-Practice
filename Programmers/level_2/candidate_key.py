# 후보 키

from itertools import combinations


def isMin(cand_keys, keys):
    for cand_key in cand_keys:
        check = True
        for i in cand_key:
            if i not in keys:
                check = False
                break
        else:
            return True
    return False


def isUnique(relation, keys, n):
    tuples = [tuple([i[j] for j in keys]) for i in relation]
    return len(set(tuples)) == n


def solution(relation):
    cand_keys = []
    ncol = len(relation[0])
    nrow = len(relation)
    subset = []
    for i in range(1, ncol + 1):
        subset.extend(list(combinations(range(ncol), i)))
    for keys in subset:
        print(keys)
        if not isMin(cand_keys, keys):
            if isUnique(relation, keys, nrow):
                cand_keys.append(keys)
    print(cand_keys)
    return len(cand_keys)