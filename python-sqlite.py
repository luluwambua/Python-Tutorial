import sqlite3

connection = sqlite3.connect('hello.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE HELLO(GREETING)''')
cursor.execute('''INSERT INTO HELLO VALUES('hello')''')
connection.commit()
connection.close()