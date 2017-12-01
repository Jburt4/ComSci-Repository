import sys

g = int(input('What was your grade?'))

if g > 89:
	print('You got an A! Excellent Work!')
elif g > 79:
	print('You got a B. Good Work.')
elif g > 69:
	print('You got a C. Work to improve your score.')
elif g > 59:
	print('You got a D. That is bad. Do better.')
else:print('You got an F. If i see you at Mcdonalds just know that I like my quarter pounders plain')