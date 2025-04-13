import streamlit as st
import subprocess

st.title("LegalEase Login")

st.write("Select your role to proceed:")

col1, col2 = st.columns(2)

with col1:
    if st.button('Login as Judge'):
        process = subprocess.Popen(['streamlit', 'run', 'app7(Final).py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()  # Capture output and errors
        st.write("Judge login output:")
        st.write(stdout.decode())
        st.write("Judge login error (if any):")
        st.write(stderr.decode())

with col2:
    if st.button('Login as Lawyer'):
        process = subprocess.Popen(['streamlit', 'run', 'trial.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()  # Capture output and errors
        st.write("Lawyer login output:")
        st.write(stdout.decode())
        st.write("Lawyer login error (if any):")
        st.write(stderr.decode())



# import streamlit as st
# import mysql.connector
# import hashlib
# import os

# # -------------------- DATABASE FUNCTIONS --------------------

# # Hashing function
# def hash_password(password):
#     return hashlib.sha256(password.encode()).hexdigest()

# # Connect to MySQL
# def get_connection():
#     return mysql.connector.connect(
#         host='127.0.0.1',
#         user='root',
#         password='',
#         database='legalease'
#     )

# # Authenticate user
# def authenticate_user(username, password, role):
#     conn = get_connection()
#     cursor = conn.cursor()
#     hashed_pw = hash_password(password)
#     cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s AND role=%s", (username, hashed_pw, role))
#     result = cursor.fetchone()
#     conn.close()
#     return result is not None

# # Register user
# def register_user(username, password, role):
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()
#         hashed_pw = hash_password(password)
#         cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", (username, hashed_pw, role))
#         conn.commit()
#         conn.close()
#         return True
#     except mysql.connector.Error as e:
#         st.error(f"MySQL Error: {e}")
#         return False



# st.title("LegalEase Authentication")

# option = st.radio("Choose Action", ["Login", "Register"])

# username = st.text_input("Username")
# password = st.text_input("Password", type="password")
# role = st.selectbox("Role", ["Judge", "Lawyer"])

# if option == "Login":
#     if st.button("Login"):
#         if authenticate_user(username, password, role):
#             st.success(f"Welcome, {username}! Logged in as {role}.")
#             if role == "Judge":
#                 st.write("Launching Judge Panel...")
                
#                 os.system("streamlit run app7(Final).py")
#             else:
#                 st.write("Launching Lawyer Panel...")
#                 os.system("streamlit run trial.py")
#         else:
#             st.error("Invalid credentials. Please try again.")

# elif option == "Register":
#     if st.button("Register"):
#         if register_user(username, password, role):
#             st.success("Registration successful! You can now log in.")
#         else:
#             st.error("Registration failed. Username may already exist.")
