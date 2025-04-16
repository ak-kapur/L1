import streamlit as st

st.title("LegalEase Login")

st.write("Select your role to proceed:")

role = st.selectbox("Choose Role", ["Select", "Judge", "Lawyer"])

if role == "Judge":
    st.switch_page("app6(Judge).py")
elif role == "Lawyer":
    st.switch_page("trial.py")
