import sys

poll =[]
num = int(input('How many people are taking the poll?'))
for d in range(num):
	row = [input('What is your name?')]
	poll.append(row)
	row1 = [input('Where are you from?')]
	poll.append(row1)
	row2 = [input('Do you prefer unicorns or narwhals?')]
	poll.append(row2)
	row3 = [input('Did you like the red cross presentation?')]
	poll.append(row3)
	row4 = [input('Did Henry Lockwood steal my question?')]
	while row4 != 'Yes' and row4 != 'yes':
		print('Wrong!')
		row4 = [input('Did Henry Lockwood steal my question?')]
	poll.append(row4)

print(poll)

