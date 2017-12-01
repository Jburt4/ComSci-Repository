class RationalNumber:
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def __str__(self):
		return str(self.a)+'/'+str(self.b) + '  ' + str(self.a/self.b)
	def __add__(self,other):
		a = self.a*other.b + self.b*other.a
		b = self.b*other.b
		return RationalNumber(a,b)
	def __sub__(self,other):
		a = self.a*other.b - self.b*other.a
		b = self.b*other.b
		return RationalNumber(a,b)
	def __mul__(self,other):
		a = self.a*other.a
		b = self.b*other.b
		return RationalNumber(a,b)
	def __truediv__(self,other):
		a = self.a*other.b
		b = self.b*other.a
		return RationalNumber(a,b)
	__repr__ = __str__
def main():
	c = RationalNumber(1,2)
	d = RationalNumber(1,3)
	print(c)
	print(d)
	print(c+d)
	print(c-d)
	print(c*d)
	print(c/d)

main()
