import random

class Combat:
	min_damage = 1
	max_damage = 3
	num_sides_dice = 6

	def roll_attack(self):
		""" Determines whether an attack is successful or not  """
		if random.randint(1, self.num_sides_dice) > 3:
			return True
		else:
			return False

	def make_attack(self):
		""" Makes an attack and return the damage done if successful """
		if self.roll_attack():
			damage = random.randint(self.min_damage, self.max_damage)
			return damage
		else:
			return 0
