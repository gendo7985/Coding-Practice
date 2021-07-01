# 가장 큰 정사각형 찾기


def solution(board):
    nrow, ncol = len(board), len(board[0])
    m = max(board[0])
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i - 1][j - 1] == board[i - 1][j] == board[i][j - 1] != 0 and board[i][j] != 0:
                board[i][j] = board[i][j - 1] + 1
                if board[i][j] > m:
                    m = board[i][j]
            elif min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1], board[i][j]) == 0:
                pass
            else:
                board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1
    return m ** 2