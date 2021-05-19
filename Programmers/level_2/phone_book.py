# 전화번호 목록

from collections import Counter


def solution(phone_book, length=1):
    for i in phone_book:
        if len(i) < length:
            return False
    head = [i[:length] for i in phone_book]
    cnt = Counter(head)
    if max(cnt.values()) < 2:
        return True
    filtered = list(filter(lambda n: cnt[n[:length]] >= 2, phone_book))
    return solution(filtered, length + 1)
