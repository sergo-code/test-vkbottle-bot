import sqlite3


conn = sqlite3.connect('users.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
               user_id INT PRIMARY KEY,
               city TEXT);
            """)
conn.commit()
