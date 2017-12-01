# Hello, World!

import sys

print('Hello,', end='')
print(sys.argv[1], end='')
print('!')

response = input('Where are you from? ')
print('That is so cool. '+response+' is a really interesting place. I am from Concord Massachusetts.')

response = input('What do you like to do? ')
print('Me too! I also like to play hockey.')

response = input('What is your favorite movie? ')
print('That is a good movie, but I prefer Kung Fu Panda.')
