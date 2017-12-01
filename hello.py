# Hello, World!

import sys

# What does end='' do in the print statement?
# Respond here: It makes it so that the output stays on the same line.

print('Hello, ', end='')
print(sys.argv[1], end='')
print(', ', end='')
print(sys.argv[2], end='')
print(', and ', end='')
print(sys.argv[3], end='')
print('! Welcome.')
# To run this code: Type Python hello.py Meghan Ned Francie
