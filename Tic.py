from random import randint, choice

board = [x-1 for x in range(1, 10)]
PLAYER1 = None
AI = None
PLAYER1_TURN = False
AI_TURN = False
RUNNING = True


def check_bingo(board):
    BINGO_STATUS = False
    if board[0] == board[1] and board[1] == board[2]:
        return not BINGO_STATUS
    elif board[3] == board[4] and board[4] == board[5]:
        return not BINGO_STATUS
    elif board[6] == board[7] and board[7] == board[8]:
        return not BINGO_STATUS
    elif board[0] == board[3] and board[3] == board[6]:
        return not BINGO_STATUS
    elif board[1] == board[4] and board[4] == board[7]:
        return not BINGO_STATUS
    elif board[2] == board[5] and board[5] == board[8]:
        return not BINGO_STATUS
    elif board[0] == board[4] and board[4] == board[8]:
        return not BINGO_STATUS
    elif board[2] == board[4] and board[4] == board[6]:
        return not BINGO_STATUS


def show_board(board):
    print("\n"*3)
    print(str(board[6]) + "|" + str(board[7]) + "|" + str(board[8]))
    print(str(board[3]) + "|" + str(board[4]) + "|" + str(board[5]))
    print(str(board[0]) + "|" + str(board[1]) + "|" + str(board[2]))


def decide_turn():
    random = randint(0, 1)
    if random == 0:
        PLAYER1_TURN = True
        AI_TURN = False
        PLAYER1 = input("Do you want to be X or O?")
        if PLAYER1.lower() == "x":
            PLAYER1 = "X"
            AI = "O"
        else:
            PLAYER1 = "O"
            AI = "X"
    else:
        PLAYER1_TURN = False
        AI_TURN = True
        random = randint(0, 1)
        if random == 0:
            AI = "X"
            PLAYER1 = "O"
        else:
            AI = "O"
            PLAYER1 = "X"
    print(f"player 1 is {PLAYER1} and the AI is {AI}")
    return PLAYER1, AI, PLAYER1_TURN, AI_TURN


def copy_board(board):
    duplicate = board.copy()
    return duplicate


def possible_moves(board):
    moves_list = []
    for moves in board:
        if type(moves) == int:
            moves_list.append(moves)

    return moves_list


def space_free(board, move):
    return type(board[move]) == int


def make_move(board, letter, spot):
    board[spot] = letter


def make_random_move(board):
    possible_move = possible_moves(board)

    if len(possible_move) != 0:
        return choice(possible_move)
    else:
        return None


def ai_move(board, letter):
    for i in possible_moves(board):
        copy = copy_board(board)
        make_move(copy, letter, i)
        if check_bingo(copy):
            return i

    for i in possible_moves(board):
        copy = copy_board(board)
        make_move(copy, PLAYER1, i)
        if check_bingo(copy):
            return i
    corners = []

    for i in [0, 2, 6, 8]:
        if space_free(board, i):
            corners.append(i)
    if corners:
        return choice(corners)

    if space_free(board, 4):
        return 4
    sides = []
    for i in [1, 3, 5, 7]:  # THIS COULD BE A PROBLEM... OVERWRITING...
        if space_free(board, i):
            sides.append(i)
    if sides:
        return choice(sides)


def check_full_board(board):
    for i in range(1, 10):
        if space_free(board, i-1):
            return False
    print("True though")
    return True


PLAYER1, AI, PLAYER1_TURN, AI_TURN = decide_turn()

while RUNNING:
    if PLAYER1_TURN:
        possible_moves(board)
        show_board(board)
        print("Player 1 turn")
        if check_full_board(board):
            print("A DRAW HAS OCCURRED..")
            break
        spot = int(input("Where do you want to place your mark?"))
        # print(make_move(board, PLAYER1, spot))
        make_move(board, PLAYER1, spot)
        # make_random_move(board)
        show_board(board)
        if check_bingo(board):
            RUNNING = False
            print("PLAYER 1 has won the game")
        PLAYER1_TURN = not PLAYER1_TURN
        AI_TURN = not AI_TURN
    else:
        print("AI TURN")
        if check_full_board(board):
            print("A DRAW HAS OCCURRED..")
            break
        spot = ai_move(board, AI)
        make_move(board, AI, spot)
        show_board(board)
        if check_bingo(board):
            RUNNING = False
            print("The AI has won the game")
        PLAYER1_TURN = not PLAYER1_TURN
        AI_turn = not AI_TURN
