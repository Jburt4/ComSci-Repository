import sys
import time
import os
import random


#INSTRUCTIONS
#Welcome to the Submarine Simulator in Python by Henry Lockwood
# This game is configured for a PC 
# If you are playing on a Mac, please go down to Line 51, and change cls to #clear

#-------------------------------------------------------------------------------------
#Functions
#-------------------------------------------------------------------------------------

class Sub:

	def __init__(self):
		self.speed = 10
		self.hull = 100
		self.under = 1

	def stats(self):
		print("Ship Stats:")
		print("SPD = "+str(self.speed)+' KTS')
		print("Hull Integrity: "+str(self.hull))
		if self.under == 1:
			print("Target is Submerged")



class Destroyer:

	def __init__(self):
		self.speed = 20
		self.hull = 100
		self.under = 0

	def stats(self):
		print("Ship Stats")
		print("SPD = "+str(self.speed)+" KTS")
		print("Hull Integrity: "+str(self.hull))
		if self.under == 1:
			print("Target is Submerged")

class PassengerShip:

	def __init__(self):
		self.speed = 25
		self.hull = 100
		self.under = 0

	def stats(self):
		print("Ship Status")
		print("SPD = "+str(self.speed)+" KTS")
		print("Hull Integrity: "+str(self.hull))
		if self.under == 1:
			print("Target is Submerged")
class Whale:

	def __init__(self):
		self.speed = 12
		self.hull = 50
		self.under = 1
	def stats(self):
		print("Ship Status")
		print("SPD = "+str(self.speed)+" KTS")
		print("Hull Integrity: "+str(self.hull))
		if self.under == 1:
			print("Target is Submerged")

def torps():
	global r
	global c
	global game
	global contact
	global printboard
	print('\nLaunching torpedo.')
	tx = int((r + 30)/4)
	ty = int((c + 6)/4)
	game[tx][ty] = '>>>'
	time.sleep(3)
	clear()
	printboard()
	print('\nFollowing torpedo using sonar')

	game[tx][ty] = '~~~'
	tx = int((r + 10)/2)
	ty = int((c + 2)/2)
	game[tx][ty] = '>>>'
	time.sleep(3)
	clear()
	printboard()
	print('\nFollowing torpedo using sonar')

	game[tx][ty] = '~~~'
	tx = int(((3*r) + 10)/4)
	ty = int(((3*c) + 2)/4)
	game[tx][ty] = '>>>'
	time.sleep(3)
	clear()
	printboard()
	print('\nFollowing torpedo using sonar')

	time.sleep(3)
	game[r][c] = '***'
	game[tx][ty] = '~~~'
	clear()
	printboard()

	time.sleep(3)
	print('\nCONN, SONAR, TARGET HIT.')

	if contact == 3:
		print('The target you sunk was a passenger ship.')
		print('\nHundreds of innocent people have been killed.')
		print('\nYou lose. Game Over.')
		again = input('Would you like to play again? Y/N')
		again = again.lower()
		while again!= 'y' and again != 'n':
			print('That is not an option.')
			again = input('Would you like to play again? Y/N')
			again = again.lower()
		if again == 'y':
			print('\nDo better this time!')
			time.sleep(2)
			main()
		if again == 'n':
			print('\nThanks for murdering hundreds.')
			time.sleep(3)
			exit()

	if contact == 4:
		print('The target you hit was an innocent whale.')
		print('\nThe media attacks you for what you have done.')
		print('\nThe admiral holds you responsible and fires you')
		print('\nGame Over\n')
		time.sleep(3)
		again = input('Would you like to play again? Y/N')
		again = again.lower()
		while again!= 'y' and again != 'n':
			print('That is not an option.')
			again = input('Would you like to play again? Y/N')
			again = again.lower()
		if again == 'y':
			main()
		if again == 'n':
			exit()

	time.sleep(3)
	clear()
	print('NEW CONTACT FOUND')

def battle():
	global r
	global c
	global game
	global main
	global contact
	global printboard
	contact = int(random.uniform(1,5))
	sub1 = Sub()
	destroyer1 = Destroyer()
	passenger1 = PassengerShip()
	whale1 = Whale()
	game = []
	for x in range(20):
		row =['~~~']*15
		game.append(row)

	r = int(random.uniform(0, 19))
	c = int(random.uniform(10, 14))
	game[r][c] = 'RUS'
	game[10][2] = 'USN'

	def printboard():
		for e in range(20):
			for f in range(15):
				print(game[e][f], end = ' ')
			print()
		print('')
		print('')
		print('')
		print('')

	printboard()

	d = int(((c-2)**2+(r-10)**2)**0.5)
	print(str(d) + ' Kilometers from target')

	attack = input('Would you like to engage or follow the contact? 1 for engage, 2 to follow.')
	while attack!= '1' and attack!= '2':
		print('Not an option.')
		attack = input('Would you like to engage or follow the contact? 1 for engage, 2 to follow.')

	if attack == '1' and contact == 1:
		torps()
		print('\nYou sunk a Russian sub. Good Job')
	if attack == '1' and contact == 2:
		torps()
		print('\nYou sunk a Russian Destroyer. Good Job.')
	if attack == '1' and contact == 3:
		torps()
	if attack == '1' and contact == 4:
		torps()

	if attack == '2':
		print('\nYou move forward and identify the contact.')
		if contact == 1:
			print('The contact is an enemy sub.')
			sub1.stats()
		elif contact == 2:
			print('The contact is an enemy destroyer.')
			destroyer1.stats()
		elif contact == 3:
			print('The contact is a Passenger Ship')
			passenger1.stats()
		elif contact == 4:
			print('The contact is a whale')
			whale1.stats()

		game[10][2] = '~~~'
		tx = int((r + 30)/4)
		ty = int((c + 6)/4)
		game[tx][ty] = 'USN'
		printboard()
		attack1 = input('Would you like to engage or continue to follow the contact? 1 for engage, 2 to follow.')
		while attack1!= '1' and attack1!= '2':
			print('Not an option.')
			attack1 = input('Would you like to engage or follow the contact? 1 for engage, 2 to follow.')

		if attack1 == '1' and contact == 1:
			game[10][2] = 'USN'
			torps()
		if attack1 == '1' and contact == 2:
			game[10][2] = 'USN'
			torps()
		if attack1 == '1' and contact == 3:
			game[10][2] = 'USN'
			torps()
		if attack1 == '1' and contact == 4:
			game[10][2] = 'USN'
			torps()
		if attack1 == '2' and contact == 1:
			game[tx][ty] = '~~~'
			tx = int((r + 10)/2)
			ty = int((c + 2)/2)
			game[tx][ty] = 'USN'
			printboard()
			time.sleep(3)
			print('\nThe enemy sub has spotted you')
			print('\nThe enemy sub fires at you')
			print('\nYou take envasive actions to avoid the fire')
			num = int(random.uniform(1,101))
			if num <= 98:
				print('Your sub successfully dodged the fire.')
				print('\nYou load the torpedo tubes to fire back.')
				time.sleep(3)
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
					main()
				if again == 'n':
					exit()
		if attack1 == '2' and contact == 2:
			torps()
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
					main()
					#^if the game is a function do this
				if again == 'n':
					exit()
		if attack1 == '2' and contact == 3:
			print('You recognize that the ship is a passenger ship and do not kill all the people on board')

			time.sleep(3)
			clear()
			print('NEW CONTACT FOUND')
		if attack1 == '2' and contact == 4:
			print('You and your crew decide to leave the whale alone.')
			print('\nThe media praises you for saving an endangered whale.')	
			time.sleep(3)
			clear()
			print('NEW CONTACT FOUND')


def name():
	last = ["Angel","Gambit","Neptune","Jaeger","Arrow","Hawk","Dagger",
	"Knight","Cobra","Bear","Dynamo","Lancer","Thunder","Traveler","Walker",
	"Swordfish","Bandit","Tiger", "Ghost","Windigo","Centurion",
	"Trinity","Hunter","Frostbite","Phoenix","Spector"]

	userinput = str(input('PLEASE ENTER YOUR LAST NAME '))
	username = userinput.strip().lower().split(" ")
	
	try:
		indexlast = ord(username[0][0])-97
	except:
		print("I guess B is your name then.")
		indexlast = ord('b')-97
	print("You are the Captain of the USS "+str(last[indexlast])+", SSN-688")
	
def turn(a):
	global CSE
	global Rudder
	if a > CSE:
		Rudder = 5
	elif a == CSE:
		print('That is already our current course')
	else:
		Rudder = -5

# IF THE USER IS ON A MAC COMPUTER PLEASE CHANGE
# CLS BELOW TO #CLEAR IN THE APOSTROPHE MARKS

def clear():
	os.system('cls')

#Submarine Story
#Introduction
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

clear()





def game1():
	global CSE
	CSE = 168
	SPD = 8
	Silent = True
	Depth = 150
	Rudder = 0
	Cav = False
	print("November, 1983, Somewhere in the North Atlantic")
	#Each time there is a text part here, it should just advance by pressing enter
	inputA = input('')
	print("NATO OPERATION ABLE ARCHER")
	inputA = input('')
	print("NATO FORCES HAVE DEPLOYED TO COUNTER THE RED FLEET IN THE NORTH ATLANTIC")
	inputA = input('')
	name()
	inputA = input('')

	clear()

	#Message comes in

	wait1 = input('Press ENTER to open OPORD')
	clear()
	print("~~~~~~~~~~~~~~~~FLASH TRAFFIC CPT EYES ONLY~~~~~~~~~~~~~~~~~~~~~")
	print('Orders from COMSUBLANT')
	print('USS DAUNTLESS TO MOVE TO 06552 94827')
	print('ENGAGE ANY ENEMY CONTACTS ATTEMPING TO CROSS SOSUS NET')
	print('DO NOT ALLOW ANY ENEMY CONTACTS TO GET PAST')
	inputA = input('')

	clear()

	print('Welcome Captain')
	inputA = input('')
	print('You are at the Conn and we have our first surface contact')
	inputA = input('')
	clear()
	print('CONN, SONAR, WE HAVE ONE CONTACT DESIGNATE SIERRA 1, BEARING 250')
	inputA = input('')
	#SPD and CSE are varibles set up in the beginning
	print('')
	print('~~~~~~~~~~~Current Gauages~~~~~~~~~~~~')
	print('CSE = '+ str(CSE) + ' Degrees')
	print('SPD = '+str(SPD) + ' KT')
	print('Depth = '+str(Depth) + ' FT')
	print('Rudder = '+str(Rudder))
	print('')
	print('We are currently not cavitating')
	print('')

	#Cavitation Depth = 20 * Speed in Knots - 100



	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	while 1 == 1:
		try:
			nCSE = int(input('Captain! We need to change course to engage the contact. What should our new course be? '))
			break
		except:
			print("That is not an option!")
	turn(int(nCSE))
	print('New CSE = '+str(nCSE)+' Degrees')
	print('Rudder = '+str(Rudder))

	CSE = nCSE
	
	inputA = input('')
	print('CONN, RADIO, WE ARE PICKING UP A TRANSMITION FROM SIERRA 1, I AM PATCHING IT THROUGH')
	inputA = input('')
	clear()
	print('.')
	time.sleep(1) 
	print('.')
	time.sleep(1) 
	print('.')
	time.sleep(1) 
	print('SOVIET CRUISER SOVREMENNY CALLING RED FLEET ATLANTIC COMMAND')
	time.sleep(1) 
	print('BEING FOLLOWED BY US SUBMARINE LOS ANGELES CLASS')
	time.sleep(1) 
	print('PLEASE ADVISE, REDFORCE-1 OUT')
	time.sleep(1) 
	print('.')
	time.sleep(1) 
	print('.')
	time.sleep(1) 
	print('.')
	time.sleep(1) 
	clear()
	print('CONN, RADIO, IM SORRY CAPTAIN THE SIGNAL WAS ENCRYPTED AND WE LOST IT')

	inputA = input('')
	battle()
def main():
	game1()
	for i in range(0,3):
		battle()
		time.sleep(3)
	clear()
	print('\nCongratulations Captain! You successfully defended the high seas.')
	time.sleep(3)
	print('Game Over')
	again = input('Would you like to play again? Y/N')
	again = again.lower()
	while again!= 'y' and again != 'n':
		print('That is not an option.')
		again = input('Would you like to play again? Y/N')
		again = again.lower()
	if again == 'y':
		main()
	if again == 'n':
		exit()

main()



#Functions for Different Outcomes







#This is the end of the game



'''
IDEAS

Possible fail states - Being torpedoed, engaging a passenger ship, hitting a whale (or your mom), 



Printing to console - Already Have
Accepting command line arguments - Already Have
Getting input from the user - ALready Have (Could add to tho)
Datatypes and casting ()
Logic, including conditionals and if-statements Already Have
Loops Already Have (Should add some)
Defining and using functions - Already Have (Could Add More)
Error checking (try/except) - Need to Add (Needs to work)
Lists (1D and 2D)
Recursive functions (Not going to add)
Image manipulation and display - Game Board?
Strings and string manipulation (ALready have, will add more in order to help error check)
Classes, including constructor, methods, and built-in functions - Different Kinds of Boats

Torpedo "sonar map" Use game board code

Certain chance (around 3%) for our torpedo to miss
	if miss = true, follow up with enemy shooting torpedo, then having small percentage chance of hitting
	(around 5%) then fire back with 100% chance of hitting.

import statment
classes then functions
Main code


'''