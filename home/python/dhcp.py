f1 = open("result.txt", 'w')

line = open("prospect.txt").readlines()#[2]
#print line.split("\t")
for i in line:
	#i=i.replace(":","") #убераем двоеточие из маков
	#macaddr=i.split(";")[1]
	comment=i.split("\t")[3]
	a="Netsh DHCP server scope 10.22.4.0 add reservedip " + i.split("\t")[0] +" " + i.split("\t")[1]+ " " + i.split("\t")[2] + " "+ '"'+ comment[0:-1] + '"'+" BOTH\n"
	#print(a) 
	f1.write(a)