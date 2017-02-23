import socket
import sys
import sqlite3


TName = 'socktest'

sqlcon = sqlite3.connect('users.db')
cur = sqlcon.cursor()
cur.execute('create table if not exists ' + TName +  ' (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, datanet VARCHAR(100))')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host =( 'localhost', 8007)



s.bind(host)
s.listen(1)
conn, addr = s.accept()
data = conn.recv(1000000)
dataS = data.decode("utf-8")
print(dataS)
cur.execute('INSERT INTO socktest  VALUES(NULL ,?)', (dataS,))
sqlcon.commit()
sqlcon.close()


#print ('client is at', addr , data)
conn.send(data)
#z = raw_input()
conn.close()
