import random
Mylist = []
x = 0
while x < 10:
	x = x + 1
	num = int(random.uniform(1,101))
	Mylist.append(num)

a = Mylist[0]
b = Mylist[2]
c = Mylist[4]
d = Mylist[6]
e = Mylist[8]

Mylist.remove(a)
Mylist.remove(b)
Mylist.remove(c)
Mylist.remove(d)
Mylist.remove(e)

Mylist.sort()

NewList = [a,b,c,d,e]

NewList.sort()

a2 = NewList[4]
b2 = NewList[3]
c2 = NewList[2]
d2 = NewList[1]
e2 = NewList[0]

Mylist.insert(0,a2)
Mylist.insert(2,b2)
Mylist.insert(4,c2)
Mylist.insert(6,d2)
Mylist.insert(8,e2)

print(Mylist)