import sys
import random

again = 'y'
while again == 'y':

	x = int(random.uniform(1,101))

	guess = int(input('Choose a number between 1 and 100'))
	while x != guess:
		if guess == x:
			print('Correct')
		elif guess < x:
			print('Too Low. Guess Again.')
		else:
			print('Too High. Guess Again')
		guess = int(input('Next Guess'))
	print('Correct! You win!')
	again = input('Do you want to play again? y/n ')
print('Thanks for playing!')

