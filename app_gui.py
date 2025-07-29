import streamlit as st
from chatbot import Chatbot

# Setup
st.set_page_config(page_title="📘 Financial Policy Chatbot", layout="wide")
st.title("🧧 Financial Policy Chatbot")
st.markdown("Ask questions about the 2005-06 Financial Policy Document.")

# Initialize chatbot
if "chatbot" not in st.session_state:
    st.session_state.chatbot = Chatbot()
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
query = st.text_input("💬 Your question:", placeholder="e.g., What about debt?")

if st.button("Ask") and query.strip():
    response = st.session_state.chatbot.answer(query)
    st.session_state.chat_history.append(("🧍 You", query))
    st.session_state.chat_history.append(("🤖 Bot", response))

# Display chat history
for speaker, message in reversed(st.session_state.chat_history):
    st.markdown(f"**{speaker}**: {message}")
