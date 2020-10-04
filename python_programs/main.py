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
        evaluate.check_for_win(board)
        check_for_tie(board)

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
        check_for_tie(board)


if __name__ == '__main__':
    main()
