l=" "
f=open("csdb.ufanet.ru.access_log", "r")
while l:
	l=f.readline()
	if l.count("83.169.60.25"):
		print l +'\b'