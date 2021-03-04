# 크레인 인형뽑기 게임


def solution(board, moves):
    answer = 0
    basket = []
    for move in moves:
        doll = 0
        for i in range(len(board)):
            if board[i][move - 1] != 0:
                doll = board[i][move - 1]
                board[i][move - 1] = 0
                break

        if doll == 0:
            pass
        elif len(basket) == 0 or doll != basket[-1]:
            basket.append(doll)
        else:
            basket.pop()
            answer += 2
    return answer


if __name__ == "__main__":
    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]
    print(solution(board, moves) == 4)
