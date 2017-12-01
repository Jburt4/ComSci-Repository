import random
Mylist = []
x = 0
while x < 10:
	x = x + 1
	num = int(random.uniform(1,101))
	if num%3 == 0:
		print(num)
	else:
		Mylist.append(num)

print(sorted(Mylist))
