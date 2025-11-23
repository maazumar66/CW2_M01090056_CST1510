import sqlite3 as sq 

# Connect to database or make it if it doesn't exist
conn = sq.connect('Data/telligence_platform.db')

def add_user(conn, name, hash):
  curr = conn.cursor() #writes AQL inside database

# Create table
  sql = ("""INSERT INTO users (username, password_hash) VALUES (?, ?,) """)

  param = ('alice', 'hashed_password_123')

  curr.execute(sql,param) #make a a table called users

  conn.commit() #saves changes to the database
def get_users():
 curr = conn.cursor()
 sql = ("""SELECT  FROM users""")
 curr.execute(sql)
 users = curr.fetchall()
 conn.close
 return users

def migrate_user_data():
 with open('Data/user.txt', 'r') as f:
  users = f.readlines()

 for user in users:
  name, hash = user.strip().split(',')
  add_user(conn,name,hash)

conn.close()

  

