import random

v = random.uniform(0,101)
w = random.uniform(0,101)
x = random.uniform(0,101)
y = random.uniform(0,101)
z = random.uniform(0,101)

avg = (v+w+x+y+z)//5
minumum = max(v,w,x,y,z)
maximum = min(v,w,x,y,z)
print(avg)
print(minumum)
print(maximum)
print(v)
print(w)
print(x)
print(y)
print(z)