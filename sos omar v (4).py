
# --------- Global Variables -----------
import sys

# Will hold our game board data
board = [['-' for _ in range(4)] for _ in range(4) ]

current_player = 0
players = [{"name":"player1", "score":0}, {"name":"player2", "score":0}]


def display_board():
    print(f"player1 score = {players[0]['score']}")
    print(f"player2 score = {players[1]['score']}")
    for r in range(4):
        print(board[r])


def handle_turn():
    global board
    # Get position from player
    print(f"{players[current_player]['name']} 's turn.")
    row = input("Choose a row from 1-4: ")
    col = input("Choose a column from 1-4: ")
    symbol = input("Choose [s,o]: ")
    valid = False
    while not valid:
        # Get correct index in our board list
        row = int(row) - 1
        col = int(col) - 1

        # Make sure the input is valid
        while row not in [ i for i in range(4)] or col not in [ i for i in range(4)]:
            row = int(input("Choose row from 1-4: "))
            col = int(input("choose col from 1-4: "))
            if board[row][col] != "-":
                row = -1
                col = -1
                print("you can't choose this position")

        while symbol.lower() not in ['s', 'o']:
            symbol = input("Choose [s,o]: ")

        # Put the game piece on the board
        board[row][col] = symbol.upper()

        valid = True


# switch player
def flip_player():
    global current_player
    current_player = 1 if current_player == 0 else 0


# end the game
def end_game():
    if players[0]['score'] == players[1]['score']:
        print("Draw!!")
        return None
    winner = players[0]['name'] if players[0]['score'] > players[1]['score'] else players[1]['name']
    print(f"{winner} won !! ")


# Check if the game is over
def check_if_game_over():
    for r in range(4):
        for c in range(4):
            if board[r][c] == "-":
                return False
    end_game()
    sys.exit(0)


def check_rows():
    for r in range(4):
        for c in range(2):
            if board[r][c] == "S" and board[r][c+1] == "O" and board[r][c+2] == "S":
                return True
    return False


def check_columns():
    for c in range(4):
        for r in range(2):
            if board[r][c] == "S" and board[r+1][c] == "O" and board[r+2][c] == "S":
                return True
    return False


def check_diagonals():
    # check for ascending diagonal
    for r in range(2):
        for c in range(1, -1, -1):
            if board[r][c] == "S" and board[r+1][c+1] == "O" and board[r+2][c+2] == "S":
                return True
    # check for descending diagonal
    for r in range(2):
        for c in range(3, 1, -1):
            if board[r][c] == "S" and board[r+1][c-1] == "O" and board[r+2][c-2] == "S":
                return True
    return False


def check_for_sos():
    return check_rows() or check_columns() or check_diagonals()


def play_game():
    global players
    # Show the initial game board
    display_board()

    # Loop until the game stops (winner or tie)
    while True:
        # Handle a turn
        handle_turn()

        # check if player make sos
        if check_for_sos():
            players[current_player]['score'] += 1
            check_if_game_over()
            display_board()
            continue


        # Check if the game is over
        check_if_game_over()

        # Flip to the other player
        flip_player()
        display_board()


play_game()




