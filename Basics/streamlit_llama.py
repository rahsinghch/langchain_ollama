import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.globals import set_debug

set_debug(True)
llm=ChatOllama(model='llama3.1')


st.title("Ask anything")
question=st.text_input("ask a question")

if question:
    response=llm.invoke(question)
    st.write(response.content)