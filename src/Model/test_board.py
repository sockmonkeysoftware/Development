from Board import Board
import unittest, random


class Test_Board(unittest.TestCase):
	board = None

	def setUp(self):
		self.board = Board(10)

	def tearDown(self):
		pass

	#--------------------------------------------------------------------------------
	def test_01_board_is_created_with_9x9_elements(self):
	#--------------------------------------------------------------------------------
		raw_board = self.board.getRaw()
		
		self.assertEqual(len(raw_board), 9, "Board was not created with 9 rows")
		self.assertEqual(len(raw_board[0]), 9, "Board was not created with 9 columns")

	#--------------------------------------------------------------------------------
	def test_02_board_elements_are_either_a_digit_or_None(self):
	#--------------------------------------------------------------------------------
		for row in self.board.getRaw():
			for cell in row:
				self.assertTrue(type(cell) is int or type(cell) is type(None), "Cell is neither an integer, nor None (blank), but a " + str(type(cell))),

				# Test that any integer cells are within 1~9
				if type(cell) == 'int': 
					self.assertIn(cell, range(1, 10), "Cell is out of range")
		

	#--------------------------------------------------------------------------------
	def test_03_board_has_10_unsolved_cells(self):
	#--------------------------------------------------------------------------------
		unsolved = 0

		for row in self.board.getRaw():
			for cell in row:
				if(type(cell) == type(None)):
					unsolved += 1

		self.assertEqual(unsolved, 10, "The number of solutions was not equal to the constructor argument.")
		
	#--------------------------------------------------------------------------------
	def test_04_board_is_initially_unsolved(self):
	#--------------------------------------------------------------------------------
		self.assertEqual(self.board.isSolved(), 'Incomplete', "Board was not created incomplete")

	#--------------------------------------------------------------------------------
	def test_05_get_row_returns_an_actual_row_from_the_board(self):
	#--------------------------------------------------------------------------------
		row = self.board.getRow(4)

		for column in range(0, 9):
			self.assertEqual(row[column], self.board.board_[4][column], "A cell in getRow did not match the board's original data.")

		# Row should be 9-cells in length
		self.assertEqual(len(row), 9, "Returned row is of abnormal length")

		# Calling an index out of range (0~8) should return None
		self.assertEqual(self.board.getRow(-1), None, "Calling row with index -1 did not produce a row of None")
		self.assertEqual(self.board.getRow(9), None, "Calling row with index 9 did not produce a row of None")

	#--------------------------------------------------------------------------------
	def test_06_get_column_returns_an_actual__column_from_the_board(self):
	#--------------------------------------------------------------------------------
		column = self.board.getColumn(6)

		# Column should be 9-cells in length
		self.assertEqual(len(column), 9, "Returned column is of abnormal length")

		for row in range(0, 9):
			self.assertEqual(column[row], self.board.board_[row][6], "A cell in getColumn did not match the board's original data.")

		# Calling an index out of range (0~8) should return None
		self.assertEqual(self.board.getColumn(-1), None, "Calling column with index -1 did not produce a column of None")		
		self.assertEqual(self.board.getColumn(9), None, "Calling column with index 9 did not produce a column of None")		

	#--------------------------------------------------------------------------------
	def test_07_get_block_returns_an_actual_block_from_the_board(self):
	#--------------------------------------------------------------------------------
		block = self.board.getBlock(2, 1)

		# Block should be 3x3-cells in dimension
		self.assertEqual(len(block), 3, "Returned block has abnormal number of rows")
		self.assertEqual(len(block[0]), 3, "Returned block has abnormal number of columns")

		for row in range(0, 3):
			for column in range(0, 3):
				self.assertEqual(block[row][column], self.board.board_[3 + row][6 + column], "A cell in getColumn did not match the board's original data.")

		# Calling an either index out of range (0~2, 0~2) should return None
		self.assertEqual(self.board.getBlock(-1, 0), None, "Calling block with coords (-1, 0) did not produce a block of None")		
		self.assertEqual(self.board.getBlock(3, 0), None, "Calling block with coords (3, 0) did not produce a block of None")		
		self.assertEqual(self.board.getBlock(0, -1), None, "Calling block with coords (0, -1) did not produce a block of None")		
		self.assertEqual(self.board.getBlock(0, 3), None, "Calling block with coords (0, 3) did not produce a block of None")		

	#--------------------------------------------------------------------------------
	def test_08_get_cell_returns_an_actual_cell_from_the_board(self):
	#--------------------------------------------------------------------------------
		row = random.randint(0, 8)
		column = random.randint(0, 8)

		self.assertEqual(self.board.getCell(column, row), self.board.board_[row][column], "Cell(" + str(row) + ", " + str(column) + ") did not match the board's original data.")

		# Calling either index out of range (0~8, 0~8) should return None
		self.assertEqual(self.board.getBlock(-1, 0), None, "Calling cell with coords (-1, 0) did not produce a cell of None")		
		self.assertEqual(self.board.getBlock(9, 0), None, "Calling cell with coords (9, 0) did not produce a cell of None")		
		self.assertEqual(self.board.getBlock(0, -1), None, "Calling cell with coords (0, -1) did not produce a cell of None")		
		self.assertEqual(self.board.getBlock(0, 9), None, "Calling cell with coords (0, 9) did not produce a cell of None")				

	#--------------------------------------------------------------------------------
	def test_09_submit_answer_sets_the_value_of_a_cell(self):
	#--------------------------------------------------------------------------------
		x = None
		y = None

		for row in range(0, 9):
			for column in range(0, 9):
				if self.board.getCell(column, row).isMutable():
					x = column
					y = row
					break
		
		self.assertNotEqual(x, None, "Failed to find a mutable cell.")
		self.assertNotEqual(y, None, "Failed to find a mutable cell.")

		guess = random.randint(1, 9)

		self.board.submitAnswer(x, y, guess)
		self.assertEqual(self.board.getCell(x, y).getAnswer(), guess, "failed to submit answer " + str(guess) + " to (" + str(x) + ", " + str(y) + ")")

		# submitting outside either index range (0~8) or answer range (1~9) results in None
		self.assertEqual(self.board.submitAnswer(-1, 0, guess), None, "submitted bad answer " + str(guess) + " to (-1, 0)")
		self.assertEqual(self.board.submitAnswer(9, 0, guess), 	None, "submitted bad answer " + str(guess) + " to (9, 0)")
		self.assertEqual(self.board.submitAnswer(0, -1, guess), None, "submitted bad answer " + str(guess) + " to (0, -1)")
		self.assertEqual(self.board.submitAnswer(0, 9, guess),  None, "submitted bad answer " + str(guess) + " to (0, 9)")
		self.assertEqual(self.board.submitAnswer(x, y, 0), 	None, "submitted bad answer 0 to (" + str(x) + ", " + str(y) + ")")
		self.assertEqual(self.board.submitAnswer(x, y, 10),	None, "submitted bad answer 10 to (" + str(x) + ", " + str(y) + ")")
		
		# submitting correct answer should yield True
		guess = self.board.getCell(x, y).getSolution()
		self.assertTrue(self.board.submitAnswer(x, y, guess))

		# submitting an incorrect answer should yield False
		guess = (guess + 5) % 9 + 1
		self.assertFalse(self.board.submitAnswer(x, y, guess))

	#--------------------------------------------------------------------------------
	def test_10_board_is_complete_when_all_filled(self):
	#--------------------------------------------------------------------------------
		unsolved = []

		for row in range(0, 9):
			for column in range(0, 9):
				if self.board.getCell(column, row).isMutable():
					unsolved.append((column, row))

		self.assertEqual(len(unsolved), 10, "Number of mutable cells different than constructor argument")

		# fill the board with correct answers
		for cell in unsolved:						
			solution = self.board.getCell(cell[0], cell[1]).getSolution()
			self.board.submitAnswer(cell[0], cell[1], solution)

		# a fully completed board with all correct solutions should return 'Correct'
		self.assertEqual(self.board.isSolved(), 'Correct', "Board was not found to be correctly completed.")

		# submit an incorrect answer
		solution = self.board.getCell(unsolved[0][0], unsolved[0][1]).getSolution()
		incorrect = (solution + 5) % 9 + 1

		self.board.submitAnswer(unsolved[0][0], unsolved[0][1], incorrect)

		# a fully completed board with an incorrect solution should return 'Incorrect'
		self.assertEqual(self.board.isSolved(), 'Incorrect', "Perturbed complete board not found to be incorrect.")

	#--------------------------------------------------------------------------------
	def test_11_board_is_well_formed(self):
	#--------------------------------------------------------------------------------
		pass

if __name__ == "__main__":
	unittest.main(verbosity = 2)
