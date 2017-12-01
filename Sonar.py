import sys
import random
import time

def torps():
	print('\nLaunching torpedo.')
	tx = int((r + 30)/4)
	ty = int((c + 6)/4)
	game[tx][ty] = '>>>'
	print('\nFollowing torpedo using sonar')
	time.sleep(5)
	printboard()

	print('\nFollowing torpedo using sonar')
	game[tx][ty] = '~~~'
	tx = int((r + 10)/2)
	ty = int((c + 2)/2)
	game[tx][ty] = '>>>'
	time.sleep(5)
	printboard()

	print('\nFollowing torpedo using sonar')
	game[tx][ty] = '~~~'
	tx = int(((3*r) + 10)/4)
	ty = int(((3*c) + 2)/4)
	game[tx][ty] = '>>>'
	time.sleep(5)
	printboard()

	time.sleep(5)
	game[r][c] = '***'
	game[tx][ty] = '~~~'
	printboard()
	time.sleep(3)
	print('\nTarget Sunk.')


def printboard():
	for e in range(20):
		for f in range(15):
			print(game[e][f], end = ' ')
		print()
def battle():
	game = []
	for x in range(20):
		row =['~~~']*15
		game.append(row)

	r = int(random.uniform(0, 19))
	c = int(random.uniform(10, 14))
	game[r][c] = 'RUS'
	game[10][2] = 'USN'

	printboard()

	d = int(((c-2)**2+(r-10)**2)**0.5)
	print(str(d) + ' Kilometers from target')

	attack = int(input('Would you like to engage or follow the contact? 1 for engage, 2 to follow.'))
	while attack!= 1 and attack!=2:
		print('Not an option.')
		attack = int(input('Would you like to engage or follow the contact? 1 for engage, 2 to follow.'))

	if attack == 1:
		torps()

	if attack == 2:

		print('\nYour submarine moves towards the enermy Russian ship.')
		game[10][2] = '~~~'
		tx = int((r + 30)/4)
		ty = int((c + 6)/4)
		game[tx][ty] = 'USN'
		print('\nIf you move any closer, the enemy ship will spot you ')
		time.sleep(3)
		printboard()

		attack = int(input('Would you like to engage or continue to follow the contact? 1 for engage, 2 to follow.'))
		while attack!= 1 and attack!=2:
			print('Not an option.')
			attack = int(input('Would you like to engage or follow the contact? 1 for engage, 2 to follow.'))

		if attack == 1:
			torps()
		if attack == 2:
			game[tx][ty] = '~~~'
			tx = int((r + 10)/2)
			ty = int((c + 2)/2)
			game[tx][ty] = 'USN'
			printboard()
			time.sleep(3)
			print('\nThe enemy ship has spotted you')
			print('\nThe enemy ship fires at you')
			print('\nYou take envasive actions to avoid the fire')
			num = int(random.uniform(1,101))
			if num <= 98:
				print('Your submarine successfully dodged the fire.')
				print('You load the torpedo tubes to fire back.')
				torps()
			else:
				print('Game Over')
				again = input('Would you like to play again? Y/N')
				again = again.lower()
				while again!= 'y' and again != 'n':
					print('That is not an option.')
					again = input('Would you like to play again? Y/N')
					again = again.lower()
				if again == 'y':
					game()
					#^if the game is a function do this
				if again == 'n':
					exit()