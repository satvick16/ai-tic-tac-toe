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
            print()
        except ValueError:
            print("Invalid entry.")
            continue

        if not(move in available):
            print("That spot is unavailable.")
            continue
        else:
            break
    
    return move


def check_board(board):
    if board[0] == board[1] == board[2]:
        return True
    elif board[3] == board[4] == board[5]:
        return True
    elif board[6] == board[7] == board[8]:
        return True
    elif board[0] == board[3] == board[6]:
        return True
    elif board[1] == board[4] == board[7]:
        return True
    elif board[2] == board[5] == board[8]:
        return True
    elif board[0] == board[4] == board[8]:
        return True
    elif board[2] == board[4] == board[6]:
        return True
    else:
        return False


def cpu_strategic_move(board):
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
    #######################################################
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


def check_for_tie(board):
    available = []

    for i in range(len(board)):
        if i != "X" and i != "O":
            available.append(i)
    
    if len(available) == 0:
        return True
    else:
        return False


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
        p_move = get_p_move(board)
        board[p_move] = "O"
        time.sleep(DELAY)
        print()
        show_board(board)

        game_is_over = check_board(board)
        if game_is_over:
            break

        game_is_tie = check_for_tie(board)
        if game_is_tie:
            print("Tie!")
            break

        time.sleep(DELAY)
        print("CPU move.\n\n")
        time.sleep(DELAY)

        cpu_move = cpu_strategic_move(board)
        board[cpu_move] = "X"
        time.sleep(DELAY)
        print()
        show_board(board)

        game_is_over = check_board(board)
        if game_is_over:
            break

        game_is_tie = check_for_tie(board)
        if game_is_tie:
            print("Tie")
            break


if __name__ == '__main__':
    main()
