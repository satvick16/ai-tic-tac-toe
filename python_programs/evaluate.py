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


def check_for_win(board):
    """Check board for whether someone has won yet.
    @type board: list
    @rtype: None
    """

    if board[0] == board[1] == board[2]:
        time.sleep(DELAY)
        return board[0]
    elif board[3] == board[4] == board[5]:
        time.sleep(DELAY)
        return board[3]
    elif board[6] == board[7] == board[8]:
        time.sleep(DELAY)
        return board[6]
    elif board[0] == board[3] == board[6]:
        time.sleep(DELAY)
        return board[0]
    elif board[1] == board[4] == board[7]:
        time.sleep(DELAY)
        return board[1]
    elif board[2] == board[5] == board[8]:
        time.sleep(DELAY)
        return board[2]
    elif board[0] == board[4] == board[8]:
        time.sleep(DELAY)
        return board[0]
    elif board[2] == board[4] == board[6]:
        time.sleep(DELAY)
        return board[2]
    else:
        return False
