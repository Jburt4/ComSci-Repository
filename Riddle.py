import sys

riddle = input("Mary's mother has five daughters. The first four are named Nana, Nene, Nini, and Nono. What is the name of the fitfh daughter?")
while riddle !='Mary':
	print('You answered wrong. Guess Again')
	riddle = input('What is your next guess? Also, do not forget to start the name with a capital letter.')
print('Correct! Mary is the name of the fifth daughter.')

