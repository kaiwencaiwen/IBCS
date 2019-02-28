import sqlite3
db=sqlite3.connect('test.db')
cursor=db.cursor()
#cursor.execute("CREATE TABLE account(id INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT )")
cursor.execute(""" INSERT INTO account (id,firstname,lastname)
					VALUES(?,?,?)""", (1,"Ted","Erg"))
db.commit()
db.close()