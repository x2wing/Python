""" fibonachi """

def fib(n):
	a, b= 0,1
	while b<n:
		print b
		a,b =b, a+b
		


def fib1(n):
	result=[]
	a, b= 0,1
	while b<n:
		result.append(b) 
		a,b =b, a+b
	return result

for i in range(128):
	print unichr(i)


