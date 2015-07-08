import random

class GameMap:
	NUM_ROWS = 3 
	NUM_COLS = 5

	@classmethod
	def random_location(cls):
		row = random.randint(0, cls.NUM_ROWS-1)
		col = random.randint(0, cls.NUM_COLS-1)
		return row, col

	@classmethod
	def draw_map(cls, **kwargs):
		hero = kwargs.get("hero", None)
		visited = kwargs.get("visited", None)
		
		monster = kwargs.get("monster", None)
		if monster not in visited:
			monster = None
		
		door = kwargs.get("door", None)
		if door not in visited:
			door = None

		print("\nMAP: (H = HERO, M = MONSTER, D = DOOR, X = UNVISITED LOCATION, O = VISITED LOCATION)")
		print("=======================================================================================")
		for x in range(0, cls.NUM_ROWS):
			temp = ""
			for y in range(0, cls.NUM_COLS):
				if hero == (x,y):
					temp += "H "
				elif monster ==(x,y):
					temp += "M "
				elif door == (x,y):
					temp += "D "
				elif (x,y) in visited:
					temp += "O "
				else:
					temp += "X "
			print(temp)
		print("\n")
