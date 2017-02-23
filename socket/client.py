import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host =( 'localhost', 8007)
s.connect(host)
s.send(b'hello1')  
data = s.recv(1000000) 
print ('received', data, len(data), 'bytes')
s.close()