
l = input('Word')
def clean(l):
	letters = []
	for x in l:#This checks to see if a letter,x, is in the input
		if not(x in letters):#If that x is not in list letters
			letters.append(x)#Then it adds the x to the list, letters
	return letters
print(clean(l))

#Canvas Answer
# def stringclean(str):
# 	if len(str) < 2:
# 		return str
# 	else:
# 		if (str[0] == str[1]):
# 			return stringclean(str[1:])
# 		else:
# 			return str[0]+stringclean(str[1:])
