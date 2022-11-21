import sqlite3 as sql


conn = sql.connect('data_users.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM phone_list")
for row in cursor:
    
    print(row)
