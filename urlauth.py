import  urllib2

#print sys.modules
#print urllib2
f = urllib2.urlopen('http://csdb.ufanet.ru')

#auth_handler = urllib2.HTTPBasicAuthHandler()
print f.read()
