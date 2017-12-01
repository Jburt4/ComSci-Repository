for number in range (1,1001):
	for x in range (2,number):
		if (number%x == 0):
			break
		else:
			print(str(number) + ', ')

