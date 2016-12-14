import random

class Dice:

	def __init__(self):
		self.min = 1
		self.max = 6
		self.roll_dice()

	def roll_dice(self):
		while True:
			roll = raw_input("Type 'y' if you want to roll the dice else type 'n' - ")
			if roll == 'n' or roll == 'N':
				print("You have chosen to end the game. Thank You!")
				break
			elif roll == 'y' or roll == 'Y':
				self.generate_number()
			else:
				print('Invalid input')

	def generate_number(self):
		print("The number is: " + str(random.randint(self.min,self.max)))


Dice()