import sys
#Worked with Henry
global num
num =[]
def addition(n):
	if n < 1:
		print(sum(num))
	else:
		dig = n%10
		n = n // 10
		num.append(dig)
		addition(n)
addition(int(input('Number')))

