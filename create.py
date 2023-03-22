import sqlite3
conn=sqlite3.connect('wheeldeal.db')
c=conn.cursor()
c.execute("""CREATE TABLE cardetails (
carid INTEGER PRIMARY KEY,
cartype TEXT NOT NULL
)""")
c.execute("""CREATE TABLE driverdetails (
carid INTEGER NOT NULL,
carnum TEXT,
name TEXT,
phnum INTEGER,
carmodel TEXT,
FOREIGN KEY(carid) REFERENCES cardetails(carid)
)""")

conn.close()