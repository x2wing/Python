from string import maketrans

f=open("in.csv", "r")
a=f.read()
g=open("slovar.txt", "r")
num=g.readlines()

for y in num:
	a=a.replace(y.strip(), 'W'+y.strip())

	#print a
f.close()
f=open("out.csv", "w")
f.write(a)
f.close()
g.close()

