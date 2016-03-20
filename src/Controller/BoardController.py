import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../Model")

from bottle import static_file, template
from Board import Board
import json

# Make this a Session variable.
game_board = None

#----------------------------------------------------------------
def play():
#----------------------------------------------------------------
# Creates a new sudoku board and returns a template displaying it
#----------------------------------------------------------------
	game_board = Board(40, False)
	
	raw_map = game_board.getRaw()
	board_map = {}

	# Translate raw 2-D digit/None array into coord : number
	# mapping. Blank (solvable) cells are simply excluded
	# from the map.
	for y in range(9):	
		for x in range(9):
			if raw_map[y][x] != None:
				id = chr(ord('a')+y) + str(x+1)
				board_map[id] = raw_map[y][x]

	return template('index', board = board_map)

#----------------------------------------------------------------
def update(cell_id, value):
#----------------------------------------------------------------
# * cell_id : the character-int pair (row-column) where the guess
#	was made.
# * value : the user's guess (1~9) for the cell's solution.
# Submits a user's input to the board.
# Returns True if the guess was correct, and False otherwise.
#----------------------------------------------------------------
	if game_board is not None:
		# Translate coordinates back to 2-D array.
		x = int(cell_id[1]) - 1
		y = ord(cell_id[0]) - ord('a')

		answer = int(value)
		
		# Submit the user's answer to the board.
		correct = game_board.submitAnswer(x, y, answer)

		return correct

#----------------------------------------------------------------
def status():
#----------------------------------------------------------------
	pass
