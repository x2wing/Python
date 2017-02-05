# -*- coding: utf-8 -*- 
import numpy as np 


def checker(V):
	for i in xrange(1,len(V)):
		if V[i-1]>V[i]:
			print("сортировка говно")
			return

def BubleSort(V):
	counter=0
	for i in xrange(V.__len__()):
		#print(len(V))
		F=0
		for j in xrange(1,V.__len__()-i):
			counter+=1
			if V[j-1]>V[j]:
				V[j-1],V[j]=V[j],V[j-1] # обмен
				F=1
				
		if F==0:
			print("counter=",counter)
			return
	print("counter=",counter)

def InsertionSort(V):
	counter=0
	for i in xrange(1,V.__len__()):
		j=i
		
		while j>0 and V[j]<V[j-1]:
			counter+=1
			V[j-1],V[j]=V[j],V[j-1]
			j-=1
		# for j in xrange(i,0,-1):  #for (j=i;)
		# 	counter+=1
		# 	if V[j]<V[j-1]:
		# 		V[j-1],V[j]=V[j],V[j-1]

				
	print("counter=",counter)




		



def SelectSort(arr):
	counter=0
	i = len(arr)
	while i > 1:
		max = 0
		for j in xrange(i):
			counter+=1
			if arr[j] > arr[max]:
				max = j
		arr[i-1], arr[max] = arr[max], arr[i-1]
		i -= 1
	print counter










Vect=np.random.randint(0, 100000, 10000).tolist()
#Vect=[10,9,8,2,3,4,5,3,2,1]
VectCopy=Vect[:]
print("not sorted",Vect)
#checker(Vect)
SelectSort(Vect)
BubleSort(VectCopy)
checker(Vect)
checker(VectCopy)
print("sorted", Vect)
print("sorted", VectCopy)
