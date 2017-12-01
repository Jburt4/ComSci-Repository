#Fibonacci Sequence
# fib(0)=0
# fib(1)=1
# fib(2)=1
# fib(3)=2
# fib(4)=3
# fib(5)=5
#pattern:[fib(n)=fib(n-1)+fib(n-2)]

# def fib(n):
# 	if n<2:
# 		return n
# 	else:
# 		return fib(n-1)+fib(n-2)

# print(fib(int(input('fib'))))

#factorial(4) = 24
#pattern:[fac(n)=n(n-1)(n-2)...(1)]
def factorial(n):
	if n < 2:
		return 1
	else:
		return factorial(n-1)*n

print(factorial(int(input('What would you like to take the factorial of?'))))