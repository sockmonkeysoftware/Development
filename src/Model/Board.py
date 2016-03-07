from Cell import Cell
import random

#================================================================
class Board:
#================================================================
# Methods
	#--------------------------------------------------------
	# - Board Constuctor
	#--------------------------------------------------------
	# * solutions : number of cells to leave as unsolved.
	#--------------------------------------------------------
	def __init__(self, solutions):
		solutions = max(1, min(80, solutions))

		self.board_ = self.generate(solutions)
		self.unsolved_ = solutions
		self.incorrect_ = solutions

	#--------------------------------------------------------
	# - Get Raw Board Array
	#--------------------------------------------------------
	# returns the current solution to the board as a raw
	# array of integers. A value of -1 represents NONE, or a
	# currently unsolved cell.
	#--------------------------------------------------------
	def getRaw(self):
		answers = []

		for row in range(0, 9):
			answers.append([])

			for column in range(0, 9):
				answers[row].append(self.board_[row][column].getAnswer())

		return answers

	#--------------------------------------------------------
	# - Generate Game Board
	#--------------------------------------------------------
	# * solutions : number of cells to leave as unsolved.
	# creates a valid Sudoku board with some cells left
	# unsolved and mutable, and the rest answered.
	#--------------------------------------------------------
	def generate(self, solutions):
		board = []
		random.seed()

		# Generate each row
		for row in range(0, 9):
			board.append([])

			# Generate each cell
			for column in range(0, 9):
				cell = Cell(random.randint(1, 9))
				board[row].append(cell)

		# Randomly hide given solutions		
		while solutions > 0:
			row = random.randint(0, 8)
			column = random.randint(0, 8)
			
			if not board[row][column].isMutable():
				board[row][column].hideAnswer()
				solutions -= 1

		return board

	#--------------------------------------------------------
	# - Get Row
	#--------------------------------------------------------
	# * index : the row's index, counting top to bottom
	# returns a single 9-item row on the game board.
	# In a correct solution, each number should be unique.
	#--------------------------------------------------------
	def getRow(self, index):
		if index not in range(0, 9):
			return None
		else:
			return self.board_[index]

	#--------------------------------------------------------
	# - Get Column
	#--------------------------------------------------------
	# * index : the column's index, counting left to right
	# returns a single 9-item column on the game board.
	# In a correct solution, each number should be unique.
	#--------------------------------------------------------
	def getColumn(self, index):
		if index not in range(0, 9):
			return None
		else:
			return [self.board_[row][index] for row in range(0, 9)]

	#--------------------------------------------------------
	# - Get 3x3 Block
	#--------------------------------------------------------
	# * x : the major column, counting left to right
	# * y : the major row, counting top to bottom
	# returns a 9-item 3x3 block on the board.
	# In a correct solution, each number should be unique.
	#--------------------------------------------------------
	def getBlock(self, x, y):
		if x not in range(0, 3) or y not in range(0, 3):
			return None
		else:
			return [self.board_[row + y * 3][3 * x : 3 * x + 3] for row in range(0, 3)]

	#--------------------------------------------------------
	# - Get Individual Cell
	#--------------------------------------------------------
	# * x : the column or x-coordinate, from left to right
	# * y : the row or y-cooridnate, from top to bottom
	# returns the exact Cell located at (x, y)
	#--------------------------------------------------------
	def getCell(self, x, y):
		if x not in range(0, 9) or y not in range(0, 9):
			return None
		else:
			return self.board_[y][x]

	#--------------------------------------------------------
	# - Submit Answer to Cell
	#--------------------------------------------------------
	# * x : the column or x-coordinate, from left to right
	# * y : the row or y-cooridnate, from top to bottom
	# * answer : the answer guessed by the user.
	# sets the cell's given answer to the user's guess, and	
	# increments/decrements the number of cells yet to be
	# solved if the answer was incorrect/correct.
	# returns True if the user's guess was correct.
	#--------------------------------------------------------
	def submitAnswer(self, x, y, answer):
		if x not in range(0, 9) or y not in range(0, 9) or answer not in range(1, 10):
			return None
		else:
			self.unsolved_ -= 1
			oldStatus = self.board_[y][x].isCorrect()
			correct = self.board_[y][x].submitAnswer(answer)
			
			self.incorrect_ += oldStatus - correct
			return correct
	
	#--------------------------------------------------------
	# - Is This Row Correctly Solved?
	#--------------------------------------------------------
	# * index : the row's index, counting top to bottom
	# returns True if each number in the row is unique, and
	# False otherwise.
	#--------------------------------------------------------
	def isRowCorrect(self, index):
		return None

	#--------------------------------------------------------
	# - Is This Column Correctly Solved?
	#--------------------------------------------------------
	# * index : the column's index, counting left to right
	# returns True if each number in the column is unique,
	# and False otherwise.
	#--------------------------------------------------------
	def isColumnCorrect(self, index):
		return None

	#--------------------------------------------------------
	# - Is This Block Correctly Solved?
	#--------------------------------------------------------
	# * x : the major column, counting left to right
	# * y : the major row, counting top to bottom
	# returns True if each number in the 3x3 block is unique,
	# and False otherwise.
	#--------------------------------------------------------
	def isBlockCorrect(self, x, y):
		return None

	#--------------------------------------------------------
	# - Is the Puzzle Solved?
	#--------------------------------------------------------
	# returns 'Correct' if the sudoku has been succesfully
	# solved, 'Incorrect' if solved but invalidly, and
	# 'Incomplete' otherwise.
	#--------------------------------------------------------
	def isSolved(self):
		if self.unsolved_ > 0:
			return 'Incomplete'
		else:
			 return 'Incorrect' if self.incorrect_ > 0 else 'Correct'

# Members
	board_ = []
	unsolved_ = 0
#================================================================
