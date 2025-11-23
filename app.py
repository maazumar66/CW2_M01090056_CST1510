import bcrypt

def hash_password(plain_text_password):
    # Encode the password to bytes (bcrypt needs bytes, not strings)
    password_bytes = plain_text_password.encode('utf-8')
    
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    
    # Decode the hash back to a string (optional, for saving in a file)
    return hashed_password.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    # Encode both the plaintext password and stored hash to bytes
    password_bytes = plain_text_password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')
    
    # bcrypt.checkpw handles extracting the salt and comparing
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)

def register_user():
    user_name = input("Enter username:")
    password = input("Enter pass:")
    hashed_password = hash_password(password)
    with open('users.txt', 'a') as f:
        f.write(f"{user_name},{hashed_password}\n")
    print("User registered succesfully")

def login_user(username, password):
    pass
