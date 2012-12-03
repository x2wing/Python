def foo2(x,y,z):
	return (x<=y and x<=z) and x or (y<=z and y or z)

for x in xrange(30):
	for y in xrange(30):
		for z in xrange(30):
			print str(x) + " " + str(y) + " " + str(z) + " " + str(foo2(x,y,z))
