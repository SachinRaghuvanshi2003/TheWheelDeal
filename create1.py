import sqlite3
conn=sqlite3.connect('wheeldeal.db')
c=conn.cursor()
c.execute("""INSERT INTO cardetails (
carid,cartype) VALUES (101,'MINI')""")
c.execute("""INSERT INTO cardetails (
carid,cartype) VALUES (102,'SEDAN')""")
c.execute("""INSERT INTO cardetails (
carid,cartype) VALUES (103,'SUV')""")
c.execute("""INSERT INTO cardetails (
carid,cartype) VALUES (104,'LUXURY')""")


conn.close()