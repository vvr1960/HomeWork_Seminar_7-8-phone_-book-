
import sqlite3 as sql

conn = sql.connect('data_users.db')
cursor = conn.cursor()


cursor.execute("""CREATE TABLE phone_list(
                   surname TEXT,
                   name TEXT,
                   patron TEXT,
                   phone_number INTEGER);
                   """)
conn.commit()
cursor.close()



