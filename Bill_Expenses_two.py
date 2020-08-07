import sqlite3

connect= sqlite3.connect("sasatechDB.db")

cursor = connect.cursor()

cursor.execute("SELECT * from employee_information")
result=cursor.fetchall()

for i in result:
    print(i)
