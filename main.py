import numpy as np
from minimax import minimax
from alphabeta import alphabeta
from game_utils import check_winner, check_draw

def initialize_board():
    return np.zeros((7, 7), dtype=int)

def print_board(board):
    for row in board:
        print(' '.join([str(elem) for elem in row]))
    print()

def play_game(ai_choice):
    board = initialize_board()
    print("Tabuleiro inicial:")
    print_board(board)
    
    while True:
        try:
            row, col = map(int, input("Digite a linha e coluna (0-6) do seu movimento: ").split())
        except ValueError:
            print("Entrada inválida. Por favor, insira dois números separados por espaço.")
            continue
        
        if 0 <= row < 7 and 0 <= col < 7 and board[row, col] == 0:
            board[row, col] = 1
        else:
            print("Movimento inválido, tente novamente.")
            continue
        print_board(board)
        
        if check_winner(board, 1):
            print("Parabéns! Você ganhou!")
            break
        if check_draw(board):
            print("Empate!")
            break

        max_depth = 3
        if ai_choice == "1":
            _, move = minimax(board, 0, False, max_depth)
        elif ai_choice == "2":
            _, move = alphabeta(board, 0, False, float('-inf'), float('inf'), max_depth)
        
        if move:
            board[move[0], move[1]] = 2
            print("Movimento da IA:")
            print_board(board)
            
            if check_winner(board, 2):
                print("A IA ganhou! Tente novamente.")
                break
            if check_draw(board):
                print("Empate!")
                break

ai_choice = input("Escolha contra qual IA você quer jogar (1: MINIMAX 2: ALPHABETA): ").strip().lower()
while ai_choice not in ["1", "2"]:
    ai_choice = input("Escolha inválida. Por favor, escolha entre 1: MINIMAX 2: ALPHABETA: ")
play_game(ai_choice)
