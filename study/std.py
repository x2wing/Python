#-*- coding: utf-8 -*-
import sys
from pprint import pprint
import codecs
print(sys.stdout.encoding)
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


with open('1.txt', "w") as fd:
	fd.write('ПРИВЕТ!')

with open('1.txt', "r") as fd:
 	for i in fd:
 		pprint(i)
