import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

llm=ChatOllama(model='llama3.1')
prompt_template=PromptTemplate(input_variable=["city","month","language","budget"],
                               template="""Welcome to the {city} travel guide!
                               if you are visiting in {month}, here is what you can do:
                               1. Must-visit attractions
                               2. Local ucisine you must try
                               3. useful phrases in {language}
                               4. Tips for travelling on a {budget} budget
                                Enjoy your trip!                               
                               """)
st.title("Travel guide")
city=st.text_input("enter city")
month=st.text_input("enter month")
language=st.text_input("enter language")
budget=st.selectbox("enter budget",["Low","Medium","High"])

if city and month and language and budget:
    response=llm.invoke(prompt_template.format(city=city,month=month,language=language,budget=budgetgit sttaus))
    st.write(response.content)
