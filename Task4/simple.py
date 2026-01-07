from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

while True:
    data = input("User: ")
    if data.lower() in ["exit", "quit", "q"]:
        break
    response = model.invoke(data)
    print("AI:", response.content)
    print("\n" * 3)
