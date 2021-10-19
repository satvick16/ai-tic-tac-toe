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

    lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
             [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for line in lines:
        if board[line[0]] == board[line[1]] == board[line[2]]:
            time.sleep(DELAY)
            return board[line[0]]

    return False
