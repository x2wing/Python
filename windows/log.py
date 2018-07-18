#!/usr/bin/env python3
import subprocess
import os

#with open('log.txt', 'wb', 0) as file:
#    subprocess.run('ps.cmd', stdout=file, check=True)

def binSearch(lst, x):
    l = 0
    r = len(lst)
    while r - l > 1:
    	#print("left " + l + " right " +r)


        m = (l + r) // 2 # Целочисленный тип в Python имеет неограниченную длину
        if x < lst[m]:
            r = m
        else:
            l = m
    return l if lst[l] == x else None # если элемент не найден, возвращаем None

lst = sorted([2,5,6,7,2,1,5,6,7,1,2,3,4,7,9])
x = 5
print(binSearch(lst, x))

print(35420.00*0.13)
print(51.5/4.5)
#r = subprocess.call("ps.cmd",shell=True) 
#print(r)