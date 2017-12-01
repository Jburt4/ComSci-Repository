import math
import random
def square(num):
	return num**2



def distance(x, x1, y, y1):
	d = math.sqrt(square(x - x1)+square(y - y1))
	return d



def coinFlip(fixed = 0):
	if random.random()<.5 or fixed == 1:
		return 'Heads'
	return 'Tails'



n = int(input('number'))

def subtract(a,b):
	try:
		return a-b
	except TypeError:
		print('Wrong Data Type')
		return None


Subtract('a','b') --> None
Subtract('1','2') --> -1
Subtract(1,'2')  --> -1
Subtract(1,2)   --> -1
Subtract('a',2)  --> None