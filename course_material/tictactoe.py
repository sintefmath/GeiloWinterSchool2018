import random
import itertools as it


def winner_horizontal(board):
    for row in board:
        if all(r == 'X' for r in row):
            return 'X'
        elif all(r == 'O' for r in row):
            return 'O'
    if all(r is not None for r in row for row in board):
        return 'D'
    return None


def winner(board):
    board = board + list(zip(*board)) + [
        [board[i][i] for i in range(3)],
        [board[i][2-i] for i in range(3)],
    ]
    return winner_horizontal(board)


def moves(board):
    return [(i,j) for i in range(3) for j in range(3) if board[i][j] is None]


def make_move(board, i, j, player):
    board = [list(row) for row in board]
    board[i][j] = player
    return board


def fork(board, player):
    nwins = 0
    for i, j in moves(board):
        if winner(make_move(board, i, j, player)) == player:
            nwins += 1
    return nwins >= 2


def tictactoe1(board, player):
    other = 'X' if player == 'O' else 'O'
    available_moves = moves(board)
    corner_moves = [(i, j) for i, j in available_moves if i in {0,2} and j in {0,2}]
    side_moves = [m for m in available_moves if m not in corner_moves and m != (1,1)]

    # Try to find a winning move
    for i, j in available_moves:
        if winner(make_move(board, i, j, player)) == player:
            return i, j

    # Try to block a winning move by the opponent
    for i, j in available_moves:
        if winner(make_move(board, i, j, other)) == other:
            return i, j

    # Pick a random move from the corners
    if corner_moves:
        return random.choice(corner_moves)

    # Pick the center, if it is free
    if (1, 1) in available_moves:
        return (1, 1)

    # Pick one of the sides
    return random.choice(side_moves)


def tictactoe2(board, player):
    other = 'X' if player == 'O' else 'O'
    available_moves = moves(board)
    corner_moves = [(i, j) for i, j in available_moves if i in {0,2} and j in {0,2}]
    side_moves = [m for m in available_moves if m not in corner_moves and m != (1,1)]

    # Try to find a winning move
    for i, j in available_moves:
        if winner(make_move(board, i, j, player)) == player:
            return i, j

    # Try to block a winning move by the opponent
    for i, j in available_moves:
        if winner(make_move(board, i, j, other)) == other:
            return i, j

    # Try to find a forking move
    for i, j in available_moves:
        if fork(make_move(board, i, j, player), player):
            return i, j

    # Find possible forking moves by the opponent
    for i, j in available_moves:
        if fork(make_move(board, i, j, other), other):
            return i, j

    # Pick a random move from the corners
    if corner_moves:
        return random.choice(corner_moves)

    # Pick the center, if it is free
    if (1, 1) in available_moves:
        return (1, 1)

    # Pick one of the sides
    return random.choice(side_moves)


def tictactoe3(board, player):
    other = 'X' if player == 'O' else 'O'
    available_moves = moves(board)
    corner_moves = [(i, j) for i, j in available_moves if i in {0,2} and j in {0,2}]
    side_moves = [m for m in available_moves if m not in corner_moves and m != (1,1)]

    # Try to find a winning move
    for i, j in available_moves:
        if winner(make_move(board, i, j, player)) == player:
            return i, j

    # Try to block a winning move by the opponent
    for i, j in available_moves:
        if winner(make_move(board, i, j, other)) == other:
            return i, j

    # Try to find a forking move
    for i, j in available_moves:
        if fork(make_move(board, i, j, player), player):
            return i, j

    # Find possible forking moves by the opponent
    nforks = 0
    blocking_move = None
    for i, j in available_moves:
        if fork(make_move(board, i, j, other), other):
            nforks += 1
            blocking_move = (i, j)

    # If just one, block it. Otherwise force a block by the opponent by playing the side
    if nforks == 1:
        return blocking_move
    elif nforks == 2 and side_moves:
        return random.choice(side_moves)

    # Pick the center, if it is free
    if (1, 1) in available_moves:
        return (1, 1)

    # Pick a random move from the corners
    if corner_moves:
        return random.choice(corner_moves)

    # Pick one of the sides
    return random.choice(side_moves)


def monkey(board, player):
    return random.choice(moves(board))


def fight(ai1, ai2, n=10):
    occ = [0, 0, 0]
    start = [[None] * 3] * 3

    for p1, p2, loc in [(ai1, ai2, 'DXO'), (ai2, ai1, 'DOX')]:
        for _ in range(n):
            board = [list(row) for row in start]
            for ai, player in it.cycle([(p1, 'X'), (p2, 'O')]):
                i, j = ai(board, player)
                board = make_move(board, i, j, player)
                win = winner(board)
                if win:
                    occ[loc.index(win)] += 1
                    break

    print(f'Draw: {occ[0]}, {ai1.__name__} wins: {occ[1]}, {ai2.__name__} wins: {occ[2]}')
