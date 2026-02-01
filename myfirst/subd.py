import sqlite3


db = sqlite3.connect('db.sqlite3')
s = db.cursor()

v = s.fetchall()
for ver in v:
        print(ver)
db.close()
