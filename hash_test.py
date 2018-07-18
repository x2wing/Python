import hashlib
'''
#print hashlib.sha256("Nobody inspects the spammish repetition").hexdigest()
for i in xrange(10000000,99999999):
    x=str(i)
    a='5213'+x+'3455'
    b=hashlib.sha256(a).hexdigest() 
    if b=="c927a991effb2d4f42d12b83d1e2347821c9419cbf6c2fb6a1dfe5289c9c6ff1":
        print a
'''



