#Daniel Kalam 04/15/2019
import random
import sys
import json

sys.stderr.write("Connect Four - Python\n")

# This is fragile and relies on the fact that the driver always passes the
# command line arguments in the order --player <p> --width <w> --height <h>.
# {"grid":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]}
player = int(sys.argv[2]) # --player <p>
width = int(sys.argv[4]) # --width <w>
height = int(sys.argv[6]) # --height <h>
wwidth = width - 1
wheight = height - 1
if player == 1:
	opponent = 2
if player == 2:
	opponent = 1
# The variable moves is a list of lists of moves that prioritize connecting four pieces
moves = []
for i in range(6):
	moves.append([])
THREE_PIECES = 0 # Highest priority is getting four in a row which allows the player to win
INSTANT_LOSE = 1 # Second highest priority is preventing a immediate lose
UNBOUNDED_HORIZ = 2 # Prevent two pieces (placed horizontally) from not having a piece next to them
TWO_PIECES = 3 # Neutral priority is getting three in a row
ONE_PIECE = 4 # Second lowest priorty is placing two consecutive pieces
NO_PIECES = 5 # Lowest priority is placing one starting piece
	
sys.stderr.write("  player = " + str(player) + '\n')
sys.stderr.write("   width = " + str(width) + '\n')
sys.stderr.write("  height = " + str(height) + '\n')
sys.stderr.write("opponent = " + str(opponent) + '\n')

def valid_moves(grid):
	"""Returns the valid moves for the state as a list of integers."""
	openmoves = []
	for i in range(width):
		if grid[i][0] == 0:
			openmoves.append(i)
	#for j in range(height):
		#print('|', end = '')
		#for i in range(width):
			#print(str(grid[i][j]), end = '|')
		#print()
	return openmoves
	
#Todo evaluate moves above the lowest empty space to prevent future wins
def evaluate_moves(openmoves, grid):
	for i in openmoves:
		for j in range(height):
			if grid[i][j] != 0: # Column is not empty
				check_ways(i, j - 1, grid)
				break
			elif j == wheight and grid[i][j] == 0: # Column is empty
				check_ways(i, j, grid)
				break

def check_ways(x, y, grid):
	downrow = []
	leftrow = []
	rightrow = []
	leftup = []
	rightup = []
	leftdown = []
	rightdown = []
	for i in range(y + 1, height):
		downrow.append(grid[x][i])
		if i > (y + 1):
			if pastpiece != grid[x][i]:
				del downrow[-1]
				break
		pastpiece = grid[x][i]

	for i in range(x - 1, -1, -1):
		if grid[i][y] != 0:
			leftrow.append(grid[i][y])
		elif len(leftrow) == 2 and grid[i][y] == 0:
			leftrow.append(grid[i][y])
			break
		if i < (x - 1):
			if pastpiece != grid[i][y]:
				del leftrow[-1]
				break
		pastpiece = grid[i][y]

	for i in range(x + 1, width):
		if grid[i][y] != 0:
			rightrow.append(grid[i][y])
		elif len(rightrow) == 2 and grid[i][y] == 0:
			rightrow.append(grid[i][y])
			break
		if i > (x + 1):
			if pastpiece != grid[i][y]:
				if grid[i][y] != 0:
					del rightrow[-1]
				else:
					rightrow.append(grid[i][y])
				break
		pastpiece = grid[i][y]

	for i in range(1, 4): # Only need to check for at most three pieces
		if (y - i) <= 0 or (x - i) <= 0:
			break
		if grid[x - i][y - i] != 0:
			leftup.append(grid[x - i][y - i])	
		else:
			break
		if i > 1:
			if pastpiece != grid[x - i][y - i]:
				del leftup[-1]
				break
		pastpiece = grid[x - i][y - i]

	for i in range(1, 4):
		if (x + i) >= width or (y - i) <= 0:
			break
		if grid[x + i][y - i] != 0:
			rightup.append(grid[x + i][y - i])
		else:
			break;
		if i > 1:
			if pastpiece != grid[x + i][y - i]:
				del rightup[-1]
				break
		pastpiece = grid[x + i][y - i]

	for i in range(1, 4):
		if (x - i) <= 0 or (y + i) >= height:
			break
		if grid[x - i][y + i] != 0:
			leftdown.append(grid[x - i][y + i])
		else:
			break
		if i > 1:
			if pastpiece != grid[x - i][y + i]:
				del leftdown[-1]
				break
		pastpiece = grid[x - i][y + i]

	for i in range(1, 4):
		if (x + i) >= width or (y + i) >= height:
			break
		if grid[x + i][y + i] != 0:
			rightdown.append(grid[x + i][y + i])
		else:
			break
		if i > 1:
			if pastpiece != grid[x + i][y + i]:
				del rightdown[-1]
				break
		pastpiece = grid[x + i][y + i]
	
	#print('y = ' + str(y) + '\n')
	#print('x = ' + str(x) + '\n')
	#print('leftup = ' + str(leftup) + '\n')
	#print('rightup = ' + str(rightup) + '\n')
	#print('leftrow = ' + str(leftrow) + '\n')
	#print('rightrow = ' + str(rightrow) + '\n')
	#print('leftdown = ' + str(leftdown) + '\n')
	#print('downrow = ' + str(downrow) + '\n')
	#print('rightdown = ' + str(rightdown) + '\n')
	row_weight(x, downrow, [])
	row_weight(x, leftrow, rightrow)
	row_weight(x, leftup, rightdown)
	row_weight(x, leftdown, rightup)
	del downrow[:]
	del leftrow[:]
	del rightrow[:]
	del leftup[:]
	del rightup[:]
	del leftdown[:]
	del rightdown[:]

def row_weight(x, row1, row2):
	if len(row1) == 0:
		moves[NO_PIECES].append(x)
	elif len(row1) > 0:
		if row1[0] == player:
			if len(row1) >= 3 and row1[len(row1) - 1] != 0:
				moves[THREE_PIECES].append(x)
			if len(row1) == 2:
				moves[TWO_PIECES].append(x)
			if len(row1) == 1:
				moves[ONE_PIECE].append(x)
		elif len(row1) == 3 and row1[0] == opponent and row1[len(row1) - 1] != 0:
			moves[INSTANT_LOSE].append(x)
		if row1[len(row1)-1] == 0:
			del row1[-1]
			moves[UNBOUNDED_HORIZ].append(x)
	if len(row2) == 0:
		moves[NO_PIECES].append(x)
	elif len(row2) > 0:
		if row2[0] == player:
			if len(row2) >= 3 and row2[len(row2) - 1] != 0:
				moves[THREE_PIECES].append(x)
			if len(row2) == 2:
				moves[TWO_PIECES].append(x)
			if len(row2) == 1:
				moves[ONE_PIECE].append(x)
		elif len(row2) == 3 and row2[0] == opponent and row2[len(row2) - 1] != 0:
			moves[INSTANT_LOSE].append(x)
		if row2[len(row2)-1] == 0:
			del row2[-1]
			moves[UNBOUNDED_HORIZ].append(x)
	if len(row1) > 0 and len(row2) > 0:
		if row1[0] == row2[0]:
			row1 = row1 + row2
			if row1[0] == player:
				if len(row1) >= 3:
					moves[THREE_PIECES].append(x)
				if len(row1) == 2:
					moves[TWO_PIECES].append(x)
				if len(row1) == 1:
					moves[ONE_PIECE].append(x)
			elif len(row1) == 3 and row1[0] == opponent:
				moves[INSTANT_LOSE].append(x)
# Loop reading the state from the driver and writing a random valid move.
for line in sys.stdin:
	for i in range(6): # Empty all of the moves per turn
		del moves[i][:]
	sys.stderr.write(line)
	state = json.loads(line)
	action = {}
	grid = state['grid']
	openmoves = valid_moves(grid)
	#print('openmoves = ' + str(openmoves) + '\n')
	evaluate_moves(openmoves, grid)
	#for i in range(6):
		#print('moves[' + str(i) + '] = ' + str(moves[i]) + '\n')
	for i in range(6): # Iterate through the lists of prioritized moves and choose randomly from one of those lists
		if moves[i]:
			action['move'] = random.choice(moves[i])
			break # Only one move is desired

	msg = json.dumps(action)
	sys.stderr.write(msg + '\n')
	sys.stdout.write(msg + '\n')
	sys.stdout.flush()

# Be a nice program and close the ports.
sys.stdin.close()
sys.stdout.close()
sys.stderr.close()
