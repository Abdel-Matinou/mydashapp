#iniatiate a db connection

import sqlite3

mydb = sqlite3.connect(
    'database.db'
    )

con = mydb.cursor()

print(mydb)
