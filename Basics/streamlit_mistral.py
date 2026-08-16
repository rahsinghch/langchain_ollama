from langchain_ollama import ChatOllama
import streamlit as st
from langchain_core.globals import set_debug

set_debug(True)
llm=ChatOllama(model='mistral:7b')

st.title("Ask anything")
question=st.text_input("Enter your question")

if question:
    response=llm.invoke(question)
    st.write(response.content)