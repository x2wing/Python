class Mcsv:
	def __init__(self,*args):
		self.args=list(args)
		self.a=1
		self.b=2
		self.c=3
	def foo(self):
		print("test")


A = Mcsv(1,2,3,4,5,6)
for key in A.__dict__:
	print(key, "->",A.__dict__[key])

