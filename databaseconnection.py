import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="0123456789kvc",database="phonenumber")
mycursor=mydb.cursor()
mycursor.execute("select * from person")
result=mycursor.fetchall()
for i in result:
    print(i)

""""
to show all databases

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="0123456789kvc")
mycursor=mydb.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)
"""