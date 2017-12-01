def subtract(a,b):
	try:
		a = int(a)
		b = int(b)
		return a-b
	except TypeError:
		print('Wrong Data Type')
		return None

subtract('1','2')

# Subtract('a','b') --> None
# Subtract('1','2') --> -1
# Subtract(1,'2')  --> -1
# Subtract(1,2)   --> -1
# Subtract('a',2)  --> None