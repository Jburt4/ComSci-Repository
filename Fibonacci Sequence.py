import math

terms = int(input('How many terms in the fibonacci sequence do you want?'))
n = 0
value = 0
value2 = 1
while n < terms:
	value3 = value + value2
	print(value3)
	value = value2
	value2 = value3
	n = n + 1