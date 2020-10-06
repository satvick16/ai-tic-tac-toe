import random
import time
import evaluate
import strategy


# default wait time (to ensure smooth gameplay)
DELAY = 2


def show_board(board):
    """Display well-formatted board.
    @type board: list
    @rtype: None
    """
    print("/-----------\\")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("|---+---+---|")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("|---+---+---|")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("\-----------/\n\n")


def get_p_move(board):
    """Get and validate user move based on current board state.
    @type board: list
    @rtype: int
    """
    # find all available spots on the board
    available = []

    for i in range(len(board)):
        if board[i] != "X" and board[i] != "O":
            available.append(i)

    while True:
        try:
            move = int(input("Your move: "))
            print()
        # reject if input is not an int
        except ValueError:
            print("Invalid entry.")
            continue

        # reject if player has selected a spot that is already occupied
        if not((move - 1) in available):
            print("That spot is unavailable.")
            continue
        else:
            break
    
    return move - 1


def who_goes_first():
    """Get and validate user preference for who plays first.
    @rtype: bool
    """
    while True:
        try:
            preference = str(input("Who should go first? (C)PU or (P)layer?"))
            print()
        # reject if input is not a string
        except ValueError:
            print("Invalid entry.")
            continue

        # reject if input is not c or p
        if not(preference == "C" or preference == "c" or preference == "P" or preference == "p"):
            print("Invalid entry")
            continue
        else:
            break

    return True if (preference == "C" or preference == "c") else False


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

    # ask user if they want to move first or second
    cpu_is_first = who_goes_first()

    # set of all corner spots and center of board (advantageous positions)
    options = [0, 2, 4, 6, 8]

    if cpu_is_first:
        print("CPU plays first.\n\n")
        time.sleep(DELAY)

        # cpu chooses random spot out of set of corner spots and center
        board[random.choice(options)] = "X"
        show_board(board)
        time.sleep(DELAY)
    else:
        # get player move
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
        evaluate.check_for_win(board)
        evaluate.check_for_tie(board)

        # cpu makes strategic move
        time.sleep(DELAY)
        print("CPU move:\n\n")
        time.sleep(DELAY)
        cpu_move = strategy.cpu_strategic_move(board)
        board[cpu_move] = "X"
        time.sleep(DELAY)
        print()
        show_board(board)

        # check if game is either won or tied
        evaluate.check_for_win(board)
        evaluate.check_for_tie(board)


if __name__ == '__main__':
    main()
