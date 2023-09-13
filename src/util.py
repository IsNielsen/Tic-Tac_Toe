# Isaac Nielsen 
# CS1440 - ****
# Assn1

"""
##   misc, low level funcions
*    functions dont need import statements
*    Some functions must be modified to change representation of game board
*    do not print or take input directly from user
"""


def black(s):
    return "\x1b[1;30m{}\x1b[0m".format(s)


def red(s):
    return "\x1b[1;31m{}\x1b[0m".format(s)


def green(s):
    return "\x1b[1;32m{}\x1b[0m".format(s)


def yellow(s):
    return "\x1b[1;33m{}\x1b[0m".format(s)


def blue(s):
    return "\x1b[1;34m{}\x1b[0m".format(s)


def magenta(s):
    return "\x1b[1;35m{}\x1b[0m".format(s)


def cyan(s):
    return "\x1b[1;36m{}\x1b[0m".format(s)


def white(s):
    return "\x1b[1;37m{}\x1b[0m".format(s)


def color(s):
    if s == 'X':
        return red(s)
    elif s == 'O':
        return cyan(s)
    else:
        return white(s)


def home():
    """return cursor to home position (upper left corner)"""
    print(end="\x1b[H")


def clear():
    """clear the screen and return cursor to home position"""
    print(end="\x1b[H\x1b[J", flush=True)


# def pos_to_rowcol(position):
#     """
#     Given a TicTacToe board position (int),
#     Return a tuple(row, col)
#
#     Inverse of the function rowcol_to_pos()
#     """
#     cell = position - 1
#     row = cell // 3
#     col = cell % 3
#     return row, col
#
#
# def rowcol_to_pos(rowcol):
#     """
#     Given a row and column (as a tuple)
#     Return a TicTacToe board position (int)
#
#     Inverse of the function pos_to_rowcol()
#     """
#     row = rowcol[0]
#     col = rowcol[1]
#     pos = row * 3 + col
#     return pos + 1


def vertical_winner(board):
    """
    Determines which player has won a game with a vertical triple
    """
    return (board[0][0] == board[0][3] == board[0][6] and board[0][6]) \
        or (board[0][1] == board[0][4] == board[0][7] and board[0][7]) \
        or (board[0][2] == board[0][5] == board[0][8] and board[0][8])


def diagonal_winner(board):
    """
    Determines which player has won a game with a diagonal triple
    """
    return (board[0][0] == board[0][4] == board[0][8] and board[0][8]) \
        or (board[0][6] == board[0][4] == board[0][2] and board[0][2])


def horizontal_winner(board):
    """
    Determines which player has won a game with a horizontal triple.
    Input: a 2D game board.
    Return: 'X' or 'O' when there is a winner, or False when no player has 3 in
    a horizontal row

    The code we arrived at borders on being too clever for our own good, and
    bears some explanation.

    The first line checks whether the three cells in the top row are all the
    same.  This is ONLY true when the same player has played their mark there.
    The `and` conjunction at the end of each sub-clause might look useless, but
    is very important.  It returns the letter of the winning player:
        https://docs.python.org/3/reference/expressions.html#boolean-operations

    Without it, this function could only return 'True' or 'False', merely
    indicating that SOMEBODY won the game instead of stating who the winner is.
    """
    return (board[0][0] == board[0][1] == board[0][2] and board[0][2]) \
        or (board[0][3] == board[0][4] == board[0][5] and board[0][5]) \
        or (board[0][6] == board[0][7] == board[0][8] and board[0][8])


def winner(board):
    """
    Returns the winner of the game (if any), or False when there is no winner
    """
    return horizontal_winner(board) or vertical_winner(board) or diagonal_winner(board)


def open_cells(board):
    """ Returns a tuple of the unmarked cells in a Tic-Tac-Toe board """
    openings = []
    for p in board[0]:
        if type(p) is int:
            openings.append(p)
    return tuple(openings)


def first_open_cell(board):
    """ Return the ID of the first unmarked cell in a Tic-Tac-Toe board """
    cells = open_cells(board)
    if cells != []:
        return cells[0]
    else:
        return None


# def open_cells(board):
#     """ Returns a tuple of the unmarked cells in a Tic-Tac-Toe board """
#     openings = []
#     for row in range(len(board)):
#         for col in range(len(board[row])):
#             if board[row][col] != 'X' and board[row][col] != 'O':
#                 # convert (row,col) into a number
#                 openings.append(rowcol_to_pos(tuple([row, col])))
#     return tuple(openings)
#
#
# def first_open_cell(board):
#     """ Return the ID of the first unmarked cell in a Tic-Tac-Toe board """
#     cells = open_cells(board)
#     if cells != []:
#         return cells[0]
#     else:
#         return None


def full(board):
    return open_cells(board) == ()


def make_board():
    """
    A board is a 3-tuple of 3-tuples, where each tuple is one row
    it is not acutally, make it a 1D tuple
    """
    return tuple([range(1, 10)])
    # return tuple([tuple([1, 2, 3]),
    #               tuple([4, 5, 6]),
    #               tuple([7, 8, 9])])
