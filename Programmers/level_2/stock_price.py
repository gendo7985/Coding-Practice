# 주식가격


def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                break
        answer[i] = j-i
    return answer