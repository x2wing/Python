# -*- coding: utf-8 -*- 
import numpy 


def checker(V):
	for i in range(1,len(V)):
		if V[i-1]>V[i]:
			print("сортировка говно")
			return

def BubleSort(V):
	counter=0
	for i in range(V.__len__()):
		#print(len(V))
		F=0
		for j in range(1,V.__len__()-i):
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
	for i in range(1,V.__len__()):
		j=i
		
		while j>0 and V[j]<V[j-1]:
			counter+=1
			V[j-1],V[j]=V[j],V[j-1]
			j-=1

				
	print("counter=",counter)




		



def SelectSort(arr):
	counter=0
	i = len(arr)
	while i > 1:
		max = 0
		for j in range(i):
			counter+=1
			if arr[j] > arr[max]:
				max = j
		arr[i-1], arr[max] = arr[max], arr[i-1]
		i -= 1
	print("counter=",counter)


def ShellSort(a):
	counter=0
	def new_increment(a): 
		i = int(len(a) / 2)
		yield i
		while i != 1:
			
			if i == 2:
				i = 1
			else:
				i = int(numpy.round(i/2.2))
			yield i
	for increment in new_increment(a):
		for i in range(increment, len(a)):
			for j in range(i, increment-1, -increment):
				counter+=1
				if a[j - increment] < a[j]:
					break
				a[j],a[j - increment] = a[j - increment],a[j]
	print("counter=",counter)
      







Vect=numpy.random.randint(0, 3000000, 1000000)
#Vect=[10,9,8,2,3,4,5,3,2,1]
#VectCopy=Vect[:]
print("not sorted",Vect)
#checker(Vect)
ShellSort(Vect)
#BubleSort(VectCopy)
checker(Vect)
#checker(VectCopy)
print("sorted", Vect)
#print("sorted", VectCopy)
