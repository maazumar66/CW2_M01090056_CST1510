import pandas as pd
import streamlit as st
if "logged_in" not in st.session_state:
 st.session_state.logged_in = False

if st.button("Log in"):
 st.session_state.logged_in = True
 st.write("Logged in!")

if st.session_state.logged_in:
 st.write("Welcome!")


if"logged_in" not in st.session_state:
 st.session_state.logged_in = False

if"username" not in st.session_state:
 st.session_state.username = ""

if"users" not in st.session_state:
 st.session_state.users = {}

 t.session_state.logged_in = True
st.session_state.username = "Alice"
st.session_state.role = "admin"

# Read values
if  st.session_state.logged_in:
 st.write(
f"Welcome, {st.session_state.username}!"
 )
st.write(
f"Role: {st.session_state.role}"

)


