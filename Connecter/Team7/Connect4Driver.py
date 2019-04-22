import json
import random
import subprocess
import sys


height = 6
width = 7
# grid[column][row]
grid = [[0 for y in range(height)] for x in range(width)]

'''
# fake game state
grid[5][5] = 1
grid[5][4] = 1
grid[5][3] = 1
grid[5][2] = 1
grid[1][5] = 2
grid[2][5] = 2
grid[3][5] = 2
grid[4][5] = 2
'''

# exes and args
exe_1 = "/Users/Dood/Desktop/Connecter/Team7/connect-four-naive"
args_1 = []
exe_2 = "/Users/Dood/Desktop/Connecter/Team8/dist/main"
args_2 = []
'''
exe_2 = "/Applications/python3.7"
args_2 = ["/Users/Dood/Desktop/Team8/main.py"]
'''


# create new grid
def new_grid(grid, move, player):
    print("")


# check for win or draw
# returns true if player has won
def is_winner(grid, player):
    # check horizontal options
    for c in range(width - 3):
        for r in range(height):
            if grid[c][r] == player and grid[c+1][r] == player and grid[c+2][r] == player and grid[c+3][r] == player:
                return True
    # check vertical options
    for c in range(width):
        for r in range(height - 3):
            if grid[c][r] == player and grid[c][r+1] == player and grid[c][r+2] == player and grid[c][r+3] == player:
                return True
    # check diagonal options
    # positively sloped
    for c in range(width - 3):
        for r in range(height - 3):
            if grid[c][r] == player and grid[c+1][r+1] == player and grid[c+2][r+2] == player and grid[c+3][r+3] == player:
                return True
    # negatively sloped
    for c in range(width - 3):
        for r in range(3, height):
            if grid[c][r] == player and grid[c+1][r-1] == player and grid[c+2][r-2] == player and grid[c+3][r-3] == player:
                return True
    return False


# check for draw
def is_draw(grid, move):
    # make sure there are no winners!
    if is_winner(grid, 1):
        return False
    if is_winner(grid, 2):
        return False
    # if grid is completely full... it is a draw!
    if width*height == move:
        return True
    return False

def is_valid_move(move, player):
    for r in range(height-1, -1, -1):
        if grid[move][r] != 1 and grid[move][r] != 2:
            grid[move][r] = player
            return True
    return False
            

# print grid
def print_grid(grid):
    for row in range(0, height):
        for column in range(0, width):
            print(grid[column][row], end=" ")
        print()

# get the next player
def next_player(player):
    if player == 1:
        player = 2
    else:
        player = 1
    return player

# main loop
def main():
    #print_grid(grid)
    # create ports for standard error (text) files
    args_1 = ["--player", "1", "--width", str(width), "--height", str(height)]
    args_2 = ["--player", "2", "--width", str(width), "--height", str(height)]
    # create subprocesses and open stderr files
    process1 = subprocess.Popen([exe_1]+args_1,
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=open("connect-four-stderr-1.txt", "w"),
                                universal_newlines=True)
    process2 = subprocess.Popen([exe_2]+args_2,
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=open("connect-four-stderr-2.txt", "w"),
                                universal_newlines=True)
    '''
    process1 = subprocess.Popen(args=args_1, executable=exe_1,
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=open("connect-four-stderr-1.txt", "w"),
                                universal_newlines=True)
    process2 = subprocess.Popen(args=args_2, executable=exe_2,
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=open("connect-four-stderr-2.txt", "w"),
                                universal_newlines=True)
    '''
    # create vector of standard port
    # game loop and alternate players called
    done = False
    winner = 0
    move = 1
    draw = False
    # player refers to current player's whose turn it is
    # make sure this is randomized
    player = random.randint(1, 2)
    while not done:
        # create json expression for the grid
        json_grid = json.dumps(json.JSONEncoder().encode({"grid": grid}))
        # send grid to appropriate player
        #print_grid(grid)
        if player == 1:
            print("player 1 processing")
            process1.stdin.write(json.JSONEncoder().encode({"grid": grid}) + '\n')
            process1.stdin.flush()
            response = process1.stdout.readline()
            response = json.JSONDecoder().decode(response)
            process1.stdout.flush()

        if player == 2:
            print("player 2 processing")
            process2.stdin.write(json.JSONEncoder().encode({"grid": grid}) + '\n')
            process2.stdin.flush()
            response = process2.stdout.readline()
            response = json.JSONDecoder().decode(response)
            process2.stdout.flush()

        # check value
        if not is_valid_move(response['move'], player):
            print("Invalid move")
        else:
            # increment number of valid moves
            move += 1
            # check for winner
            # output winner / draw data
            if is_winner(grid, player):
                done = True
                winner = player
                print("The winner is %d" % player)
            elif is_draw(grid, move):
                done = True
                draw = True
                print("The game ends in a draw")
            player = next_player(player)
    print_grid(grid)
    # close ports
    


main()
