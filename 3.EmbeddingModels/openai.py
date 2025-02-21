from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding1 = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

result1 = embedding1.embed_query("Delhi is the capital of India")

print(str(result1))

#if you have documnet try this 


embedding2 = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

result2 = embedding2.embed_documents(documents)

print(str(result2))