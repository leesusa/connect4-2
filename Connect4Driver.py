import json


height = 6
width = 7
# grid[column][row]
grid = [[0 for y in range(height)] for x in range(width)]
grid[5][3] = 1


exe_1 = "connect-four-naive"
args_1 = []
exe_2 = "connect-four-naive"
args_2 = []


# create new grid
def new_grid(grid, move, player):
    print("")


# check for win or draw
# returns true if player has won
def is_winner(grid, player):
    # check horizontal options
    for c in range(width - 3):
        for r in range(height):
            if grid[r][c] == player and grid[r][c+1] == player and grid[r][c+2] == player and grid[r][c+3] == player:
                return True
    # check vertical options
    for c in range(width):
        for r in range(height - 3):
            if grid[r][c] == player and grid[r+1][c] == player and grid[r+2][c] == player and grid[r+3][c] == player:
                return True
    # check diagonal options
    # positively sloped
    for c in range(width - 3):
        for r in range(height - 3):
            if grid[r][c] == player and grid[r+1][c+1] == player and grid[r+2][c+2] == player and grid[r+3][c+3] == player:
                return True
    # negatively sloped
    for c in range(width - 3):
        for r in range(3, height):
            if grid[r][c] == player and grid[r-1][c+1] == player and grid[r-2][c+2] == player and grid[r-3][c+3] == player:
                return True
    return False


# check for draw
def is_draw(grid):
    print("")

# print grid
def print_grid(grid):
    for row in range(0, height):
        for column in range(0, width):
            print(grid[column][row], end=" ")
        print()


# main loop
def main():
    print_grid(grid)
    # create ports for standard error (text) files
    # create subprocesses
    # create vector of standard ports
    # game loop and alternate players called
    done = False
    # player refers to current player's whose turn it is
    # make sure this is randomized
    player = 1
    while not done:
        # send grid to player
        # get returned value
        # check value
        # print grid / move / player
        # check for winner
        if is_winner(grid, player) or is_draw(grid):
            done = True
            # output winner / draw data
    # close ports


main()
