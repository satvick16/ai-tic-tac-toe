import time


DELAY = 2


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
