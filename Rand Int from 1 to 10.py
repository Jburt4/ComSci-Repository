import random
import sys

again = 'y'

while again == 'y':
	x = int(random.uniform(1,11))

	y = int(input('Guess a number between 1 and 10 '))



	if y == x:
		print('Correct')
	else:
		print('Wrong')
	print(x)

	again = input('Do you want to play again? y/n ')