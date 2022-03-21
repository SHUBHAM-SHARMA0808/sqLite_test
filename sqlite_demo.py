import sqlite3

conn = sqlite3.connect("test.db")
c = conn.cursor()

# c.execute('''INSERT INTO USERS (username, password, email) 
# VALUES ("Henry", "mypassword", "abc")''')

c.execute('''SELECT * FROM USERS
WHERE username = "sharma"''')
conn.commit()

conn.close()