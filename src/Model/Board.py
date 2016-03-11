from Cell import Cell
import random, math

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
		solutions = max(0, min(81, solutions))

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

		# Generate base puzzle: known to be valid.
		# Generate each row
		for row in range(0, 9):
			board.append([])

			# Generate each cell
			for column in range(0, 9):
				shift = ((row * 3) % 9) + math.floor(row / 3)
				number = ((column + shift) % 9) + 1

				cell = Cell(number)
				board[row].append(cell)

		# Randomly perturb the puzzle iteratively to generate a new puzzle
		# Legal Transorfmations:
		#--------------------------------------------------
		#1. swap all cells across either diagonal
		#2. swap regions (column/row triplets)
		#3. rotate around 4th row/col: 1, 2, 3, 4, 5, 6, 7, 9 => 9, 8, 5, 4, 3, 6, 7, 2, 1
		#4. swap rows/cols within region
		#5. swap two specific digits
		#6. puzzle rotate

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
		if index not in range(0, 9):
			return None
		else:		
			numbers = [cell.getAnswer() for cell in self.getRow(index)]

			if(None in numbers):
				return False

			numbers.sort()

			return numbers == list(range(1, 10))

	#--------------------------------------------------------
	# - Is This Column Correctly Solved?
	#--------------------------------------------------------
	# * index : the column's index, counting left to right
	# returns True if each number in the column is unique,
	# and False otherwise.
	#--------------------------------------------------------
	def isColumnCorrect(self, index):
		if index not in range(0, 9):
			return None
		else:		
			numbers = [cell.getAnswer() for cell in self.getColumn(index)]

			if None in numbers:
				return False

			numbers.sort()

			return numbers == list(range(1, 10))

	#--------------------------------------------------------
	# - Is This Block Correctly Solved?
	#--------------------------------------------------------
	# * x : the major column, counting left to right
	# * y : the major row, counting top to bottom
	# returns True if each number in the 3x3 block is unique,
	# and False otherwise.
	#--------------------------------------------------------
	def isBlockCorrect(self, x, y):
		if x not in range(0, 3) or y not in range(0, 3):
			return None
		else:		
			numbers = [cell.getAnswer() for row in self.getBlock(x, y) for cell in row]

			if None in numbers:
				return False

			numbers.sort()

			return numbers == list(range(1, 10))

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

	#--------------------------------------------------------
	# - Is the Puzzle Valid?
	#--------------------------------------------------------
	# returns IF the sudoku is a valid board: no row, column
	# or block contains two of the same number. 
	#--------------------------------------------------------
	def isValid(self):
		for row in range(0, 9):
			numbers = [cell.getSolution() for cell in self.getRow(row)]
			numbers.sort()

			if numbers != list(range(1, 10)):
				return False

		for column in range(0, 9):
			numbers = [cell.getSolution() for cell in self.getColumn(column)]
			numbers.sort()

			if numbers != list(range(1, 10)):
				return False
		
		for x in range(0, 3):
			for y in range(0, 3):
				numbers = [cell.getSolution() for row in self.getBlock(x, y) for cell in row]
				numbers.sort()

				if numbers != list(range(1, 10)):
					return False

		return True

	#--------------------------------------------------------
	# - Swap Rows
	#--------------------------------------------------------
	# * y1 : index of first row to be swapped
	# * y2 : index of second row to be swapped
	# Swaps the cells in rows at y1 and y2.
	#--------------------------------------------------------
	def swapRows(y1, y2):
		return None

	#--------------------------------------------------------
	# - Swap Columns
	#--------------------------------------------------------
	# * x1 : index of first column to be swapped
	# * x2 : index of second column to be swapped
	# Swaps the cells in columns at x1 and x2.
	#--------------------------------------------------------
	def swapColumns(x1, x2):
		return None

# Members
	board_ = []
	unsolved_ = 0
#================================================================
