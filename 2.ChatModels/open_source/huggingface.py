from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()  

LLM = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.1",  # Public model
    task="text-generation"
)

model = ChatHuggingFace(llm=LLM)

print(model.invoke("What is the capital of India?"))
