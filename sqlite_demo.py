import sqlite3

conn = sqlite3.connect("test.db")
c = conn.cursor()

# c.execute('''INSERT INTO USERS (username, password, email) 
# VALUES ("Hero", "mypassword", "abc")''')

c.execute('''SELECT * FROM USERS''')

rows = c.fetchall()
print(rows)

conn.commit()

conn.close()