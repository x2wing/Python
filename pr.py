import math
def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped
 
def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
def test():
	return ("test")

#a = makebold(test)
#print (a)
#print (makeitalic(a)())
#for i in range(9):
#	print (i*32)


#print ((23000-10000)*12*3)
#print (13000*12*3)
#print (48000.0*32*120*4/(8*1024*1024))

#S = "spam"
#for i in dir(S):
#	print (i)
#for i in [0,1,2,3]:
#	print (S[i])
#print("\0\0")
#M = [[1,1,1],
#	[2,2,2],
#	[3,3,3]]
#M.append([4,4,4])
#A=map(sum,M)
#print(list(A))
'''C=[1,2,3]
D={"c":1,'b':2,'a':3}
E=["q","i","u","y","r","w"]
F={"q":1,'w':2,'e':3}
F.get("a",3)
T = (1, 2, 3, 4, 10,"w")
G = {"q","i","u","y","r","w"}
H = set(T)

A=1+5j
B=2+10j
c=9999999999999999999999999999999
#print(c.bit_length())
i="ОАОА"
A=[i for i in range(10)]
print(A)
for i in A:
	if((int(str(A[i])+"8"+str(A[i]))/6)%1==0):
		print (i)'''

#a=("" + "[1,[2,3,[4],5],6,[7]]").split(',')

print(6.96*10**8/(1.737*10**6))

print(1.496*10**11/(3.844*10**8))
#print(33*20000)
print(30*1600)

print(0.90/300*100)
print(45/25000*100)
print(2.2/300*100)
print(1.5*2.48)


'''
418
624 
iptables -I INPUT -s 10.22.5.222 -j ACCEPT
iptables -I INPUT -s 10.22.5.245 -j ACCEPT
iptables -I INPUT -s 10.22.5.220 -j ACCEPT


auto eth0
iface eth0 inet static
address 10.22.5.250
netmask 255.255.252.0

'''

