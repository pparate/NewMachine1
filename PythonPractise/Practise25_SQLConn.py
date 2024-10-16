#  pip install mysql-connector
import mysql.connector

mydb = mysql.connector.connect(host='', user='', passwd='', database='')

mycursor = mydb.cursor()

mycursor.execute('select * from table')

for i in mycursor:
    print(i)  # each row

mycursor.execute('select * from table')

result = mycursor.fetchall()  # fetchone
for i in result:
    print(i)  # each row
