def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True

    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def make_move(board, player, row, col):
    board[row][col] = player


board = [[' ' for _ in range(3)] for _ in range(3)]


players = ['X', 'O']
current_player = players[0]


while True:
    display_board(board)

   
    row = int(input(f"Player {current_player}'s turn. Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    if is_valid_move(board, row, col):
        make_move(board, current_player, row, col)

        if is_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            display_board(board)
            print("It's a draw!")
            break

        
        current_player = players[1] if current_player == players[0] else players[0]
    else:
        print("Invalid move. Try again.")
