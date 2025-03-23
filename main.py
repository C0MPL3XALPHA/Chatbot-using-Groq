import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 

API_KEY=os.getenv('API_KEY')

client=Groq(api_key=API_KEY)

st.title("💬 Your own chatbot!")
st.caption("🚀 A Streamlit chatbot powered by Groq")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": "Remember your previous responses . Use previous responses as context.Also if you make a mistake then say sorry.Be polite."},
                                    {"role": "assistant", "content": "How can I help you?"}]



# Display chat history
for msg in st.session_state.messages:
    if (msg["role"]!="system"):
     st.chat_message(msg["role"]).write(msg["content"])


# Handle user input
if prompt := st.chat_input():
   
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    # Get response from Groq API
    response = client.chat.completions.create(
        messages=st.session_state.messages,
        model="llama-3.3-70b-versatile",
    )

  
    msg = response.choices[0].message.content
    
    # Append assistant response
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)





