import random
import sys
speed = int(random.uniform(30,101))

print(speed)
print('This is how fast you were going.')
if speed < 61:
	print('You are free to go. Continue to drive safely.')
elif speed < 66:
	print('You are lucky it is your birthday. You were speeding but im going to let you go.')
elif speed < 81:
	print('You were speeding out there. I am going to have to give you a ticket. Drive slower.')
elif speed < 86:
	print('You were speeding very fast. You are lucky that its your birthday otherwise you would be getting a big ticket.')
else:
	print('You were going way too fast. What do you think you were doing out there? I am going to have to give you a big ticket.')
