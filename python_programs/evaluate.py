import time


DELAY = 2


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


def check_for_win(board, letter):
    """Check board for whether someone has won yet.
    @type board: list
    @rtype: None
    """

    if letter == "X":
        msg = "CPU WINS!"
    else:
        msg = "YOU WIN!"

    # check if someone has won
    if board[0] == board[1] == board[2] == letter:
        print(msg)
        time.sleep(DELAY)
        exit()
    elif board[3] == board[4] == board[5] == letter:
        print(msg)
        time.sleep(DELAY)
        exit()
    elif board[6] == board[7] == board[8] == letter:
        print(msg)
        time.sleep(DELAY)
        exit()
    elif board[0] == board[3] == board[6] == letter:
        print(msg)
        time.sleep(DELAY)
        exit()
    elif board[1] == board[4] == board[7] == letter:
        print(msg)
        time.sleep(DELAY)
        exit()
    elif board[2] == board[5] == board[8] == letter:
        print(msg)
        time.sleep(DELAY)
        exit()
    elif board[0] == board[4] == board[8] == letter:
        print(msg)
        time.sleep(DELAY)
        exit()
    elif board[2] == board[4] == board[6] == letter:
        print(msg)
        time.sleep(DELAY)
        exit()
    else:
        pass
