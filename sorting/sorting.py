# -*- coding: utf-8 -*- 
import numpy 
import time


def checker(V):
    for i in range(1, len(V)):
        if V[i-1] > V[i]:
            print("Sorting is Shit")
            return False
    return True




def TimeOfWork(infoo, V):
    t1 = time.clock()
    infoo(V)
    print(time.clock()-t1)

def BubleSort(V):
    counter = 0
    for i in range(V.__len__()):
        #print(len(V))
        F = 0
        for j in range(1, V.__len__()-i):
            counter += 1
            if V[j-1] > V[j]:
                V[j-1], V[j] = V[j], V[j-1] # обмен
                F = 1
        if F == 0:
            print("counter=", counter)
            return
    print("counter=", counter)

def InsertionSort(V):
    for i in range(1, V.__len__()):
        j = i
        while j > 0 and V[j] < V[j-1]:
            V[j-1], V[j]=V[j], V[j-1]
            j -= 1

                
    


def GnomeSort(arr):
    i = 1
    while i < len(arr):
        if not i or arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1



def SelectSort(arr):
    counter = 0
    i = len(arr)
    while i > 1:
        max = 0
        for j in range(i):
            counter += 1
            if arr[j] > arr[max]:
                max = j
        arr[i-1], arr[max] = arr[max], arr[i-1]
        i -= 1
    print("counter=", counter)

def MergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        MergeSort(lefthalf)
        MergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1



def ShellSort(a):
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
                if a[j - increment] < a[j]:
                    break
                a[j], a[j - increment] = a[j - increment], a[j]





Vect1=numpy.random.randint(-50, 50, 3000).tolist()
#print("not sorted",Vect1)
#TimeOfWork(InsertionSort, Vect1)
numpy.random.shuffle(Vect1)
TimeOfWork(ShellSort, Vect1)
numpy.random.shuffle(Vect1)
TimeOfWork(MergeSort, Vect1)




#if checker(Vect1):
    #print("sorted", Vect1)


'''
Vect2=numpy.random.randint(-50000, 50000, 30000)



TimeOfWork(MergeSort, Vect1)
checker(Vect1)
print("sorted", Vect1)
'''
#numpy.random.shuffle(Vect1)
#Vect=[10,9,8,2,3,4,5,3,2,1]
#VectCopy=Vect[:]
# print("not sorted",Vect1)
# print("not sorted",Vect2)
# #checker(Vect)
# print("сортировка int32")

# print("сортировка byte")
# TimeOfWork(ShellSort, Vect2)
# #BubleSort(VectCopy)
# checker(Vect1)
# checker(Vect2)
# #checker(VectCopy)
# 
# print("sorted", Vect2)
#print("sorted", VectCopy)
