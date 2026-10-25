import os    
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
# Select the model
model = genai.GenerativeModel("gemini-3.5-flash")  
# Streamlit page config
st.set_page_config(page_title="Chatbot by jatin", page_icon="🤖")
st.title("🤖Chatbot by jatin")
# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []
   
# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])    
       
# Chat input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(prompt)
                reply = response.text
                st.markdown(reply)
            except Exception as e:
                st.error(f"Error: {e}")
                reply = "Sorry, I encountered an error."

    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": reply})