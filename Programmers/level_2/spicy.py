# 더 맵게

import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + 2 * b)
        cnt += 1
    return cnt