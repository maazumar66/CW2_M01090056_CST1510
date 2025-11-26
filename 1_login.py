#creating login page
import streamlit as st
import bcrypt
import os

st.title("Please Login to Intelligence Platform")

#initialize database, using old auth functions
#same code we used in auth.py just in web format!
def verify_password(password: str, hashed: bytes):
    return bcrypt.checkpw(password.encode("utf-8"), hashed)

def load_users():
    users = {}
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    try:
                        username, hashed, role = line.split(",")
                        users[username] = (hashed.encode("utf-8"), role)
                    except:
                        continue
    return users

#login form
with st.form("login_form"):
    st.subheader("User Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    login_button = st.form_submit_button("Login")
    
    if login_button:
        if username and password:
            users = load_users()
            
            if username in users:
                stored_hash, role = users[username]
                
                if verify_password(password, stored_hash):
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.session_state.role = role.lower()
                    st.success(f"Welcome {username}! Role: {role}")
                    st.info("You can now navigate to your dashboard")
                else:
                    st.error("Invalid password!")
            else:
                st.error("User not found.")
        else:
            st.error("Please enter both username and password")

#for registering new users
st.markdown("---")
st.subheader("Don't have an account? Register Here")

with st.form("register_form"):
    st.write("Create a new account")
    new_username = st.text_input("Choose Username", key="reg_user")
    new_password = st.text_input("Choose Password", type="password", key="reg_pass")
    role = st.selectbox("Select Role", ["Cyber", "IT"], key="reg_role") 
    
    register_button = st.form_submit_button("Register")
    
    if register_button:
        if new_username and new_password:
            users = load_users()
            
            if new_username in users:
                st.error("Username already exists!")
            else:
                #hashes pass and saves user
                salt = bcrypt.gensalt()
                hashed = bcrypt.hashpw(new_password.encode("utf-8"), salt)
                
                with open("users.txt", "a") as f:
                    f.write(f"{new_username},{hashed.decode('utf-8')},{role}\n")
                
                st.success(f"User {new_username} registered as {role}!")
                st.info("You can now login with your new account")
        else:
            st.error("Please enter both username and password")
