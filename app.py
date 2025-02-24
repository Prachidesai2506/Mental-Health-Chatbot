import streamlit as st
import requests

# FastAPI server URL
FASTAPI_URL = "http://127.0.0.1:8000/chat"

st.title("🧠 Mental Health Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.text_input("You:", key="user_input")

if st.button("Send") and user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Make request to FastAPI chatbot
    response = requests.get(FASTAPI_URL, params={"user_message": user_input})

    if response.status_code == 200:
        bot_reply = response.json().get("response", "Sorry, I couldn't understand that.")
    else:
        bot_reply = "Error: Unable to reach chatbot API."

    # Append chatbot response
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    # Display bot reply
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
