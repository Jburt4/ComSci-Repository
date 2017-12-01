import random
EmptyList = []
NewList = [1,2,3,4]
NewList.append(5)
print(NewList)

#use NewList.remove to remove a value
#use NewList.pop to remove a place in the list
#NewList.pop(int(input('A Place in the list\n')))
#print(NewList)

#Accessing the last value in the list
#print(NewList[-1])

NewList.insert(3,7)

print(NewList)

#Finding the length of a function
print(len(NewList))

a = NewList[0]
b = NewList[1]

#This removes the old numbers in these poistions
NewList.pop(0)
NewList.pop(1)
#This adds the new numbers to those positions
NewList.insert(0,b)
NewList.insert(1,a)

print(NewList)

for x in range (0,100):
	EmptyList.append(x*7)
print(EmptyList)
print(EmptyList[int(random.uniform(0,101))])

