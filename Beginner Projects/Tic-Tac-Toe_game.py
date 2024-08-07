# Initialize the game board as a list of 9 empty spaces
board = [' ' for _ in range(9)]

# Function to print the game board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Function to check for a win or a draw
def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full (draw)
def check_draw(board):
    return ' ' not in board

# Main game loop
def tic_tac_toe():
    current_player = 'X'  # Start with player X
    while True:
        print_board()  # Print the current board
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
        if board[move] == ' ':  # If the move is valid (spot is empty)
            board[move] = current_player  # Place the player's mark on the board
            if check_winner(board, current_player):  # Check if the current player won
                print_board()
                print(f"Player {current_player} wins!")
                break
            elif check_draw(board):  # Check if the game is a draw
                print_board()
                print("It's a draw!")
                break
            current_player = 'O' if current_player == 'X' else 'X'  # Switch players
        else:
            print("Invalid move. Try again.")  # Prompt for a valid move

# Start the game
tic_tac_toe()
