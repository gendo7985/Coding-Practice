# 불량 사용자


from itertools import combinations, permutations


def isBanned(a, b):
    if len(a) != len(b):
        return False
    for i, j in zip(a, b):
        if i != j and j != "*":
            return False
    return True


def perm_check(group, banned_id):
    li = permutations(banned_id)
    for perm in li:
        if all([isBanned(group[i], perm[i]) for i in range(len(banned_id))]):
            return True
    return False


def solution(user_id, banned_id):
    cnt = 0
    li = combinations(user_id, len(banned_id))
    for group in li:
        if perm_check(group, banned_id):
            cnt += 1
    return cnt