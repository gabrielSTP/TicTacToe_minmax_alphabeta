import numpy as np
from game_utils import check_winner, check_draw, evaluate_board

def alphabeta(board, depth, is_maximizing, alpha, beta, max_depth):
    if check_winner(board, 2):
        return -10 + depth, None
    elif check_winner(board, 1):
        return 10 - depth, None
    elif check_draw(board):
        return 0, None
    elif depth == max_depth:
        return evaluate_board(board), None

    if is_maximizing:
        max_eval = float('-inf')
        best_move = None
        for i in range(7):
            for j in range(7):
                if board[i, j] == 0:
                    board[i, j] = 1
                    evaluation, _ = alphabeta(board, depth + 1, False, alpha, beta, max_depth)
                    board[i, j] = 0
                    if evaluation > max_eval:
                        max_eval = evaluation
                        best_move = (i, j)
                    alpha = max(alpha, evaluation)
                    if beta <= alpha:
                        break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for i in range(7):
            for j in range(7):
                if board[i, j] == 0:
                    board[i, j] = 2
                    evaluation, _ = alphabeta(board, depth + 1, True, alpha, beta, max_depth)
                    board[i, j] = 0
                    if evaluation < min_eval:
                        min_eval = evaluation
                        best_move = (i, j)
                    beta = min(beta, evaluation)
                    if beta <= alpha:
                        break
        return min_eval, best_move
