# 튜플

def solution(s):
    parsed = map(lambda x: list(map(int,x.split(","))),s[2:-2].split("},{"))
    ordered = sorted(parsed, key = lambda x: len(x))
    ans = []
    for i in ordered:
        for j in i:
            if j not in ans:
                ans.append(j)
    return ans