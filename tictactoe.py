import random
import time


def show_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print(f"---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print(f"---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n\n")


def get_p_move(board):
    available = []

    for i in range(len(board)):
        if board[i] != "X" and board[i] != "O":
            available.append(i)

    while True:
        try:
            move = int(input("Your move: "))
        except ValueError:
            print("Invalid entry.")
            continue

        if not(move in available):
            print("That spot is unavailable.")
            continue
        else:
            break
    
    return move


def main():
    DELAY = 2

    board = [str(i) for i in range (0, 9)]

    print()
    show_board(board)
    time.sleep(DELAY)
    print("CPU plays first.\n\n")
    time.sleep(DELAY)

    options = [0, 2, 4, 6, 8]
    board[random.choice(options)] = "X"

    show_board(board)

    p_move = get_p_move(board)
    board[p_move] = "O"
    time.sleep(DELAY)
    print()
    show_board(board)
    time.sleep(DELAY)
    print("CPU move.\n\n")
    time.sleep(DELAY)

    new_options = []

    for option in options:
        if not(board[option] == "X" or board[option] == "O"):
            new_options.append(option)
    
    board[random.choice(new_options)] = "X"
    show_board(board)

    while True:
        pass


if __name__ == '__main__':
    main()
