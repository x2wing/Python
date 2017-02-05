def myzip(*seqs):
	seqs = [list(S) for S in seqs]
	
	res = []
	while all(seqs):
		res.append([S.pop(0) for S in seqs])
	return res

A = myzip([5,2,3], [1,2,3], [1,2,3], [1,2,3,78])
print (A)


