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
