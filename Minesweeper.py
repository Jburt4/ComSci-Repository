import sys
import random

#inputs for rows, columns and bombs
rows = 20
columns = 15

#the array for the board
game = []
for x in range(rows):
	row =['~~~']*columns
	game.append(row)


r = int(random.uniform(10, 19))
c = int(random.uniform(10, 14))
game[r][c] = 'RUS'
game[10][2] = 'USN'

for e in range(rows):
	for d in range(columns):
		print(game[e][d], end = ' ')
	print()

d = int(((c-2)**2+(r-10)**2)**0.5)
print(str(d) + ' Kilometers from target')



#Successes
#I managed to print the bombs into the array in a random position
#The board now prints on different lines

#Problems
#I don't know how to change the numbers based on the bomb's position

