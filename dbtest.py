import sqlite3

# Step one create connection to DB
# Also Creates db if it does not exist
conn = sqlite3.connect("dbtest.db")

# Create Curson
cursor = conn.cursor()

# Create Database
cursor.execute("create table people (id integer primary key, name text, count integer)")

cursor.execute("insert into people (name, count) values ('Bob', 1)")
cursor.execute("insert into people (name, count) values (?, ?)", ("Jill", 15))

cursor.execute("insert into people (name, count) values (:username, :usercount)", {"username": "Joe", "usercount": 10})

conn.commit()


result = cursor.execute("select * from people")
print(result.fetchall())
result = cursor.execute("select * from people where name like :name", {"name": "bob"})
print(result.fetchall())
cursor.execute("update people set count=? where name=?", (20, "Jill"))
result = cursor.execute("select * from people")
print(result.fetchall())



