import pycurl

import StringIO
data = StringIO.StringIO()

curl = pycurl.Curl()

curl.setopt(pycurl.URL, 'csdb.ufanet.ru')
#curl.setopt(pycurl.WRITEFUNCTION, data.write)
curl.setopt(pycurl.VERBOSE, True)
curl.perform()

curl.close()

#print data.getvalue()
#print help(data)