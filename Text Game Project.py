import sys
import time
import random

#Castle Adventure
#By John Burt
#10/6/2017
#On my honor, I have neither given nor received unauthorized aid.

#I wasn't exactly sure what to do for comments so I hope this is what you were looking for

#Functions
def GoodLuck(a,b):
	global again
	num = int(random.uniform(1,11))
	if num > 8:
		print(a)
		return None
	else:
		print('Game Over')
		print(b)
		again = input('Play Again? Print Y/N')
		while again != 'Y' and again != 'y' and again != 'N' and again !='n':
			print('That is not an option.')
			again = input('Play Again? Print Y/N')
	if again == 'Y' or again =='y':
		Game()
#The good luck fucntion is used when someone makes the wrong decision,
#they are still able to not lose.

def PlayAgain():
	global again
	again = input('Play Again? Print Y/N')
	while again != 'Y' and again != 'y' and again != 'N' and again !='n':
		print('That is not an option.')
		again = input('Play Again? Print Y/N')
	if again == 'Y' or again =='y':
		Game()
	elif again == 'N' or again == 'n':
		print('Thanks For Playing! Come again soon.')
	return None
#This function asks the player if they want to play again

def Battle():
	global name
	print('You go to the jail and let your guards out. The pick up some nearby weapons and you look for the rest of the enemies.\n')
	#time.sleep(3)
	print('You find the other ten enemies waiting for you and your guards at the keep.\n')
	#time.sleep(3)
	print('Both groups charge at each other, but only one comes out victorious')
	num = int(random.uniform(1,101))
	if num < 95:
		print('You defeated the enemy.\n')
		time.sleep(2)
		print('You successfully took back your castle! Congratulations! ' + name + ', you Win!\n')
		return None
	else:
		print('You could not hold onto the walls smooth surfaces.\n')
		Print('Game Over\n')
		again = input('Play Again? Print Y/N ')
		while again != 'Y' and again != 'y' and again != 'N' and again !='n':
			print('That is not an option.')
			again = input('Play Again? Print Y/N')
		if again == 'Y' or again =='y':
			Game()
#this is the function for the battle sequence

#This is the main function. It runs the game
def Game():
	global name
	name = input('What is your name?\n')
	Castle = input('What is the name of your castle?\n')
	print('You wake in a forest hunting for food when you realize that you have no clue where you are.\n')
	time.sleep(3)
	#this is for a wait so that people have time to read the lines
	print('The last thing you remember is drinking water from a nearby river when someone whacked you on the head with a hammer.\n')
	time.sleep(3)
	print('As you struggle to stand up, you realize that the stranger robbed you of all your gold and weapons except your sword.\n')
	time.sleep(3)
	print('You look around to see where you came from, but you dont remember a thing.\n')
	time.sleep(3)
	print('You decide to walk in a direction in hopes of finding your way home.\n')
	time.sleep(3)
	print('You soon find a road. Hoping it leads you to your castle, you follow it.\n')
	time.sleep(3)
	print('On the road in front of you, you see an angry giant stopped ahead of you with what looks like your armor and your bow and arrows.\n')
	time.sleep(3)
	x = input('Would like to kindly ask for your armor, attack him and take it, or wait and attempt to steal it?\n Print 1 for Ask, 2 for Attack, or 3 for Steal.\n')
	#this while loop is to make sure that you can only put 1,2,or 3 in for the input
	while x != '1' and x != '2' and x !='3':
		print('That is not an option!\n')
		x = input('Would like to kindly ask for your armor, attack him and take it, or wait and attempt to steal it?\n Print 1 for Ask, 2 for Attack, or 3 for Steal.\n')
	if x == '1':
		print('When the giant spots you, he runs towards you with his hammer and crushes your skull with it.')
		print('You died. Game Over. Do not make bad choices.')
		PlayAgain()
		return None
	if x == '2':
		GoodLuck('Luckily, the giant was looking away when you walked behind him and stabbed him.','You are seen with your sword and the giant squashes you with his hammer.')
		return None	
	else:
		num = int(random.uniform(1,11))
		if num == 10:
			print('You trip and fall onto the giant and wake him up. He picks you up and throws you against a tree and you die.\n')
			PlayAgain()
			return None
		else:
			print('You sneakily grab your stuff while the giant is sleeping.\n')
			time.sleep(2)
	print('Now that you have your stuff, you put the armor on, grab your bow and arrows, and continue down the road\n.')
	time.sleep(2)
	print('It is getting very late and you are getting very tired and can barely stand on your feet.\n')
	time.sleep(3)
	tired = input('Would you like to sleep? Print Y/N')
	while tired != 'Y' and tired != 'y':
		print('That is not an option!\n')
		tired = input('Would you like to sleep? Print Y/N')
	if tired == 'Y' or tired == 'y':
		print('You wake up the next day feel energized and ready to continue your quest home.\n')
	else:
		print('You continue to walk until your vision gets really blurry and you fall over and die from exhaustion.\n')
		print('Game Over')
		PlayAgain()
		return None
	print('As you continue to walk, you notice a sketchy shack on the side of the road.\n')
	time.sleep(3)
	print('Hoping to get directions home, you knock on the door to see if there is anyone home.\n')
	time.sleep(3)
	print('After a few seconds, what seems to be the voice of an elderly man says, "You may enter my house only if you can answer my riddle?\n')
	time.sleep(3)
	riddle = input('What has hands, but cannot clap ')
	while riddle != 'a clock':
		#This next few lines of code is for people who can't get the riddle
		#There is a chance that the man will just let you in even if it's the wrong answer
		num = int(random.uniform(1,11))
		if num < 9:
			print(' Guess Again\n')
			riddle = input('What has hands, but cannot clap?')
			#The answer is a clock
		else:
			print('Nevermind. It is a stupid riddle.')
			riddle = 'a clock'
	print('\nYou may enter my house\n')
	time.sleep(2)
	print('Welcome to my humle abode\n')
	time.sleep(2)
	print('Now I can sense that you are a little lost, so I shall help you on your way home. \n')
	time.sleep(3)
	print('Keep following this road until you get to the fork. At the fork, take the left path in order to get home.\n')
	time.sleep(3)
	print('Others may try to lead you astray, but you must follow my directions in order to get home.\n')
	time.sleep(3)
	print('Now i shall feed you and you can be on your way.\n')
	time.sleep(2)
	print('You 3hank the man his hospitality and continue on your journey home.\n')
	time.sleep(3)
	print('After some walking, you come to a fork in the road with a man standing in between each new pathway.\n')
	time.sleep(3)
	print('You also notice a sign pointing to the right path with ' + Castle + ' on it.\n')
	time.sleep(2)
	print('You are a little confused because the elderly man told you to go left, but the sign says to go right.\n')
	time.sleep(3)
	print('You decide to ask the stranger nearby for directions.\n')
	time.sleep(2)
	print('You say to him, "Excuse me sir but do you know the way to ' + Castle)
	time.sleep(2)
	print('\nHe responds with, "Why of course. It is just down this right pathway.\n')
	time.sleep(2)
	print('You respond with, "But the old man back there told me to go left."\n')
	time.sleep(2)
	print('"HA!! That old man has no idea what he is talking about. It is definitely to the right.\n')
	time.sleep(2)
	print('Now you have a choice.\n')
	time.sleep(2)
	fork = input('Do you want to go left or right? Print 1 for left or 2 for Right.')
	while fork != '1' and fork != '2':
		print('\nThat is not an option')
		fork = input('Do you want to go left or right? Print 1 for left or 2 for Right. ')
	if fork == '2':
		print('\nYou walk down the right path for quite a while before you stop to take a break.\n')
		time.sleep(2)
		print('Looking around, you realize that none of this area looks vaguely famiiar to you\n')
		time.sleep(2)
		print('You start to doubt your choice and the stranger.\n')
		time.sleep(1)
		if fork == '1':
			print('You decide to turn around and walk back towards the fork.\n')
			time.sleep(2)
			print('When you get there, you decide to go left instead of right.\n')
			time.sleep(3)
		fork = input('Would you like to turn around? Print 1 for yes or 2 for no')
	if fork == '2':
		print('You decide to contine down the right path and hope that the sign and the stranger were right.\n')
		time.sleep(2)
		print('It starts to get really dark out but you continue walking anyway.\n')
		time.sleep(2)
		GoodLuck('With some luck, you managed to notice the cliff before stepping over it.\nYou turn around and walk all the way back to the fork and go left instead', 'Because you cannot see in front of you, you accidentaly fall of a cliff and die.')
		return None
	time.sleep(3)
	print('\nAs you travel further and further, you start to recognize some of the scenary.\n')
	time.sleep(2)
	print('You realize that you are getting closer and closer to home.\n')
	time.sleep(2)
	print('After a couple more hours on the road, you finally see a tall stony structure ahead.\n')
	time.sleep(3)
	print('However, as you get closer and closer, you realize that your castle has been taken over.\n')
	time.sleep(3)
	print('Thankfully, there are not too many of them manning the castle right now so there is still a chance you can take it back.\n')
	time.sleep(4)
	print('Unfortunately, your guards have been taken prisoner and are stuck inside the jail unless you break them out.\n')
	time.sleep(3)
	print('You reckon that there are about 12 enemies in total guarding the castle.\n')
	time.sleep(3)
	print('After some time, you have think you have come up with three good options of how you are going to attack?\n')
	time.sleep(3)
	print('Each option has its own level of risk and it will involve fighting a certain number of enemies.\n')
	time.sleep(3)
	print('If you shoot the two guards far apart on the wall with your bow, you can climb it, but there is a chance you might fall off.\n')
	time.sleep(3)
	print('If you try to disguise yourself and sneak in, the enemies will know you are there and will attack you plus you will have to take off your armor for your disguise.\n')
	time.sleep(4)
	print('Third, you can just charge ' + Castle + ' with your sword and armor and hope for the best.\n')
	time.sleep(2)
	attack = input('Would you like to climb the wall, sneak in, or storm the castle? Print 1 for climb, 2 for sneak, and 3 for storm. ')
	while attack != '1' and attack != '2' and attack != '3':
		print('That is not an option')
		attack = input('Would you like to climb the wall, sneak in, or storm the castle? Print 1 for climb, 2 for sneak, and 3 for storm. ')
	if attack == '1':
		print('\nSo you have decided to climb the castle walls.\n')
		time.sleep(2)
		print('You take your bow and arrows out and approach the castle sneakily.\n')
		time.sleep(3)
		print('You aim the arrow at the first guard and release it.\n')
		time.sleep(3)
		number = int(random.uniform(1,11))
		if number == 10:
			print('Your arrow gets blown a litle to the right in the wind and you hit the guard in the arm and he lets out a scream. The other guards now know you are here. You must charge.\n')
			time.sleep(3)
			print('The enemies start to attack.\n')
			num = int(random.uniform(1,11))
			if num >= 9:
				print('Because of your talent with your sword and the inexperience of the enemy, you manage to kill all 12 enemies\n')
				time.sleep(3)
				print('You successfully took back your castle! Congratulations! ' + name + ', you Win!\n')
				time.sleep(2)
				PlayAgain()
				return None
			else:
				print('The enemies overwhelm you and kill you. Game Over\n')
				PlayAgain()
				return None
		else:
			print('Your arrow strikes the guard right in the chest and he silently falls over. You immeadiately turn and shoot the second guard who also falls silently.\n')
			time.sleep(4)
			print('Now you start to climb the wall.\n')
			time.sleep(2)
			#In these last few battle scenes, there are escentially random chances where
			# you are either unlucky and die, or very lucky and you succeed
			num = int(random.uniform(1,11))
		if num <= 7:
			print('You successfully climb the wall without being noticed')
			Battle()
			return None
		else:
			print('You could not hold onto the walls smooth surfaces.\n')
			print('Game Over\n')
			again = input('Play Again? Print Y/N ')
			if again == 'Y':
				Game()
	if attack == '2':
		print('You have decided to sneak into the castle.\n')
		time.sleep(2)
		print('You put on a disguise as a commoner and walk towards the gate.\n')
		time.sleep(2)
		num =int(random.uniform(1,11))
		if num <= 8:
			print('The enemies open the gates and let you in\n')
			Battle()
			return None
		else:
			print('The enemies realize who you are and attack.\n')
			num = int(random.uniform(1,11))
			if num >= 9:
				print('Because of your talent with your sword and the inexperience of the enemy, you manage to kill all 12 enemies\n')
				time.sleep(3)
				print('You successfully took back your castle! Congratulations! ' + name + ', you Win!\n')
				PlayAgain()
				return None
			else:
				print('The enemies overwhelm you and kill you. Game Over')
				PlayAgain()
				return None
	if attack == '3':
		print('You have decided to storm the castle.\n')
		time.sleep(2)
		print('You put on your armor and walk towards the gate.\n')
		time.sleep(2)
		print('The enemies spot you and the battle begins.\n')
		time.sleep(2)
		num = int(random.uniform(1,11))
		if num <= 7:
			print('Your armor blocks all of their blows and you easily cut the enemies down\n')
			time.sleep(3)
			print('You successfully took back your castle! Congratulations! ' + name + ', you Win!\n')
			PlayAgain()
			return None
		else:
			print('The enemies overwhelm you and kill you. Game Over')
			PlayAgain()
			return None


Game()
#this is to actually run the function