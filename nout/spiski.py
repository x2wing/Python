

def inter(*args):
	result=[]
	for first in args[0]:
		for spisok in args[1:]:
			if not first in spisok:
				break
			else: 
				result.append(first)

	return notduble(result)

def notduble(spisok):
	spisok=spisok[::]
	for i in spisok[::-1]:
		if spisok.count(i)>1:
			print(i, spisok.count(i))
			for j in range(spisok.count(i)-1):
				spisok.remove(i)
	return spisok

def notduble2(spisok):
	return list(set(spisok))

	
spisok=[8,1,2,3,5,5,5,5,"jghg",2,7,9,4,2,4,1,3,7,7,7,4,8,]
#spisok.remove(2)
#print(spisok.remove(9),spisok)
#print(help([]))
print(notduble(spisok))
print(notduble2(spisok))
print(spisok)
print(spisok[::-1])
#print(len(notduble2(spisok)))
#print(inter([-6,0,1,1,1,10,"abc",56,908,3,-76.645,98,3,7,5],["abc",5,7,3,8,1,-6,9,7,-76.645]))
