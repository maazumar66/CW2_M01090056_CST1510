import sqlite3
import os

print(os.path.abspath("bcript_test/DATA/telligence_platform.db"))

def create_user_table(conn):
    curr = conn.cursor()
    sql = """CREATE TABLE IF NOT EXISTS users ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    username TEXT NOT NULL UNIQUE, 
    password_hash TEXT NOT NULL
    );"""
    curr.execute(sql)
    conn.commit()

def add_user(conn, name, hash_password):
    curr = conn.cursor()
    sql = "INSERT INTO users (username, password_hash) VALUES (?,?)" 
    curr.execute(sql, (name, hash_password))
    conn.commit()

# Connect
conn = sqlite3.connect('bcript_test/DATA/telligence_platform.db')

# Create table if not exists
create_user_table(conn)

# OPTIONAL — Clear previous data
# curr = conn.cursor()
# curr.execute("DELETE FROM users")
# conn.commit()

# Insert data
with open('C:/Users/aqib_/Downloads/CW2_M01090056_CST1510/bcript_test/DATA/users.txt') as f:
    for line in f:
        if "," in line:               # protection
            name, hash_val = line.strip().split(',')
            add_user(conn, name, hash_val)

conn.close()
