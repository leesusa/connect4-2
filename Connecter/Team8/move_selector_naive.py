import random


def validMoveRow(grid, col):
    '''
    Validates that a column has an available space on the game board by checking
        top row for empty (row-major format)
    :param col: column number
    :return: True if column top row is empty, otherwise False
    '''
    if grid[0][col] == 0:
        return True
    return False


def validMoveCol(grid, col):
    '''
    Validates that a column has an available space on the game board by checking
        top row for empty (column-major format)
    :param col: column number
    :return: True if column top row is empty, otherwise False
    '''
    if grid[col][0] == 0:
        return True
    return False


def randMove(gridObj):
    '''
    Generates a random column number in which to drop a game piece
    :param grid: game board
    :return: valid column number for move
    '''
    valid = False
    while not valid:
        col = random.randint(0, gridObj.width - 1)
        if validMoveRow(gridObj.grid, col):
            valid = True
    return col