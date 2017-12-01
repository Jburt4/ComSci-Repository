import sys

y = int(input('Year'))
m = int(input('Month'))
d = int(input('Day'))

a = y - (14 - m) // 12
x = a + (a//4) - (a//100) + (a//400)
b = m + 12 * ((14 - m) // 12) - 2
c = (d + x + (31*b)// 12)%7


if c == 0:
	print('Sunday')
if c == 1:
	print('Monday')
if c == 2:
	print('Tuesday')
if c == 3:
	print('Wednesday')
if c == 4:
	print('Thursday')
if c == 5:
	print('Friday')
if c == 6:
	print('Saturday')
# I think that the formula from canvas does 
# not give the right numbers. Everything else
# in my code works, but the numbers only work 
# sometimes.