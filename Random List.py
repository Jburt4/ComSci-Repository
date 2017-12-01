import random

# Mylist = []
# for x in range (0,101):
# 	Mylist.append(int(random.uniform(0,101)))
# print(Mylist)

#print(sorted(Mylist))
Newlist = []
for x in range (1,101):
	Newlist.append(x)
print(Newlist)
w = 1
while w < 101:
	Newlist.remove(w)
	Newlist.append(w)
	w =w +2
print(Newlist)