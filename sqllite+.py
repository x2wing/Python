# -*- coding: utf-8 -*-"
import sqlite3
###################################foo####################################
def FillTable(TableName):
    for i in range(1000):
        sqlcommand = 'INSERT INTO ' + TableName + ' (data) VALUES(' + str(i) +')'
        cur.execute(sqlcommand)
    con.commit()
# заполнение таблицы
def Fill2T(TableName, info):
    #i=info
    sqlcommand = 'INSERT INTO ' + TableName + ' (data) VALUES(' + str(info) +')'
    cur.execute(sqlcommand)
    con.commit()

#вывод содержимого таблицы
def ReadTable(TableName):
    sqlcommand='SELECT * FROM ' + TableName
    cur.execute()
    data = cur.fetchall()
    for i in data:
        print (i)

#очистка таблицы
def ClearTable(TableName):
    cur.execute("DELETE FROM " + TableName)
    con.commit()
###################################/foo####################################


TName = 'TableInt'
con = sqlite3.connect('users.db')
cur = con.cursor()
#cur.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, firstName VARCHAR(100), secondName VARCHAR(30))')



#con.commit()
ClearTable(TName)
#for i in range(10):
Fill2T(TName, 5)




con.close()