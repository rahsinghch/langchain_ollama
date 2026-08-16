import os
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.prompts import PromptTemplate


OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(model='gpt-4o',api_key=OPENAI_API_KEY)
promp_template=PromptTemplate(input_variables=["country","no_of_paras","language"],
                              template="""You are an expert in traiditional cusisines. You provide information about a specific dish from a specific country.
                              Avoid giving information about fictional places. If the country is fictional or non-existent asnwer: I don't know.
                              Answer the question: What is the traditional cusines of {country}?
                              Answer in {no_of_paras} short paras in {language}
                              """)

st.title("Cusiine information")
country=st.text_input("enter country")
no_of_paras=st.number_input("enter no of paraagraph",min_value=1,max_value=5)
language=st.text_input("enter the language")

if country:
    response=llm.invoke(promp_template.format(country=country,no_of_paras=no_of_paras,language=language))
    st.write(response.content)
