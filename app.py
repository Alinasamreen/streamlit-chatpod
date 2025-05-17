import os
os.environ["GOOGLE_API_KEY"]=st.secrets["GOOGLE_API_KEY"]
import streamlit as st
st.title("streamlit chatbot")
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Initialize chat model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="You are a helpful assistant.")]

st.title("🧠 Gemini Chat Assistant")

# Display chat history
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)

# User input
user_input = st.chat_input("Say something...")
if user_input:
    # Append user input to history
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    
    # Generate response
    result = llm.invoke(st.session_state.chat_history)
    
    # Append AI response
    st.session_state.chat_history.append(AIMessage(content=result.content))
    
    # Display AI response
    st.chat_message("assistant").write(result.content)
    

