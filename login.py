import streamlit as st

st.title("LegalEase Login")

st.write("Select your role to proceed:")

role = st.selectbox("Choose Role", ["Select", "Judge", "Lawyer"])

if "page" not in st.session_state:
    st.session_state.page = "login"

if role == "Judge":
    st.session_state.page = "app7(Final)"
    st.experimental_rerun()
elif role == "Lawyer":
    st.session_state.page = "trial"
    st.experimental_rerun()

if st.session_state.page == "app7(Final)":
    st.write("Redirecting to Judge page...")
    # Include the content of app7(Final).py here
elif st.session_state.page == "trial":
    st.write("Redirecting to Lawyer page...")
    # Include the content of trial.py here