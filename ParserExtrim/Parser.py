# -*- coding: utf-8 -*-
from string import maketrans
f=open("spisok.txt", "r")
a=f.read()

a=a.replace("www", "AAAAAAAAAAAAAAA")

f=open("out.txt", "w")
f.write(a)
f.close()