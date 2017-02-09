# -*- coding: utf-8 -*-"
import sqlite3

con = sqlite3.connect('users.db')
cur = con.cursor()

fd = open('user.txt', 'w')

    


#вывод
cur.execute('SELECT * FROM TableInt')
data = cur.fetchall()
for i in data:
    fd.write(i + '\n')
con.close()
fd.close()
