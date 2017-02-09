
def seq(MaxCountChar=4, start=0, end=100 ):
	spisok =[]
	for i in range(start,end):
		Count_Ledir_Noley = MaxCountChar - len(str(i))
		spisok += ['0'* Count_Ledir_Noley + str(i)]
	return spisok

i=seq(5)

print(seq(5))


'''
for i in range(10,11):
	FIRSTNAME="123.txt"
	SECONDNAME="2.txt"

	#FIRSTNAME="transactions.txt.0" + str(i)
	#SECONDNAME="transactions.txt.0" + str(i+1)
	#SECONDNAMEtmp="transactions.txt.0" + str(i+1) + ".csv"


	myfile = open(FIRSTNAME, 'a') 
	myfile.write(open(SECONDNAME).readlines()[0])
	myfile.close()

	f=open(SECONDNAME,'r')
	f.readline()  #read firs string and forgot it
	newf=open(SECONDNAME,'w')
	newf.write(f.read())
	f.close()
	newf.close()

'''

"""
for i in range(1,8):
	FIRSTNAME="transactions.txt.00" + str(i)
	SECONDNAME="transactions.txt.00" + str(i+1)
	SECONDNAMEtmp="transactions.txt.00" + str(i+1) + ".csv"


	myfile = open('transactions.txt.001', 'a') 
	myfile.write(open("transactions.txt.002").readlines()[0])
	myfile.close()

	f=open(SECONDNAME,'r')
	f.readline()  #read firs string and forgot it
	newf=open(SECONDNAMEtmp,'w')
	newf.write(f.read())
	f.close()
	newf.close()
"""