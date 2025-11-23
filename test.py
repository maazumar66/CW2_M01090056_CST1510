import sqlite3

import pandas as pd

def create_user_table(conn): #defining a function to create a table
    curr = conn.cursor() #a function that sends SQL commands to the databse
  #instructions for what we want (SQL Commands)
  #HOW IT WORKS:
  #IF NOT means create table only if it isnt there
  #ID automatically counts up basically a index
  #username (text) has to be unique and cannot be emptu
  #password (text) cannot be empty
    sql = """CREATE TABLE IF NOT EXISTS users ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    username TEXT NOT NULL UNIQUE, 
    password_hash TEXT NOT NULL
    )"""
    curr.execute(sql)
    #saves the changes to the database
    conn.commit()

def add_user(conn, name, hash_password):
    curr = conn.cursor() #transfers the SQL commands to the df
    #INSERT INTO means add a new row and the columns should be username and password_hash
    #? ? are placeholders basically we give the actual values later
    sql = "INSERT INTO users (username, password_hash) VALUES (?,?)" 
    param = (name, hash_password) #param gives the actual values to the VALUES(?,?)
    curr.execute(sql, param) #Executes everything
    conn.commit()

#conn.close()


def migrate_users():
    with open('C:/Users/aqib_/Downloads/CW2_M01090056_CST1510/bcript_test/DATA/users.txt') as f:
        users = f.readlines()

    for user in users:
        name, hash = user.strip().split(',')
        add_user(conn, name, hash)
    conn.close()


def get_all_users(conn):
    curr = conn.cursor()
    sql = "SELECT * FROM users"
    curr.execute(sql)
    users = curr.fetchall()
    conn.close()
    return(users)

def get_user():
    
    curr = conn.cursor()
    sql = "SELECT * FROM users WHERE username = ?"
    param = ('maazumar',)
    curr.execute(sql, param)
    user = curr.fetchone() # Returns single row or None
    conn.close()
    return user 

def migrate_datasets_metadata():
    data = pd.read_csv("C:/Users/aqib_/Downloads/CW2_M01090056_CST1510/bcript_test/DATA/datasets_metadata.csv")
    data.to_sql('datasets_metadata', conn, if_exists = 'append', index = False)
    print(data)
    conn.close()

def get_data_pandas():
    sql = 'SELECT * FROM datasets_metadata'
    data = pd.read_sql(sql, conn)

    print(data)

#BASICALLY THE STANDARD FORMAT
conn = sqlite3.connect('bcript_test/DATA/telligence_platform.db') #if db exists connect to it if it dont then SQL makes it
curr = conn.cursor()
sql = ""
param = ""
curr.execute(sql, param)
conn.commit()
conn.close()
