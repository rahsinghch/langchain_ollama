from langchain_openai import ChatOpenAI
import streamlit as st
import os
from langchain_core.globals import set_debug

set_debug(True)
OPEN_API_AI=os.getenv("OPENAI_API_KEY")

st.title("Ask anything")
question=st.text_input("enter question")
llm=ChatOpenAI(model='gpt-4o',api_key=OPEN_API_AI)
llm.invoke(question)

if question:
    response=llm.invoke(question)
    st.write(response.content)
