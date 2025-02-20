from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

print(model.invoke("What is the capital of India?"))

print(model.invoke("What is the capital of India?").content)