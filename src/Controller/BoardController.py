import sys
sys.path.append("/home/jadamek/Sudoku/Development/src/Model")

from bottle import static_file, template
from Board import Board
import json

game_board = None

def play():
	game_board = Board(40)
	
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

def update(cell_id, value):
	pass

def status():
	pass
