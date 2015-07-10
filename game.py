import os
import sys

from game.hero import Hero
from game.gamemap import GameMap
from game.monster import Monster
from game.door import Door

class Game:
	def setup(self):
		""" Generates a hero, monster and door at random locations. """
		player_start = GameMap.random_location()
	
		# Generate monster location. Make sure it is not the same as player location
		while True:
			monster_start = GameMap.random_location()
			if monster_start == player_start:
				continue
			else:
				break

		# Generate door location. Make sure it is not the same as player and monster location.
		while True:
			door_start = GameMap.random_location()
			if door_start == monster_start or door_start == player_start:
				continue
			else:
				break
			
		self.player = Hero(position=player_start)
		self.monster = Monster(position=monster_start)
		self.door = Door(position=door_start)

		self.player.visit_location(player_start)

	def player_turn(self):
		""" Asks the user to take an action to either attack or recover """
		while True:
			action = input("Attack or Heal: ").lower().strip()
			if action == "heal":
				self.player.heal()
				print("new hp {}".format(self.player.hp))
				break
			elif action == "attack":
				damage = self.player.make_attack()
				print("\nYou hit the monster for {} damage.".format(damage))
				self.monster.hp -= damage
				break
			else:
				print("Invalid action, try again.\n")
		
	def monster_turn(self):
		""" The monster attemps to attack the player """
		damage = self.monster.make_attack()
		print("The monster hits you for {} damage.\n".format(damage))
		self.player.hp -= damage

	def fight(self):
		""" Handles the fight between the player and the monster. """
		while True:
			print('-' * 30)
			print(self.player)
			print(self.monster)
			print('-' * 30)
			self.player_turn()

			if self.monster.hp <= 0:
				print("You have slain the monster and taken the key from it's dead body.\n")
				self.player.key = True
				self.monster.position = None
				break

			self.monster_turn()
			
			if self.player.hp <= 0:
				print("You have been killed by the monster. Game over!\n")
				sys.exit()

	def clear(self):
		""" Clears the screen """
		os.system('cls' if os.name == 'nt' else 'clear')

	def __init__(self):
		self.clear()
		
		self.setup()
	
		message = None

		while True:
			self.clear()

			print("Hero: " + self.player.name.title() + " / Weapon: " + self.player.weapon.title()) 
			self.player.draw_map(hero = self.player.position, 
								monster=self.monster.position, 
								door = self.door.position, 
								visited=self.player.visited_list)

			if message:
				print(message)
				message = None

			if self.player.key == True:
				print("Inventory: Key")
				
			move = input("{}: ".format(self.player.get_valid_moves(self.player.position))).upper().strip()

			if self.player.is_valid_move(move, self.player.position):
				print("You moved {}.\n\n".format(move))
				self.player.change_position(move)
			else:
				message="That is not a valid move."
			if self.player.position == self.door.position:
				if self.player.key:
					print("You found the exit. You win!")
					break
				else:
					message = "You found the exit, but the door is locked."
			elif self.player.position == self.monster.position:
				print("You have found the monster!\n")
				self.fight()

			
		print("Game over. You made {} moves.\n\n".format(len(self.player.visited_list)-1))

Game()
