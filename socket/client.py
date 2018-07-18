# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
for i in range(50000):
	sock.send(b'hello, world!\n'+byte(i))

data = sock.recv(1024)
sock.close()

print (data)