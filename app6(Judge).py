import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
import google.generativeai as genai
import os
import webbrowser
from langchain_community.vectorstores import FAISS

GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

def get_suggested_decision(case_details):
    """
    Use the Google Gemini model to suggest a decision based on the case details.
    """
    decision_prompt_template = """
    Based on the following case details and the Indian Law Acts and Section, suggest an appropriate decision.

    Case Details: {case_details}

    Suggested Decision:
    """
    
    # Create the prompt with the provided case details
    prompt = PromptTemplate(template=decision_prompt_template, input_variables=["case_details"])
    formatted_prompt = prompt.format(case_details=case_details)
    
    # Initialize the ChatGoogleGenerativeAI with the specified Gemini model
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3, google_api_key=GOOGLE_API_KEY)
    
    # Create a HumanMessage with the formatted prompt
    input_message = HumanMessage(content=formatted_prompt) 
    
    # Generate the suggested decision
    decision = model([input_message])
    
    return decision.content
st.sidebar.title("Navigation")

if "page" not in st.session_state:
    st.session_state.page = "app6"

st.sidebar.title("Navigation")
if st.sidebar.button("Judge"):
    st.session_state.page = "app6"
if st.sidebar.button("Chatbot"):
    st.session_state.page = "chatbot"
if st.sidebar.button("Scan Documents"):
    st.session_state.page = "ocr1"
# Streamlit App
def main():
    st.title("Suggested Decision ")
    st.write("This tool generates a suggested decision for cases under the Indian Legal Acts, based on the details provided.")

    # Text area for the user to input case details
    case_details = st.text_area("Enter Case Details:", height=300)
    
    # Generate suggested decision on button click
    if st.button("Get Suggested Decision"):
        if case_details.strip():
            with st.spinner("Generating suggested decision..."):
                decision = get_suggested_decision(case_details)
                st.write(f"**Suggested Decision:** {decision}")
        else:
            st.error("Please enter the case details.")

if __name__ == "__main__":
    main()
# Page router
if st.session_state.page == "app6(Judge)":
    main()

elif st.session_state.page == "chatbot":
    import chatbot
    chatbot.main()

elif st.session_state.page == "ocr1":
    import ocr1
    ocr1.main()
