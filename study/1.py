import itertools
import random
import sys
import os

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

# print([x for x in map(lambda x, y: [x**2, y**2], [1,2],[3,4])])
	
# A = [[i*j for i in range(1,10)] for j in range(1,10) ]
# print(A)

# print (list(itertools.accumulate([1,2,3,4,5])))
# B = [1,2,3,4,5,6,7]

# A = itertools.chain([1,2],[4,5],[6,7])
# print(list(A))

# print(list(itertools.permutations(B,2)))

# import webbrowser
# webbrowser.open_new_tab('http://habrahabr.ru/') 

# with open("test_seen.log", 'r') as f:
# 	for line in f:
# 		linelist=line.split(" ")
# 		if linelist[1] == '7' and linelist[0] == '1' and linelist[4] == 'Olimpieva':
# 			print(line, end='')

class CLS(object):
	pass

TestMassive = [i for i in range(15)]
def testing(TestMassive):
	return TestMassive[choice(TestMassive)]

if __name__ == '__main__':
	print(sys.getdefaultencoding())
	print(sys.stdout.encoding)
	# print(''.join((random.sample('1234567890abcdefghiklmnoprstuyqwxz', 7))))
	# a=['a','b','c','d']
	# a[1:3]=['x','y','z']
	# print(a)
	# a = "input test tuple".split()
	# a.reverse()
	# b = ' '.join(a)
	# print(b)
	# a="test"
	# print(*a, sep='&')
	B = b'spam'          # Создаст объект bytes (8-битные байты)
	S = b'sadf'           # Создаст объект st-
                        # (символы Юникода, 8-битные или многобайтовые)
A = {1:10, 2:20}
print(A.key_values())
