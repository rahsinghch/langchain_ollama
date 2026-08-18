from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

llm=ChatOllama(model='gemma:2b')
title_prompt=PromptTemplate(input_variable=["topic"],
                              template="""You are an experienced speech writer. You need to craft an impactful title for a speech 
                              on a given topic:{topic}
                              Answer exactly with one title
                              """)



speech_prompt=PromptTemplate(input_variable=["title"],
                             template="""You need to write a powerful speech of 350 workds for the following title:{title}
                             """
)

first_chain=title_prompt| llm|StrOutputParser()|(lambda title: (st.write(title),title)[1])
second_chain=speech_prompt|llm

final_chain=first_chain|second_chain

st.title("speech Generator")

topic=st.text_input("Enter the topic")

if topic:
    response=final_chain.invoke({"topic":topic})
    st.write(response.content)







