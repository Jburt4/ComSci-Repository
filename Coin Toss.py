import sys
import random

n =int(input('How many times would you like to flip a coin?'))
z = 0
for x in range(1,n):
	y = int(random.randrange(0,2))
	if y == 1:
		z = z + 1
print(z)
print((z/n)*100, '% Heads')
#n = 10, 30% Heads
#n = 100, 54% Heads
#n = 1000, 51.2% Heads
#n = 10000, 49.48% Heads
#n = 100000, 50.144% Heads
#n = 1000000, 49.9431% Heads
#This shows that as the numbers of samples increases, the percent
# of heads gets closer to 50%. So as the number of samples increases
# the less random it becomes.