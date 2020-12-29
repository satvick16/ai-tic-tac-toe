import random
import time
import evaluate
import strategy


DELAY = 1.5


def show_board(board):
    """
    Display well-formatted board in the console.
    :param board: a list containing the current state of the board
    """
    print("/-----------\\")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("|---+---+---|")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("|---+---+---|")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("\-----------/\n\n")


def get_p_move(board):
    """
    Get and validate user move based on current board state.
    :param board: a list containing the current state of the board
    :return: the integer index of the player's next move
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


def who_goes_first():
    """
    Get and validate user preference for who plays first.
    :return: True if player wants computer to go first
    """
    while True:
        try:
            preference = str(input("Who should go first? (C)PU or (P)layer: "))
            print()
        except ValueError:
            print("Invalid entry.")
            continue

        if not(preference == "C" or preference == "c" or preference == "P" or preference == "p"):
            print("Invalid entry.")
            continue
        else:
            break

    return True if (preference == "C" or preference == "c") else False


def check_if_game_over(board):
    """
    Check if game is a tie or someone has won yet and end game when necessary.
    :param board: a list containing the current state of the board
    """
    spam = evaluate.check_for_win(board)

    if spam == "X":
        print("CPU WINS!")
        exit()
    if spam == "O":
        print("YOU WIN!")
        exit()

    evaluate.check_for_tie(board)


def main():
    # declare 9x9 board
    board = [str(i) for i in range (1, 10)]
    
    # print welcome message
    print("\n~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to Tic Tac Toe!")
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(DELAY)
    print("\n")
    show_board(board)
    time.sleep(DELAY)

    # get user preference for who goes first
    cpu_is_first = who_goes_first()

    if cpu_is_first:
        # execute AI-driven strategic move for CPU
        print("CPU move:\n\n")
        time.sleep(DELAY)
        cpu_move = strategy.cpu_strategic_move(board)
        board[cpu_move] = "X"
        show_board(board)
        time.sleep(DELAY)
    
    while True:
        # get, validate and execute player move
        p_move = get_p_move(board)
        board[p_move] = "O"
        time.sleep(DELAY)
        print()
        show_board(board)

        # check if game is tied or someone has won
        check_if_game_over(board)
        time.sleep(DELAY)
        
        # execute AI-driven strategic move for CPU
        print("CPU move:\n\n")
        time.sleep(DELAY)
        cpu_move = strategy.cpu_strategic_move(board)
        board[cpu_move] = "X"
        time.sleep(DELAY)
        print()
        show_board(board)

        # check if game is tied or someone has won
        check_if_game_over(board)


if __name__ == '__main__':
    main()
