import os
os.environ['GOOGLE_API_KEY"]=ST.SECRETS["GOOGLE_API_KEY]
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Initialize chat history in Streamlit session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful assistant.")
    ]
if "responses" not in st.session_state:
    st.session_state.responses = []

# Streamlit page setup
st.set_page_config(page_title="Gemini Chatbot")
st.title("💬 Chat with Gemini 2.0 Flash")

# Display chat history
for i in range(1, len(st.session_state.chat_history), 2):
    human_msg = st.session_state.chat_history[i]
    ai_msg = st.session_state.chat_history[i + 1]
    with st.chat_message("user"):
        st.markdown(human_msg.content)
    with st.chat_message("assistant"):
        st.markdown(ai_msg.content)

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI response
    response = llm.invoke(user_input)
    ai_message = AIMessage(content=response.content)
    st.session_state.chat_history.append(ai_message)

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(response.content)
