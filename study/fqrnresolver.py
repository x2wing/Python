# nslookup on python
import socket; 
IP =[ 
'10.22.4.27',
'10.22.4.47',
'10.22.5.81',
'10.22.4.87',
'10.22.5.114',
'10.22.5.117',
'10.22.4.131',
'10.22.5.146',
'10.22.4.150',
'10.22.4.157',
'10.22.4.188',
'10.22.5.214',
'10.22.5.234',
'10.22.7.108',
'10.22.7.114',
'10.22.7.147',
'10.22.7.151',
'10.22.7.184',
'10.22.7.235',
'10.22.7.227',
'10.22.5.250'
]
for i in IP:
	result = socket.gethostbyaddr(i)
	print(result[0])

