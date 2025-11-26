#importing bcrypt it helps in hashing passwords
import bcrypt
import os

#USERS stores all the users credentials
USERS = "users.txt"

#function to turn plain text into a hash
def hash_password(password):
    hashvalue = password.encode("utf-8")
    #gensalt makes sure using same password twice isnt a problem
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(hashvalue, salt)

#checks if users password matches the passowrd in the file
#bcrypt only works w/ bytes not normal text
def verify_password(password: str, hashed: bytes):
    return bcrypt.checkpw(password.encode("utf-8"), hashed)

#this function saves new users into the file1
def save_user(username: str, hashed_password: bytes, role: str):
    with open(USERS, "a") as f:
        line = f"{username},{hashed_password.decode('utf-8')},{role}\n"
        f.write(line)
#this helps access the users information
def load_users():
    if not os.path.exists(USERS):
        return {}

    users = {}
    with open(USERS, "r") as f:
        for line in f:
            username, hashed, role = line.strip().split(",")
            users[username] = (hashed.encode("utf-8"), role)
    return users

#function registers new users
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role (cyber, IT, admin): ")

    hashed = hash_password(password)
    save_user(username, hashed, role)
    print("User registered successfully!")

#function lets users login
def login():
    users = load_users()
    username = input("Enter username: ")

    if username not in users:
        print("User not found.")
        return False

    enteredPassword = input("Enter password: ")
    stored_hashed, role = users[username]

    if verify_password(enteredPassword, stored_hashed):
        print(f"Login successful! Role: {role}")
        return True
    else:
        print("Incorrect password.")
        return False

#the 2 options that pop in the start
if __name__ == "__main__":
    print("1. Register")
    print("2. Login")

    choice = input("Choose an option: ")
#using elif loop
    if choice == "1":
        register()
    elif choice == "2":
        login()