import random
import time


# default wait time (to ensure smooth gameplay)
DELAY = 2


def show_board(board):
    """Display well-formatted board.
    @type board: list
    @rtype: None
    """
    print("-------------")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("|---+---+---|")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("|---+---+---|")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("-------------\n\n")


def get_p_move(board):
    """Get and validate user move based on current board state.
    @type board: list
    @rtype: int
    """
    available = []

    for i in range(len(board)):
        if board[i] != "X" and board[i] != "O":
            available.append(i)

    while True:
        try:
            move = int(input("Your move: "))
            print()
        except ValueError:
            print("Invalid entry.")
            continue

        if not((move - 1) in available):
            print("That spot is unavailable.")
            continue
        else:
            break
    
    return move - 1


def check_for_win(board):
    """Check board for whether someone has won yet.
    @type board: list
    @rtype: None
    """

    # check if cpu wins
    if board[0] == board[1] == board[2] == "X":
        print("CPU WINS!")
        time.sleep(DELAY)
        exit()
    elif board[3] == board[4] == board[5] == "X":
        print("CPU WINS!")
        time.sleep(DELAY)
        exit()
    elif board[6] == board[7] == board[8] == "X":
        print("CPU WINS!")
        time.sleep(DELAY)
        exit()
    elif board[0] == board[3] == board[6] == "X":
        print("CPU WINS!")
        time.sleep(DELAY)
        exit()
    elif board[1] == board[4] == board[7] == "X":
        print("CPU WINS!")
        time.sleep(DELAY)
        exit()
    elif board[2] == board[5] == board[8] == "X":
        print("CPU WINS!")
        time.sleep(DELAY)
        exit()
    elif board[0] == board[4] == board[8] == "X":
        print("CPU WINS!")
        time.sleep(DELAY)
        exit()
    elif board[2] == board[4] == board[6] == "X":
        print("CPU WINS!")
        time.sleep(DELAY)
        exit()

    # check if player wins
    elif board[0] == board[1] == board[2] == "O":
        print("YOU WIN!")
        time.sleep(DELAY)
        exit()
    elif board[3] == board[4] == board[5] == "O":
        print("YOU WIN!")
        time.sleep(DELAY)
        exit()
    elif board[6] == board[7] == board[8] == "O":
        print("YOU WIN!")
        time.sleep(DELAY)
        exit()
    elif board[0] == board[3] == board[6] == "O":
        print("YOU WIN!")
        time.sleep(DELAY)
        exit()
    elif board[1] == board[4] == board[7] == "O":
        print("YOU WIN!")
        time.sleep(DELAY)
        exit()
    elif board[2] == board[5] == board[8] == "O":
        print("YOU WIN!")
        time.sleep(DELAY)
        exit()
    elif board[0] == board[4] == board[8] == "O":
        print("YOU WIN!")
        time.sleep(DELAY)
        exit()
    elif board[2] == board[4] == board[6] == "O":
        print("YOU WIN!")
        time.sleep(DELAY)
        exit()
    else:
        pass


def cpu_strategic_move(board):
    """Determine optimal cpu move based on current state of board.
    @type board: list
    @rtype: int
    """

    # check for spots where cpu is one move away from winning
    if (board[0] == board[1] == "X") and (board[2] != "O"):
        return 2
    if (board[1] == board[2] == "X") and (board[0] != "O"):
        return 0
    if (board[3] == board[4] == "X") and (board[5] != "O"):
        return 5
    if (board[4] == board[5] == "X") and (board[3] != "O"):
        return 3
    if (board[6] == board[7] == "X") and (board[8] != "O"):
        return 8
    if (board[7] == board[8] == "X") and (board[6] != "O"):
        return 6
    if (board[0] == board[3] == "X") and (board[6] != "O"):
        return 6
    if (board[3] == board[6] == "X") and (board[0] != "O"):
        return 0
    if (board[1] == board[4] == "X") and (board[7] != "O"):
        return 7
    if (board[4] == board[7] == "X") and (board[1] != "O"):
        return 1
    if (board[2] == board[5] == "X") and (board[8] != "O"):
        return 8
    if (board[5] == board[8] == "X") and (board[2] != "O"):
        return 2
    if (board[0] == board[4] == "X") and (board[8] != "O"):
        return 8
    if (board[2] == board[4] == "X") and (board[6] != "O"):
        return 6
    if (board[6] == board[4] == "X") and (board[2] != "O"):
        return 2
    if (board[8] == board[4] == "X") and (board[0] != "O"):
        return 0
    if (board[0] == board[2] == "X") and (board[1] != "O"):
        return 1
    if (board[3] == board[5] == "X") and (board[4] != "O"):
        return 4
    if (board[6] == board[8] == "X") and (board[7] != "O"):
        return 7
    if (board[0] == board[6] == "X") and (board[3] != "O"):
        return 3
    if (board[2] == board[8] == "X") and (board[5] != "O"):
        return 5
    if (board[1] == board[7] == "X") and (board[4] != "O"):
        return 4
    if (board[0] == board[8] == "X") and (board[4] != "O"):
        return 4
    if (board[2] == board[6] == "X") and (board[4] != "O"):
        return 4
    
    # check for spots where the cpu is one away from losing
    if (board[0] == board[1] == "O") and (board[2] != "X"):
        return 2
    if (board[1] == board[2] == "O") and (board[0] != "X"):
        return 0
    if (board[3] == board[4] == "O") and (board[5] != "X"):
        return 5
    if (board[4] == board[5] == "O") and (board[3] != "X"):
        return 3
    if (board[6] == board[7] == "O") and (board[8] != "X"):
        return 8
    if (board[7] == board[8] == "O") and (board[6] != "X"):
        return 6
    if (board[0] == board[3] == "O") and (board[6] != "X"):
        return 6
    if (board[3] == board[6] == "O") and (board[0] != "X"):
        return 0
    if (board[1] == board[4] == "O") and (board[7] != "X"):
        return 7
    if (board[4] == board[7] == "O") and (board[1] != "X"):
        return 1
    if (board[2] == board[5] == "O") and (board[8] != "X"):
        return 8
    if (board[5] == board[8] == "O") and (board[2] != "X"):
        return 2
    if (board[0] == board[4] == "O") and (board[8] != "X"):
        return 8
    if (board[2] == board[4] == "O") and (board[6] != "X"):
        return 6
    if (board[6] == board[4] == "O") and (board[2] != "X"):
        return 2
    if (board[8] == board[4] == "O") and (board[0] != "X"):
        return 0
    if (board[0] == board[2] == "O") and (board[1] != "X"):
        return 1
    if (board[3] == board[5] == "O") and (board[4] != "X"):
        return 4
    if (board[6] == board[8] == "O") and (board[7] != "X"):
        return 7
    if (board[0] == board[6] == "O") and (board[3] != "X"):
        return 3
    if (board[2] == board[8] == "O") and (board[5] != "X"):
        return 5
    if (board[1] == board[7] == "O") and (board[4] != "X"):
        return 4
    if (board[0] == board[8] == "O") and (board[4] != "X"):
        return 4
    if (board[2] == board[6] == "O") and (board[4] != "X"):
        return 4

    # choose random spot if board is neutral
    available = []

    for i in range(len(board)):
        if board[i] != "X" and board[i] != "O":
            available.append(i)
    
    return random.choice(available)


def check_for_tie(board):
    """Checks if game is a draw based on current state of board.
    @type board: list
    @rtype: None
    """
    available = 0

    for i in board:
        if i != "O" and i != "X":
            available += 1
    
    if available == 0:
        print("IT'S A TIE!")
        time.sleep(DELAY)
        exit()


def main():
    # declare board with list comprehension
    board = [str(i) for i in range (1, 10)]
    
    # game intro
    print("\n~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to Tic Tac Toe!")
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(DELAY)
    print()
    print()
    show_board(board)
    time.sleep(DELAY)
    print("CPU plays first.\n\n")
    time.sleep(DELAY)

    # cpu chooses random spot out of set of corner spots and center
    options = [0, 2, 4, 6, 8]
    board[random.choice(options)] = "X"

    # get player move
    show_board(board)
    p_move = get_p_move(board)
    board[p_move] = "O"
    time.sleep(DELAY)
    print()
    show_board(board)
    time.sleep(DELAY)
    print("CPU move:\n\n")
    time.sleep(DELAY)

    # cpu chooses spot out of remaining corner and center spots
    new_options = []
    for option in options:
        if not(board[option] == "X" or board[option] == "O"):
            new_options.append(option)
    board[random.choice(new_options)] = "X"
    show_board(board)

    # game mainloop
    while True:
        # get player move
        p_move = get_p_move(board)
        board[p_move] = "O"
        time.sleep(DELAY)
        print()
        show_board(board)

        # check if game is either won or tied
        check_for_win(board)
        check_for_tie(board)

        # cpu makes strategic move
        time.sleep(DELAY)
        print("CPU move:\n\n")
        time.sleep(DELAY)
        cpu_move = cpu_strategic_move(board)
        board[cpu_move] = "X"
        time.sleep(DELAY)
        print()
        show_board(board)

        # check if game is either won or tied
        check_for_win(board)
        check_for_tie(board)


if __name__ == '__main__':
    main()
