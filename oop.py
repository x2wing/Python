class B(object):
	arg = 'Python'
	def g(self):
		return self.arg


if __name__ == '__main__':
	b = B()
	print(b.g())
