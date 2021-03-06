import random

from .combat import Combat

COLORS = ['yellow', 'red', 'blue', 'green']

class Monster(Combat):
	def __init__(self, **kwargs):
		self.color = random.choice(COLORS)
		self.hp = 10
		self.position = kwargs.get('position', None)

		for key, value in kwargs.items():
			setattr(self, key, value)

	def __str__(self):
		return "{} Monster: HP {}".format(self.color.title(), self.hp)
