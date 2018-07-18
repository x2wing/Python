

#for i in range(500):
#	print(3**i %17)

# Общие параметры
A=56498789798798494
P=5646847978461587987467897897564232

# секретные ключи
X1=1684
X2=8645
def DH(A,P,X1,X2):
	#открытые ключи
	Y1=A**X1%P
	Y2=A**X2%P
	#общие секретные ключи
	Z1=Y2**X1%P
	Z2=Y1**X2%P
	if (Z1==Z2):
		return Z1

print(DH(A,P,X1,X2))

R1=30.0
R2=150000.0
print(R1*R2/(R1+R2))
'''print('A =',A)
print('P =',P)
print('X1 =',X1)
print('X2 =',X2)
print('Y1 =',Y1)
print('Y2 =',Y2)
print('Z1 =',Z1)
print('Z2 =',Z2)
'''

