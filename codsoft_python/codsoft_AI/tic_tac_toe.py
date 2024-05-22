import math

# Constants for the players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Define the board size
BOARD_SIZE = 3

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (BOARD_SIZE * 4 - 1))

# Function to check if a player has won
def check_win(board, player):
    for i in range(BOARD_SIZE):
        # Check rows and columns
        if all(board[i][j] == player for j in range(BOARD_SIZE)) or all(board[j][i] == player for j in range(BOARD_SIZE)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(BOARD_SIZE)) or all(board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)):
        return True
    return False

# Function to check if the board is full
def board_full(board):
    return all(board[i][j] != EMPTY for i in range(BOARD_SIZE) for j in range(BOARD_SIZE))

# Function to evaluate the board
def evaluate(board):
    if check_win(board, PLAYER_X):
        return 1
    elif check_win(board, PLAYER_O):
        return -1
    else:
        return 0

# Function to find the best move using Minimax algorithm
def minimax(board, depth, maximizing_player):
    if check_win(board, PLAYER_X):
        return 1
    elif check_win(board, PLAYER_O):
        return -1
    elif board_full(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move for AI player
def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                eval = minimax(board, 0, False)
                board[i][j] = EMPTY
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Function to play the game
def play_game():
    # Initialize an empty board
    board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    # Main game loop
    while True:
        # Player's move
        row, col = map(int, input("Enter row and column (0-2) for your move: ").split())
        if board[row][col] != EMPTY:
            print("Invalid move! Try again.")
            continue
        board[row][col] = PLAYER_O
        print_board(board)

        # Check if player wins
        if check_win(board, PLAYER_O):
            print("Congratulations! You win!")
            break

        # Check if the game is a draw
        if board_full(board):
            print("It's a draw!")
            break

        # AI's move
        print("AI is thinking...")
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = PLAYER_X
        print_board(board)

        # Check if AI wins
        if check_win(board, PLAYER_X):
            print("AI wins! Better luck next time.")
            break

        # Check if the game is a draw
        if board_full(board):
            print("It's a draw!")
            break

# Start the game
play_game()