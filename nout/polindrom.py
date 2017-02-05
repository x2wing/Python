import sys
def reverse(text):
	return text[::-1]

def is_palindrome(text):
	return (text == reverse(text))

def inputtext():
	#print('please input text:')
	return "fu@c,k: cuf"#sys.stdin.readline()

def triming():
	TrimCharset = (' ','.','?','!',':',';','-','-','(',')','[',']','...',',','_','@') 
	OUT = inputtext().strip()
	for i in TrimCharset:
		OUT = OUT.replace(i, '')
		#print(OUT)
	return OUT


#print triming()

something = triming()
print(something)

if (is_palindrome(something)):
	print("yes, it's polindrom")
else:
	print("no, it's not polindrom")

