import numpy as np

def check_winner(board, player):
    for i in range(7):
        for j in range(7):
            if (j <= 3 and all(board[i, j:j+4] == player)) or \
               (i <= 3 and all(board[i:i+4, j] == player)) or \
               (i <= 3 and j <= 3 and all([board[i+k, j+k] == player for k in range(4)])) or \
               (i >= 3 and j <= 3 and all([board[i-k, j+k] == player for k in range(4)])):
                return True
    return False

def check_draw(board):
    return np.all(board != 0)

def evaluate_board(board):
    score = 0
    for i in range(7):
        for j in range(7):
            if board[i, j] != 0:
                if j <= 3:
                    score += evaluate_window(board[i, j:j+4], board[i, j])
                if i <= 3:
                    score += evaluate_window(board[i:i+4, j], board[i, j])
                if i <= 3 and j <= 3:
                    score += evaluate_window(np.array([board[i+k, j+k] for k in range(4)]), board[i, j])
                if i >= 3 and j <= 3:
                    score += evaluate_window(np.array([board[i-k, j+k] for k in range(4)]), board[i, j])
    return score

def evaluate_window(window, player):
    score = 0
    opp_player = 2 if player == 1 else 1
    player_count = np.count_nonzero(window == player)
    opp_count = np.count_nonzero(window == opp_player)
    empty_count = np.count_nonzero(window == 0)

    if player_count == 4:
        score += 100
    elif player_count == 3 and empty_count == 1:
        score += 5
    elif player_count == 2 and empty_count == 2:
        score += 2
    if opp_count == 3 and empty_count == 1:
        score -= 4
    return score
