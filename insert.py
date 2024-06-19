import sqlite3

conn = sqlite3.connect('example.db')
print("Successfully connected")

conn.execute("INSERT INTO Employee VALUES (1,'Mark','Mugo',45,120000.00,'Manager')")
conn.execute("INSERT INTO Employee VALUES (2,'Moses','Mwendwa',25,122000.00,'HR')")
conn.execute("INSERT INTO Employee VALUES (3,'Mary','Choney',35,125000.00,'Driver')")
conn.execute("INSERT INTO Employee VALUES (4,'Ahmed','Abdul',34,130000.00,'Manager')")
conn.execute("INSERT INTO Employee VALUES (5,'Mercy','Linah',42,105000.00,'General Manager')")
conn.execute("INSERT INTO Employee VALUES (6,'Lucy','Kagwiria',29,110000.00,'Janitor')")

conn.commit()
print("Successfully inserted values into Employee table")