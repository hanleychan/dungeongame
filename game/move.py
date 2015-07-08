from .gamemap import GameMap

class Move(GameMap):
	def get_valid_moves(self, location):
		valid_moves_list = []
		
		if location == (0,0):  # top left corner
			valid_moves_list = ["DOWN", "RIGHT"]
		elif location == (0, self.NUM_COLS-1):  # top right corner
			valid_moves_list = ["DOWN", "LEFT"]
		elif location == (self.NUM_ROWS-1, 0):  # bottom left corner
			valid_moves_list = ["UP", "RIGHT"]
		elif location == (self.NUM_ROWS-1, self.NUM_COLS-1):  # bottom right corner
			valid_moves_list = ["UP", "LEFT"]
		elif location[0] == 0:  # top row
			valid_moves_list = ["DOWN", "LEFT", "RIGHT"]
		elif location[0] == (self.NUM_ROWS - 1): # bottom row
			valid_moves_list = ["UP", "LEFT", "RIGHT"]
		elif location[1] == 0:  # left column
			valid_moves_list = ["UP", "DOWN", "RIGHT"]
		elif location[1] == self.NUM_COLS-1:  # right column
			valid_moves_list = ["UP", "DOWN", "LEFT"]
		else:  # anywhere else
			valid_moves_list = ["UP", "DOWN", "LEFT", "RIGHT"]

		return(valid_moves_list)

	def is_valid_move(self, move, location):
		if move in self.get_valid_moves(location):
			return True
		else:
			return False

	def is_valid_location(self, location):
		gameGrid = []

		for x in range(0, self.NUM_ROWS):
			for y in range(0, self.NUM_COLS):
				gameGrid.append((x,y))

		if location in gameGrid:
			return True
		else:
			return False



