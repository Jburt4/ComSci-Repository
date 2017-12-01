import sys

x = float(input('X Value'))
y = float(input('Y Value'))
z = float(input('Z Value'))

result = bool(x<y<z)
final = bool(x>y>z)

Answer = result or final
print(Answer)