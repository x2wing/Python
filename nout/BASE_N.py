#difrent base

def inbase(chislo1, base1, base2):
	Dec=int(chislo1,base1)
	if base2==2:
		return bin(Dec)
	elseif base2==8:
		return oct(Dec)
	elseif base2==16:
		return hex(Dec)
	else:
		return "fail might be base=2 or 8 or 16 only"
