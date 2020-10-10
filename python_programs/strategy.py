import random
from evaluate import check_for_win


def cpu_strategic_move(board):
    """Determine optimal cpu move based on current state of board.
    @type board: list
    @rtype: int
    """
    possible_moves = [spot for spot in range(len(board)) if not(board[spot] == "X" or board[spot] == "O")]

    for letter in ["X", "O"]:
        for move in possible_moves:
            board_copy = board[:]
            board_copy[move] = letter
            if check_for_win(board_copy):
                return move

    good_spots = []
    for i in possible_moves:
        if i in [0, 2, 4, 6, 8]:
            good_spots.append(i)

    if 4 in good_spots:
        return 4

    if len(good_spots) > 0:
        return random.choice(good_spots)

    edge_spots = []
    for i in possible_moves:
        if i in [1, 3, 5, 7]:
            edge_spots.append(i)
    
    if len(edge_spots) > 0:
        return random.choice(edge_spots)
