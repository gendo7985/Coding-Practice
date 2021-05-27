# 메뉴 리뉴얼

from itertools import combinations


def isContain(order, menu):
    for i in menu:
        if not i in order:
            return False
    return True


def possible_menus(orders, num):
    ans = set([])
    for i in orders:
        if len(i) >= num:
            ans.update(list(combinations(i, num)))
    return list(ans)


def solution(orders, course):
    ans = []
    for i in range(len(orders)):
        orders[i] = "".join(sorted(list(orders[i])))
    for num in course:
        candidates = possible_menus(orders, num)
        possible = []
        m = 2
        for menu in candidates:
            cnt = 0
            for order in orders:
                if isContain(order, menu):
                    cnt += 1
            if cnt > m:
                possible = ["".join(menu)]
                m = cnt
            elif cnt == m:
                possible.append("".join(menu))
        ans += possible
    return sorted(ans)