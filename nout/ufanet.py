#! /usr/bin/python
#print((700000+4841.66)*0.083/12)

def foo(x):
	print(x**2)
M ="fuck you"

def writefile(filename, stri):
	f = open(filename, 'w')
	f.write(stri)
	f.close()

def readfile(filename):
	return open(filename).read()


writefile('test34', "privet111")
print readfile('test34')
#slovari
#D = {'a' : 1, 'b':2, 'c':3}
#a = D['a']=10 if D['a']==2 else 0
M=('a',2, [1,2,3,4,5])
M[2].append(5)
print (M)

#print(4809.01+4934.52)



