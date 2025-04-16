import streamlit as st

st.title("LegalEase Login")

st.write("Select your role to proceed:")

role = st.selectbox("Choose Role", ["Select", "Judge", "Lawyer"])

if role == "Judge":
    st.switch_page("pages/app7(Final).py")
elif role == "Lawyer":
    st.switch_page("pages/trial.py")
