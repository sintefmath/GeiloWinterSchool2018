import random
import itertools as it
import numpy as np


def winner_horizontal(board):
    # Rows where all entries are equal to 1 or 2
    max = np.max(board, axis=1)
    min = np.min(board, axis=1)
    indices = np.where((max == min) & (min > 0))[0]

    # If there are any, return
    for i in indices:
        return board[i,0]

    # Check for draw
    if (board > 0).all():
        return -1

    return None


_check = [
    (0,3,6,0,1,2,0,2),
    (1,4,7,3,4,5,4,4),
    (2,5,8,6,7,8,8,6),
]
def winner(board):
    i, j, k = _check
    board = np.array([board[(i,)], board[(j,)], board[(k,)]]).T
    return winner_horizontal(board)


def moves(board):
    return np.where(board == 0)[0]


def make_move(board, i, player):
    board = np.copy(board)
    board[i] = player
    return board


def fork(board, player):
    nwins = 0
    for i in moves(board):
        if winner(make_move(board, i, player)) == player:
            nwins += 1
    return nwins >= 2


def tictactoe1(board, player):
    other = 3 - player
    available_moves = moves(board)
    corner_moves = [i for i in available_moves if i in {0,2,6,8}]
    side_moves = [i for i in available_moves if i in {1,3,5,7}]

    # Try to find a winning move
    for i in available_moves:
        if winner(make_move(board, i, player)) == player:
            return i

    # Try to block a winning move by the opponent
    for i in available_moves:
        if winner(make_move(board, i, other)) == other:
            return i

    # Pick a random move from the corners
    if corner_moves:
        return random.choice(corner_moves)

    # Pick the center, if it is free
    if 4 in available_moves:
        return 4

    # Pick one of the sides
    return random.choice(side_moves)


def tictactoe2(board, player):
    other = 3 - player
    available_moves = moves(board)
    corner_moves = [i for i in available_moves if i in {0,2,6,8}]
    side_moves = [i for i in available_moves if i in {1,3,5,7}]

    # Try to find a winning move
    for i in available_moves:
        if winner(make_move(board, i, player)) == player:
            return i

    # Try to block a winning move by the opponent
    for i in available_moves:
        if winner(make_move(board, i, other)) == other:
            return i

    # Try to find a forking move
    for i in available_moves:
        if fork(make_move(board, i, player), player):
            return i

    # Find possible forking moves by the opponent
    for i in available_moves:
        if fork(make_move(board, i, other), other):
            return i

    # Pick a random move from the corners
    if corner_moves:
        return random.choice(corner_moves)

    # Pick the center, if it is free
    if 4 in available_moves:
        return 4

    # Pick one of the sides
    return random.choice(side_moves)


def tictactoe3(board, player):
    other = 3 - player
    available_moves = moves(board)
    corner_moves = [i for i in available_moves if i in {0,2,6,8}]
    side_moves = [i for i in available_moves if i in {1,3,5,7}]

    # Try to find a winning move
    for i in available_moves:
        if winner(make_move(board, i, player)) == player:
            return i

    # Try to block a winning move by the opponent
    for i in available_moves:
        if winner(make_move(board, i, other)) == other:
            return i

    # Try to find a forking move
    for i in available_moves:
        if fork(make_move(board, i, player), player):
            return i

    # Find possible forking moves by the opponent
    nforks = 0
    blocking_move = None
    for i in available_moves:
        if fork(make_move(board, i, other), other):
            nforks += 1
            blocking_move = i

    # If just one, block it. Otherwise force a block by the opponent by playing the side
    if nforks == 1:
        return blocking_move
    elif nforks == 2 and side_moves:
        return random.choice(side_moves)

    # Pick the center, if it is free
    if 4 in available_moves:
        return 4

    # Pick a random move from the corners
    if corner_moves:
        return random.choice(corner_moves)

    # Pick one of the sides
    return random.choice(side_moves)


def monkey(board, player):
    return random.choice(moves(board))


def fight(ai1, ai2, n=10):
    occ = [0, 0, 0]

    for p1, p2, loc in [(ai1, ai2, [-1, 1, 2]), (ai2, ai1, [-1, 2, 1])]:
        for _ in range(n):
            board = np.zeros(9, dtype=np.int8)
            for ai, player in it.cycle([(p1, 1), (p2, 2)]):
                i = ai(board, player)
                board = make_move(board, i, player)
                win = winner(board)
                if win:
                    occ[loc.index(win)] += 1
                    break

    print(f'Draw: {occ[0]}, {ai1.__name__} wins: {occ[1]}, {ai2.__name__} wins: {occ[2]}')
