from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
import streamlit as st

llm1=ChatOllama(model='mistral:7b')
llm2=ChatOllama(model='llama3.1:latest')

title_prompt=PromptTemplate(input_variable=['topic'],
                            template="""You are an experienced speech writer. You
                            need to craft an impactful title for a speech on the following topics
                            :{topic}. Answer exactly with one title."""
                            )

speech_prompt=PromptTemplate(input_variable=["title"],
                             template="""You need to write a powerful speech writer of 350 words for the following
                             title:{title}""")

first_chain=title_prompt|llm1| StrOutputParser()|(lambda title:(st.write(title),title)[1])
second_chain=speech_prompt|llm2
final_chain=first_chain|second_chain
st.title("Speech generator/")
topic=st.text_input("Enter a topic")

if topic:
    response=final_chain.invoke({"topic":topic})
    st.write(response.content)