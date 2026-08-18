import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_core.globals import set_debug

llm=ChatOllama(model='mistral:7b')
set_debug(True)

title_prompt=PromptTemplate(input_variable=["topic"],
                            template="""You are ane experienced speech writer. You need 
                            to craft an impactful title for a speech 
                            on the following topic:{topic}. Answer exactly in one title
                            
                            """)

speech_prompt=PromptTemplate(input_variable=["title","emotion"],
                             template="""You need to write a powerful {emotion} speech of 350 words.
                             for the following title?:{title}
                             Format the output with 2 keys: 'title','speech' and fill them with
                             the respective values
                             
                             
                             """)


first_chain=title_prompt|llm|StrOutputParser()|(lambda title:(st.write(title),title)[1])
second_chain=speech_prompt|llm|JsonOutputParser()

final_chain=first_chain|(lambda title:{"title":title,"emotion":emotion})|second_chain

st.title("Speech Generator")
topic=st.text_input("Enter the topic")
emotion=st.text_input("select emotion")

if topic and emotion:
    response=final_chain.invoke({"topic":topic})
    st.write(response)
