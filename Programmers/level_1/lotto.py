# 로또의 최고 순위와 최저 순위


def solution(lottos, win_nums):
    win = 0
    zero = 0
    for i in lottos:
        if i == 0:
            zero += 1
        elif i in win_nums:
            win += 1
    if zero == 6:
        return [7 - zero, 6 - win]
    if win == 0:
        return [6 - zero, 6 - win]
    return [7 - win - zero, 7 - win]