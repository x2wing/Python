f1 = open("result.txt", 'w')

line = open(u"shafieva.csv.txt").readlines()#[2]
#print line.split("\t")
for i in line:
	i=i.replace(":","")
	a=i.split(";")
	#print(a) 
	f1.write(a)