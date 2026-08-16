from langchain_openai import ChatOpenAI
import os


OPEN_API_KEY=os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(model="gpt-4o",api_key=OPEN_API_KEY)
question=input("enter a question")
response=llm.invoke(question)
print(response.content)
