from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash')

response = model.invoke("Hello, how are you?")

print(response.text)


