import random

from .move import Move
from .combat import Combat

class Hero(Move, Combat):
	BASE_HP = 10
	
	def __init__(self, **kwargs):
		self.name = input("Name: ")
		self.weapon = self.choose_weapon()
		self.hp = self.BASE_HP 
		self.position = (0,0)
		self.visited_list = []
		self.key = False

		for key, value in kwargs.items():
			setattr(self, key, value)
	
	def __str__(self):
		return "{}: HP {}".format(self.name, self.hp)


	def visit_location(self, position):
		self.visited_list.append(position)

	def choose_weapon(self):
		weapon_choice = input("Weapon: [S]word, [A]xe, [B]ow: ").lower()

		if weapon_choice == 's' or weapon_choice == 'sword':
			return 'sword'
		elif weapon_choice == 'a' or weapon_choice == 'axe':
			return 'axe'
		elif weapon_choice == 'b' or weapon_choice =='bow':
			return 'bow'
		else:
			return self.choose_weapon()

	def heal(self):
		heal_amount = random.randint(1,2)
		new_hp = self.hp + heal_amount

		if new_hp > self.BASE_HP:
			self.hp = self.BASE_HP
		else:
			self.hp = new_hp

	def change_position(self, move):
		if move == "UP":
			new_position = (self.position[0]-1,self.position[1])
		elif move == "DOWN":
			new_position = (self.position[0]+1, self.position[1])
		elif move == "LEFT":
			new_position = (self.position[0], self.position[1]-1)
		else: # move is RIGHT
			new_position = (self.position[0], self.position[1]+1)

		if self.is_valid_location(new_position):
			self.position = new_position
			self.visit_location(new_position)
		else:
			print("That is an invalid move.")
