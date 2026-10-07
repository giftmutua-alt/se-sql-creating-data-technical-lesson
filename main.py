import sqlite3
import pandas as pd

conn = sqlite3.connect('my_db.sqlite')
cur = conn.cursor()

#cur.execute("""
#   CREATE TABLE users (
#       id INTEGER PRIMARY KEY,
#       name TEXT NOT NULL,
#       email TEXT UNIQUE NOT NULL,
#       signup_date DATE DEFAULT CURRENT_DATE
#   );
#""")

#cur.execute("""
#   INSERT INTO users (name, email)
#   VALUES 
#       ('Sofia Ramirez', 'sofia.ramirez@example.com'),
#       ('Devon Blake', 'devon.blake@example.com');
#""")

#conn.commit()

cur.execute("""SELECT * FROM users;""")
print(cur.fetchall())

cur.execute("""
    UPDATE users
    SET email = 'devon.blake@newdomain.com'
    WHERE id = 2;
""")

conn.commit()

conn.close()