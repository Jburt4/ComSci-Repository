# Hello, World!

import sys

print('Hello,', end='')
print(sys.argv[1], end='')
print('!')

response = input('What is your favorite food? ')

print('Mmm! '+response+' is delicious')